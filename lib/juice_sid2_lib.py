"""
    JUICE RPWI HF SID2 (RAW): L1a QL -- 2024/1/16
"""
import numpy as np
import juice_cdf_lib as juice_cdf
import scipy.stats as stats


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID2 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid2_read(cdf):
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
    data.B0_startf = cdf['B0_startf'][...]
    data.B0_stopf = cdf['B0_stopf'][...]
    data.B0_step = cdf['B0_step'][...]
    data.B0_repeat = cdf['B0_repeat'][...]
    data.B0_subdiv = cdf['B0_subdiv'][...]
    data.B1_startf = cdf['B1_startf'][...]
    data.B1_stopf = cdf['B1_stopf'][...]
    data.B1_step = cdf['B1_step'][...]
    data.B1_repeat = cdf['B1_repeat'][...]
    data.B1_subdiv = cdf['B1_subdiv'][...]
    data.B2_startf = cdf['B2_startf'][...]
    data.B2_stopf = cdf['B2_stopf'][...]
    data.B2_step = cdf['B2_step'][...]
    data.B2_repeat = cdf['B2_repeat'][...]
    data.B2_subdiv = cdf['B2_subdiv'][...]
    data.B3_startf = cdf['B3_startf'][...]
    data.B3_stopf = cdf['B3_stopf'][...]
    data.B3_step = cdf['B3_step'][...]
    data.B3_repeat = cdf['B3_repeat'][...]
    data.B3_subdiv = cdf['B3_subdiv'][...]
    data.B4_startf = cdf['B4_startf'][...]
    data.B4_stopf = cdf['B4_stopf'][...]
    data.B4_step = cdf['B4_step'][...]
    data.B4_repeat = cdf['B4_repeat'][...]
    data.B4_subdiv = cdf['B4_subdiv'][...]

    # Data
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]
    #
    data.Eu_i = cdf['Eu_i'][...] # * 10**(cf/20)
    data.Eu_q = cdf['Eu_q'][...] # * 10**(cf/20)
    data.Ev_i = cdf['Ev_i'][...] # * 10**(cf/20)
    data.Ev_q = cdf['Ev_q'][...] # * 10**(cf/20)
    data.Ew_i = cdf['Ew_i'][...] # * 10**(cf/20)
    data.Ew_q = cdf['Ew_q'][...] # * 10**(cf/20)
    data.pps_count = cdf['pps_count'][...]
    data.sweep_start = cdf['sweep_start'][...]
    data.reduction = cdf['reduction'][...]
    data.overflow = cdf['overflow'][...]
    #
    data.time = cdf['time'][...]
    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]

    # ### ASW1: SPECIAL: data shift -16
    date = data.epoch[0];  month = date.strftime('%Y%m')
    if month == "202304" or month == "202305" or month == "202307":
        data.Eu_i = np.roll(data.Eu_i, -16);  data.Eu_q = np.roll(data.Eu_q, -16)
        data.Ev_i = np.roll(data.Ev_i, -16);  data.Ev_q = np.roll(data.Ev_q, -16)
        data.Ew_i = np.roll(data.Ew_i, -16);  data.Ew_q = np.roll(data.Ew_q, -16)
        print("-16 shift in ASW1 data")

    return data


