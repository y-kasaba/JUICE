"""
    JUICE RPWI HF SID2 (RAW): L1a spec -- 2024/7/18
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
    spec.freq     = np.zeros(n_time * n_freq * n_samp);  spec.freq     = spec.freq.reshape(n_time, n_freq, n_samp)
    spec.freq_w   = np.zeros(n_time * n_freq * n_samp);  spec.freq_w   = spec.freq_w.reshape(n_time, n_freq, n_samp)
    # spec.freq_cen = np.zeros(n_time * n_freq * n_samp);  spec.freq_cen = spec.freq_cen.reshape(n_time, n_freq, n_samp)
    # spec.freq_num = np.zeros(n_time * n_freq * n_samp);  spec.freq_num = spec.freq_num.reshape(n_time, n_freq, n_samp)
    #
    """
    spec.EE       = np.zeros(n_time * n_freq * n_samp);  spec.EE       = spec.EE.reshape(n_time, n_freq, n_samp)
    spec.EuEu     = np.zeros(n_time * n_freq * n_samp);  spec.EuEu     = spec.EuEu.reshape(n_time, n_freq, n_samp)
    spec.EvEv     = np.zeros(n_time * n_freq * n_samp);  spec.EvEv     = spec.EvEv.reshape(n_time, n_freq, n_samp)
    spec.EwEw     = np.zeros(n_time * n_freq * n_samp);  spec.EwEw     = spec.EwEw.reshape(n_time, n_freq, n_samp)
    spec.EuEv_re  = np.zeros(n_time * n_freq * n_samp);  spec.EuEv_re  = spec.EuEv_re.reshape(n_time, n_freq, n_samp)
    spec.EvEw_re  = np.zeros(n_time * n_freq * n_samp);  spec.EvEw_re  = spec.EvEw_re.reshape(n_time, n_freq, n_samp)
    spec.EwEu_re  = np.zeros(n_time * n_freq * n_samp);  spec.EwEu_re  = spec.EwEu_re.reshape(n_time, n_freq, n_samp)
    spec.EuEv_im  = np.zeros(n_time * n_freq * n_samp);  spec.EuEv_im  = spec.EuEv_re.reshape(n_time, n_freq, n_samp)
    spec.EvEw_im  = np.zeros(n_time * n_freq * n_samp);  spec.EvEw_im  = spec.EvEw_re.reshape(n_time, n_freq, n_samp)
    spec.EwEu_im  = np.zeros(n_time * n_freq * n_samp);  spec.EwEu_im  = spec.EwEu_re.reshape(n_time, n_freq, n_samp)
    #
    spec.E_Iuv    = np.zeros(n_time * n_freq * n_samp);  spec.E_Iuv    = spec.E_Iuv.reshape(n_time, n_freq, n_samp) 
    spec.E_Quv    = np.zeros(n_time * n_freq * n_samp);  spec.E_Quv    = spec.E_Quv.reshape(n_time, n_freq, n_samp) 
    spec.E_Uuv    = np.zeros(n_time * n_freq * n_samp);  spec.E_Uuv    = spec.E_Uuv.reshape(n_time, n_freq, n_samp)
    spec.E_Vuv    = np.zeros(n_time * n_freq * n_samp);  spec.E_Vuv    = spec.E_Vuv.reshape(n_time, n_freq, n_samp)
    spec.E_Ivw    = np.zeros(n_time * n_freq * n_samp);  spec.E_Ivw    = spec.E_Ivw.reshape(n_time, n_freq, n_samp) 
    spec.E_Qvw    = np.zeros(n_time * n_freq * n_samp);  spec.E_Qvw    = spec.E_Qvw.reshape(n_time, n_freq, n_samp) 
    spec.E_Uvw    = np.zeros(n_time * n_freq * n_samp);  spec.E_Uvw    = spec.E_Uvw.reshape(n_time, n_freq, n_samp)
    spec.E_Vvw    = np.zeros(n_time * n_freq * n_samp);  spec.E_Vvw    = spec.E_Vvw.reshape(n_time, n_freq, n_samp)
    spec.E_Iwu    = np.zeros(n_time * n_freq * n_samp);  spec.E_Iwu    = spec.E_Iwu.reshape(n_time, n_freq, n_samp) 
    spec.E_Qwu    = np.zeros(n_time * n_freq * n_samp);  spec.E_Qwu    = spec.E_Qwu.reshape(n_time, n_freq, n_samp) 
    spec.E_Uwu    = np.zeros(n_time * n_freq * n_samp);  spec.E_Uwu    = spec.E_Uwu.reshape(n_time, n_freq, n_samp)
    spec.E_Vwu    = np.zeros(n_time * n_freq * n_samp);  spec.E_Vwu    = spec.E_Vwu.reshape(n_time, n_freq, n_samp)
    #
    spec.E_DoPuv  = np.zeros(n_time * n_freq * n_samp);  spec.E_DoPuv  = spec.E_DoPuv.reshape(n_time, n_freq, n_samp)
    spec.E_DoLuv  = np.zeros(n_time * n_freq * n_samp);  spec.E_DoLuv  = spec.E_DoLuv.reshape(n_time, n_freq, n_samp)
    spec.E_DoCuv  = np.zeros(n_time * n_freq * n_samp);  spec.E_DoCuv  = spec.E_DoCuv.reshape(n_time, n_freq, n_samp)
    spec.E_ANGuv  = np.zeros(n_time * n_freq * n_samp);  spec.E_ANGuv  = spec.E_ANGuv.reshape(n_time, n_freq, n_samp)
    spec.E_DoPvw  = np.zeros(n_time * n_freq * n_samp);  spec.E_DoPvw  = spec.E_DoPvw.reshape(n_time, n_freq, n_samp)
    spec.E_DoLvw  = np.zeros(n_time * n_freq * n_samp);  spec.E_DoLvw  = spec.E_DoLvw.reshape(n_time, n_freq, n_samp)
    spec.E_DoCvw  = np.zeros(n_time * n_freq * n_samp);  spec.E_DoCvw  = spec.E_DoCvw.reshape(n_time, n_freq, n_samp)
    spec.E_ANGvw  = np.zeros(n_time * n_freq * n_samp);  spec.E_ANGvw  = spec.E_ANGvw.reshape(n_time, n_freq, n_samp)
    spec.E_DoPwu  = np.zeros(n_time * n_freq * n_samp);  spec.E_DoPwu  = spec.E_DoPwu.reshape(n_time, n_freq, n_samp)
    spec.E_DoLwu  = np.zeros(n_time * n_freq * n_samp);  spec.E_DoLwu  = spec.E_DoLwu.reshape(n_time, n_freq, n_samp)
    spec.E_DoCwu  = np.zeros(n_time * n_freq * n_samp);  spec.E_DoCwu  = spec.E_DoCwu.reshape(n_time, n_freq, n_samp)
    spec.E_ANGwu  = np.zeros(n_time * n_freq * n_samp);  spec.E_ANGwu  = spec.E_ANGwu.reshape(n_time, n_freq, n_samp)
    """

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
    spec.EE   = spec.EuEu + spec.EvEv + spec.EwEw
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
    spec.EE       = spec.EE  [:, :, samp1:samp2];        spec.EE      = np.array(spec.EE).reshape(n_time, n_freq * n_samp)
    #
    spec.EuEv_re  = spec.EuEv_re[:, :, samp1:samp2];     spec.EuEv_re = np.array(spec.EuEv_re).reshape(n_time, n_freq * n_samp)
    spec.EvEw_re  = spec.EvEw_re[:, :, samp1:samp2];     spec.EvEw_re = np.array(spec.EvEw_re).reshape(n_time, n_freq * n_samp)
    spec.EwEu_re  = spec.EwEu_re[:, :, samp1:samp2];     spec.EwEu_re = np.array(spec.EwEu_re).reshape(n_time, n_freq * n_samp)
    spec.EuEv_im  = spec.EuEv_im[:, :, samp1:samp2];     spec.EuEv_im = np.array(spec.EuEv_im).reshape(n_time, n_freq * n_samp)
    spec.EvEw_im  = spec.EvEw_im[:, :, samp1:samp2];     spec.EvEw_im = np.array(spec.EvEw_im).reshape(n_time, n_freq * n_samp)
    spec.EwEu_im  = spec.EwEu_im[:, :, samp1:samp2];     spec.EwEu_im = np.array(spec.EwEu_im).reshape(n_time, n_freq * n_samp)

    # Background / CAL only
    if cal_mode < 2:
        index = np.where(data.cal_signal == cal_mode)
        #
        spec.epoch = data.epoch[index[0]]
        spec.freq  = spec.freq[index[0]];       spec.freq_w  = spec.freq_w[index[0]]
        #
        spec.EuEu    = spec.EuEu[index[0]];     spec.EvEv    = spec.EvEv[index[0]];     spec.EwEw    = spec.EwEw[index[0]];    spec.EE = spec.EE[index[0]]
        spec.EuEv_re = spec.EuEv_re[index[0]];  spec.EvEw_re = spec.EvEw_re[index[0]];  spec.EvEw_re = spec.EvEw_re[index[0]]
        spec.EuEv_im = spec.EuEv_im[index[0]];  spec.EvEw_im = spec.EvEw_im[index[0]];  spec.EvEw_im = spec.EvEw_im[index[0]]
    else:
        spec.epoch = data.epoch[:]

    # Stokes Parameters and Polarization
    spec.E_Iuv, spec.E_Quv, spec.E_Uuv, spec.E_Vuv = juice_math.get_stokes(spec.EuEu, spec.EvEv, spec.EuEv_re, spec.EuEv_im)
    spec.E_Ivw, spec.E_Qvw, spec.E_Uvw, spec.E_Vvw = juice_math.get_stokes(spec.EvEv, spec.EwEw, spec.EvEw_re, spec.EvEw_im)
    spec.E_Iwu, spec.E_Qwu, spec.E_Uwu, spec.E_Vwu = juice_math.get_stokes(spec.EwEw, spec.EuEu, spec.EwEu_re, spec.EwEu_im)
    spec.E_DoPuv, spec.E_DoLuv, spec.E_DoCuv, spec.E_ANGuv = juice_math.get_pol(spec.E_Iuv, spec.E_Quv, spec.E_Uuv, spec.E_Vuv)
    spec.E_DoPvw, spec.E_DoLvw, spec.E_DoCvw, spec.E_ANGvw = juice_math.get_pol(spec.E_Ivw, spec.E_Qvw, spec.E_Uvw, spec.E_Vvw)
    spec.E_DoPwu, spec.E_DoLwu, spec.E_DoCwu, spec.E_ANGwu = juice_math.get_pol(spec.E_Iwu, spec.E_Qwu, spec.E_Uwu, spec.E_Vwu)

    return spec


"""
def hf_sid2_speccal_unit(spec, unit_mode):
    # input:  data, unit_mode
    # return: data
    # CUT & Reshape
    n_time = spec.EE.shape[0]
    n_freq = spec.EE.shape[1]
    freq_1d = spec.freq[n_time//2]
    print(" speccal_org:", spec.EE.shape, n_time, "x", n_freq,)
    print(freq_1d.shape, freq_1d)
    
    cal_unit = juice_cdf.cal_unit(unit_mode, freq_1d)

    # unit_mode       0: raw    1: dBm＠ADC  2: V@HF   3:V2@HF   4:V2@RWI
    # ******************************************************
    # [EM2-0]
    # "1-bit" = -104.1 dBm = -114.1 dB V  = 1.97E-6 V    ==> "20-bit": 2.06 Vpp
    # "HF input"  +15dB(AMP) -3dB(50-ohm) = "+12dB"      ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    # [EM2-3 / FM / FS]
    # "1-bit" = -110.1 dBm = -110.1 dB V  = 0.99E-7 V "  ==> "20-bit": 1.03 Vpp
    # "HF input"  +9dB(AMP)  -3dB(50-ohm) = "+6dB"       ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************

    cf = 0.0                                # Conversion Factor: RAW

    if unit_mode == 1:
        cf = -104.1                         # dBm @ ADC 
    elif unit_mode == 2:
        cf = -104.1 - 10.00 - 15.0          # V(amplitude) @ HF -- in EM2-1: HF-gain +15dB, ADC: 2Vpp  ==> EM2-3 & later: same [-6dB + 6dB]
    elif unit_mode == 3:
        cf = -104.1 - 13.01 - 15.0          # V^2 @ HF (EM2-0 case)
    elif unit_mode == 4:
        cf = -104.1 - 13.01 - 15.0 - 5.0    # V^2 @ RWIin -- temporary

    # *** Max / Min in plots ***
    p_max = p_raw_max + cf/10
    p_min = p_raw_min + cf/10

    return cf, p_max, p_min
    return spec
"""


"""
# ---------------------------------------------------------------------
def hf_sid2_getauto(data):
    # input:  data
    # return: auto

    # AutoCorr formation
    auto = struct()
    auto.EuEu = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    auto.EvEv = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    auto.EwEw = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    auto.EE   = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    auto.EuEu = auto.EuEu.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    auto.EvEv = auto.EvEv.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    auto.EwEw = auto.EwEw.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    auto.EE   = auto.EE.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)

    for i in range(data.n_time):
        for j in range(data.N_block[0]):
            EuEu = data.Eu_i[i][j]**2 + data.Eu_q[i][j]**2  
            EvEv = data.Ev_i[i][j]**2 + data.Ev_q[i][j]**2  
            EwEw = data.Ew_i[i][j]**2 + data.Ew_q[i][j]**2  
            EE = EuEu + EvEv + EwEw
            EuEu = stats.zscore(EuEu); EvEv = stats.zscore(EvEv); EwEw = stats.zscore(EwEw); EE = stats.zscore(EE)

            EuEu_auto = np.correlate(EuEu, EuEu, mode='full')
            EuEu_auto = EuEu_auto[EuEu_auto.shape[0]//2:]
            EuEu_auto /= len(EuEu_auto)
            auto.EuEu[i][j] = EuEu_auto

            EvEv_auto = np.correlate(EvEv, EvEv, mode='full')
            EvEv_auto = EvEv_auto[EvEv_auto.shape[0]//2:]
            EvEv_auto /= len(EvEv_auto)
            auto.EvEv[i][j] = EvEv_auto

            EwEw_auto = np.correlate(EwEw, EwEw, mode='full')
            EwEw_auto = EwEw_auto[EwEw_auto.shape[0]//2:]
            EwEw_auto /= len(EwEw_auto)
            auto.EwEw[i][j] = EwEw_auto

            EE_auto   = np.correlate(EE, EE, mode='full')
            EE_auto   = EE_auto[EE_auto.shape[0]//2:]
            EE_auto   /= len(EE_auto)
            auto.EE[i][j] = EE_auto

            auto.EuEu[i][j][0] = 0
            auto.EvEv[i][j][0] = 0
            auto.EwEw[i][j][0] = 0
            auto.EE[i][j][0] = 0
            auto.EuEu[i][j][1] = 0
            auto.EvEv[i][j][1] = 0
            auto.EwEw[i][j][1] = 0
            auto.EE[i][j][1] = 0
    return auto
"""