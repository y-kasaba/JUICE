# JUICE RPWI HF SID23 (PSSR3 rich): L1a QL -- 2023/10/15

class struct:
    pass
import numpy as np

#---------------------------------------------------------------------
#--- SID20 ------------------------------------------------------------
#---------------------------------------------------------------------
def juice_getdata_hf_sid23(cdf):

    data = struct()

    # Data
    data.Eu_i = cdf['Eu_i'][...]
    data.Eu_q = cdf['Eu_q'][...]
    data.Ev_i = cdf['Ev_i'][...]
    data.Ev_q = cdf['Ev_q'][...]
    data.Ew_i = cdf['Ew_i'][...]
    data.Ew_q = cdf['Ew_q'][...]
    data.pps_count = cdf['pps_count'][...]
    data.sweep_start = cdf['sweep_start'][...]
    data.reduction = cdf['reduction'][...]
    data.overflow = cdf['overflow'][...]
    #
    data.time = cdf['time'][...]
    #s
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]

    # AUX
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    data.cal_signal = cdf['cal_signal'][...]
    data.pol_AUX = cdf['pol_AUX'][...]
    data.decimation_AUX = cdf['decimation_AUX'][...]
    data.N_block = cdf['N_block'][...]
    data.freq_center = cdf['freq_center'][...]
    data.N_feed = cdf['N_feed'][...]
    data.N_skip = cdf['N_skip'][...]

    # Header
    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]
    data.pol = cdf['pol'][...]

    # Reshape: Auto_Corr
    # n_time = data.auto_corr.shape[0]
    # data.auto_corr = np.array(data.auto_corr).reshape(n_time, 16, data.N_samp_AUX[0])

    # Time
    # data.time = np.arange(0, data.N_samp_AUX[0], 1) / (296e+3 / 2**data.decimation_AUX[0])

    return data