"""
    JUICE RPWI HF SID22 (PSSR2 rich): L1a QL -- 2024/9/19
"""
import numpy as np
import juice_cdf_lib as juice_cdf


class struct:
    pass


#---------------------------------------------------------------------
#--- SID20 ------------------------------------------------------------
#---------------------------------------------------------------------
def hf_sid22_read(cdf, RPWI_FSW_version):
    """
    input:  CDF, cf:conversion factor
    return: data
    """
    data = struct()
    data.RPWI_FSW_version = RPWI_FSW_version

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
    data.freq_auto_corr = cdf['freq_auto_corr'][...]

    return data


def hf_sid22_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # AUX
    data.ch_selected    = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal     = np.r_["0", data.cal_signal, data1.cal_signal]
    data.pol_AUX        = np.r_["0", data.pol_AUX, data1.pol_AUX]
    data.decimation_AUX = np.r_["0", data.decimation_AUX, data1.decimation_AUX]
    data.N_samp_AUX     = np.r_["0", data.N_samp_AUX, data1.N_samp]
    data.N_auto_corr    = np.r_["0", data.N_auto_corr, data1.N_auto_corr]
    data.N_step_AUX     = np.r_["0", data.N_step_AUX, data1.N_step]
    data.freq_start     = np.r_["0", data.freq_start, data1.freq_start]
    data.freq_stop      = np.r_["0", data.freq_stop, data1.freq_stop]

    # Header
    data.N_samp         = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step         = np.r_["0", data.N_step, data1.N_step]
    data.decimation     = np.r_["0", data.decimation, data1.decimation]
    data.pol            = np.r_["0", data.pol, data1.pol]
    data.B0_startf      = np.r_["0", data.B0_startf, data1.B0_startf]
    data.B0_stopf       = np.r_["0", data.B0_stopf, data1.B0_stopf]
    data.B0_step        = np.r_["0", data.B0_step, data1.B0_step]
    data.B0_repeat      = np.r_["0", data.B0_repeat, data1.B0_repeat]
    data.B0_subdiv      = np.r_["0", data.B0_subdiv, data1.B0_subdiv]

    # Data
    data.epoch          = np.r_["0", data.epoch, data1.epoch]
    data.scet           = np.r_["0", data.scet, data1.scet]
    #
    data.auto_corr      = np.r_["0", data.auto_corr, data1.auto_corr]
    data.freq_auto_corr = np.r_["0", data.freq_auto_corr, data1.freq_auto_corr]
        
    return data


def hf_sid22_shaping(data):
    """
    input:  data
    return: data
    """
    n_time = data.auto_corr.shape[0]
    data.auto_corr = np.array(data.auto_corr).reshape(n_time, 16, data.N_samp_AUX[0])
    data.time = np.arange(0, data.N_samp_AUX[0], 1) / juice_cdf._sample_rate(data.decimation_AUX[0])

    return data