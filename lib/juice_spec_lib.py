"""
    JUICE RPWI HF: L1a spec -- 2024/9/17
"""
import copy
import math
import numpy as np
import juice_cdf_lib as juice_cdf

class struct:
    pass


def hf_getspec_angle(spec):
    """
    input:  spec
    return: spec
    """
    # Coherency
    spec.E_COHuv = spec.EuEv_re**2 / (spec.EuEu * spec.EvEv)
    spec.E_COHvw = spec.EvEw_re**2 / (spec.EvEv * spec.EwEw)
    spec.E_COHwu = spec.EwEu_re**2 / (spec.EwEw * spec.EuEu)
    spec.E_PHAuv = np.rad2deg(np.arctan2(spec.EuEv_im, spec.EuEv_re))
    spec.E_PHAvw = np.rad2deg(np.arctan2(spec.EvEw_im, spec.EvEw_re))
    spec.E_PHAwu = np.rad2deg(np.arctan2(spec.EwEu_im, spec.EwEu_re))
    return spec


def hf_getspec_stokes(spec):
    """
    input:  spec
    return: spec
    """
    spec.E_Iuv,   spec.E_Quv,   spec.E_Uuv,   spec.E_Vuv   = get_stokes(spec.EuEu,  spec.EvEv,  spec.EuEv_re, spec.EuEv_im)
    spec.E_Ivw,   spec.E_Qvw,   spec.E_Uvw,   spec.E_Vvw   = get_stokes(spec.EvEv,  spec.EwEw,  spec.EvEw_re, spec.EvEw_im)
    spec.E_Iwu,   spec.E_Qwu,   spec.E_Uwu,   spec.E_Vwu   = get_stokes(spec.EwEw,  spec.EuEu,  spec.EwEu_re, spec.EwEu_im)
    spec.E_DoPuv, spec.E_DoLuv, spec.E_DoCuv, spec.E_ANGuv = get_pol   (spec.E_Iuv, spec.E_Quv, spec.E_Uuv,   spec.E_Vuv)
    spec.E_DoPvw, spec.E_DoLvw, spec.E_DoCvw, spec.E_ANGvw = get_pol   (spec.E_Ivw, spec.E_Qvw, spec.E_Uvw,   spec.E_Vvw)
    spec.E_DoPwu, spec.E_DoLwu, spec.E_DoCwu, spec.E_ANGwu = get_pol   (spec.E_Iwu, spec.E_Qwu, spec.E_Uwu,   spec.E_Vwu)
    return spec


def hf_getspec_stokes_3d(spec):
    """
    input:  spec
    return: spec
    """
    spec.E_I_3d  = spec.EuiEui + spec.EuqEuq + spec.EviEvi + spec.EvqEvq + spec.EwiEwi + spec.EwqEwq
    spec.E_Q_3d  = spec.EuiEvi - spec.EuqEuq + spec.EviEvi - spec.EvqEvq + spec.EwiEwi - spec.EwqEwq
    spec.E_U_3d  =  2. * (spec.EuiEuq + spec.EviEvq + spec.EwiEwq)
    spec.E_Vu_3d = -2. * (spec.EviEwq - spec.EvqEwi)
    spec.E_Vv_3d = -2. * (spec.EwiEuq - spec.EwqEui)
    spec.E_Vw_3d = -2. * (spec.EuiEvq - spec.EuqEvi)
    spec.E_DoP_3d, spec.E_DoL_3d, spec.E_DoC_3d, spec.E_ANG_3d, spec.E_k_lon, spec.E_k_lat = \
        get_pol_3D(spec.E_I_3d, spec.E_Q_3d, spec.E_U_3d, spec.E_Vu_3d, spec.E_Vv_3d, spec.E_Vw_3d)
    return spec


