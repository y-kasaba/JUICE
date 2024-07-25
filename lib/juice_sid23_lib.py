"""
    JUICE RPWI HF SID23 (PSSR3 rich): L1a QL -- 2024/7/25
"""
import numpy as np
import scipy.stats as stats
import juice_cdf_lib as juice_cdf
import juice_math_lib as juice_math
import copy

class struct:
    pass


# ---------------------------------------------------------------------
# --- SID23 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid23_read(cdf):
    """
    input:  CDF
    return: data
    """
    data = struct()

    # AUX
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    data.cal_signal = cdf['cal_signal'][...]
    data.pol_AUX = cdf['pol_AUX'][...]
    data.decimation_AUX = cdf['decimation_AUX'][...]
    data.N_block = cdf['N_block'][...]
    data.freq_center = cdf['freq_center'][...]
    data.N_feed = cdf['N_feed'][...]
    data.N_skip = cdf['N_skip'][...]

    # Header
    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]
    data.pol = cdf['pol'][...]

    # Data
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]
    #
    data.Eu_i = np.float64(cdf['Eu_i'][...])
    data.Eu_q = np.float64(cdf['Eu_q'][...])
    data.Ev_i = np.float64(cdf['Ev_i'][...])
    data.Ev_q = np.float64(cdf['Ev_q'][...])
    data.Ew_i = np.float64(cdf['Ew_i'][...])
    data.Ew_q = np.float64(cdf['Ew_q'][...])
    data.pps_count = cdf['pps_count'][...]
    data.sweep_start = cdf['sweep_start'][...]
    data.reduction = cdf['reduction'][...]
    data.overflow = cdf['overflow'][...]
    return data


def hf_sid23_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # AUX
    data.U_selected     = np.r_["0", data.U_selected, data1.U_selected]
    data.V_selected     = np.r_["0", data.V_selected, data1.V_selected]
    data.W_selected     = np.r_["0", data.W_selected, data1.W_selected]
    data.cal_signal     = np.r_["0", data.cal_signal, data1.cal_signal]
    data.pol_AUX        = np.r_["0", data.pol_AUX, data1.pol_AUX]
    data.decimation_AUX = np.r_["0", data.decimation_AUX, data1.decimation_AUX]
    data.N_block        = np.r_["0", data.N_block, data1.N_block]
    data.freq_center    = np.r_["0", data.freq_center, data1.freq_center]
    data.N_feed         = np.r_["0", data.N_feed, data1.N_feed]
    data.N_skip         = np.r_["0", data.N_skip, data1.N_skip]

    # Header
    data.N_samp         = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step         = np.r_["0", data.N_step, data1.N_step]
    data.decimation     = np.r_["0", data.decimation, data1.decimation]
    data.pol            = np.r_["0", data.pol, data1.pol]

    # Data
    data.epoch          = np.r_["0", data.epoch, data1.epoch]
    data.scet           = np.r_["0", data.scet, data1.scet]
    #
    data.Eu_i           = np.r_["0", data.Eu_i, data1.Eu_i]
    data.Eu_q           = np.r_["0", data.Eu_q, data1.Eu_q]
    data.Ev_i           = np.r_["0", data.Ev_i, data1.Ev_i]
    data.Ev_q           = np.r_["0", data.Ev_q, data1.Ev_q]
    data.Ew_i           = np.r_["0", data.Ew_i, data1.Ew_i]
    data.Ew_q           = np.r_["0", data.Ew_q, data1.Ew_q]
    data.pps_count      = np.r_["0", data.pps_count, data1.pps_count] 
    data.sweep_start    = np.r_["0", data.sweep_start, data1.sweep_start]
    data.reduction      = np.r_["0", data.reduction, data1.reduction]
    data.overflow       = np.r_["0", data.overflow, data1.overflow]
    return data


