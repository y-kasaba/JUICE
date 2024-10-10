"""
    JUICE SPICE LIB -- 2024/10/6
"""
# import datetime
import math
import numpy as np
import spiceypy as spice
from planetary_coverage import MetaKernel

# ---------------------------------------------------------
# Geometry file name
# ---------------------------------------------------------
def name_geometry(ID_target, ID_observer, ID_frame, Epoch_min, Epoch_max):
    """
    ID_target   = 3         # 0:Sun  3:Earth  5:Jupiter  52:Europa  53:Ganymede  54:Callisto  99:JUICE
    ID_observer = 99        # 0:Sun  3:Earth  5:Jupiter  52:Europa  53:Ganymede  54:Callisto  99:JUICE
    ID_frame    = 99        # 0:Sun  3:Earth  5:Jupiter  52:Europa  53:Ganymede  54:Callisto  99:JUICE  991:RWI
    Epoch_min   = '2024-08-19 00:00:00'
    Epoch_max   = '2024-08-24 00:00:00'
    """
    if   ID_target   == 0:   name_target   = 'SUN'
    elif ID_target   == 3:   name_target   = 'EARTH'
    elif ID_target   == 5:   name_target   = 'JUPITER'
    elif ID_target   == 52:  name_target   = 'EUROPA'
    elif ID_target   == 53:  name_target   = 'GANYMEDE'
    elif ID_target   == 54:  name_target   = 'CALLISTO'
    elif ID_target   == 99:  name_target   = 'SC'
    else:                    print("!!! ID_target error !!! : ", ID_target)
    #
    if   ID_observer == 0:   name_observer = 'SUN'
    elif ID_observer == 3:   name_observer = 'EARTH'
    elif ID_observer == 5:   name_observer = 'JUPITER'
    elif ID_observer == 52:  name_observer = 'EUROPA'
    elif ID_observer == 53:  name_observer = 'GANYMEDE'
    elif ID_observer == 54:  name_observer = 'CALLISTO'
    elif ID_observer == 99:  name_observer = 'SC'
    else:                    print("!!! ID_observer error !!! : ", ID_observer)
    #
    if   ID_frame    == 0:   name_frame    = 'SUN'
    elif ID_frame    == 3:   name_frame    = 'EARTH'
    elif ID_frame    == 5:   name_frame    = 'JUPITER'
    elif ID_frame    == 52:  name_frame    = 'EUROPA'
    elif ID_frame    == 53:  name_frame    = 'GANYMEDE'
    elif ID_frame    == 54:  name_frame    = 'CALLISTO'
    elif ID_frame    == 99:  name_frame    = 'SC'
    elif ID_frame    == 991: name_frame    = 'RWI'
    else:                    print("!!! ID_frame error !!! : ", ID_frame)
    #
    name_yyyymm = Epoch_min[0:4] + Epoch_min[5:7]
    #
    name_file = 'JUICE_' + name_target + '_' + name_observer+ '_' +  name_frame + '_' +  name_yyyymm + '.csv'
    #
    return  name_file, name_target, name_observer, name_frame 


# ---------------------------------------------------------
# Load NAIF SPICE kernels for S/C
# ---------------------------------------------------------
def spice_ini(source_dir):
    # load spice kernel files
    spice.furnsh(source_dir + 'spk/juice_crema_5_1_150lb_23_1_v01.bsp')
    spice.furnsh(source_dir + 'spk/jup365_19900101_20500101.bsp')
    spice.furnsh(source_dir + 'spk/de432s.bsp')
    spice.furnsh(source_dir + 'lsk/naif0012.tls')
    spice.furnsh(source_dir + 'pck/pck00011.tpc')
    return

def spice_predict_ini(source_dir):
    # load spice kernel files
    # spice.furnsh(source_dir + "mk/juice_ops.tm")
    # spice.furnsh(source_dir + "mk/juice_plan.tm")
    spice.furnsh(MetaKernel(source_dir + "mk/juice_plan.tm", kernels=source_dir))
    #
    spice.furnsh(source_dir + "ck/juice_sc_crema_5_1_150lb_default_v01.bc")
    spice.furnsh(source_dir + "spk/jup365_19900101_20500101.bsp")
    spice.furnsh(source_dir + "spk/de432s.bsp")
    spice.furnsh(source_dir + "lsk/naif0012.tls")
    spice.furnsh(source_dir + "pck/pck00011.tpc")

    return


