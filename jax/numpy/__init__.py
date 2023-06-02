# Copyright 2018 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: import <name> as <name> is required for names to be exported.
# See PEP 484 & https://github.com/google/jax/issues/7570

from jax.numpy import fft as fft
from jax.numpy import linalg as linalg

from jax._src.basearray import Array as ndarray

from jax._src.numpy.lax_numpy import (
    ComplexWarning as ComplexWarning,
    NINF as NINF,
    NZERO as NZERO,
    PZERO as PZERO,
    allclose as allclose,
    angle as angle,
    append as append,
    apply_along_axis as apply_along_axis,
    apply_over_axes as apply_over_axes,
    arange as arange,
    argmax as argmax,
    argmin as argmin,
    argsort as argsort,
    argwhere as argwhere,
    around as around,
    array as array,
    array_equal as array_equal,
    array_equiv as array_equiv,
    array_repr as array_repr,
    array_split as array_split,
    array_str as array_str,
    asarray as asarray,
    atleast_1d as atleast_1d,
    atleast_2d as atleast_2d,
    atleast_3d as atleast_3d,
    bartlett as bartlett,
    bfloat16 as bfloat16,
    bincount as bincount,
    blackman as blackman,
    block as block,
    bool_ as bool_,
    broadcast_arrays as broadcast_arrays,
    broadcast_shapes as broadcast_shapes,
    broadcast_to as broadcast_to,
    can_cast as can_cast,
    cdouble as cdouble,
    character as character,
    choose as choose,
    clip as clip,
    column_stack as column_stack,
    complex128 as complex128,
    complex64 as complex64,
    complex_ as complex_,
    complexfloating as complexfloating,
    compress as compress,
    concatenate as concatenate,
    convolve as convolve,
    copy as copy,
    corrcoef as corrcoef,
    correlate as correlate,
    cov as cov,
    cross as cross,
    csingle as csingle,
    delete as delete,
    diag as diag,
    diagflat as diagflat,
    diag_indices as diag_indices,
    diag_indices_from as diag_indices_from,
    diagonal as diagonal,
    diff as diff,
    digitize as digitize,
    dot as dot,
    double as double,
    dsplit as dsplit,
    dstack as dstack,
    dtype as dtype,
    e as e,
    ediff1d as ediff1d,
    einsum as einsum,
    einsum_path as einsum_path,
    empty as empty,
    empty_like as empty_like,
    euler_gamma as euler_gamma,
    expand_dims as expand_dims,
    extract as extract,
    eye as eye,
    finfo as finfo,
    fix as fix,
    flatnonzero as flatnonzero,
    flexible as flexible,
    flip as flip,
    fliplr as fliplr,
    flipud as flipud,
    float16 as float16,
    float32 as float32,
    float64 as float64,
    float8_e4m3fn as float8_e4m3fn,
    float8_e5m2 as float8_e5m2,
    float_ as float_,
    floating as floating,
    fmax as fmax,
    fmin as fmin,
    frombuffer as frombuffer,
    fromfile as fromfile,
    fromfunction as fromfunction,
    fromiter as fromiter,
    fromstring as fromstring,
    from_dlpack as from_dlpack,
    full as full,
    full_like as full_like,
    gcd as gcd,
    generic as generic,
    geomspace as geomspace,
    get_printoptions as get_printoptions,
    gradient as gradient,
    hamming as hamming,
    hanning as hanning,
    histogram as histogram,
    histogram_bin_edges as histogram_bin_edges,
    histogram2d as histogram2d,
    histogramdd as histogramdd,
    hsplit as hsplit,
    hstack as hstack,
    i0 as i0,
    identity as identity,
    iinfo as iinfo,
    indices as indices,
    inexact as inexact,
    inf as inf,
    inner as inner,
    insert as insert,
    int8 as int8,
    int16 as int16,
    int32 as int32,
    int64 as int64,
    int_ as int_,
    integer as integer,
    interp as interp,
    isclose as isclose,
    iscomplex as iscomplex,
    iscomplexobj as iscomplexobj,
    isreal as isreal,
    isrealobj as isrealobj,
    isscalar as isscalar,
    issubdtype as issubdtype,
    issubsctype as issubsctype,
    iterable as iterable,
    ix_ as ix_,
    kaiser as kaiser,
    kron as kron,
    lcm as lcm,
    lexsort as lexsort,
    linspace as linspace,
    load as load,
    logspace as logspace,
    mask_indices as mask_indices,
    matmul as matmul,
    matrix_transpose as matrix_transpose,
    meshgrid as meshgrid,
    moveaxis as moveaxis,
    nan as nan,
    nan_to_num as nan_to_num,
    nanargmax as nanargmax,
    nanargmin as nanargmin,
    argpartition as argpartition,
    ndim as ndim,
    newaxis as newaxis,
    nonzero as nonzero,
    number as number,
    object_ as object_,
    ones as ones,
    ones_like as ones_like,
    outer as outer,
    packbits as packbits,
    pad as pad,
    partition as partition,
    pi as pi,
    piecewise as piecewise,
    place as place,
    printoptions as printoptions,
    promote_types as promote_types,
    put as put,
    ravel as ravel,
    ravel_multi_index as ravel_multi_index,
    repeat as repeat,
    reshape as reshape,
    resize as resize,
    result_type as result_type,
    roll as roll,
    rollaxis as rollaxis,
    rot90 as rot90,
    round as round,
    round_ as round_,
    row_stack as row_stack,
    save as save,
    savez as savez,
    searchsorted as searchsorted,
    select as select,
    set_printoptions as set_printoptions,
    shape as shape,
    signedinteger as signedinteger,
    single as single,
    size as size,
    sort as sort,
    sort_complex as sort_complex,
    split as split,
    squeeze as squeeze,
    stack as stack,
    swapaxes as swapaxes,
    take as take,
    take_along_axis as take_along_axis,
    tensordot as tensordot,
    tile as tile,
    trace as trace,
    trapz as trapz,
    transpose as transpose,
    tri as tri,
    tril as tril,
    tril_indices as tril_indices,
    tril_indices_from as tril_indices_from,
    trim_zeros as trim_zeros,
    triu as triu,
    triu_indices as triu_indices,
    triu_indices_from as triu_indices_from,
    trunc as trunc,
    uint as uint,
    uint8 as uint8,
    uint16 as uint16,
    uint32 as uint32,
    uint64 as uint64,
    unpackbits as unpackbits,
    unravel_index as unravel_index,
    unsignedinteger as unsignedinteger,
    unwrap as unwrap,
    vander as vander,
    vdot as vdot,
    vsplit as vsplit,
    vstack as vstack,
    where as where,
    zeros as zeros,
    zeros_like as zeros_like,
)