def hf_sid2_add(data, data1):
    """
    input:  data, data1
    return: data
    """

    # AUX
    data.U_selected = np.r_["0", data.U_selected, data1.U_selected]
    data.V_selected = np.r_["0", data.V_selected, data1.V_selected]
    data.W_selected = np.r_["0", data.W_selected, data1.W_selected]
    data.cal_signal = np.r_["0", data.cal_signal, data1.cal_signal]
    data.sweep_table = np.r_["0", data.sweep_table, data1.sweep_table]
    #
    data.onboard_cal = np.r_["0", data.onboard_cal, data1.onboard_cal]
    data.complex = np.r_["0", data.complex, data1.complex]
    data.BG_subtract = np.r_["0", data.BG_subtract, data1.BG_subtract]
    data.BG_select = np.r_["0", data.BG_select, data1.BG_select]
    data.FFT_window = np.r_["0", data.FFT_window, data1.FFT_window]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    data.Pol_sep_thres = np.r_["0", data.Pol_sep_thres, data1.Pol_sep_thres]
    data.Pol_sep_SW = np.r_["0", data.Pol_sep_SW, data1.Pol_sep_SW]
    data.overflow_U = np.r_["0", data.overflow_U, data1.overflow_U]
    data.overflow_V = np.r_["0", data.overflow_V, data1.overflow_V]
    data.overflow_W = np.r_["0", data.overflow_W, data1.overflow_W]
    data.proc_param0 = np.r_["0", data.proc_param0, data1.proc_param0]
    data.proc_param1 = np.r_["0", data.proc_param1, data1.proc_param1]
    data.proc_param2 = np.r_["0", data.proc_param2, data1.proc_param2]
    data.proc_param3 = np.r_["0", data.proc_param3, data1.proc_param3]
    data.BG_downlink = np.r_["0", data.BG_downlink, data1.BG_downlink]
    data.N_block = np.r_["0", data.N_block, data1.N_block]
    data.T_RWI_CH1 = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2 = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]

    # Header
    data.N_samp = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step = np.r_["0", data.N_step, data1.N_step]
    data.decimation = np.r_["0", data.decimation, data1.decimation]
    data.pol = np.r_["0", data.pol, data1.pol]
    data.B0_startf = np.r_["0", data.B0_startf, data1.B0_startf]
    data.B0_stopf = np.r_["0", data.B0_stopf, data1.B0_stopf]
    data.B0_step = np.r_["0", data.B0_step, data1.B0_step]
    data.B0_repeat = np.r_["0", data.B0_repeat, data1.B0_repeat]
    data.B0_subdiv = np.r_["0", data.B0_subdiv, data1.B0_subdiv]
    data.B1_startf = np.r_["0", data.B1_startf, data1.B1_startf]
    data.B1_stopf = np.r_["0", data.B1_stopf, data1.B1_stopf]
    data.B1_step = np.r_["0", data.B1_step, data1.B1_step]
    data.B1_repeat = np.r_["0", data.B1_repeat, data1.B1_repeat]
    data.B1_subdiv = np.r_["0", data.B1_subdiv, data1.B1_subdiv]
    data.B2_startf = np.r_["0", data.B2_startf, data1.B2_startf]
    data.B2_stopf = np.r_["0", data.B2_stopf, data1.B2_stopf]
    data.B2_step = np.r_["0", data.B2_step, data1.B2_step]
    data.B2_repeat = np.r_["0", data.B2_repeat, data1.B2_repeat]
    data.B2_subdiv = np.r_["0", data.B2_subdiv, data1.B2_subdiv]
    data.B3_startf = np.r_["0", data.B3_startf, data1.B3_startf]
    data.B3_stopf = np.r_["0", data.B3_stopf, data1.B3_stopf]
    data.B3_step = np.r_["0", data.B3_step, data1.B3_step]
    data.B3_repeat = np.r_["0", data.B3_repeat, data1.B3_repeat]
    data.B3_subdiv = np.r_["0", data.B3_subdiv, data1.B3_subdiv]
    data.B4_startf = np.r_["0", data.B4_startf, data1.B4_startf]
    data.B4_stopf = np.r_["0", data.B4_stopf, data1.B4_stopf]
    data.B4_step = np.r_["0", data.B4_step, data1.B4_step]
    data.B4_repeat = np.r_["0", data.B4_repeat, data1.B4_repeat]
    data.B4_subdiv = np.r_["0", data.B4_subdiv, data1.B4_subdiv]

    # Data
    data.epoch = np.r_["0", data.epoch, data1.epoch]
    data.scet = np.r_["0", data.scet, data1.scet]
    #
    data.Eu_i = np.r_["0", data.Eu_i, data1.Eu_i]
    data.Eu_q = np.r_["0", data.Eu_q, data1.Eu_q]
    data.Ev_i = np.r_["0", data.Ev_i, data1.Ev_i]
    data.Ev_q = np.r_["0", data.Ev_q, data1.Ev_q]
    data.Ew_i = np.r_["0", data.Ew_i, data1.Ew_i]
    data.Ew_q = np.r_["0", data.Ew_q, data1.Ew_q]
    data.pps_count = np.r_["0", data.pps_count, data1.pps_count] 
    data.sweep_start = np.r_["0", data.sweep_start, data1.sweep_start]
    data.reduction = np.r_["0", data.reduction, data1.reduction]
    data.overflow = np.r_["0", data.overflow, data1.overflow]
    #
    data.time = np.r_["0", data.time, data1.time]
    data.frequency = np.r_["0", data.frequency, data1.frequency]
    data.freq_step = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width = np.r_["0", data.freq_width, data1.freq_width]
    
    return data


