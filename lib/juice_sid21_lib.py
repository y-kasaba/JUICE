"""
    JUICE RPWI HF SID21 (PSSR1 rich): L1a QL -- 2023/11/16
"""
import juice_math_lib as juice_math


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID21 ------------------------------------------------------------
# ---------------------------------------------------------------------
def juice_getdata_hf_sid21(cdf, cf):
    """
    input:  CDF, cf:conversion factor
    return: data
    """
    data = struct()

    # AUX
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    data.complex = cdf['complex'][...]
    #
    data.cal_signal = cdf['cal_signal'][...]
    data.sweep_table = cdf['sweep_table'][...]    # (fixed: not defined in V.2)
    data.onboard_cal = cdf['onboard_cal'][...]    # (not used)
    data.BG_subtract = cdf['BG_subtract'][...]
    data.BG_select = cdf['BG_select'][...]
    data.FFT_window = cdf['FFT_window'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    data.Pol_sep_thres = cdf['Pol_sep_thres'][...]
    data.Pol_sep_SW = cdf['Pol_sep_SW'][...]
    data.overflow_U = cdf['overflow_U'][...]      # (fixed: not defined in V.2)
    data.overflow_V = cdf['overflow_V'][...]      # (fixed: not defined in V.2)
    data.overflow_W = cdf['overflow_W'][...]      # (fixed: not defined in V.2)
    data.proc_param0 = cdf['proc_param0'][...]
    data.proc_param1 = cdf['proc_param1'][...]
    data.proc_param2 = cdf['proc_param2'][...]
    data.proc_param3 = cdf['proc_param3'][...]
    data.freq_start = cdf['freq_start'][...]      # [same with ‘B0_startf’]

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
    data.EuEu = cdf['EuEu'][...] * 10**(cf/10)
    data.EvEv = cdf['EvEv'][...] * 10**(cf/10)
    data.EwEw = cdf['EwEw'][...] * 10**(cf/10)
    if data.complex[0] > 0:    # Matrix
        data.EuEv_re = cdf['EuEv_re'][...] * 10**(cf/10)
        data.EuEv_im = cdf['EuEv_im'][...] * 10**(cf/10)
        data.EvEw_re = cdf['EvEw_re'][...] * 10**(cf/10)
        data.EvEw_im = cdf['EvEw_im'][...] * 10**(cf/10)
        data.EwEu_re = cdf['EwEu_re'][...] * 10**(cf/10)
        data.EwEu_im = cdf['EwEu_im'][...] * 10**(cf/10)
        data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv = \
            juice_math.get_stokes(data.EuEu, data.EvEv, data.EuEv_re, data.EuEv_im)
        data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw = \
            juice_math.get_stokes(data.EvEv, data.EwEw, data.EvEw_re, data.EvEw_im)
        data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu = \
            juice_math.get_stokes(data.EwEw, data.EuEu, data.EwEu_re, data.EwEu_im)
        data.E_DoPuv, data.E_DoLuv, data.E_DoCuv, data.E_ANGuv = \
            juice_math.get_pol(data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv)
        data.E_DoPvw, data.E_DoLvw, data.E_DoCvw, data.E_ANGvw = \
            juice_math.get_pol(data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw)
        data.E_DoPwu, data.E_DoLwu, data.E_DoCwu, data.E_ANGwu = \
            juice_math.get_pol(data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu)

    # CUT
    n_num = data.B0_step[0] * data.B0_subdiv[0]
    if n_num < data.EuEu.shape[1]:
        print("Cut: ", data.EuEu.shape[1], " ->", n_num)
        data.frequency = data.frequency[:, 0:n_num]
        data.freq_step = data.freq_step[:, 0:n_num]
        data.freq_width = data.freq_width[:, 0:n_num]
        #
        data.EuEu = data.EuEu[:, 0:n_num]
        data.EvEv = data.EvEv[:, 0:n_num]
        data.EwEw = data.EwEw[:, 0:n_num]
        #
        if data.complex[0] > 0:    # Matrix
            data.EuEv_re = data.EuEv_re[:, 0:n_num]
            data.EuEv_im = data.EuEv_im[:, 0:n_num]
            data.EvEw_re = data.EvEw_re[:, 0:n_num]
            data.EvEw_im = data.EvEw_im[:, 0:n_num]
            data.EwEu_re = data.EwEu_re[:, 0:n_num]
            data.EwEu_im = data.EwEu_im[:, 0:n_num]
            #
            data.E_Iuv = data.E_Iuv[:, 0:n_num]
            data.E_Quv = data.E_Quv[:, 0:n_num]
            data.E_Uuv = data.E_Uuv[:, 0:n_num]
            data.E_Vuv = data.E_Vuv[:, 0:n_num]
            data.E_Ivw = data.E_Ivw[:, 0:n_num]
            data.E_Qvw = data.E_Qvw[:, 0:n_num]
            data.E_Uvw = data.E_Uvw[:, 0:n_num]
            data.E_Vvw = data.E_Vvw[:, 0:n_num]
            data.E_Iwu = data.E_Iwu[:, 0:n_num]
            data.E_Qwu = data.E_Qwu[:, 0:n_num]
            data.E_Uwu = data.E_Uwu[:, 0:n_num]
            data.E_Vwu = data.E_Vwu[:, 0:n_num]
            data.E_DoPuv = data.E_DoPuv[:, 0:n_num]
            data.E_DoLuv = data.E_DoLuv[:, 0:n_num]
            data.E_DoCuv = data.E_DoCuv[:, 0:n_num]
            data.E_ANGuv = data.E_ANGuv[:, 0:n_num]
            data.E_DoPvw = data.E_DoPvw[:, 0:n_num]
            data.E_DoLvw = data.E_DoLvw[:, 0:n_num]
            data.E_DoCvw = data.E_DoCvw[:, 0:n_num]
            data.E_ANGvw = data.E_ANGvw[:, 0:n_num]
            data.E_DoPwu = data.E_DoPwu[:, 0:n_num]
            data.E_DoLwu = data.E_DoLwu[:, 0:n_num]
            data.E_DoCwu = data.E_DoCwu[:, 0:n_num]
            data.E_ANGwu = data.E_ANGwu[:, 0:n_num]
    return data