# TODO(phawkins): make this import unconditional after increasing the ml_dtypes
# minimum version.
import jax._src.numpy.lax_numpy
if hasattr(jax._src.numpy.lax_numpy, "int4"):
  from jax._src.numpy.lax_numpy import (
    int4 as int4,
    uint4 as uint4,
  )


from jax._src.numpy.index_tricks import (
  c_ as c_,
  index_exp as index_exp,
  mgrid as mgrid,
  ogrid as ogrid,
  r_ as r_,
  s_ as s_,
)

from jax._src.numpy.polynomial import (
    poly as poly,
    polyadd as polyadd,
    polyder as polyder,
    polydiv as polydiv,
    polyfit as polyfit,
    polyint as polyint,
    polymul as polymul,
    polysub as polysub,
    polyval as polyval,
    roots as roots,
)

from jax._src.numpy.reductions import (
    amin as amin,
    amax as amax,
    any as any,
    all as all,
    average as average,
    count_nonzero as count_nonzero,
    cumsum as cumsum,
    cumprod as cumprod,
    max as max,
    mean as mean,
    median as median,
    min as min,
    nancumsum as nancumsum,
    nancumprod as nancumprod,
    nanmax as nanmax,
    nanmean as nanmean,
    nanmedian as nanmedian,
    nanmin as nanmin,
    nanpercentile as nanpercentile,
    nanprod as nanprod,
    nanquantile as nanquantile,
    nanstd as nanstd,
    nansum as nansum,
    nanvar as nanvar,
    percentile as percentile,
    prod as prod,
    ptp as ptp,
    quantile as quantile,
    std as std,
    sum as sum,
    var as var,
)

