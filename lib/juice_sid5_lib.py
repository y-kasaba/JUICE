"""
    JUICE RPWI HF SID5 (PSSR1 surv): L1a QL -- 2024/9/28
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
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    #
    data.cal_signal = cdf['cal_signal'][...]
    data.sweep_table = cdf['sweep_table'][...]      # (fixed: not defined in V.2)
    data.FFT_window = cdf['FFT_window'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    data.N_freq     = cdf['N_freq'][...]
    data.freq_start = cdf['freq_start'][...]        # [same with ‘B0_startf’]
    data.freq_stop  = cdf['freq_stop'][...]          # [same with ‘B0_stopf’]
    data.subdiv_reduction = cdf['subdiv_reduction'][...]
    #
    data.T_RWI_CH1 = np.float64(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2 = np.float64(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA = np.float64(cdf['T_HF_FPGA'][...])

    # Header
    data.N_samp = np.int64(cdf['N_samp'][...])
    data.N_step = np.int64(cdf['N_step'][...])
    data.decimation = cdf['decimation'][...]
    data.pol = cdf['pol'][...]
    data.B0_startf = cdf['B0_startf'][...]
    data.B0_stopf  = cdf['B0_stopf'][...]
    data.B0_step   = cdf['B0_step'][...]
    data.B0_repeat = cdf['B0_repeat'][...]
    data.B0_subdiv = cdf['B0_subdiv'][...]

    # Data
    data.frequency  = cdf['frequency'][...]
    data.freq_step  = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]
    #
    data.epoch = cdf['Epoch'][...]
    data.scet  = cdf['SCET'][...]
    #
    data.EE    = np.float64(cdf['EE'][...])

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
    #
    data.cal_signal    = np.r_["0", data.cal_signal, data1.cal_signal]
    data.sweep_table   = np.r_["0", data.sweep_table, data1.sweep_table]
    data.FFT_window    = np.r_["0", data.FFT_window, data1.FFT_window]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    data.N_freq        = np.r_["0", data.N_freq, data1.N_freq]
    data.freq_start    = np.r_["0", data.freq_start, data1.freq_start]
    data.freq_stop     = np.r_["0", data.freq_stop, data1.freq_stop]
    data.subdiv_reduction = np.r_["0", data.subdiv_reduction, data1.subdiv_reduction]
    #
    data.T_RWI_CH1     = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2     = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA     = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]

    # Header
    data.N_samp       = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step       = np.r_["0", data.N_step, data1.N_step]
    data.decimation   = np.r_["0", data.decimation, data1.decimation]
    data.pol          = np.r_["0", data.pol, data1.pol]
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


def hf_sid5_shaping(data):
    """
    input:  data
    return: data
    """
    # CUT
    n_num = np.int16(data.B0_step[0] * data.B0_subdiv[0] / data.subdiv_reduction[0])
    print(data.B0_step[0], data.B0_subdiv[0], data.subdiv_reduction[0])

    if n_num < data.EE.shape[1]:
        print("Cut: ", data.EE.shape[1], " ->", n_num)
        data.EE = data.EE[:, 0:n_num]
        data.frequency = data.frequency[:, 0:n_num]
        data.freq_step = data.freq_step[:, 0:n_num]
        data.freq_width = data.freq_width[:, 0:n_num]

    data.freq   = data.frequency
    data.freq_w = data.freq_width 

    return data