"""
    JUICE RPWI HF SID22 (PSSR2 rich): L1a QL -- 2025/7/5
"""
import numpy as np


class struct:
    pass


#---------------------------------------------------------------------
#--- SID22 ------------------------------------------------------------
#---------------------------------------------------------------------
def hf_sid22_read(cdf, sid, RPWI_FSW_version):
    """
    input:  CDF, cf:conversion factor
    return: data
    """
    data = struct()
    data.RPWI_FSW_version = RPWI_FSW_version

    # Data
    data.E_i         = np.float64(cdf['E_i'][...]);  data.E_q            = np.float64(cdf['E_q'][...])
    data.auto_corr   = np.float64(cdf['auto_corr'][...])
    data.frequency   = cdf['frequency'][...]
    data.time        = np.float64(cdf['time'][...])
    data.epoch       = cdf['Epoch'][...];        data.scet      = cdf['SCET'][...]
    # AUX
    data.ch_selected = cdf['ch_selected'][...]      # [0:U  1:V  2:W]
    data.cal_signal  = cdf['cal_signal'][...]
    data.N_lag       = np.int64(cdf['N_lag'][...])
    #
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    # Header
    data.N_step      = np.int64(cdf['N_step'][...])
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]
    data.ISW_ver   = cdf['ISW_ver'][...]

    return data


def hf_sid22_add(data, data1, sid):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.E_i         = np.r_["0", data.E_i, data1.E_i]
    data.E_q         = np.r_["0", data.E_q, data1.E_q]
    data.auto_corr   = np.r_["0", data.auto_corr, data1.auto_corr]
    data.frequency   = np.r_["0", data.frequency, data1.frequency]
    data.time        = np.r_["0", data.time, data1.time]
    data.epoch       = np.r_["0", data.epoch, data1.epoch]
    data.scet        = np.r_["0", data.scet, data1.scet]
    # AUX
    data.ch_selected = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.N_lag       = np.r_["0", data.N_lag, data1.N_lag]
    #
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.N_step      = np.r_["0", data.N_step, data1.N_step]
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver     = np.r_["0", data.ISW_ver, data1.ISW_ver]

    return data


def hf_sid22_shaping(data, sid):
    """
    input:  data
    return: data
    """

    # Size - original
    data.n_time  = data.auto_corr.shape[0]
    data.n_step  = data.N_step[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("    org:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag)

    # ---------------------------
    # --- shape-check ---
    # ---------------------------
    index = np.where( (data.N_step == data.n_step) & (data.N_lag == data.n_lag) )
    # Data
    data.auto_corr   = data.auto_corr [index[0]]
    data.E_i         = data.E_i [index[0]];        data.E_q = data.E_q [index[0]]
    data.frequency   = data.frequency [index[0]];  data.time        = data.time [index[0]]
    data.epoch       = data.epoch[index[0]];       data.scet = data.scet[index[0]]
    # AUX
    data.ch_selected = data.ch_selected[index[0]]
    data.cal_signal  = data.cal_signal [index[0]]
    data.N_lag       = data.N_lag [index[0]]
    #
    data.T_RWI_CH1   = data.T_RWI_CH1[index[0]]
    data.T_RWI_CH2   = data.T_RWI_CH2[index[0]]
    data.T_HF_FPGA   = data.T_HF_FPGA[index[0]]
    # Header
    data.N_step      = data.N_step    [index[0]]
    data.ADC_ovrflw  = data.ADC_ovrflw[index[0]]
    data.ISW_ver     = data.ISW_ver   [index[0]]

    data.n_time  = data.auto_corr.shape[0]
    data.n_step  = data.N_step[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("    cut:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag)
    
    return data
