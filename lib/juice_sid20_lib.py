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
def juice_getdata_hf_sid20(cdf):

    data = struct()

    data.EuEu = cdf['EuEu'][...]
    data.EvEv = cdf['EvEv'][...]
    data.EwEw = cdf['EwEw'][...]
    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]

    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]
    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]
    data.B0_step = cdf['B0_step'][...]

    # Data mode
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    print("U:", data.U_selected)
    print("V:", data.V_selected)
    print("W:", data.W_selected)

    # CUT -- Ver.1
    n_num = data.B0_step[0]
    if n_num == 255:
        data.EuEu = data.EuEu[:, 0:n_num] 
        data.EvEv = data.EvEv[:, 0:n_num] 
        data.EwEw = data.EwEw[:, 0:n_num] 
        data.frequency = data.frequency[:, 0:n_num] 
        data.freq_step = data.freq_step[:, 0:n_num] 
        data.freq_width = data.freq_width[:, 0:n_num]     

    print("data.EuEu", data.EuEu)
    return data