"""
    Deblocking functions and wrappers.
"""
from functools import partial
from importlib.metadata import version
from typing import Any, Optional, Sequence, Tuple, Union

import vapoursynth as vs
from packaging import version as pck_version

from .types import Matrix
from .util import get_prop

core = vs.core


def autodb_dpir(clip: vs.VideoNode, edgevalue: int = 24,
                strs: Sequence[float] = [30, 50, 75],
                thrs: Sequence[Tuple[float, float, float]] = [(1.5, 2.0, 2.0), (3.0, 4.5, 4.5), (5.5, 7.0, 7.0)],
                matrix: Optional[Union[Matrix, int]] = None,
                cuda: bool = True, device_index: int = 0,
                write_props: bool = False,
                **vsdpir_args: Any) -> vs.VideoNode:
    """
    A rewrite of fvsfunc.AutoDeblock that uses vspdir instead of dfttest to deblock.

    This function checks for differences between a frame and an edgemask with some processing done on it,
    and for differences between the current frame and the next frame.
    For frames where both thresholds are exceeded, it will perform deblocking at a specified strength.
    This will ideally be frames that show big temporal *and* spatial inconsistencies.

    Thresholds and calculations are added to the frameprops to use as reference when setting the thresholds.

    Keep in mind that vsdpir is not perfect; it may cause weird, black dots to appear sometimes.
    If that happens, you can perform a denoise on the original clip (maybe even using vsdpir's denoising mode)
    and grab the brightest pixels from your two clips. That should return a perfectly fine clip.

    Thanks Vardë, louis, setsugen_no_ao!

    Dependencies:

    * vs-dpir

    :param clip:            Input clip
    :param edgevalue:       Remove edges from the edgemask that exceed this threshold (higher means more edges removed)
    :param strs:            A list of DPIR strength values (higher means stronger deblocking).
                            You can pass any arbitrary number of values here.
                            The amount of values in strs and thrs need to be equal.
    :param thrs:            A list of thresholds, written as [(EdgeValRef, NextFrameDiff, PrevFrameDiff)].
                            You can pass any arbitrary number of values here.
                            The amount of values in strs and thrs need to be equal.
    :param matrix:          Enum for the matrix of the input clip. See ``types.Matrix`` for more info.
                            If `None`, gets matrix from the "_Matrix" prop of the clip unless it's an RGB clip,
                            in which case it stays as `None`.
    :param cuda:            Device type used for deblocking. Uses CUDA if True, else CPU
    :param device_index:    The 'device_index' + 1º device of type device type in the system
    :write_props            Will write verbose props
    :vsdpir_args            Additional args to pass to ``vsdpir``

    :return:                Deblocked clip
    """
    if clip.format is None:
        raise ValueError("autodb_dpir: 'Variable-format clips not supported'")

    def _eval_db(n: int, f: Sequence[vs.VideoFrame],
                 clip: vs.VideoNode, db_clips: Sequence[vs.VideoNode],
                 nthrs: Sequence[Tuple[float, float, float]]) -> vs.VideoNode:

        evref_diff, y_next_diff, y_prev_diff = [
            get_prop(f[i], prop, float)
            for i, prop in zip(range(3), ['EdgeValRefDiff', 'YNextDiff', 'YPrevDiff'])
        ]
        f_type = get_prop(f[0], '_PictType', bytes).decode('utf-8')

        if f_type == 'I':
            y_next_diff = (y_next_diff + evref_diff) / 2

        out = clip
        nthr_used = (-1., ) * 3
        for dblk, nthr in zip(db_clips, nthrs):
            if all(p > t for p, t in zip([evref_diff, y_next_diff, y_prev_diff], nthr)):
                out = dblk
                nthr_used = nthr

        if write_props:
            for prop_name, prop_val in zip(
                ['Adb_EdgeValRefDiff', 'Adb_YNextDiff', 'Adb_YPrevDiff',
                 'Adb_EdgeValRefDiffThreshold', 'Adb_YNextDiffThreshold', 'Adb_YPrevDiffThreshold'],
                [evref_diff, y_next_diff, y_prev_diff] + list(nthr_used)
            ):
                out = out.std.SetFrameProp(prop_name, floatval=max(prop_val * 255, -1))

        return out

    if len(strs) != len(thrs):
        raise ValueError('autodb_dpir: You must pass an equal amount of values to '
                         f'strenght {len(strs)} and thrs {len(thrs)}!')

    nthrs = [tuple(x / 255 for x in thr) for thr in thrs]

    is_rgb = clip.format.color_family is vs.RGB

    if not matrix and not is_rgb:
        matrix = get_prop(clip.get_frame(0), "_Matrix", int)

    rgb = core.resize.Bicubic(clip, format=vs.RGBS, matrix_in=matrix) if not is_rgb else clip

    assert rgb.format

    maxvalue = (1 << rgb.format.bits_per_sample) - 1
    evref = core.std.Prewitt(rgb)
    evref = core.std.Expr(evref, f"x {edgevalue} >= {maxvalue} x ?")
    evref_rm = evref.std.Median().std.Convolution(matrix=[1, 2, 1, 2, 4, 2, 1, 2, 1])

    diffevref = core.std.PlaneStats(evref, evref_rm, prop='EdgeValRef')
    diffnext = core.std.PlaneStats(rgb, rgb.std.DeleteFrames([0]), prop='YNext')
    diffprev = core.std.PlaneStats(rgb, rgb[0] + rgb, prop='YPrev')

    db_clips = [
        vsdpir(rgb, strength=st, mode='deblock', cuda=cuda, device_index=device_index, **vsdpir_args)
        .std.SetFrameProp('Adb_DeblockStrength', intval=int(st)) for st in strs
    ]

    debl = core.std.FrameEval(
        rgb, partial(_eval_db, clip=rgb, db_clips=db_clips, nthrs=nthrs),
        prop_src=[diffevref, diffnext, diffprev]
    )

    return core.resize.Bicubic(debl, format=clip.format.id, matrix=matrix if not is_rgb else None)