def get_stokes(p1, p2, re, im):
    """
    Input:  EuEu, EvEv, EuEv_re, EuEv_im
    Output: I, Q, U, V: Stokes parameters [Any]
    """
    m = p1.shape[0]
    n = p1.shape[1]
    I = np.zeros((m, n))
    Q = np.zeros((m, n))
    U = np.zeros((m, n))
    V = np.zeros((m, n))
    if p1[0][0] > 0:
        I = p1 + p2     # total
        Q = p1 - p2     # 0deg -  90deg
        U = re * 2.0    # 45deg - 135deg
        V = im * 2.0    # Right -  Left  (minus?)
    return I, Q, U, V


def get_pol(I, Q, U, V):
    """
    Input:  I, Q, U, V: Stokes parameters [Any]
    Output: DoP, DoL, DoC, Ang
    """
    m = I.shape[0];  n = I.shape[1]
    dop = np.zeros((m, n))
    dol = ang = np.zeros((m, n))
    doc = np.zeros((m, n))
    ang = np.zeros((m, n))
    for j in range(m):
        if I[j][0] > 0 and Q[j][0] > -1e30 and U[j][0] > -1e30 and V[j][0] > -1e30:
            dop[j] = (Q[j]*Q[j] + U[j]*U[j] + V[j]*V[j])**0.5 / I[j]   # Degree of Total Polarization
            dol[j] = (Q[j]*Q[j] + U[j]*U[j])**0.5 / I[j]               # Degree of Linear Polarization
            doc[j] = V[j] / I[j]                                       # Degree of Circular Polarization

            for i in range(n):
                if U[j][i] >= 0.0 and Q[j][i] > 0.0:    # 0-90
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi
                elif U[j][i] <= 0.0 and Q[j][i] > 0.0:  # 270-360
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi + 180.
                elif Q[j][i] < 0.0:                     # 90-270
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi + 90.
                else:
                    if U[j][i] >= 0.0:
                        ang[j][i] = 45.
                    else:
                        ang[j][i] = 135.
    return dop, dol, doc, ang


def get_pol_3D(I, Q, U, Vu, Vv, Vw):
    """
    Input:  I, Q, U, V: Stokes parameters [Any]
    Output: DoP, DoL, DoC, Ang, k_lon, k_lat
    """
    m = I.shape[0]
    n = I.shape[1]
    dop = np.zeros((m, n))
    dol = np.zeros((m, n))
    doc = np.zeros((m, n))
    ang = np.zeros((m, n))
    k_lon = np.zeros((m, n))
    k_lat = np.zeros((m, n))
    if I[0][0] > 0:
        V_mag = (Vu*Vu + Vv*Vv + Vw*Vw)**0.5
        dop = (Q*Q + U*U + V_mag*V_mag)**0.5 / I  # Degree of Total Polari.
        dol = (Q*Q + U*U)**0.5 / I                # Degree of Linear Polari.
        doc = V_mag / I                           # Degree of Circular Polari.

        # Linear Polarization Angle (deg)
        for j in range(m):
            for i in range(n):
                if U[j][i] >= 0.0 and Q[j][i] > 0.0:    # 0-90
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi
                elif U[j][i] <= 0.0 and Q[j][i] > 0.0:  # 270-360
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi + 180.
                elif Q[j][i] < 0.0:                     # 90-270
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi + 90.
                else:
                    if U[j][i] >= 0.0:
                        ang[j][i] = 45.
                    else:
                        ang[j][i] = 135.

                #k_lat[j][i] = math.asin(Vw[j][i]/(Vu[j][i]*Vu[j][i] + Vv[j][i]*Vv[j][i])**0.5) * 180./math.pi
                k_lat[j][i] = math.atan2(Vw[j][i], (Vu[j][i]*Vu[j][i] + Vv[j][i]*Vv[j][i])**0.5) * 180./math.pi
                k_lon[j][i] = math.atan2(Vv[j][i], Vu[j][i]) * 180.0/math.pi
    return dop, dol, doc, ang, k_lon, k_lat


