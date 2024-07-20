"""
    JUICE RPWI HF SID22 (PSSR2 rich): L1a QL -- 2024/7/20
"""
import numpy as np
import juice_cdf_lib as juice_cdf


class struct:
    pass


#---------------------------------------------------------------------
#--- SID20 ------------------------------------------------------------
#---------------------------------------------------------------------
def juice_getdata_hf_sid22(cdf):
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
    data.N_samp_AUX = cdf['N_samp_AUX'][...]
    data.N_auto_corr = cdf['N_auto_corr'][...]
    data.N_step_AUX = cdf['N_step_AUX'][...]
    data.freq_start = cdf['freq_start'][...]
    data.freq_stop = cdf['freq_stop'][...]

    # Header
    data.N_samp = cdf['N_samp'][...]            # not used
    data.N_step = cdf['N_step'][...]            # [same with ‘N_step_AUX’]
    data.decimation = cdf['decimation'][...]    # [same with ‘decimation_AUX’]
    data.pol = cdf['pol'][...]                  # [same with ‘pol_AUX’]	
    data.B0_startf = cdf['B0_startf'][...]
    data.B0_stopf = cdf['B0_stopf'][...]
    data.B0_step = cdf['B0_step'][...]
    data.B0_repeat = cdf['B0_repeat'][...]
    data.B0_subdiv = cdf['B0_subdiv'][...]

    # Data
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]
    #
    data.auto_corr = cdf['auto_corr'][...]
    n_time = data.auto_corr.shape[0]
    data.auto_corr = np.array(data.auto_corr).reshape(n_time, 16, data.N_samp_AUX[0])
    #
    data.freq_auto_corr = cdf['freq_auto_corr'][...]
    data.time = np.arange(0, data.N_samp_AUX[0], 1) / juice_cdf._sample_rate(data.decimation_AUX[0])

    return data