def vsdpir(clip: vs.VideoNode, strength: float = 25, mode: str = 'deblock',
           matrix: Optional[Union[Matrix, int]] = None,
           cuda: bool = True, device_index: int = 0,
           i444: bool = False, **vsdpir_args: Any) -> vs.VideoNode:
    """
    A simple vs-dpir wrapper for convenience.

    You must have vs-dpir 1.6.0 or higher.
    https://github.com/HolyWu/vs-dpir.

    Converts to RGB -> runs vs-dpir -> converts back to original format.
    For more information, see https://github.com/cszn/DPIR.

    Dependencies:

    * vs-dpir

    :param clip:            Input clip
    :param strength:        vs-dpir strength.
                            Sane values lie between 20-50 for ``mode='deblock'``, and 2-5 for ``mode='denoise'``
    :param mode:            vs-dpir mode. Valid modes are 'deblock' and 'denoise'.
    :param matrix:          Enum for the matrix of the input clip. See ``types.Matrix`` for more info.
                            If `None`, gets matrix from the "_Matrix" prop of the clip unless it's an RGB clip,
                            in which case it stays as `None`.
    :param cuda:            Use CUDA if True, else CPU
    :param i444:            Forces the returned clip to be YUV444PS instead of the input clip's format
    :param vsdpir_args:     Additional args to pass onto vs-dpir
                            (Note: strength, task, and device_type can't be overridden!)

    :return:                Deblocked or denoised clip in either the given clip's format or YUV444PS
    """
    try:
        from vsdpir import DPIR
    except ModuleNotFoundError:
        raise ModuleNotFoundError("'vsdpir: vs-dpir and pytorch are required to use this function.'")

    # Forcing user to use a version of vsdpir that doesn't have the dotting issue rather than worry about that here.
    if pck_version.parse(version('vsdpir')) < pck_version.parse("1.6.0"):
        raise ImportError(f"vsdpir: 'Your vs-dpir version must be at least 1.6.0. Current version: {version('vsdpir')}"
                          "\nPlease install the latest version from <https://github.com/HolyWu/vs-dpir>'")

    if clip.format is None:
        raise ValueError("vsdpir: 'Variable-format clips not supported'")

    is_rgb = clip.format.color_family is vs.RGB

    if matrix is None and not is_rgb:
        matrix = get_prop(clip.get_frame(0), "_Matrix", int)

    vsdpir_args |= dict(strength=strength, task=mode, device_type='cuda' if cuda else 'cpu')

    clip_rgb = core.resize.Bicubic(clip, format=vs.RGBS, matrix_in=matrix, dither_type='error_diffusion')
    run_dpir = DPIR(clip_rgb, **vsdpir_args)

    if i444:
        return core.resize.Bicubic(run_dpir, format=vs.YUV444PS, matrix=matrix)
    return core.resize.Bicubic(run_dpir, format=clip.format.id, matrix=matrix)
