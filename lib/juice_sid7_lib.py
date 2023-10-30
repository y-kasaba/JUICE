# JUICE RPWI HF SID6 (PSSR3 surv): L1a QL -- 2023/10/29

class struct:
    pass
import numpy as np
import juice_cdf_lib as juice_cdf

#---------------------------------------------------------------------
#--- SID7 ------------------------------------------------------------ 
#---------------------------------------------------------------------
def juice_getdata_hf_sid7(cdf):

    data = struct()

    # Data: N_auto_corr (128) * N_step_AUX (48) x 4B = 24576
    data.auto_corr = cdf['auto_corr'][...]
    # data.time = cdf['time'][...]

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
    data.interval = cdf['interval'][...]
    data.freq_center = cdf['freq_center'][...]
    data.N_samp_AUX = cdf['N_samp_AUX'][...]
    data.T_RWI_CH1 = cdf['T_RWI_CH1'][...]
    data.T_RWI_CH2 = cdf['T_RWI_CH2'][...]
    data.T_HF_FPGA = cdf['T_HF_FPGA'][...]

    # Header
    data.N_samp = cdf['N_samp'][...]            # not used
    data.N_step = cdf['N_step'][...]            # not used  [same with ‘N_step_AUX’]
    data.decimation = cdf['decimation'][...]    #           [same with ‘decimation_AUX’]
    data.pol = cdf['pol'][...]                  #           [same with ‘pol_AUX’]	

    # CUT & Reshape
    data.n_time = data.auto_corr.shape[0]
    n_num = data.N_block[0] * data.N_samp_AUX[0]
    if n_num < data.auto_corr.shape[1]:
        # print(" org:", data.auto_corr.shape, data.N_block[0], data.N_samp_AUX[0])
        data.auto_corr = data.auto_corr[:, 0:n_num]
        # data.time = data.time[:, 0:n_num]
    
    # print(" cut:", data.auto_corr.shape, data.N_block[0], data.N_samp_AUX[0])
    data.auto_corr = np.array(data.auto_corr).reshape(data.n_time, data.N_block[0], data.N_samp_AUX[0])
    # data.time = np.array(data.time).reshape(data.n_time, data.N_block[0], data.N_samp_AUX[0])
    print("sort:", data.auto_corr.shape, data.N_block[0], data.N_samp_AUX[0])

    # Time
    data.time = np.arange(0, data.N_samp_AUX[0], 1) / data.N_samp_AUX[0] / juice_cdf._sample_rate(data.decimation_AUX[0]) * 2048

    return data