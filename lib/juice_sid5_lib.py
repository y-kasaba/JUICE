"""
    JUICE RPWI HF SID5 (PSSR1 surv): L1a QL -- 2025/7/4
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

    # Data
    data.EE         = np.float64(cdf['EE'][...])
    data.frequency  = cdf['frequency'][...];   data.freq_step = cdf['freq_step'][...]; data.freq_width = cdf['freq_width'][...]
    data.epoch       = cdf['Epoch'][...];      data.scet      = cdf['SCET'][...]
    # AUX
    data.ch_selected = cdf['ch_selected'][...]      # [0:U  1:V  2:W]
    data.cal_signal  = cdf['cal_signal'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    #
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    # Header
    data.N_step      = np.int64(cdf['N_step'][...])
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]
    data.ISW_ver     = cdf['ISW_ver'][...]
    return data


def hf_sid5_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.EE           = np.r_["0", data.EE, data1.EE]
    data.frequency    = np.r_["0", data.frequency, data1.frequency]
    data.freq_step    = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width   = np.r_["0", data.freq_width, data1.freq_width]
    data.epoch        = np.r_["0", data.epoch, data1.epoch]
    data.scet         = np.r_["0", data.scet, data1.scet]
    # AUX
    data.ch_selected   = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal    = np.r_["0", data.cal_signal, data1.cal_signal]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    #
    data.T_RWI_CH1     = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2     = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA     = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.N_step       = np.r_["0", data.N_step, data1.N_step]
    data.ADC_ovrflw   = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver      = np.r_["0", data.ISW_ver, data1.ISW_ver]
    return data


def hf_sid5_shaping(data, cal_mode):
    """
    input:  data
            cal_mode    [Power]     0: background          1: CAL           2: all
    return: data
    """
    n_time = data.EE.shape[0];  n_freq = data.EE.shape[1]
    print("  org:", data.EE.shape, n_time, "x", n_freq, "[", n_time*n_freq, "]")

    if cal_mode < 2:
        index = np.where( (data.cal_signal == cal_mode)                                                 )
        print("  cut:", data.EE.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode)

        # Data
        data.EE          = data.EE        [index[0]]
        data.frequency   = data.frequency [index[0]]
        data.freq_step   = data.freq_step [index[0]]
        data.freq_width  = data.freq_width[index[0]]
        data.epoch       = data.epoch     [index[0]]
        data.scet        = data.scet      [index[0]]
        # AUX
        data.ch_selected = data.ch_selected[index[0]]
        data.cal_signal  = data.cal_signal[index[0]]
        data.RFI_rejection = data.RFI_rejection[index[0]]
        #
        data.T_RWI_CH1   = data.T_RWI_CH1 [index[0]]
        data.T_RWI_CH2   = data.T_RWI_CH2 [index[0]]
        data.T_HF_FPGA   = data.T_HF_FPGA [index[0]]
        # Header
        data.N_samp      = data.N_samp    [index[0]]
        data.ADC_ovrflw  = data.ADC_ovrflw[index[0]]
        data.ISW_ver     = data.ISW_ver   [index[0]]
    
        n_time = data.EE.shape[0]
        if cal_mode < 2:
            print("  cut:", data.EE.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode)
        if cal_mode == 0:         print("<only BG>")
        else:                     print("<only CAL>")

    data.n_time = data.EE.shape[0]
    data.n_step = data.N_step[data.n_time//2]

    # *** frequncy & width for spec cal
    data.freq   = data.frequency
    data.freq_w = data.freq_width
    return data


def spec_nan(data, i):
    data.EE[i] = math.nan