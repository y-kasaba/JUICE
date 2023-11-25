"""
    JUICE RPWI HF SID2 (RAW): L1a QL -- 2023/11/19
"""
import numpy as np
import juice_cdf_lib as juice_cdf
import scipy.stats as stats


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID2 ------------------------------------------------------------
# ---------------------------------------------------------------------
def juice_getdata_hf_sid2(cdf, cf):
    """
    input:  CDF, cf:conversion factor
    return: data
    """
    data = struct()

    # AUX
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    data.cal_signal = cdf['cal_signal'][...]
    data.sweep_table = cdf['sweep_table'][...]   # (fixed: not defined in V.2)
    #
    data.onboard_cal = cdf['onboard_cal'][...]   # (not used)
    data.complex = cdf['complex'][...]
    data.BG_subtract = cdf['BG_subtract'][...]
    data.BG_select = cdf['BG_select'][...]
    data.FFT_window = cdf['FFT_window'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    data.Pol_sep_thres = cdf['Pol_sep_thres'][...]
    data.Pol_sep_SW = cdf['Pol_sep_SW'][...]
    data.overflow_U = cdf['overflow_U'][...]     # (fixed: not defined in V.2)
    data.overflow_V = cdf['overflow_V'][...]     # (fixed: not defined in V.2)
    data.overflow_W = cdf['overflow_W'][...]     # (fixed: not defined in V.2)
    data.proc_param0 = cdf['proc_param0'][...]
    data.proc_param1 = cdf['proc_param1'][...]
    data.proc_param2 = cdf['proc_param2'][...]
    data.proc_param3 = cdf['proc_param3'][...]
    data.BG_downlink = cdf['BG_downlink'][...]
    data.N_block = cdf['N_block'][...]
    data.T_RWI_CH1 = cdf['T_RWI_CH1'][...]
    data.T_RWI_CH2 = cdf['T_RWI_CH2'][...]
    data.T_HF_FPGA = cdf['T_HF_FPGA'][...]

    # Header
    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]
    data.pol = cdf['pol'][...]

    # Data
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]
    #
    data.Eu_i = cdf['Eu_i'][...] * 10**(cf/20)
    data.Eu_q = cdf['Eu_q'][...] * 10**(cf/20)
    data.Ev_i = cdf['Ev_i'][...] * 10**(cf/20)
    data.Ev_q = cdf['Ev_q'][...] * 10**(cf/20)
    data.Ew_i = cdf['Ew_i'][...] * 10**(cf/20)
    data.Ew_q = cdf['Ew_q'][...] * 10**(cf/20)
    data.pps_count = cdf['pps_count'][...]
    data.sweep_start = cdf['sweep_start'][...]
    data.reduction = cdf['reduction'][...]
    data.overflow = cdf['overflow'][...]
    #
    data.time = cdf['time'][...]
    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]

    # ### SPECIAL: 202305 & 202307 -- data shift -16
    date = data.epoch[0];  month = date.strftime('%Y%m')
    if month == "202305" or month == "202307":
        data.Eu_i = np.roll(data.Eu_i, -16);  data.Eu_q = np.roll(data.Eu_q, -16)
        data.Ev_i = np.roll(data.Ev_i, -16);  data.Ev_q = np.roll(data.Ev_q, -16)
        data.Ew_i = np.roll(data.Ew_i, -16);  data.Ew_q = np.roll(data.Ew_q, -16)
        print("-16 shift in 202305 data")
    # ### SPECIAL: 202305 & 202307 -- data shift -16

    # CUT & Reshape
    n_time = data.Eu_i.shape[0]
    n_freq = data.N_step[0]
    n_samp = data.N_samp[0]
    n_num = n_freq * n_samp
    print("  org:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "[", n_num, "]")
    if n_num < data.Eu_i.shape[1]:
        data.Eu_i = data.Eu_i[:, 0:n_num];  data.Eu_q = data.Eu_q[:, 0:n_num]
        data.Ev_i = data.Ev_i[:, 0:n_num];  data.Ev_q = data.Ev_q[:, 0:n_num]
        data.Ew_i = data.Ew_i[:, 0:n_num];  data.Ew_q = data.Ew_q[:, 0:n_num]
        data.frequency = data.frequency[:, 0:n_num]
        data.freq_step = data.freq_step[:, 0:n_num]
        data.freq_width = data.freq_width[:, 0:n_num]
        data.time = data.time[:, 0:n_num]
        data.pps_count = data.pps_count[:, 0:n_num]
        data.sweep_start = data.sweep_start[:, 0:n_num]
        data.reduction = data.reduction[:, 0:n_num]
        data.overflow = data.overflow[:, 0:n_num]
        print("cut1 :", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp)
    # Merge & CUT
    n_freq0 = n_freq
    if data.frequency[0][0] < data.frequency[1][0]:
        i = 1
        while data.frequency[0][0] < data.frequency[i][0]:
            i += 1
            if i >= n_time:
                break
            n_freq0 += data.N_step[i]
        n_time = n_time // i
        n_freq = n_freq * i
        print(" cut2:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp)
        data.epoch = np.array(data.epoch).reshape(n_time, i)
        print(data.epoch.shape)
        print(data.epoch)
        data.epoch = data.epoch[:, 0]
        print(data.epoch.shape)
        print(data.epoch)
    # Reshape
    data.Eu_i = np.array(data.Eu_i).reshape(n_time, n_freq, n_samp)
    data.Eu_q = np.array(data.Eu_q).reshape(n_time, n_freq, n_samp)
    data.Ev_i = np.array(data.Ev_i).reshape(n_time, n_freq, n_samp)
    data.Ev_q = np.array(data.Ev_q).reshape(n_time, n_freq, n_samp)
    data.Ew_i = np.array(data.Ew_i).reshape(n_time, n_freq, n_samp)
    data.Ew_q = np.array(data.Ew_q).reshape(n_time, n_freq, n_samp)
    data.frequency   = np.array(data.frequency).reshape(n_time, n_freq, n_samp)
    data.freq_step   = np.array(data.freq_step).reshape(n_time, n_freq, n_samp)
    data.freq_width  = np.array(data.freq_width).reshape(n_time, n_freq, n_samp)
    data.time        = np.array(data.time).reshape(n_time, n_freq, n_samp)
    data.pps_count   = np.array(data.pps_count).reshape(n_time, n_freq, n_samp)
    data.sweep_start = np.array(data.sweep_start).reshape(n_time, n_freq, n_samp)
    data.reduction   = np.array(data.reduction).reshape(n_time, n_freq, n_samp)
    data.overflow    = np.array(data.overflow).reshape(n_time, n_freq, n_samp)

    # CUT & Reshape
    print(" sort:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp)
    if n_freq > n_freq0:
        n_freq = n_freq0
        data.Eu_i = data.Eu_i[:, 0:n_freq]
        data.Eu_q = data.Eu_q[:, 0:n_freq]
        data.Ev_i = data.Ev_i[:, 0:n_freq]
        data.Ev_q = data.Ev_q[:, 0:n_freq]
        data.Ew_i = data.Ew_i[:, 0:n_freq]
        data.Ew_q = data.Ew_q[:, 0:n_freq]
        data.frequency = data.frequency[:, 0:n_freq]
        data.freq_step = data.freq_step[:, 0:n_freq]
        data.freq_width = data.freq_width[:, 0:n_freq]
        data.time = data.time[:, 0:n_freq]
        data.pps_count = data.pps_count[:, 0:n_freq]
        data.sweep_start = data.sweep_start[:, 0:n_freq]
        data.reduction = data.reduction[:, 0:n_freq]
        data.overflow = data.overflow[:, 0:n_freq]
        print("  cut:", data.Eu_i.shape)
    print("fixed:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp)

    # ### SPECIAL: 202305 & 202307 -- data shift -16
    if month == "202305" or month == "202307":
        data.Eu_i[:, -1, n_samp//2:n_samp] = 0.;  data.Eu_q[:, -1, n_samp//2:n_samp] = 0.
        data.Ev_i[:, -1, n_samp//2:n_samp] = 0.;  data.Ev_q[:, -1, n_samp//2:n_samp] = 0.
        data.Ew_i[:, -1, n_samp//2:n_samp] = 0.;  data.Ew_q[:, -1, n_samp//2:n_samp] = 0.
    # ### SPECIAL: 202305 & 202307 -- data shift -16
    return data


# ---------------------------------------------------------------------
def hf_sid2_getspec(data, unit_mode):
    """
    input:  data, unit_mode
    return: spec
    """
    # Spec formation
    spec = struct()

    n_time = data.Eu_i.shape[0]
    n_freq = data.Eu_i.shape[1]
    n_samp = data.Eu_i.shape[2]
    spec.EuEu = np.zeros(n_time * n_freq * n_samp)
    spec.EvEv = np.zeros(n_time * n_freq * n_samp)
    spec.EwEw = np.zeros(n_time * n_freq * n_samp)
    spec.EE = np.zeros(n_time * n_freq * n_samp)
    spec.freq = np.zeros(n_time * n_freq * n_samp)
    spec.EuEu = spec.EuEu.reshape(n_time, n_freq, n_samp)
    spec.EvEv = spec.EvEv.reshape(n_time, n_freq, n_samp)
    spec.EwEw = spec.EwEw.reshape(n_time, n_freq, n_samp)
    spec.EE = spec.EE.reshape(n_time, n_freq, n_samp)
    spec.freq = spec.freq.reshape(n_time, n_freq, n_samp)

    # Frequency
    dt = 1.0 / juice_cdf._sample_rate(data.decimation[0])
    freq = np.fft.fftshift(np.fft.fftfreq(n_samp, d=dt)) / 1000.

    for i in range(n_time):
        for j in range(n_freq):
            spec.freq[i][j] = data.frequency[i][j] + freq

    # FFT
    window = np.hanning(n_samp)
    acf = 1/(sum(window)/n_samp)
    #
    s = np.fft.fft((data.Eu_i - data.Eu_q * 1j) * window);  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf
    spec.EuEu = np.fft.fftshift(s, axes=(2,))
    s = np.fft.fft((data.Ev_i - data.Ev_q * 1j) * window);  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf
    spec.EvEv = np.fft.fftshift(s, axes=(2,))
    s = np.fft.fft((data.Ew_i - data.Ew_q * 1j) * window);  s = np.power(np.abs(s) / n_samp, 2.0) * acf * acf
    spec.EwEw = np.fft.fftshift(s, axes=(2,))
    spec.EE = spec.EuEu + spec.EvEv + spec.EwEw
    

    samp1 = 0
    samp2 = n_samp
    """
    # Cut: 75%
    samp1 = n_samp//8
    samp2 = n_samp - n_samp//8

    # for i in range(data.n_freq - 1):
    i = 0
    while ( spec.freq[0][i][samp2] > spec.freq[0][i+1][samp1] ):
        samp1 += 1
        samp2 -= 1
    print("cut: 1st-start/end 2nd-first-end:", spec.freq[0][i][samp2], spec.freq[0][i+1][samp1], 100*(samp2-samp1)/n_samp, "%") 
    spec.EuEu = spec.EuEu[:, :, samp1:samp2]
    spec.EvEv = spec.EvEv[:, :, samp1:samp2]
    spec.EwEw = spec.EwEw[:, :, samp1:samp2]
    spec.EE   = spec.EE  [:, :, samp1:samp2]
    spec.freq = spec.freq[:, :, samp1:samp2]
    n_samp = samp2 - samp1
    """

    # Reshape
    spec.EuEu = np.array(spec.EuEu).reshape(n_time, n_freq * n_samp)
    spec.EvEv = np.array(spec.EvEv).reshape(n_time, n_freq * n_samp)
    spec.EwEw = np.array(spec.EwEw).reshape(n_time, n_freq * n_samp)
    spec.EE = np.array(spec.EE).reshape(n_time, n_freq * n_samp)
    spec.freq = np.array(spec.freq).reshape(n_time, n_freq * n_samp)
    return spec


# ---------------------------------------------------------------------
def hf_sid2_getauto(data):
    """
    input:  data
    return: auto
    """
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

            auto.EuEu[i][j][0] = auto.EvEv[i][j][0] = auto.EwEw[i][j][0] = auto.EE[i][j][0] = 0
            auto.EuEu[i][j][1] = auto.EvEv[i][j][1] = auto.EwEw[i][j][1] = auto.EE[i][j][1] = 0
    return auto
