# JUICE RPWI HF SID6 (PSSR2 surv): L1a QL -- 2023/11/11
import numpy as np
import juice_cdf_lib as juice_cdf


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID6 ------------------------------------------------------------
# ---------------------------------------------------------------------
def juice_getdata_hf_sid6(cdf):
    """
    input:  CDF, cf:conversion factor
    return: data
    """
    data = struct()

    # AUX
    data.ch_selected = cdf['ch_selected'][...]      # [0:U  1:V  2:W]
    data.cal_signal = cdf['cal_signal'][...]
    data.pol_AUX = cdf['pol_AUX'][...]
    data.decimation_AUX = cdf['decimation_AUX'][...]
    data.N_step_AUX = cdf['N_step_AUX'][...]
    data.N_auto_corr = cdf['N_auto_corr'][...]
    data.freq_start = cdf['freq_start'][...]
    data.freq_stop = cdf['freq_stop'][...]
    data.T_RWI_CH1 = cdf['T_RWI_CH1'][...]
    data.T_RWI_CH2 = cdf['T_RWI_CH2'][...]
    data.T_HF_FPGA = cdf['T_HF_FPGA'][...]

    # Header
    data.N_samp = cdf['N_samp'][...]           # not used
    data.N_step = cdf['N_step'][...]           # [same with ‘N_step_AUX’]
    data.decimation = cdf['decimation'][...]   # [same with ‘decimation_AUX’]
    data.pol = cdf['pol'][...]                 # [same with ‘pol_AUX’]	
    data.B0_startf = cdf['B0_startf'][...]
    data.B0_stopf = cdf['B0_stopf'][...]
    data.B0_step = cdf['B0_step'][...]
    data.B0_repeat = cdf['B0_repeat'][...]
    data.B0_subdiv = cdf['B0_subdiv'][...]

    # Data: N_auto_corr (128) * N_step_AUX (48) x 4B = 24576
    data.auto_corr = cdf['auto_corr'][...]
    #
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]

    # Reshape: Auto_Corr
    n_time = data.auto_corr.shape[0]
    data.auto_corr = np.array(data.auto_corr).reshape(n_time, data.N_step_AUX[0], data.N_auto_corr[0])

    # Time
    data.time = np.arange(0, data.N_auto_corr[0], 1) / juice_cdf._sample_rate(data.decimation_AUX[0]) * 16
    data.freq = data.freq_start[0] + np.arange(0, data.N_step_AUX[0]-3, 1) * (data.freq_stop[0] - data.freq_start[0]) / (data.N_step_AUX[0] - 4)

    return data