# ---------------------------------------------------------------------
# --- SID-2
# ---------------------------------------------------------------------
def hf_getspec_sid2(data):
    """
    input:  data
    return: spec
    """
    # Spec formation
    spec = struct()
    spec.RPWI_FSW_version = data.RPWI_FSW_version

    n_time = data.Eu_i.shape[0]
    n_freq = data.Eu_i.shape[1]
    n_samp = data.Eu_i.shape[2]

    # Frequency
    spec.freq     = np.zeros(n_time * n_freq * n_samp);  spec.freq     = spec.freq.reshape  (n_time, n_freq, n_samp)
    spec.freq_w   = np.zeros(n_time * n_freq * n_samp);  spec.freq_w   = spec.freq_w.reshape(n_time, n_freq, n_samp)
    dt = 1.0 / juice_cdf._sample_rate(data.decimation[0])
    freq = np.fft.fftshift(np.fft.fftfreq(n_samp, d=dt)) / 1000.
    for i in range(n_time):
        for j in range(n_freq):
            spec.freq[i][j]   = data.frequency[i][j] + freq
            spec.freq_w[i][j] = freq[1] - freq[0]

    # FFT
    window = np.hanning(n_samp*1.0)
    acf = 1.0/(sum(window)/n_samp) # / 1.23

    """
    # ***DEBUG***
    Eu = data.Eu_i[0][6]; Eq = data.Eu_q[0][6];  s1 = np.mean(Eu**2.0 + Eq**2.0)
    s = np.fft.fft((Eu - Eq * 1.0j) * window);  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf 
    EuEu = np.fft.fftshift(s); s2 = np.sum(EuEu)
    print(s1, s2, s2/s1, (s2/s1)**.5)
    s = np.fft.fft((Eu - Eq * 1.0j) * window);  s_u_re = s.real; s_u_im = s.imag;  s = (s_u_re*s_u_re + s_u_im*s_u_im) / n_samp**2.0 * acf**2 
    EuEu = np.fft.fftshift(s); s2 = np.sum(EuEu)
    print(s1, s2, s2/s1, (s2/s1)**.5)
    # ***DEBUG***
    """

    # -- auto
    s = np.fft.fft((data.Eu_i - data.Eu_q * 1j) * window);  s_u_re = s.real; s_u_im = s.imag;  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf; spec.EuEu = np.fft.fftshift(s, axes=(2,))
    s = np.fft.fft((data.Ev_i - data.Ev_q * 1j) * window);  s_v_re = s.real; s_v_im = s.imag;  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf; spec.EvEv = np.fft.fftshift(s, axes=(2,))
    s = np.fft.fft((data.Ew_i - data.Ew_q * 1j) * window);  s_w_re = s.real; s_w_im = s.imag;  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf; spec.EwEw = np.fft.fftshift(s, axes=(2,))
    # -- cross
    s = s_u_re * s_v_re + s_u_im * s_v_im;  s = s / n_samp / n_samp * acf * acf;  spec.EuEv_re = np.fft.fftshift(s, axes=(2,))
    s = s_v_re * s_w_re + s_v_im * s_w_im;  s = s / n_samp / n_samp * acf * acf;  spec.EvEw_re = np.fft.fftshift(s, axes=(2,))
    s = s_w_re * s_u_re + s_w_im * s_u_im;  s = s / n_samp / n_samp * acf * acf;  spec.EwEu_re = np.fft.fftshift(s, axes=(2,))
    s = s_u_im * s_v_re - s_u_re * s_v_im;  s = s / n_samp / n_samp * acf * acf;  spec.EuEv_im = np.fft.fftshift(s, axes=(2,))
    s = s_v_im * s_w_re - s_v_re * s_w_im;  s = s / n_samp / n_samp * acf * acf;  spec.EvEw_im = np.fft.fftshift(s, axes=(2,))
    s = s_w_im * s_u_re - s_w_re * s_u_im;  s = s / n_samp / n_samp * acf * acf;  spec.EwEu_im = np.fft.fftshift(s, axes=(2,))

    # Cut: 75%
    samp1 = n_samp//8           # 0
    samp2 = n_samp - n_samp//8  # n_samp

    # for i in range(data.n_freq - 1):
    i = 0
    while (spec.freq[0][i][samp2] > spec.freq[0][i+1][samp1]):
        samp1 += 1; samp2 -= 1
    print("cut: 1st-start/end 2nd-first-end:", spec.freq[0][i][samp2], spec.freq[0][i+1][samp1], 100*(samp2-samp1)/n_samp, "%") 
    n_samp = samp2 - samp1
    #
    spec.freq     = spec.freq   [:, :, samp1:samp2];     spec.freq    = np.array(spec.freq).reshape   (n_time, n_freq * n_samp)
    spec.freq_w   = spec.freq_w [:, :, samp1:samp2];     spec.freq_w  = np.array(spec.freq_w).reshape (n_time, n_freq * n_samp)
    # 
    spec.EuEu     = spec.EuEu   [:, :, samp1:samp2];     spec.EuEu    = np.array(spec.EuEu).reshape   (n_time, n_freq * n_samp)
    spec.EvEv     = spec.EvEv   [:, :, samp1:samp2];     spec.EvEv    = np.array(spec.EvEv).reshape   (n_time, n_freq * n_samp)
    spec.EwEw     = spec.EwEw   [:, :, samp1:samp2];     spec.EwEw    = np.array(spec.EwEw).reshape   (n_time, n_freq * n_samp)
    #
    spec.EuEv_re  = spec.EuEv_re[:, :, samp1:samp2];     spec.EuEv_re = np.array(spec.EuEv_re).reshape(n_time, n_freq * n_samp)
    spec.EvEw_re  = spec.EvEw_re[:, :, samp1:samp2];     spec.EvEw_re = np.array(spec.EvEw_re).reshape(n_time, n_freq * n_samp)
    spec.EwEu_re  = spec.EwEu_re[:, :, samp1:samp2];     spec.EwEu_re = np.array(spec.EwEu_re).reshape(n_time, n_freq * n_samp)
    spec.EuEv_im  = spec.EuEv_im[:, :, samp1:samp2];     spec.EuEv_im = np.array(spec.EuEv_im).reshape(n_time, n_freq * n_samp)
    spec.EvEw_im  = spec.EvEw_im[:, :, samp1:samp2];     spec.EvEw_im = np.array(spec.EvEw_im).reshape(n_time, n_freq * n_samp)
    spec.EwEu_im  = spec.EwEu_im[:, :, samp1:samp2];     spec.EwEu_im = np.array(spec.EwEu_im).reshape(n_time, n_freq * n_samp)
    #
    spec.epoch    = data.epoch[:]
    return spec