def hf_sid23_shaping(data):
    """
    input:  data
    return: data
    """
    # Size
    data.n_time = data.Eu_i.shape[0]
    n_num0 = data.N_feed[0] * 128
    n_num1 = (data.N_feed[0] + data.N_skip[0]) * 128
    n_num = n_num0 * data.N_block[0]
    print("  org:", data.Eu_i.shape, data.n_time, n_num, data.N_block[0], data.N_feed[0])

    # CUT & Shaping: less packet length
    if n_num < data.Eu_i.shape[1]:
        data.Eu_i = data.Eu_i[:, 0:n_num];  data.Eu_q = data.Eu_q[:, 0:n_num]
        data.Ev_i = data.Ev_i[:, 0:n_num];  data.Ev_q = data.Ev_q[:, 0:n_num]
        data.Ew_i = data.Ew_i[:, 0:n_num];  data.Ew_q = data.Ew_q[:, 0:n_num]
        data.pps_count = data.pps_count[:, 0:n_num]
        data.sweep_start = data.sweep_start[:, 0:n_num]
        data.reduction = data.reduction[:, 0:n_num]
        data.overflow = data.overflow[:, 0:n_num]
        print("  cut:", data.Eu_i.shape, data.n_time, n_num, data.N_block[0], data.N_feed[0])

    # Reshape from "2D: n_time * (n_freq * n_samp)" to "3D: n_time * n_block * n_feed"
    data.Eu_i = np.array(data.Eu_i).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Eu_q = np.array(data.Eu_q).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ev_i = np.array(data.Ev_i).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ev_q = np.array(data.Ev_q).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ew_i = np.array(data.Ew_i).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ew_q = np.array(data.Ew_q).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.pps_count  = np.array(data.pps_count).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.sweep_start= np.array(data.sweep_start).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.reduction  = np.array(data.reduction).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.overflow   = np.array(data.overflow).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    print(" sort:", data.Eu_i.shape, data.n_time, n_num, data.N_block[0], data.N_feed[0])

    # Time   
    time = np.arange(0, n_num0, 1) / juice_cdf._sample_rate(data.decimation_AUX[0])
    time0 = np.float32(np.arange(0, n_num, 1))
    for i in range(data.N_block[0]):
        time0[n_num0*i:n_num0*(i+1)] = time + i * n_num1 / juice_cdf._sample_rate(data.decimation_AUX[0])
    time0 = np.array(time0).reshape(data.N_block[0], data.N_feed[0]*128)
    #
    data.time = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    data.time = data.time.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    for i in range(data.n_time):
        data.time[i][:][:] = time0

    return data


