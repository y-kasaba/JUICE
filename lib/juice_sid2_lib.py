"""
    JUICE RPWI HF SID2 (RAW): L1a read -- 2025/4/6
"""
import numpy as np
import math

class struct:
    pass


# ---------------------------------------------------------------------
# --- SID2 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid2_read(cdf, RPWI_FSW_version):
    """
    input:  CDF, FSW version
    return: data
    """
    data = struct()
    data.RPWI_FSW_version = RPWI_FSW_version

    # AUX
    data.U_selected  = cdf['U_selected'][...];  data.V_selected = cdf['V_selected'][...];  data.W_selected = cdf['W_selected'][...]
    data.complex     = cdf['complex'][...]
    data.cal_signal  = cdf['cal_signal'][...]
    data.sweep_table = cdf['sweep_table'][...]  # (fixed: not defined in V.2)
    data.onboard_cal = cdf['onboard_cal'][...]  # (not used)
    data.BG_subtract = cdf['BG_subtract'][...]
    data.BG_select   = cdf['BG_select'][...]
    data.FFT_window  = cdf['FFT_window'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    data.Pol_sep_thres = cdf['Pol_sep_thres'][...]
    data.Pol_sep_SW  = cdf['Pol_sep_SW'][...]
    # data.overflow_U  = cdf['overflow_U'][...]   # (fixed: not defined in V.2)
    # data.overflow_V  = cdf['overflow_V'][...]   # (fixed: not defined in V.2)
    # data.overflow_W  = cdf['overflow_W'][...]   # (fixed: not defined in V.2)
    data.proc_param0 = cdf['proc_param0'][...];  data.proc_param1 = cdf['proc_param1'][...]
    data.proc_param2 = cdf['proc_param2'][...];  data.proc_param3 = cdf['proc_param3'][...]
    data.BG_downlink = cdf['BG_downlink'][...]
    data.N_block     = np.int64(cdf['N_block'][...])
    data.Rich_flag   = np.int64(cdf['Rich_data_flag'][...])
    data.T_RWI_CH1   = np.float64(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float64(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float64(cdf['T_HF_FPGA'][...])
    # Header
    data.N_samp      = np.int64(cdf['N_samp'][...])
    data.N_step      = np.int64(cdf['N_step'][...])
    data.decimation  = cdf['decimation'][...]; data.pol       = cdf['pol'][...]
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]; data.ISW_ver   = cdf['ISW_ver'][...]
    data.B0_startf   = cdf['B0_startf'][...];  data.B0_stopf  = cdf['B0_stopf'][...];  data.B0_step = cdf['B0_step'][...]
    data.B0_repeat   = cdf['B0_repeat'][...];  data.B0_subdiv = cdf['B0_subdiv'][...]
    data.B1_startf   = cdf['B1_startf'][...];  data.B1_stopf  = cdf['B1_stopf'][...];  data.B1_step = cdf['B1_step'][...]
    data.B1_repeat   = cdf['B1_repeat'][...];  data.B1_subdiv = cdf['B1_subdiv'][...]
    data.B2_startf   = cdf['B2_startf'][...];  data.B2_stopf  = cdf['B2_stopf'][...];  data.B2_step = cdf['B2_step'][...]
    data.B2_repeat   = cdf['B2_repeat'][...];  data.B2_subdiv = cdf['B2_subdiv'][...]
    data.B3_startf   = cdf['B3_startf'][...];  data.B3_stopf  = cdf['B3_stopf'][...];  data.B3_step = cdf['B3_step'][...]
    data.B3_repeat   = cdf['B3_repeat'][...];  data.B3_subdiv = cdf['B3_subdiv'][...]
    data.B4_startf   = cdf['B4_startf'][...];  data.B4_stopf  = cdf['B4_stopf'][...];  data.B4_step = cdf['B4_step'][...]
    data.B4_repeat   = cdf['B4_repeat'][...];  data.B4_subdiv = cdf['B4_subdiv'][...]
    # Data
    data.frequency   = cdf['frequency'][...];  data.freq_step = cdf['freq_step'][...]; data.freq_width = cdf['freq_width'][...]
    data.epoch       = cdf['Epoch'][...];      data.scet      = cdf['SCET'][...];      data.time       = cdf['time'][...]
    data.Eu_i        = np.float64(cdf['Eu_i'][...]);  data.Eu_q = np.float64(cdf['Eu_q'][...])
    data.Ev_i        = np.float64(cdf['Ev_i'][...]);  data.Ev_q = np.float64(cdf['Ev_q'][...])
    data.Ew_i        = np.float64(cdf['Ew_i'][...]);  data.Ew_q = np.float64(cdf['Ew_q'][...])
    data.pps_count   = cdf['pps_count'][...];  data.sweep_start = cdf['sweep_start'][...]
    data.reduction   = cdf['reduction'][...];  data.overflow    = cdf['overflow'][...]

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
    data.U_selected  = np.r_["0", data.U_selected, data1.U_selected]
    data.V_selected  = np.r_["0", data.V_selected, data1.V_selected]
    data.W_selected  = np.r_["0", data.W_selected, data1.W_selected]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.sweep_table = np.r_["0", data.sweep_table, data1.sweep_table]
    #
    data.onboard_cal = np.r_["0", data.onboard_cal, data1.onboard_cal]
    data.complex     = np.r_["0", data.complex, data1.complex]
    data.BG_subtract = np.r_["0", data.BG_subtract, data1.BG_subtract]
    data.BG_select   = np.r_["0", data.BG_select, data1.BG_select]
    data.FFT_window  = np.r_["0", data.FFT_window, data1.FFT_window]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    data.Pol_sep_thres = np.r_["0", data.Pol_sep_thres, data1.Pol_sep_thres]
    data.Pol_sep_SW  = np.r_["0", data.Pol_sep_SW, data1.Pol_sep_SW]
    # data.overflow_U  = np.r_["0", data.overflow_U, data1.overflow_U]
    # data.overflow_V  = np.r_["0", data.overflow_V, data1.overflow_V]
    # data.overflow_W  = np.r_["0", data.overflow_W, data1.overflow_W]
    data.proc_param0 = np.r_["0", data.proc_param0, data1.proc_param0]
    data.proc_param1 = np.r_["0", data.proc_param1, data1.proc_param1]
    data.proc_param2 = np.r_["0", data.proc_param2, data1.proc_param2]
    data.proc_param3 = np.r_["0", data.proc_param3, data1.proc_param3]
    data.BG_downlink = np.r_["0", data.BG_downlink, data1.BG_downlink]
    data.N_block     = np.r_["0", data.N_block, data1.N_block]
    data.Rich_flag   = np.r_["0", data.Rich_flag, data1.Rich_flag]
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.N_samp      = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step      = np.r_["0", data.N_step, data1.N_step]
    data.decimation  = np.r_["0", data.decimation, data1.decimation]
    data.pol         = np.r_["0", data.pol, data1.pol]
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver     = np.r_["0", data.ISW_ver, data1.ISW_ver]
    data.B0_startf   = np.r_["0", data.B0_startf, data1.B0_startf]
    data.B0_stopf    = np.r_["0", data.B0_stopf, data1.B0_stopf]
    data.B0_step     = np.r_["0", data.B0_step, data1.B0_step]
    data.B0_repeat   = np.r_["0", data.B0_repeat, data1.B0_repeat]
    data.B0_subdiv   = np.r_["0", data.B0_subdiv, data1.B0_subdiv]
    data.B1_startf   = np.r_["0", data.B1_startf, data1.B1_startf]
    data.B1_stopf    = np.r_["0", data.B1_stopf, data1.B1_stopf]
    data.B1_step     = np.r_["0", data.B1_step, data1.B1_step]
    data.B1_repeat   = np.r_["0", data.B1_repeat, data1.B1_repeat]
    data.B1_subdiv   = np.r_["0", data.B1_subdiv, data1.B1_subdiv]
    data.B2_startf   = np.r_["0", data.B2_startf, data1.B2_startf]
    data.B2_stopf    = np.r_["0", data.B2_stopf, data1.B2_stopf]
    data.B2_step     = np.r_["0", data.B2_step, data1.B2_step]
    data.B2_repeat   = np.r_["0", data.B2_repeat, data1.B2_repeat]
    data.B2_subdiv   = np.r_["0", data.B2_subdiv, data1.B2_subdiv]
    data.B3_startf   = np.r_["0", data.B3_startf, data1.B3_startf]
    data.B3_stopf    = np.r_["0", data.B3_stopf, data1.B3_stopf]
    data.B3_step     = np.r_["0", data.B3_step, data1.B3_step]
    data.B3_repeat   = np.r_["0", data.B3_repeat, data1.B3_repeat]
    data.B3_subdiv   = np.r_["0", data.B3_subdiv, data1.B3_subdiv]
    data.B4_startf   = np.r_["0", data.B4_startf, data1.B4_startf]
    data.B4_stopf    = np.r_["0", data.B4_stopf, data1.B4_stopf]
    data.B4_step     = np.r_["0", data.B4_step, data1.B4_step]
    data.B4_repeat   = np.r_["0", data.B4_repeat, data1.B4_repeat]
    data.B4_subdiv   = np.r_["0", data.B4_subdiv, data1.B4_subdiv]
    # Data
    data.epoch       = np.r_["0", data.epoch, data1.epoch]
    data.scet        = np.r_["0", data.scet, data1.scet]
    #
    data.Eu_i        = np.r_["0", data.Eu_i, data1.Eu_i]
    data.Eu_q        = np.r_["0", data.Eu_q, data1.Eu_q]
    data.Ev_i        = np.r_["0", data.Ev_i, data1.Ev_i]
    data.Ev_q        = np.r_["0", data.Ev_q, data1.Ev_q]
    data.Ew_i        = np.r_["0", data.Ew_i, data1.Ew_i]
    data.Ew_q        = np.r_["0", data.Ew_q, data1.Ew_q]
    data.pps_count   = np.r_["0", data.pps_count, data1.pps_count] 
    data.sweep_start = np.r_["0", data.sweep_start, data1.sweep_start]
    data.reduction   = np.r_["0", data.reduction, data1.reduction]
    data.overflow    = np.r_["0", data.overflow, data1.overflow]
    #
    data.time        = np.r_["0", data.time, data1.time]
    data.frequency   = np.r_["0", data.frequency, data1.frequency]
    data.freq_step   = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width  = np.r_["0", data.freq_width, data1.freq_width]
    return data


def hf_sid2_shaping(data, cal_mode):
    """
    input:  data, cal_mode
    return: data
    """
    # Size
    n_time = data.Eu_i.shape[0];  n_freq = data.N_step[n_time//2];  n_samp = data.N_samp[n_time//2];  n_num = n_freq * n_samp
    print("  org:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "[", n_num, "]")

    # CUT & Shaping: less packet length
    if n_num < data.Eu_i.shape[1]:
        data.Eu_i = data.Eu_i[:, 0:n_num];  data.Eu_q = data.Eu_q[:, 0:n_num]
        data.Ev_i = data.Ev_i[:, 0:n_num];  data.Ev_q = data.Ev_q[:, 0:n_num]
        data.Ew_i = data.Ew_i[:, 0:n_num];  data.Ew_q = data.Ew_q[:, 0:n_num]
        data.pps_count   = data.pps_count  [:, 0:n_num]
        data.sweep_start = data.sweep_start[:, 0:n_num]
        data.reduction   = data.reduction  [:, 0:n_num]
        data.overflow    = data.overflow   [:, 0:n_num]
        data.time        = data.time       [:, 0:n_num]
        data.frequency   = data.frequency  [:, 0:n_num]
        data.freq_step   = data.freq_step  [:, 0:n_num]
        data.freq_width  = data.freq_width [:, 0:n_num]
        print(" cut1:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "[", n_num, "]")

    # Merge & CUT: separated packets
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
            data.epoch = np.array(data.epoch).reshape(n_time, i);   print(data.epoch)
            data.epoch = data.epoch[:, 0];                          print(data.epoch.shape, data.epoch)

    # Reshape from "2D: n_time * (n_freq * n_samp)" to "3D: n_time * n_freq * n_samp"
    data.Eu_i        = np.array(data.Eu_i).reshape(n_time, n_freq, n_samp)
    data.Eu_q        = np.array(data.Eu_q).reshape(n_time, n_freq, n_samp)
    data.Ev_i        = np.array(data.Ev_i).reshape(n_time, n_freq, n_samp)
    data.Ev_q        = np.array(data.Ev_q).reshape(n_time, n_freq, n_samp)
    data.Ew_i        = np.array(data.Ew_i).reshape(n_time, n_freq, n_samp)
    data.Ew_q        = np.array(data.Ew_q).reshape(n_time, n_freq, n_samp)
    data.pps_count   = np.array(data.pps_count).reshape(n_time, n_freq, n_samp)
    data.sweep_start = np.array(data.sweep_start).reshape(n_time, n_freq, n_samp)
    data.reduction   = np.array(data.reduction).reshape(n_time, n_freq, n_samp)
    data.overflow    = np.array(data.overflow).reshape(n_time, n_freq, n_samp)
    data.time        = np.array(data.time).reshape(n_time, n_freq, n_samp)
    data.frequency   = np.array(data.frequency).reshape(n_time, n_freq, n_samp)
    data.freq_step   = np.array(data.freq_step).reshape(n_time, n_freq, n_samp)
    data.freq_width  = np.array(data.freq_width).reshape(n_time, n_freq, n_samp)
    print(" sort:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp)

    # CUT & Reshape for separated packets with a short end
    if n_freq > n_freq0:
        n_freq = n_freq0
        data.Eu_i        = data.Eu_i[:, 0:n_freq]
        data.Eu_q        = data.Eu_q[:, 0:n_freq]
        data.Ev_i        = data.Ev_i[:, 0:n_freq]
        data.Ev_q        = data.Ev_q[:, 0:n_freq]
        data.Ew_i        = data.Ew_i[:, 0:n_freq]
        data.Ew_q        = data.Ew_q[:, 0:n_freq]
        data.pps_count   = data.pps_count[:, 0:n_freq]
        data.sweep_start = data.sweep_start[:, 0:n_freq]
        data.reduction   = data.reduction[:, 0:n_freq]
        data.overflow    = data.overflow[:, 0:n_freq]
        data.time        = data.time[:, 0:n_freq]
        data.frequency   = data.frequency[:, 0:n_freq]
        data.freq_step   = data.freq_step[:, 0:n_freq]
        data.freq_width   = data.freq_width[:, 0:n_freq]
        print(" cut3:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp)

    # ### ASW1: data shift -16
    date = data.epoch[0];  month = date.strftime('%Y%m')
    if month == "202304" or month == "202305" or month == "202307":
        data.Eu_i[:, -1, n_samp//2:n_samp] = 0.;  data.Eu_q[:, -1, n_samp//2:n_samp] = 0.
        data.Ev_i[:, -1, n_samp//2:n_samp] = 0.;  data.Ev_q[:, -1, n_samp//2:n_samp] = 0.
        data.Ew_i[:, -1, n_samp//2:n_samp] = 0.;  data.Ew_q[:, -1, n_samp//2:n_samp] = 0.

    # ### ASW1: CAL flag
    if data.cal_signal[0] == 255:
        power = data.Eu_i[:,-1]**2 + data.Eu_q[:,-1]**2 + data.Ev_i[:,-1]**2 + data.Ev_q[:,-1]**2 + data.Ew_i[:,-1]**2 + data.Ew_q[:,-1]**2
        power = np.mean(power, axis=1)
        index = np.where(power > 1e4)
        data.cal_signal[:] = 0
        data.cal_signal[index[0]] = 1

    # Selection: CAL
    if cal_mode < 2:
        index = np.where(data.cal_signal == cal_mode)
        # AUX
        data.U_selected  = data.U_selected [index[0]]
        data.V_selected  = data.V_selected [index[0]]
        data.W_selected  = data.W_selected [index[0]]
        data.cal_signal  = data.cal_signal [index[0]]
        data.sweep_table = data.sweep_table[index[0]]
        #
        data.onboard_cal = data.onboard_cal[index[0]]
        data.complex     = data.complex    [index[0]]
        data.BG_subtract = data.BG_subtract[index[0]]
        data.BG_select   = data.BG_select  [index[0]]
        data.FFT_window  = data.FFT_window [index[0]]
        data.RFI_rejection = data.RFI_rejection[index[0]]
        data.Pol_sep_thres = data.Pol_sep_thres[index[0]]
        data.Pol_sep_SW  = data.Pol_sep_SW [index[0]]
        # data.overflow_U  = data.overflow_U [index[0]]
        # data.overflow_V  = data.overflow_V [index[0]]
        # data.overflow_W  = data.overflow_W [index[0]]
        data.proc_param0 = data.proc_param0[index[0]]
        data.proc_param1 = data.proc_param1[index[0]]
        data.proc_param2 = data.proc_param2[index[0]]
        data.proc_param3 = data.proc_param3[index[0]]
        data.BG_downlink = data.BG_downlink[index[0]]
        data.N_block     = data.N_block    [index[0]]
        data.Rich_flag   = data.Rich_flag  [index[0]]
        data.T_RWI_CH1   = data.T_RWI_CH1  [index[0]]
        data.T_RWI_CH2   = data.T_RWI_CH2  [index[0]]
        data.T_HF_FPGA   = data.T_HF_FPGA  [index[0]]
        # Header
        data.N_samp      = data.N_samp     [index[0]]
        data.N_step      = data.N_step     [index[0]]
        data.decimation  = data.decimation [index[0]]
        data.pol         = data.pol        [index[0]]
        data.ADC_ovrflw  = data.ADC_ovrflw [index[0]]
        data.ISW_ver     = data.ISW_ver    [index[0]]
        data.B0_startf   = data.B0_startf  [index[0]]
        data.B0_stopf    = data.B0_stopf   [index[0]]
        data.B0_step     = data.B0_step    [index[0]]
        data.B0_repeat   = data.B0_repeat  [index[0]]
        data.B0_subdiv   = data.B0_subdiv  [index[0]]
        data.B1_startf   = data.B1_startf  [index[0]]
        data.B1_stopf    = data.B1_stopf   [index[0]]
        data.B1_step     = data.B1_step    [index[0]]
        data.B1_repeat   = data.B1_repeat  [index[0]]
        data.B1_subdiv   = data.B1_subdiv  [index[0]]
        data.B2_startf   = data.B2_startf  [index[0]]
        data.B2_stopf    = data.B2_stopf   [index[0]]
        data.B2_step     = data.B2_step    [index[0]]
        data.B2_repeat   = data.B2_repeat  [index[0]]
        data.B2_subdiv   = data.B2_subdiv  [index[0]]
        data.B3_startf   = data.B3_startf  [index[0]]
        data.B3_stopf    = data.B3_stopf   [index[0]]
        data.B3_step     = data.B3_step    [index[0]]
        data.B3_repeat   = data.B3_repeat  [index[0]]
        data.B3_subdiv   = data.B3_subdiv  [index[0]]
        data.B4_startf   = data.B4_startf  [index[0]]
        data.B4_stopf    = data.B4_stopf   [index[0]]
        data.B4_step     = data.B4_step    [index[0]]
        data.B4_repeat   = data.B4_repeat  [index[0]]
        data.B4_subdiv   = data.B4_subdiv  [index[0]]
        # Data
        data.epoch       = data.epoch      [index[0]];  data.scet = data.scet[index[0]]
        data.Eu_i        = data.Eu_i       [index[0]];  data.Eu_q = data.Eu_q[index[0]]
        data.Ev_i        = data.Ev_i       [index[0]];  data.Ev_q = data.Ev_q[index[0]]
        data.Ew_i        = data.Ew_i       [index[0]];  data.Ew_q = data.Ew_q[index[0]]
        data.pps_count   = data.pps_count  [index[0]]
        data.sweep_start = data.sweep_start[index[0]]
        data.reduction   = data.reduction  [index[0]]
        data.overflow    = data.overflow   [index[0]]
        data.time        = data.time       [index[0]]
        data.frequency   = data.frequency  [index[0]]
        data.freq_step   = data.freq_step  [index[0]]
        data.freq_width  = data.freq_width [index[0]]

        n_time = data.Eu_i.shape[0]
        if cal_mode == 0: print("  cut:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "<only BG>")
        else:             print("  cut:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "<only CAL>")

    # NAN
    index = np.where(data.U_selected == 0);  data.Eu_i[index[0]] = math.nan;  data.Eu_q[index[0]] = math.nan
    index = np.where(data.V_selected == 0);  data.Ev_i[index[0]] = math.nan;  data.Ev_q[index[0]] = math.nan
    index = np.where(data.W_selected == 0);  data.Ew_i[index[0]] = math.nan;  data.Ew_q[index[0]] = math.nan
    return data


def hf_sid2_spec_nan(data, i):
    data.EE        [i] = math.nan; 
    data.EuEu      [i] = math.nan; data.EvEv      [i] = math.nan; data.EwEw      [i] = math.nan
    data.EuEv_re   [i] = math.nan; data.EvEw_re   [i] = math.nan; data.EwEu_re   [i] = math.nan
    data.EuEv_im   [i] = math.nan; data.EvEw_im   [i] = math.nan; data.EwEu_im   [i] = math.nan