# ---------------------------------------------------------------------
# --- SID-23
# ---------------------------------------------------------------------
def hf_getspec_sid23(data):
    """
    input:  data
    return: spec
    """
    # Spec formation
    spec = struct()
    spec.RPWI_FSW_version = data.RPWI_FSW_version

    n_time  = data.Eu_i.shape[0]
    n_block = data.Eu_i.shape[1]
    n_samp  = data.Eu_i.shape[2]     # data.N_feed[0]*128

    # -- init --
    spec.freq     = np.zeros(n_time * n_block * n_samp);  spec.freq     = spec.freq.reshape  (n_time, n_block, n_samp)
    spec.freq_w   = np.zeros(n_time * n_block * n_samp);  spec.freq_w   = spec.freq_w.reshape(n_time, n_block, n_samp)

    # Frequency
    dt = 1.0 / juice_cdf._sample_rate(data.decimation[0])
    freq = np.fft.fftshift(np.fft.fftfreq(n_samp, d=dt)) / 1000.
    for i in range(n_time):
        for j in range(n_block):
            spec.freq[i][j]   = data.freq_center[i] + freq
            spec.freq_w[i][j] = freq[1] - freq[0]
    print("freq:", spec.freq.shape, spec.freq_w.shape)
    print("freq:", spec.freq[0][0], spec.freq_w[0][0])

    """
    # Frequency
    dt = 1.0 / juice_cdf._sample_rate(data.decimation_AUX[0])
    spec.freq = np.fft.fftshift(np.fft.fftfreq(data.N_feed[0]*128, d=dt)) / 1000.
    spec.freq = spec.freq + data.freq_center[0]
    spec.freq_w = spec.freq[1] - spec.freq[0]
    print("freq:", spec.freq.shape, spec.freq_w.shape)
    """

    # FFT
    window = np.hanning(n_samp)
    acf = 1/(sum(window)/n_samp)
    #
    # -- auto
    s = np.fft.fft((data.Eu_i - data.Eu_q * 1j) * window);  s_u_re = s.real; s_u_im = s.imag;  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf; spec.EuEu = np.fft.fftshift(s, axes=(2,))
    s = np.fft.fft((data.Ev_i - data.Ev_q * 1j) * window);  s_v_re = s.real; s_v_im = s.imag;  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf; spec.EvEv = np.fft.fftshift(s, axes=(2,))
    s = np.fft.fft((data.Ew_i - data.Ew_q * 1j) * window);  s_w_re = s.real; s_w_im = s.imag;  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf; spec.EwEw = np.fft.fftshift(s, axes=(2,))
    spec.EE   = spec.EuEu + spec.EvEv + spec.EwEw
    # -- cross
    s = s_u_re * s_v_re + s_u_im * s_v_im;  s = s / n_samp / n_samp * acf * acf;  spec.EuEv_re = np.fft.fftshift(s, axes=(2,))
    s = s_v_re * s_w_re + s_v_im * s_w_im;  s = s / n_samp / n_samp * acf * acf;  spec.EvEw_re = np.fft.fftshift(s, axes=(2,))
    s = s_w_re * s_u_re + s_w_im * s_u_im;  s = s / n_samp / n_samp * acf * acf;  spec.EwEu_re = np.fft.fftshift(s, axes=(2,))
    s = s_u_im * s_v_re - s_u_re * s_v_im;  s = s / n_samp / n_samp * acf * acf;  spec.EuEv_im = np.fft.fftshift(s, axes=(2,))
    s = s_v_im * s_w_re - s_v_re * s_w_im;  s = s / n_samp / n_samp * acf * acf;  spec.EvEw_im = np.fft.fftshift(s, axes=(2,))
    s = s_w_im * s_u_re - s_w_re * s_u_im;  s = s / n_samp / n_samp * acf * acf;  spec.EwEu_im = np.fft.fftshift(s, axes=(2,))

    # Stokes Parameters and Polarization
    spec.E_Iuv   = copy.copy(spec.EE);  spec.E_Quv   = copy.copy(spec.EE);  spec.E_Uuv   = copy.copy(spec.EE);  spec.E_Vuv   = copy.copy(spec.EE) 
    spec.E_Ivw   = copy.copy(spec.EE);  spec.E_Qvw   = copy.copy(spec.EE);  spec.E_Uvw   = copy.copy(spec.EE);  spec.E_Vvw   = copy.copy(spec.EE) 
    spec.E_Iwu   = copy.copy(spec.EE);  spec.E_Qwu   = copy.copy(spec.EE);  spec.E_Uwu   = copy.copy(spec.EE);  spec.E_Vwu   = copy.copy(spec.EE) 
    spec.E_DoPuv = copy.copy(spec.EE);  spec.E_DoLuv = copy.copy(spec.EE);  spec.E_DoCuv = copy.copy(spec.EE);  spec.E_ANGuv = copy.copy(spec.EE) 
    spec.E_DoPvw = copy.copy(spec.EE);  spec.E_DoLvw = copy.copy(spec.EE);  spec.E_DoCvw = copy.copy(spec.EE);  spec.E_ANGvw = copy.copy(spec.EE) 
    spec.E_DoPwu = copy.copy(spec.EE);  spec.E_DoLwu = copy.copy(spec.EE);  spec.E_DoCwu = copy.copy(spec.EE);  spec.E_ANGwu = copy.copy(spec.EE) 
    for i in range(n_time):
        spec.E_Iuv[i],   spec.E_Quv[i],   spec.E_Uuv[i],   spec.E_Vuv[i]   = get_stokes(spec.EuEu[i],  spec.EvEv[i],  spec.EuEv_re[i], spec.EuEv_im[i])
        spec.E_Ivw[i],   spec.E_Qvw[i],   spec.E_Uvw[i],   spec.E_Vvw[i]   = get_stokes(spec.EvEv[i],  spec.EwEw[i],  spec.EvEw_re[i], spec.EvEw_im[i])
        spec.E_Iwu[i],   spec.E_Qwu[i],   spec.E_Uwu[i],   spec.E_Vwu[i]   = get_stokes(spec.EwEw[i],  spec.EuEu[i],  spec.EwEu_re[i], spec.EwEu_im[i])
        spec.E_DoPuv[i], spec.E_DoLuv[i], spec.E_DoCuv[i], spec.E_ANGuv[i] = get_pol   (spec.E_Iuv[i], spec.E_Quv[i], spec.E_Uuv[i],   spec.E_Vuv[i])
        spec.E_DoPvw[i], spec.E_DoLvw[i], spec.E_DoCvw[i], spec.E_ANGvw[i] = get_pol   (spec.E_Ivw[i], spec.E_Qvw[i], spec.E_Uvw[i],   spec.E_Vvw[i])
        spec.E_DoPwu[i], spec.E_DoLwu[i], spec.E_DoCwu[i], spec.E_ANGwu[i] = get_pol   (spec.E_Iwu[i], spec.E_Qwu[i], spec.E_Uwu[i],   spec.E_Vwu[i])

    print("EuEu:", spec.EuEu.shape)
    return spec