# ---------------------------------------------------------------------
def hf_sid23_getspec(data, band_mode):
    """
    input:  data, band_mode
    return: spec
    """
    # Spec formation
    spec = struct()
    n_time  = data.Eu_i.shape[0]
    n_block = data.Eu_i.shape[1]
    n_samp  = data.Eu_i.shape[2]     # data.N_feed[0]*128
    print(data.Eu_i.shape, n_samp)

    # Frequency
    dt = 1.0 / juice_cdf._sample_rate(data.decimation_AUX[0])
    spec.freq = np.fft.fftshift(np.fft.fftfreq(data.N_feed[0]*128, d=dt)) / 1000.
    spec.freq = spec.freq + data.freq_center[0]
    spec.freq_w = spec.freq[1] - spec.freq[0]

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

    print(spec.EuEu.shape)
    # Stokes Parameters and Polarization
    spec.E_Iuv   = copy.copy(spec.EE);  spec.E_Quv   = copy.copy(spec.EE);  spec.E_Uuv   = copy.copy(spec.EE);  spec.E_Vuv   = copy.copy(spec.EE) 
    spec.E_Ivw   = copy.copy(spec.EE);  spec.E_Qvw   = copy.copy(spec.EE);  spec.E_Uvw   = copy.copy(spec.EE);  spec.E_Vvw   = copy.copy(spec.EE) 
    spec.E_Iwu   = copy.copy(spec.EE);  spec.E_Qwu   = copy.copy(spec.EE);  spec.E_Uwu   = copy.copy(spec.EE);  spec.E_Vwu   = copy.copy(spec.EE) 
    spec.E_DoPuv = copy.copy(spec.EE);  spec.E_DoLuv = copy.copy(spec.EE);  spec.E_DoCuv = copy.copy(spec.EE);  spec.E_ANGuv = copy.copy(spec.EE) 
    spec.E_DoPvw = copy.copy(spec.EE);  spec.E_DoLvw = copy.copy(spec.EE);  spec.E_DoCvw = copy.copy(spec.EE);  spec.E_ANGvw = copy.copy(spec.EE) 
    spec.E_DoPwu = copy.copy(spec.EE);  spec.E_DoLwu = copy.copy(spec.EE);  spec.E_DoCwu = copy.copy(spec.EE);  spec.E_ANGwu = copy.copy(spec.EE) 
    for i in range(n_time):
        spec.E_Iuv[i],   spec.E_Quv[i],   spec.E_Uuv[i],   spec.E_Vuv[i]   = juice_math.get_stokes(spec.EuEu[i],  spec.EvEv[i],  spec.EuEv_re[i], spec.EuEv_im[i])
        spec.E_Ivw[i],   spec.E_Qvw[i],   spec.E_Uvw[i],   spec.E_Vvw[i]   = juice_math.get_stokes(spec.EvEv[i],  spec.EwEw[i],  spec.EvEw_re[i], spec.EvEw_im[i])
        spec.E_Iwu[i],   spec.E_Qwu[i],   spec.E_Uwu[i],   spec.E_Vwu[i]   = juice_math.get_stokes(spec.EwEw[i],  spec.EuEu[i],  spec.EwEu_re[i], spec.EwEu_im[i])
        spec.E_DoPuv[i], spec.E_DoLuv[i], spec.E_DoCuv[i], spec.E_ANGuv[i] = juice_math.get_pol   (spec.E_Iuv[i], spec.E_Quv[i], spec.E_Uuv[i],   spec.E_Vuv[i])
        spec.E_DoPvw[i], spec.E_DoLvw[i], spec.E_DoCvw[i], spec.E_ANGvw[i] = juice_math.get_pol   (spec.E_Ivw[i], spec.E_Qvw[i], spec.E_Uvw[i],   spec.E_Vvw[i])
        spec.E_DoPwu[i], spec.E_DoLwu[i], spec.E_DoCwu[i], spec.E_ANGwu[i] = juice_math.get_pol   (spec.E_Iwu[i], spec.E_Qwu[i], spec.E_Uwu[i],   spec.E_Vwu[i])

    return spec


# ---------------------------------------------------------------------
def hf_sid23_getauto(data):
    """
    input:  data
    return: auto
    """
    # Spec formation
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


# TMP
# ---------------------------------------------------------------------
def hf_sid23_rime_detect(data):
    data.EuEu = (data.Eu_i * data.Eu_i + data.Eu_q * data.Eu_q) ** .5
    data.EvEv = (data.Ev_i * data.Ev_i + data.Ev_q * data.Ev_q) ** .5
    data.EwEw = (data.Ew_i * data.Ew_i + data.Ew_q * data.Ew_q) ** .5
    # print(data.EuEu.shape, data.n_time, data.N_block[0], data.N_feed[0]*128)

    """
    index = np.where(data.EuEu < 1000);  data.EuEu[index] = 0
    index = np.where(data.EvEv < 1000);  data.EvEv[index] = 0
    index = np.where(data.EwEw < 1000);  data.EwEw[index] = 0
    index = np.where(data.EuEu >= 1000); data.EuEu[index] = 50000
    index = np.where(data.EvEv >= 1000); data.EvEv[index] = 50000
    index = np.where(data.EwEw >= 1000); data.EwEw[index] = 50000
    """

    k0 = 0
    for i in range(data.n_time):
        for j in range(data.N_block[0]):
            for k in range(data.N_feed[0]*128):
                if data.EuEu[i][j][k] >= 1000:
                    if k-k0 > 80:
                        print(k0, k)
                        data.EuEu[i][j][k:k0-1] = 10000
                        k0 = k
                    # else:
                    #    data.EuEu[i][j][k:k0-1] = 50000
    
    """
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
    """
    return data
