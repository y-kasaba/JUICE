"""
    JUICE RPWI HF SID5 (PSSR1 surv): L1a QL -- 2023/11/15
"""
import numpy as np


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID21 ------------------------------------------------------------
# ---------------------------------------------------------------------
def juice_getdata_hf_sid5(cdf, cf):
    """
    Input:  cdf
    Output: data
    """
    data = struct()

    # AUX
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    #
    data.cal_signal = cdf['cal_signal'][...]
    data.sweep_table = cdf['sweep_table'][...]      # (fixed: not defined in V.2)
    data.FFT_window = cdf['FFT_window'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    data.N_freq = cdf['N_freq'][...]
    data.freq_start = cdf['freq_start'][...]        # [same with ‘B0_startf’]
    data.freq_stop = cdf['freq_stop'][...]          # [same with ‘B0_stopf’]
    data.subdiv_reduction = cdf['subdiv_reduction'][...]
    #
    data.T_RWI_CH1 = cdf['T_RWI_CH1'][...]
    data.T_RWI_CH2 = cdf['T_RWI_CH2'][...]
    data.T_HF_FPGA = cdf['T_HF_FPGA'][...]

    # Header
    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]
    data.pol = cdf['pol'][...]
    data.B0_startf = cdf['B0_startf'][...]
    data.B0_stopf = cdf['B0_stopf'][...]
    data.B0_step = cdf['B0_step'][...]
    data.B0_repeat = cdf['B0_repeat'][...]
    data.B0_subdiv = cdf['B0_subdiv'][...]

    # Data
    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]
    #
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]
    #
    data.EE = cdf['EE'][...] * 10**(cf/10)

    # CUT
    n_num = np.int16(data.B0_step[0] * data.B0_subdiv[0] / data.subdiv_reduction[0])
    print(data.B0_step[0], data.B0_subdiv[0], data.subdiv_reduction[0])
    if n_num < data.EE.shape[1]:
        print("Cut: ", data.EE.shape[1], " ->", n_num)
        data.EE = data.EE[:, 0:n_num]
        data.frequency = data.frequency[:, 0:n_num]
        data.freq_step = data.freq_step[:, 0:n_num]
        data.freq_width = data.freq_width[:, 0:n_num]

    return data