# ---------------------------------------------------------------------
# --- generic
# ---------------------------------------------------------------------
"""
def hf_getspec(data):
    # input:  data    waveform:      Eu_i, Eu_q, Ev_i, Ev_q, Ew_i, Ew_q   ([n_time, n_samp], For usual waveform, "*_i" can be set as 0.)
    #                 sampling rate: sample_rate (/sec)
    # return: spec   
    # Spec formation
    spec = struct()
    spec.RPWI_FSW_version = data.RPWI_FSW_version

    n_time = data.Eu_i.shape[0]
    n_samp = data.Eu_i.shape[1]

    # Frequency
    dt = 1.0 / data.sample_rate
    spec.freq    = np.fft.fftshift(np.fft.fftfreq(n_samp, d=dt))
    spec.freq_w  = spec.freq[1] - spec.freq[0]
    print("freq:", spec.freq[0], spec.freq[-1], spec.freq_w[0])

    # FFT
    window = np.hanning(n_samp)
    acf = 1/(sum(window)/n_samp)
    #
    # -- auto
    s = np.fft.fft((data.Eu_i - data.Eu_q * 1j) * window);  s_u_re = s.real; s_u_im = s.imag;  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf; spec.EuEu = np.fft.fftshift(s, axes=(1,))
    s = np.fft.fft((data.Ev_i - data.Ev_q * 1j) * window);  s_v_re = s.real; s_v_im = s.imag;  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf; spec.EvEv = np.fft.fftshift(s, axes=(1,))
    s = np.fft.fft((data.Ew_i - data.Ew_q * 1j) * window);  s_w_re = s.real; s_w_im = s.imag;  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf; spec.EwEw = np.fft.fftshift(s, axes=(1,))
    spec.EE   = spec.EuEu + spec.EvEv + spec.EwEw
    # -- cross
    s = s_u_re * s_v_re + s_u_im * s_v_im;  s = s / n_samp / n_samp * acf * acf;  spec.EuEv_re = np.fft.fftshift(s, axes=(1,))
    s = s_v_re * s_w_re + s_v_im * s_w_im;  s = s / n_samp / n_samp * acf * acf;  spec.EvEw_re = np.fft.fftshift(s, axes=(1,))
    s = s_w_re * s_u_re + s_w_im * s_u_im;  s = s / n_samp / n_samp * acf * acf;  spec.EwEu_re = np.fft.fftshift(s, axes=(1,))
    s = s_u_im * s_v_re - s_u_re * s_v_im;  s = s / n_samp / n_samp * acf * acf;  spec.EuEv_im = np.fft.fftshift(s, axes=(1,))
    s = s_v_im * s_w_re - s_v_re * s_w_im;  s = s / n_samp / n_samp * acf * acf;  spec.EvEw_im = np.fft.fftshift(s, axes=(1,))
    s = s_w_im * s_u_re - s_w_re * s_u_im;  s = s / n_samp / n_samp * acf * acf;  spec.EwEu_im = np.fft.fftshift(s, axes=(1,))

    # Stokes Parameters and Polarization
    spec.E_Iuv   = copy.copy(spec.EE);  spec.E_Quv   = copy.copy(spec.EE);  spec.E_Uuv   = copy.copy(spec.EE);  spec.E_Vuv   = copy.copy(spec.EE) 
    spec.E_Ivw   = copy.copy(spec.EE);  spec.E_Qvw   = copy.copy(spec.EE);  spec.E_Uvw   = copy.copy(spec.EE);  spec.E_Vvw   = copy.copy(spec.EE) 
    spec.E_Iwu   = copy.copy(spec.EE);  spec.E_Qwu   = copy.copy(spec.EE);  spec.E_Uwu   = copy.copy(spec.EE);  spec.E_Vwu   = copy.copy(spec.EE) 
    spec.E_DoPuv = copy.copy(spec.EE);  spec.E_DoLuv = copy.copy(spec.EE);  spec.E_DoCuv = copy.copy(spec.EE);  spec.E_ANGuv = copy.copy(spec.EE) 
    spec.E_DoPvw = copy.copy(spec.EE);  spec.E_DoLvw = copy.copy(spec.EE);  spec.E_DoCvw = copy.copy(spec.EE);  spec.E_ANGvw = copy.copy(spec.EE) 
    spec.E_DoPwu = copy.copy(spec.EE);  spec.E_DoLwu = copy.copy(spec.EE);  spec.E_DoCwu = copy.copy(spec.EE);  spec.E_ANGwu = copy.copy(spec.EE) 
    for i in range(n_time):
        spec.E_Iuv[i],   spec.E_Quv[i],   spec.E_Uuv[i],   spec.E_Vuv[i]   = get_stokes(spec.EuEu[i],  spec.EvEv[i],  spec.EuEv_re[i], spec.EuEv_im[i])
        spec.E_Ivw[i],   spec.E_Qvw[i],   spec.E_Uvw[i],   spec.E_Vvw[i]   = get_stokes(spec.EvEv[i],  spec.EwEw[i],  spec.EvEw_re[i], spec.EvEw_im[i])
        spec.E_Iwu[i],   spec.E_Qwu[i],   spec.E_Uwu[i],   spec.E_Vwu[i]   = get_stokes(spec.EwEw[i],  spec.EuEu[i],  spec.EwEu_re[i], spec.EwEu_im[i])
        spec.E_DoPuv[i], spec.E_DoLuv[i], spec.E_DoCuv[i], spec.E_ANGuv[i] = get_pol   (spec.E_Iuv[i], spec.E_Quv[i], spec.E_Uuv[i],   spec.E_Vuv[i])
        spec.E_DoPvw[i], spec.E_DoLvw[i], spec.E_DoCvw[i], spec.E_ANGvw[i] = get_pol   (spec.E_Ivw[i], spec.E_Qvw[i], spec.E_Uvw[i],   spec.E_Vvw[i])
        spec.E_DoPwu[i], spec.E_DoLwu[i], spec.E_DoCwu[i], spec.E_ANGwu[i] = get_pol   (spec.E_Iwu[i], spec.E_Qwu[i], spec.E_Uwu[i],   spec.E_Vwu[i])

    print("EuEu:", spec.EuEu.shape)
    return spec
"""
