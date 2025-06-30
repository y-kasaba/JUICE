"""
    JUICE RPWI HF SID5 (PSSR1 surv): L1a QL -- 2025/6/30
"""
import numpy as np


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID5 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid5_read(cdf, RPWI_FSW_version):
    """
    Input:  cdf
    Output: data
    """
    data = struct()
    data.RPWI_FSW_version = RPWI_FSW_version

    # AUX
    data.U_selected  = cdf['U_selected'][...];  data.V_selected = cdf['V_selected'][...];  data.W_selected = cdf['W_selected'][...]
    data.cal_signal  = cdf['cal_signal'][...]
    data.sweep_table = cdf['sweep_table'][...]  # (fixed: not defined in V.2)
    data.FFT_window  = cdf['FFT_window'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    # data.N_freq      = cdf['N_freq'][...]
    # data.freq_start  = cdf['freq_start'][...]    # [same with ‘B0_startf’]
    # data.freq_stop   = cdf['freq_stop'][...]     # [same with ‘B0_stopf’]
    if RPWI_FSW_version == '3.0':
        data.subdiv_reduction = cdf['proc_param3'][...]
    else:
        data.subdiv_reduction = cdf['subdiv_reduction'][...]
    #
    data.T_RWI_CH1 = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2 = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA = np.float32(cdf['T_HF_FPGA'][...])

    # Header
    data.N_samp      = np.int64(cdf['N_samp'][...])
    data.N_step      = np.int64(cdf['N_step'][...])
    data.decimation  = cdf['decimation'][...]; data.pol       = cdf['pol'][...]
    if data.RPWI_FSW_version == '3.0':  ### tentative !!!!
        data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]; data.ISW_ver   = cdf['ISW_ver'][...]
    data.B0_startf   = cdf['B0_startf'][...];  data.B0_stopf  = cdf['B0_stopf'][...];  data.B0_step   = cdf['B0_step'][...]
    data.B0_repeat   = cdf['B0_repeat'][...];  data.B0_subdiv = cdf['B0_subdiv'][...]

    # Data
    data.frequency  = cdf['frequency'][...];   data.freq_step = cdf['freq_step'][...]; data.freq_width = cdf['freq_width'][...]
    data.epoch      = cdf['Epoch'][...];       data.scet      = cdf['SCET'][...]
    #
    data.EE         = np.float64(cdf['EE'][...])

    return data


def hf_sid5_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # AUX
    data.U_selected    = np.r_["0", data.U_selected, data1.U_selected]
    data.V_selected    = np.r_["0", data.V_selected, data1.V_selected]
    data.W_selected    = np.r_["0", data.W_selected, data1.W_selected]
    data.cal_signal    = np.r_["0", data.cal_signal, data1.cal_signal]
    data.sweep_table   = np.r_["0", data.sweep_table, data1.sweep_table]
    data.FFT_window    = np.r_["0", data.FFT_window, data1.FFT_window]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    data.subdiv_reduction = np.r_["0", data.subdiv_reduction, data1.subdiv_reduction]
    data.T_RWI_CH1     = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2     = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA     = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]

    # Header
    data.N_samp       = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step       = np.r_["0", data.N_step, data1.N_step]
    data.decimation   = np.r_["0", data.decimation, data1.decimation]
    data.pol          = np.r_["0", data.pol, data1.pol]
    if data.RPWI_FSW_version == '3.0':  ### tentative !!!!
        data.ADC_ovrflw   = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
        data.ISW_ver      = np.r_["0", data.ISW_ver, data1.ISW_ver]
    data.B0_startf    = np.r_["0", data.B0_startf, data1.B0_startf]
    data.B0_stopf     = np.r_["0", data.B0_stopf, data1.B0_stopf]
    data.B0_step      = np.r_["0", data.B0_step, data1.B0_step]
    data.B0_repeat    = np.r_["0", data.B0_repeat, data1.B0_repeat]
    data.B0_subdiv    = np.r_["0", data.B0_subdiv, data1.B0_subdiv]
    # Data
    data.frequency    = np.r_["0", data.frequency, data1.frequency]
    data.freq_step    = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width   = np.r_["0", data.freq_width, data1.freq_width]
    #
    data.epoch        = np.r_["0", data.epoch, data1.epoch]
    data.scet         = np.r_["0", data.scet, data1.scet]
    #
    data.EE           = np.r_["0", data.EE, data1.EE]
    return data


def hf_sid5_shaping(data, cal_mode):
    """
    input:  data
            cal_mode    [Power]     0: background          1: CAL           2: all
    return: data
    """
    n_time = data.EE.shape[0];  n_freq = data.EE.shape[1]
    print("  org:", data.EE.shape, n_time, "x", n_freq, "[", n_time*n_freq, "]")
    N_ch0 = data.U_selected + data.V_selected + data.W_selected

    if cal_mode < 2:
        index = np.where( (data.cal_signal == cal_mode)                                                 )
        print("  cut:", data.EE.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode)

        # AUX
        data.U_selected  = data.U_selected[index[0]];  data.V_selected  = data.V_selected[index[0]];  data.W_selected  = data.W_selected[index[0]]
        data.cal_signal  = data.cal_signal[index[0]]
        data.sweep_table = data.sweep_table[index[0]]
        data.FFT_window  = data.FFT_window[index[0]]
        data.RFI_rejection = data.RFI_rejection[index[0]]
        data.subdiv_reduction = data.subdiv_reduction[index[0]]
        data.T_RWI_CH1   = data.T_RWI_CH1 [index[0]]
        data.T_RWI_CH2   = data.T_RWI_CH2 [index[0]]
        data.T_HF_FPGA   = data.T_HF_FPGA [index[0]]
        # Header
        data.N_samp      = data.N_samp    [index[0]]
        data.N_step      = data.N_step    [index[0]]
        data.decimation  = data.decimation[index[0]]
        data.pol         = data.pol       [index[0]]
        if data.RPWI_FSW_version == '3.0':  ### tentative !!!!
            data.ADC_ovrflw  = data.ADC_ovrflw[index[0]]
            data.ISW_ver     = data.ISW_ver   [index[0]]
        data.B0_startf   = data.B0_startf [index[0]];  data.B0_stopf   = data.B0_stopf[index[0]];  data.B0_step = data.B0_step[index[0]]
        data.B0_repeat   = data.B0_repeat [index[0]];  data.B0_subdiv  = data.B0_subdiv[index[0]]
        # Data
        data.epoch       = data.epoch     [index[0]]
        data.scet        = data.scet      [index[0]]
        data.frequency   = data.frequency [index[0]]
        data.freq_step   = data.freq_step [index[0]]
        data.freq_width  = data.freq_width[index[0]]
        #
        data.EE          = data.EE        [index[0]]
    
        n_time = data.EE.shape[0]
        if cal_mode < 2:
            print("  cut:", data.EE.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode)
        if cal_mode == 0:         print("<only BG>")
        else:                     print("<only CAL>")

    # *** frequncy & width for spec cal
    data.freq   = data.frequency
    data.freq_w = data.freq_width
    return data


def spec_nan(data, i):
    data.EE[i] = math.nan