# ---------------------------------------------------------
#   Calculate JUICE orbit
#   refernce target on the x-axis: x_ref
#   reference frame: ref
#   target: tar
#   origin: org
#   light time correction: corr
# ---------------------------------------------------------
def get_pos_xref(et, ref="IAU_SUN", tar="JUICE", org="SUN", x_ref="JUPITER", corr="LT+S"):
    """_return JUICE orbit from Sun_

    Args:
        et (_np.array_): _time array_
        ref (str, optional): _referrence_. Defaults to 'IAU_SUN'.
        tar (str, optional): _target_. Defaults to 'JUICE'.
        org (str, optional): _observer_. Defaults to 'SUN'.
        x_ref (str, optional): _x_axis definition (direction from org to x_ref in x-y plane is defied as x_axis)_. Defaults to 'JUPITER'.
        corr (str, optional): _light time correction_. Defaults to 'LT+S'.

    Returns:
        _np.ndarray?_: _[[x,y,z,r,lat,lon](t1), [x,y,z,r,lat,lon](t2), [..](t3),[] ... []]_
    """

    # number of data
    nd = len(et)

    # get S/C orbit
    x = np.zeros(nd)
    y = np.zeros(nd)
    z = np.zeros(nd)
    r = np.zeros(nd)
    lat = np.zeros(nd)
    lon = np.zeros(nd)

    # spice temporal variable
    vec_z = [0.0, 0.0, 1.0]

    for i in range(0, nd):

        # Get state vector of S/C
        [state, lttime] = spice.spkezr(tar, et[i], ref, corr, org)
        x_s = state[0]
        y_s = state[1]
        z_s = state[2]

        # Get state vector of reference target
        [state, lttime] = spice.spkezr(x_ref, et[i], ref, corr, org)
        x_r = state[0]
        y_r = state[1]
        z_r = state[2]

        vec_x = [x_r, y_r, 0.0]
        # x軸(1)をvec_x にz軸をvec_zにする座標変換行列を返す
        mout = spice.twovec(vec_x, 1, vec_z, 3)
        vec_in = [x_s, y_s, z_s]
        vec_out = spice.mxv(mout, vec_in)  # 座標変換のための行列を

        x[i] = vec_out[0]
        y[i] = vec_out[1]
        z[i] = vec_out[2]
        r[i] = math.sqrt(x[i] ** 2 + y[i] ** 2 + z[i] ** 2)
        lat[i] = math.asin(z[i] / r[i])
        lon[i] = math.atan2(y[i], x[i])

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate JUICE orbit
#   reference frame: IAU_SUN
#   target: JUICE
#   origin: SUN
#   refernce target on the x-axis: x_ref
# ---------------------------------------------------------
def get_juice_pos_sun(et, x_ref="JUPITER"):

    x, y, z, r, lat, lon = get_pos_xref(
        et, ref="IAU_SUN", tar="JUICE", org="SUN", x_ref=x_ref, corr="LT+S"
    )

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate JUICE orbit
#   reference frame: IAU_JUPITER
#   target: JUICE
#   origin: JUPITER
#   refernce target on the x-axis: x_ref
# ---------------------------------------------------------
def get_juice_pos_jup(et, x_ref="GANYMEDE"):

    x, y, z, r, lat, lon = get_pos_xref(
        et, ref="IAU_JUPITER", tar="JUICE", org="JUPITER", x_ref=x_ref, corr="LT+S"
    )

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate JUICE orbit
#   reference frame: IAU_EARTH
#   target: JUICE
#   origin: EARTH
#   refernce target on the x-axis: x_ref
# ---------------------------------------------------------
def get_juice_pos_earth(et, x_ref="SUN"):

    x, y, z, r, lat, lon = get_pos_xref(
        et, ref="IAU_EARTH", tar="JUICE", org="EARTH", x_ref=x_ref, corr="LT+S"
    )

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate Moon orbit
#   reference frame: IAU_EARTH
#   target: JUICE
#   origin: EARTH
#   refernce target on the x-axis: x_ref
# ---------------------------------------------------------
def get_moon_pos_earth(et, x_ref="SUN"):

    x, y, z, r, lat, lon = get_pos_xref(
        et, ref="IAU_EARTH", tar="Moon", org="EARTH", x_ref=x_ref, corr="LT+S"
    )

    return [x, y, z, r, lat, lon]


