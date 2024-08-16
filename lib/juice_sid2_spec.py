"""
    JUICE RPWI HF SID2 (RAW): L1a spec -- 2024/8/15
"""
import numpy as np
import scipy.stats as stats
import juice_cdf_lib as juice_cdf
import juice_math_lib as juice_math

class struct:
    pass


# ---------------------------------------------------------------------
# --- SID2 SPEC -------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid2_getspec(data, cal_mode):
    """
    input:  data, cal_mode
    return: spec
    """
    # Spec formation
    spec = struct()

    n_time = data.Eu_i.shape[0]
    n_freq = data.Eu_i.shape[1]
    n_samp = data.Eu_i.shape[2]

    # -- init --
    spec.freq     = np.zeros(n_time * n_freq * n_samp);  spec.freq     = spec.freq.reshape  (n_time, n_freq, n_samp)
    spec.freq_w   = np.zeros(n_time * n_freq * n_samp);  spec.freq_w   = spec.freq_w.reshape(n_time, n_freq, n_samp)

    # Frequency
    dt = 1.0 / juice_cdf._sample_rate(data.decimation[0])
    freq = np.fft.fftshift(np.fft.fftfreq(n_samp, d=dt)) / 1000.
    for i in range(n_time):
        for j in range(n_freq):
            spec.freq[i][j]   = data.frequency[i][j] + freq
            spec.freq_w[i][j] = freq[1] - freq[0]

    # FFT
    window = np.hanning(n_samp)
    acf = 1/(sum(window)/n_samp)

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
    spec.freq     = spec.freq[:, :, samp1:samp2];        spec.freq    = np.array(spec.freq).reshape(n_time, n_freq * n_samp)
    spec.freq_w   = spec.freq_w[:, :, samp1:samp2];      spec.freq_w  = np.array(spec.freq_w).reshape(n_time, n_freq * n_samp)
    #
    spec.EuEu     = spec.EuEu[:, :, samp1:samp2];        spec.EuEu    = np.array(spec.EuEu).reshape(n_time, n_freq * n_samp)
    spec.EvEv     = spec.EvEv[:, :, samp1:samp2];        spec.EvEv    = np.array(spec.EvEv).reshape(n_time, n_freq * n_samp)
    spec.EwEw     = spec.EwEw[:, :, samp1:samp2];        spec.EwEw    = np.array(spec.EwEw).reshape(n_time, n_freq * n_samp)
    #
    spec.EuEv_re  = spec.EuEv_re[:, :, samp1:samp2];     spec.EuEv_re = np.array(spec.EuEv_re).reshape(n_time, n_freq * n_samp)
    spec.EvEw_re  = spec.EvEw_re[:, :, samp1:samp2];     spec.EvEw_re = np.array(spec.EvEw_re).reshape(n_time, n_freq * n_samp)
    spec.EwEu_re  = spec.EwEu_re[:, :, samp1:samp2];     spec.EwEu_re = np.array(spec.EwEu_re).reshape(n_time, n_freq * n_samp)
    spec.EuEv_im  = spec.EuEv_im[:, :, samp1:samp2];     spec.EuEv_im = np.array(spec.EuEv_im).reshape(n_time, n_freq * n_samp)
    spec.EvEw_im  = spec.EvEw_im[:, :, samp1:samp2];     spec.EvEw_im = np.array(spec.EvEw_im).reshape(n_time, n_freq * n_samp)
    spec.EwEu_im  = spec.EwEu_im[:, :, samp1:samp2];     spec.EwEu_im = np.array(spec.EwEu_im).reshape(n_time, n_freq * n_samp)
    #
    spec.epoch    = data.epoch[:]

    """
    # Background / CAL only
    if cal_mode < 2:
        index = np.where(data.cal_signal == cal_mode)
        spec.epoch   = data.epoch  [index[0]]
        spec.freq    = spec.freq   [index[0]];  spec.freq_w  = spec.freq_w [index[0]]
        spec.EuEu    = spec.EuEu   [index[0]];  spec.EvEv    = spec.EvEv   [index[0]];  spec.EwEw    = spec.EwEw   [index[0]]
        spec.EuEv_re = spec.EuEv_re[index[0]];  spec.EvEw_re = spec.EvEw_re[index[0]];  spec.EwEu_re = spec.EwEu_re[index[0]]
        spec.EuEv_im = spec.EuEv_im[index[0]];  spec.EvEw_im = spec.EvEw_im[index[0]];  spec.EwEu_im = spec.EwEu_im[index[0]]
        if cal_mode == 0:
            print("cut: only background")
        else:
            print("cut: only CAL")
    else:
        spec.epoch = data.epoch[:]
    """
    return spec


def hf_sid2_getspec2(spec):
    """
    input:  spec
    return: spec
    """
    # Stokes and Polarization Parameters
    spec.E_Iuv,   spec.E_Quv,   spec.E_Uuv,   spec.E_Vuv   = juice_math.get_stokes(spec.EuEu,  spec.EvEv,  spec.EuEv_re, spec.EuEv_im)
    spec.E_Ivw,   spec.E_Qvw,   spec.E_Uvw,   spec.E_Vvw   = juice_math.get_stokes(spec.EvEv,  spec.EwEw,  spec.EvEw_re, spec.EvEw_im)
    spec.E_Iwu,   spec.E_Qwu,   spec.E_Uwu,   spec.E_Vwu   = juice_math.get_stokes(spec.EwEw,  spec.EuEu,  spec.EwEu_re, spec.EwEu_im)
    spec.E_DoPuv, spec.E_DoLuv, spec.E_DoCuv, spec.E_ANGuv = juice_math.get_pol   (spec.E_Iuv, spec.E_Quv, spec.E_Uuv,   spec.E_Vuv)
    spec.E_DoPvw, spec.E_DoLvw, spec.E_DoCvw, spec.E_ANGvw = juice_math.get_pol   (spec.E_Ivw, spec.E_Qvw, spec.E_Uvw,   spec.E_Vvw)
    spec.E_DoPwu, spec.E_DoLwu, spec.E_DoCwu, spec.E_ANGwu = juice_math.get_pol   (spec.E_Iwu, spec.E_Qwu, spec.E_Uwu,   spec.E_Vwu)
    # Coherency
    spec.E_COHuv = spec.EuEv_re**2 / (spec.EuEu * spec.EvEv)
    spec.E_COHvw = spec.EvEw_re**2 / (spec.EvEv * spec.EwEw)
    spec.E_COHwu = spec.EwEu_re**2 / (spec.EwEw * spec.EuEu)
    spec.E_PHAuv = np.rad2deg(np.arctan2(spec.EuEv_im, spec.EuEv_re))
    spec.E_PHAvw = np.rad2deg(np.arctan2(spec.EvEw_im, spec.EvEw_re))
    spec.E_PHAwu = np.rad2deg(np.arctan2(spec.EwEu_im, spec.EwEu_re))
    return spec