def hf_sid2_proc(data):
    """
    input:  data
    return: data
    """

    # CUT & Reshape
    n_time = data.Eu_i.shape[0]
    n_freq = data.N_step[n_time//2]
    n_samp = data.N_samp[n_time//2]
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
        print(" cut1:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "[", n_num, "]")

    # Merge & CUT
    n_freq0 = n_freq
    if n_time > 1:
        if data.frequency[0][0] < data.frequency[1][0]:
            i = 1
            while data.frequency[0][0] < data.frequency[i][0]:
                n_freq0 += data.N_step[i]
                i += 1
                if i >= n_time:
                    break
            n_time = n_time // i
            n_freq = n_freq * i
            print(" cut2:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp)
            data.epoch = np.array(data.epoch).reshape(n_time, i)
            # print(data.epoch.shape)
            # print(data.epoch)
            data.epoch = data.epoch[:, 0]
            print(data.epoch.shape, data.epoch)
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
        print(" cut2:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp)

    # ### ASW1: data shift -16
    date = data.epoch[0];  month = date.strftime('%Y%m')
    if month == "202304" or month == "202305" or month == "202307":
        data.Eu_i[:, -1, n_samp//2:n_samp] = 0.;  data.Eu_q[:, -1, n_samp//2:n_samp] = 0.
        data.Ev_i[:, -1, n_samp//2:n_samp] = 0.;  data.Ev_q[:, -1, n_samp//2:n_samp] = 0.
        data.Ew_i[:, -1, n_samp//2:n_samp] = 0.;  data.Ew_q[:, -1, n_samp//2:n_samp] = 0.

    # ### ASW1: CAL
    if data.cal_signal[0] == 255:
        power = data.Eu_i[:,-1]**2 + data.Eu_q[:,-1]**2 + data.Ev_i[:,-1]**2 + data.Ev_q[:,-1]**2 + data.Ew_i[:,-1]**2 + data.Ew_q[:,-1]**2
        power = np.mean(power, axis=1)
        index = np.where(power > 1e4)
        data.cal_signal[:] = 0
        data.cal_signal[index[0]]=1

    return data


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

    # Cut: 75%
    samp1 = n_samp//8           # 0
    samp2 = n_samp - n_samp//8  # n_samp

    # for i in range(data.n_freq - 1):
    i = 0
    while (spec.freq[0][i][samp2] > spec.freq[0][i+1][samp1]):
        samp1 += 1; samp2 -= 1
    print("cut: 1st-start/end 2nd-first-end:", spec.freq[0][i][samp2], spec.freq[0][i+1][samp1], 100*(samp2-samp1)/n_samp, "%") 
    # print("df @ f_low  [kHz]: ", spec.freq[0][i+1][samp1] - spec.freq[0][i][samp2], spec.freq[0][i][samp2+1] - spec.freq[0][i][samp2]) 
    # i = n_freq-2
    # print("df @ f_high [kHz]: ", spec.freq[0][i+1][samp1] - spec.freq[0][i][samp2], spec.freq[0][i][samp2+1] - spec.freq[0][i][samp2]) 
    spec.EuEu = spec.EuEu[:, :, samp1:samp2]
    spec.EvEv = spec.EvEv[:, :, samp1:samp2]
    spec.EwEw = spec.EwEw[:, :, samp1:samp2]
    spec.EE = spec.EE[:, :, samp1:samp2]
    spec.freq = spec.freq[:, :, samp1:samp2]
    n_samp = samp2 - samp1

    # Reshape
    spec.EvEv = np.array(spec.EvEv).reshape(n_time, n_freq * n_samp)
    spec.EwEw = np.array(spec.EwEw).reshape(n_time, n_freq * n_samp)
    spec.EE = np.array(spec.EE).reshape(n_time, n_freq * n_samp)
    spec.EuEu = np.array(spec.EuEu).reshape(n_time, n_freq * n_samp)
    spec.freq = np.array(spec.freq).reshape(n_time, n_freq * n_samp)

    # Median formation
    if cal_mode < 2:
        index = np.where(data.cal_signal == cal_mode)
        spec.EuEu = spec.EuEu[index[0]]
        spec.EvEv = spec.EvEv[index[0]]
        spec.EwEw = spec.EwEw[index[0]]
        spec.EE = spec.EE[index[0]]
        spec.freq = spec.freq[index[0]]
        spec.epoch = data.epoch[index[0]]
    else:
        spec.epoch = data.epoch[:]
    return spec


def hf_sid2_speccal_unit(spec, unit_mode):
    """
    input:  data, unit_mode
    return: data
    """
    # CUT & Reshape
    n_time = spec.EE.shape[0]
    n_freq = spec.EE.shape[1]
    freq_1d = spec.freq[n_time//2]
    print(" speccal_org:", spec.EE.shape, n_time, "x", n_freq,)
    print(freq_1d.shape, freq_1d)
    
    """
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
    """
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

            auto.EuEu[i][j][0] = 0
            auto.EvEv[i][j][0] = 0
            auto.EwEw[i][j][0] = 0
            auto.EE[i][j][0] = 0
            auto.EuEu[i][j][1] = 0
            auto.EvEv[i][j][1] = 0
            auto.EwEw[i][j][1] = 0
            auto.EE[i][j][1] = 0
    return auto
