"""
    JUICE RPWI HF SID7 (PSSR3 surv): L1a QL -- 2025/6/29
"""
import numpy as np
import juice_cdf_lib as juice_cdf


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID7 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid7_read(cdf, RPWI_FSW_version):
    """
    input:  CDF
    return: data
    """
    data = struct()
    data.RPWI_FSW_version = RPWI_FSW_version

    # AUX
    data.ch_selected = cdf['ch_selected'][...]
    data.cal_signal  = cdf['cal_signal'][...]
    data.N_block     = np.int16(cdf['N_block'][...])
    data.N_lag       = np.int16(cdf['N_lag'][...])
    data.N_feed      = np.int16(cdf['N_feed'][...])
    data.N_skip      = np.int16(cdf['N_skip'][...])
    data.freq_center = cdf['freq_center'][...]
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    # Header
    data.N_samp      = np.int64(cdf['N_samp'][...]) 
    data.N_step      = np.int64(cdf['N_step'][...]) 
    data.decimation  = cdf['decimation'][...]       
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]; 
    data.ISW_ver     = cdf['ISW_ver'][...]
    # Data
    data.E_i            = np.float64(cdf['E_i'][...]);  
    data.E_q            = np.float64(cdf['E_q'][...])
    data.auto_corr      = np.float64(cdf['auto_corr'][...])
    data.time_auto_corr = cdf['time_auto_corr'][...]
    data.time           = np.float64(cdf['time'][...])
    #
    data.epoch       = cdf['Epoch'][...]

    return data


def hf_sid7_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # AUX
    data.ch_selected = np.r_["0", data.ch_selected, data1.U_selected]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.N_block     = np.r_["0", data.N_block, data1.N_block]
    data.N_lag       = np.r_["0", data.N_lag, data1.N_lag]
    data.N_skip      = np.r_["0", data.N_skip, data1.N_skip]
    data.N_feed      = np.r_["0", data.N_feed, data1.N_feed]
    data.freq_center = np.r_["0", data.freq_center, data1.freq_center]
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
    data.E_i            = np.r_["0", data.E_i, data1.E_i]
    data.E_q            = np.r_["0", data.E_q, data1.E_q]
    data.auto_corr      = np.r_["0", data.auto_corr, data1.auto_corr]
    data.time_auto_corr = np.r_["0", data.time_auto_corr, data1.time_auto_corr]
    data.time           = np.r_["0", data.time, data1.time]
    #
    data.epoch          = np.r_["0", data.epoch, data1.epoch]
    return data



def hf_sid7_shaping(data):
    """
    input:  data
    return: data
    """
    # CUT & Reshape
    data.n_time = data.auto_corr.shape[0]
    n_num = data.N_block[0] * data.N_lag[0]
    if n_num < data.auto_corr.shape[1]:
        print(" org:", data.auto_corr.shape, data.N_block[0], data.N_lag[0])
        data.auto_corr = data.auto_corr[:, 0:n_num]
        data.time = data.time[:, 0:n_num]
        print(" cut:", data.auto_corr.shape, data.N_block[0], data.N_lag[0])
    data.auto_corr = np.array(data.auto_corr).reshape(data.n_time, data.N_block[0], data.N_lag[0])
    data.time      = np.array(data.time).reshape(data.n_time, data.N_block[0], data.N_lag[0])
    
    # Time
    # data.time = np.arange(0, data.N_samp[0], 1) / data.N_samp[0] / juice_cdf._sample_rate(data.decimation[0]) * 2048

    print("data.E_i",            data.E_i.shape)
    print("data.E_q",            data.E_q.shape)
    print("data.time_auto_corr", data.time_auto_corr.shape)
    print("data.auto_corr",      data.auto_corr.shape)
    print("data.time",           data.time.shape)

    return data