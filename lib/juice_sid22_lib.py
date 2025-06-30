"""
    JUICE RPWI HF SID22 (PSSR2 rich): L1a QL -- 2025/6/29
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

    # AUX
    data.ch_selected = cdf['ch_selected'][...]      # [0:U  1:V  2:W]
    data.cal_signal  = cdf['cal_signal'][...]
    data.N_lag       = np.int64(cdf['N_lag'][...])
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])

    # Header
    data.N_samp      = np.int64(cdf['N_samp'][...])
    data.N_step      = np.int64(cdf['N_step'][...])
    data.decimation  = cdf['decimation'][...]
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]
    data.ISW_ver   = cdf['ISW_ver'][...]

    # Data
    data.E_i            = np.float64(cdf['E_i'][...]);  data.E_q            = np.float64(cdf['E_q'][...])
    data.auto_corr      = np.float64(cdf['auto_corr'][...])
    data.freq_auto_corr = cdf['freq_auto_corr'][...]
    data.time           = np.float64(cdf['time'][...])
    #
    data.epoch       = cdf['Epoch'][...]

    return data


def hf_sid22_add(data, data1, sid):
    """
    input:  data, data1
    return: data
    """
    # AUX
    data.ch_selected = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.N_lag       = np.r_["0", data.N_lag, data1.N_lag]
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]

    # Header
    data.N_samp      = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step      = np.r_["0", data.N_step, data1.N_step]
    data.decimation  = np.r_["0", data.decimation, data1.decimation]
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver     = np.r_["0", data.ISW_ver, data1.ISW_ver]

    # Data
    data.epoch       = np.r_["0", data.epoch, data1.epoch]
    #
    data.E_i            = np.r_["0", data.E_i, data1.E_i]
    data.E_q            = np.r_["0", data.E_q, data1.E_q]
    data.auto_corr      = np.r_["0", data.auto_corr, data1.auto_corr]
    data.freq_auto_corr = np.r_["0", data.freq_auto_corr, data1.freq_auto_corr]
    data.time           = np.r_["0", data.time, data1.time]

    return data


def hf_sid22_shaping(data, sid):
    """
    input:  data
    return: data
    """

    """
    n_time = data.auto_corr.shape[0]
    data.auto_corr = np.array(data.auto_corr).reshape(n_time, data.N_step[0], data.N_lag[0])
    data.time      = np.array(data.time).reshape(n_time, data.N_step[0], data.N_lag[0])
    """

    print("data.E_i",            data.E_i.shape)
    print("data.E_q",            data.E_q.shape)
    print("data.freq_auto_corr", data.freq_auto_corr.shape)
    print("data.auto_corr",      data.auto_corr.shape)
    print("data.time",           data.time.shape)
    
    return data
