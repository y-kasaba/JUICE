"""
    JUICE RPWI HF SID7 (PSSR3 surv): L1a QL -- 2024/9/29
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
    data.U_selected  = cdf['U_selected'][...]
    data.V_selected  = cdf['V_selected'][...]
    data.W_selected  = cdf['W_selected'][...]
    data.cal_signal  = cdf['cal_signal'][...]
    data.pol_AUX     = cdf['pol_AUX'][...]
    data.decimation_AUX = cdf['decimation_AUX'][...]
    data.N_block     = np.int16(cdf['N_block'][...])
    data.interval    = cdf['interval'][...]
    data.freq_center = cdf['freq_center'][...]
    data.N_samp_AUX  = np.int16(cdf['N_samp_AUX'][...])
    data.T_RWI_CH1   = np.float64(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float64(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float64(cdf['T_HF_FPGA'][...])

    # Header
    data.N_samp      = np.int64(cdf['N_samp'][...]) # not used
    data.N_step      = np.int64(cdf['N_step'][...]) # [same with ‘N_step_AUX’]
    data.decimation  = cdf['decimation'][...]    # [same with ‘decimation_AUX’]
    data.pol         = cdf['pol'][...]                  # [same with ‘pol_AUX’]	

    # Data: N_auto_corr (128) * N_step_AUX (48) x 4B = 24576
    data.epoch       = cdf['Epoch'][...]
    data.scet        = cdf['SCET'][...]
    #
    data.auto_corr   = np.float64(cdf['auto_corr'][...])
    return data


def hf_sid7_add(data, data1):
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
    data.interval       = np.r_["0", data.interval, data1.interval]
    data.freq_center    = np.r_["0", data.freq_center, data1.freq_center]
    data.N_samp_AUX     = np.r_["0", data.N_samp_AUX, data1.N_samp_AUX]
    data.T_RWI_CH1      = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2      = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA      = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]

    # Header
    data.N_samp         = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step         = np.r_["0", data.N_step, data1.N_step]
    data.decimation     = np.r_["0", data.decimation, data1.decimation]
    data.pol            = np.r_["0", data.pol, data1.pol]

    # Data: N_auto_corr (128) * N_step_AUX (48) x 4B = 24576
    data.epoch          = np.r_["0", data.epoch, data1.epoch]
    data.scet           = np.r_["0", data.scet, data1.scet]
    #
    data.auto_corr      = np.r_["0", data.auto_corr, data1.auto_corr]

    return data



def hf_sid7_shaping(data):
    """
    input:  data
    return: data
    """
    # CUT & Reshape
    data.n_time = data.auto_corr.shape[0]
    n_num = data.N_block[0] * data.N_samp_AUX[0]
    if n_num < data.auto_corr.shape[1]:
        print(" org:", data.auto_corr.shape, data.N_block[0], data.N_samp_AUX[0])
        data.auto_corr = data.auto_corr[:, 0:n_num]
        print(" cut:", data.auto_corr.shape, data.N_block[0], data.N_samp_AUX[0])
    data.auto_corr = np.array(data.auto_corr).reshape(data.n_time, data.N_block[0], data.N_samp_AUX[0])
    
    # Time
    data.time = np.arange(0, data.N_samp_AUX[0], 1) / data.N_samp_AUX[0] / juice_cdf._sample_rate(data.decimation_AUX[0]) * 2048
    return data