from jax._src.numpy.setops import (
    in1d as in1d,
    intersect1d as intersect1d,
    isin as isin,
    setdiff1d as setdiff1d,
    setxor1d as setxor1d,
    union1d as union1d,
    unique as unique,
)

from jax._src.numpy.ufuncs import (
    abs as abs,
    absolute as absolute,
    add as add,
    arccos as arccos,
    arccosh as arccosh,
    arcsin as arcsin,
    arcsinh as arcsinh,
    arctan as arctan,
    arctan2 as arctan2,
    arctanh as arctanh,
    bitwise_and as bitwise_and,
    bitwise_not as bitwise_not,
    bitwise_or as bitwise_or,
    bitwise_xor as bitwise_xor,
    cbrt as cbrt,
    ceil as ceil,
    conj as conj,
    conjugate as conjugate,
    copysign as copysign,
    cos as cos,
    cosh as cosh,
    deg2rad as deg2rad,
    degrees as degrees,
    divide as divide,
    divmod as divmod,
    equal as equal,
    exp as exp,
    exp2 as exp2,
    expm1 as expm1,
    fabs as fabs,
    float_power as float_power,
    floor as floor,
    floor_divide as floor_divide,
    fmod as fmod,
    frexp as frexp,
    greater as greater,
    greater_equal as greater_equal,
    heaviside as heaviside,
    hypot as hypot,
    imag as imag,
    invert as invert,
    isfinite as isfinite,
    isinf as isinf,
    isnan as isnan,
    isneginf as isneginf,
    isposinf as isposinf,
    ldexp as ldexp,
    left_shift as left_shift,
    less as less,
    less_equal as less_equal,
    log as log,
    log10 as log10,
    log1p as log1p,
    log2 as log2,
    logaddexp as logaddexp,
    logaddexp2 as logaddexp2,
    logical_and as logical_and,
    logical_not as logical_not,
    logical_or as logical_or,
    logical_xor as logical_xor,
    maximum as maximum,
    minimum as minimum,
    mod as mod,
    modf as modf,
    multiply as multiply,
    negative as negative,
    nextafter as nextafter,
    not_equal as not_equal,
    positive as positive,
    power as power,
    rad2deg as rad2deg,
    radians as radians,
    real as real,
    reciprocal as reciprocal,
    remainder as remainder,
    right_shift as right_shift,
    rint as rint,
    sign as sign,
    signbit as signbit,
    sin as sin,
    sinc as sinc,
    sinh as sinh,
    sqrt as sqrt,
    square as square,
    subtract as subtract,
    tan as tan,
    tanh as tanh,
    true_divide as true_divide,
)

from jax._src.numpy.vectorize import vectorize as vectorize

# Dynamically register numpy-style methods on JAX arrays.
from jax._src.numpy.array_methods import register_jax_array_methods
register_jax_array_methods()
del register_jax_array_methods


# Deprecations

_deprecations = {
    # Added March 14, 2023:
    "DeviceArray": (
        "jax.numpy.DeviceArray is deprecated. Use jax.Array.",
        ndarray,
    ),
    # Added June 2, 2023:
    "alltrue": (
        "jax.numpy.alltrue is deprecated. Use jax.numpy.all",
        all,
    ),
    "cumproduct": (
        "jax.numpy.cumproduct is deprecated. Use jax.numpy.cumprod",
        cumprod,
    ),
    "product": (
        "jax.numpy.product is deprecated. Use jax.numpy.prod",
        prod,
    ),
    "sometrue": (
        "jax.numpy.sometrue is deprecated. Use jax.numpy.any",
        any,
    ),
}

import typing
if typing.TYPE_CHECKING:
  from jax._src.basearray import Array as DeviceArray
  alltrue = all
  cumproduct = cumprod
  product = prod
  sometrue = any
else:
  from jax._src.deprecations import deprecation_getattr as _deprecation_getattr
  __getattr__ = _deprecation_getattr(__name__, _deprecations)
  del _deprecation_getattr
del typing