# ---------------------------------------------------------
#   Calculate JUICE orbit
#   reference frame: IAU_MOON
#   target: JUICE
#   origin: MOON
#   refernce target on the x-axis: x_ref
# ---------------------------------------------------------
def get_juice_pos_moon(et, x_ref="SUN"):

    x, y, z, r, lat, lon = get_pos_xref(
        et, ref="IAU_MOON", tar="JUICE", org="MOON", x_ref=x_ref, corr="LT+S"
    )

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate JUICE orbit
#   reference frame: IAU_VENUS
#   target: JUICE
#   origin: VENUS
#   refernce target on the x-axis: x_ref
# ---------------------------------------------------------
def get_juice_pos_venus(et, x_ref="SUN"):

    x, y, z, r, lat, lon = get_pos_xref(
        et, ref="IAU_VENUS", tar="JUICE", org="VENUS", x_ref=x_ref, corr="LT+S"
    )

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate orbit
#   reference frame: ref
#   origin: org
#   target: tar
# ---------------------------------------------------------
def get_pos(et, ref="IAU_SUN", tar="JUICE", org="SUN"):

    # light time correction
    corr = "LT+S"

    # number of data
    nd = len(et)

    # get S/C orbit
    x = np.zeros(nd)
    y = np.zeros(nd)
    z = np.zeros(nd)
    r = np.zeros(nd)
    lat = np.zeros(nd)
    lon = np.zeros(nd)

    for i in range(0, nd):

        # Get state vector of target
        [state, lttime] = spice.spkezr(tar, et[i], ref, corr, org)
        x[i] = state[0]
        y[i] = state[1]
        z[i] = state[2]
        r[i] = math.sqrt(x[i] ** 2 + y[i] ** 2 + z[i] ** 2)
        lat[i] = math.asin(z[i] / r[i])
        lon[i] = math.atan2(y[i], x[i])

    return [x, y, z, r, lat, lon]


# ---------------------------------------------------------
#   Calculate JUICE orbit
#   reference frame: ref
#   target: tar
#   origin: org
#   refernce target on the x-axis: x_ref
#   light time correction: corr
#
#   new reference frame for output position of this function
#   x : vector from the origin to the reference target
#   y : vector of the orbital direction of the reference target
# ---------------------------------------------------------
def get_pos_ref(
    et, ref="IAU_JUPITER", tar="JUICE", org="JUPITER", tar_ref="GANYMEDE", corr="LT+S"
):

    # number of data
    nd = len(et)

    # get target orbit
    x = np.zeros(nd)
    y = np.zeros(nd)
    z = np.zeros(nd)
    r = np.zeros(nd)
    lat = np.zeros(nd)
    lon = np.zeros(nd)

    for i in range(0, nd):

        # Get state vector of target
        [state, lttime] = spice.spkezr(tar, et[i], ref, corr, org)
        x_t = [state[0], state[1], state[2]]

        # Get state vector of reference target
        [state, lttime] = spice.spkezr(tar_ref, et[i], ref, corr, org)
        x_r = [state[0], state[1], state[2]]
        v_r = [state[3], state[4], state[5]]
        r_r = math.sqrt(x_r[0] ** 2 + x_r[1] ** 2 + x_r[2] ** 2)

        # create a plane whose normal vector is parallel to org-ref_target and at position of ref_target
        plane = spice.nvc2pl(x_r, r_r)
        # project v_r onto the plane
        vec_y = spice.vprjp(v_r, plane)

        mout = spice.twovec(x_r, 1, vec_y, 2)
        vec_out = spice.mxv(mout, x_t)

        x[i] = vec_out[0]
        y[i] = vec_out[1]
        z[i] = vec_out[2]
        r[i] = math.sqrt(x[i] ** 2 + y[i] ** 2 + z[i] ** 2)
        lat[i] = math.asin(z[i] / r[i])
        lon[i] = math.atan2(y[i], x[i])

    return [x, y, z, r, lat, lon]
