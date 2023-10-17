# import glob
# import spacepy.pycdf
import numpy as np

class struct:
    pass

"""
import numpy as np
import statistics

import juice_cdf_lib as juice_cdf
import juice_math_lib as juice_math
"""

#---------------------------------------------------------------------
#--- HID3 ------------------------------------------------------------
#---------------------------------------------------------------------
def juice_getdata_hf_sid03(cdf):

    data = struct()

    # Data
    data.EuEu = cdf['EuEu'][...]
    data.EvEv = cdf['EvEv'][...]
    data.EwEw = cdf['EwEw'][...]
    data.EwEu_re = cdf['EwEu_re'][...]
    data.EwEu_im = cdf['EwEu_im'][...]
    data.EvEw_re = cdf['EvEw_re'][...]
    data.EvEw_im = cdf['EvEw_im'][...]
    data.EuEv_re = cdf['EuEv_re'][...]
    data.EuEv_im = cdf['EuEv_im'][...]
    #
    data.EuEu_RH = cdf['EuEu_RH'][...]
    data.EvEv_RH = cdf['EvEv_RH'][...]
    data.EwEw_RH = cdf['EwEw_RH'][...]
    data.EwEu_re_RH = cdf['EwEu_re_RH'][...]
    data.EwEu_im_RH = cdf['EwEu_im_RH'][...]
    data.EvEw_re_RH = cdf['EvEw_re_RH'][...]
    data.EvEw_im_RH = cdf['EvEw_im_RH'][...]
    data.EuEv_re_RH = cdf['EuEv_re_RH'][...]
    data.EuEv_im_RH = cdf['EuEv_im_RH'][...]
    #
    data.EuEu_LH = cdf['EuEu_LH'][...]
    data.EvEv_LH = cdf['EvEv_LH'][...]
    data.EwEw_LH = cdf['EwEw_LH'][...]
    data.EwEu_re_LH = cdf['EwEu_re_LH'][...]
    data.EwEu_im_LH = cdf['EwEu_im_LH'][...]
    data.EvEw_re_LH = cdf['EvEw_re_LH'][...]
    data.EvEw_im_LH = cdf['EvEw_im_LH'][...]
    data.EuEv_re_LH = cdf['EuEv_re_LH'][...]
    data.EuEv_im_LH = cdf['EuEv_im_LH'][...]
    #
    data.EuiEui = cdf['EuiEui'][...]
    data.EuqEuq = cdf['EuqEuq'][...]
    data.EwiEwi = cdf['EwiEwi'][...]
    data.EwqEwq = cdf['EwqEwq'][...]
    data.EviEvi = cdf['EviEvi'][...]
    data.EvqEvq = cdf['EvqEvq'][...]
    data.EwiEui = cdf['EwiEui'][...]
    data.EviEwi = cdf['EviEwi'][...]
    data.EuiEvi = cdf['EuiEvi'][...]
    data.EwqEuq = cdf['EwqEuq'][...]
    data.EvqEwq = cdf['EvqEwq'][...]
    data.EuqEvq = cdf['EuqEvq'][...]
    data.EwiEuq = cdf['EwiEuq'][...]
    data.EwqEui = cdf['EwqEui'][...]
    data.EviEwq = cdf['EviEwq'][...]
    data.EvqEwi = cdf['EvqEwi'][...]
    data.EuiEvq = cdf['EuiEvq'][...]
    data.EuqEvi = cdf['EuqEvi'][...]
    data.EuiEuq = cdf['EuiEuq'][...]
    data.EwiEwq = cdf['EwiEwq'][...]
    data.EviEvq = cdf['EviEvq'][...]
    #
    data.BG_Eu = cdf['BG_Eu'][...]
    data.BG_Ev = cdf['BG_Ev'][...]
    data.BG_Ew = cdf['BG_Ew'][...]
    data.BG_Eu_num = cdf['BG_Eu_num'][...]
    data.BG_Ev_num = cdf['BG_Ev_num'][...]
    data.BG_Ew_num = cdf['BG_Ew_num'][...]

    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]

    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]
    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]
    data.B0_step = cdf['B0_step'][...]

    # AUX & Header
    data.T_RWI_U = cdf['T_RWI_U'][...]
    data.T_RWI_W = cdf['T_RWI_W'][...]
    data.T_HF_FPGA = cdf['T_HF_FPGA'][...]

    # Data mode
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    data.complex = cdf['complex'][...]
    data.BG_downlink = cdf['BG_downlink'][...]
    #
    # data.N_component = cdf['N_component'][...]

    # CUT -- Ver.1
    n_num = data.B0_step[0]
    if n_num == 255:
        data.EuEu = data.EuEu[:, 0:n_num]
        data.EvEv = data.EvEv[:, 0:n_num]
        data.EwEw = data.EwEw[:, 0:n_num]
        data.frequency = data.frequency[:, 0:n_num]
        data.freq_step = data.freq_step[:, 0:n_num]
        data.freq_width = data.freq_width[:, 0:n_num]
        print("Mode: Ver.1")
    else:
        print("Mode: Ver.2")

    return data