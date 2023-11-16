"""
    JUICE RPWI HF SID4 (Burst surv): L1a QL -- 2023/11/13
"""
import juice_math_lib as juice_math


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID20 ------------------------------------------------------------
# ---------------------------------------------------------------------
def juice_getdata_hf_sid4(cdf, cf):
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
    data.sweep_table = cdf['sweep_table'][...]   # (fixed: not defined in V.2)
    data.onboard_cal = cdf['onboard_cal'][...]   # (not used)
    data.BG_subtract = cdf['BG_subtract'][...]
    data.BG_select = cdf['BG_select'][...]
    data.FFT_window = cdf['FFT_window'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    data.Pol_sep_thres = cdf['Pol_sep_thres'][...]
    data.Pol_sep_SW = cdf['Pol_sep_SW'][...]
    data.overflow_U = cdf['overflow_U'][...]     # (fixed: not defined in V.2)
    data.overflow_V = cdf['overflow_V'][...]     # (fixed: not defined in V.2)
    data.overflow_W = cdf['overflow_W'][...]     # (fixed: not defined in V.2)
    data.proc_param0 = cdf['proc_param0'][...]
    data.proc_param1 = cdf['proc_param1'][...]
    data.proc_param2 = cdf['proc_param2'][...]
    data.proc_param3 = cdf['proc_param3'][...]
    data.BG_downlink = cdf['BG_downlink'][...]
    data.N_block = cdf['N_block'][...]
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
    data.EuEu = cdf['EuEu'][...] * 10**(cf/10)
    data.EvEv = cdf['EvEv'][...] * 10**(cf/10)
    data.EwEw = cdf['EwEw'][...] * 10**(cf/10)
    if data.complex[0] == 1:    # Matrix
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
    #
    if data.complex[0] == 2:    # 3D-matrix
        data.EuiEui = cdf['EuiEui'][...] * 10**(cf/10)
        data.EuqEuq = cdf['EuqEuq'][...] * 10**(cf/10)
        data.EviEvi = cdf['EviEvi'][...] * 10**(cf/10)
        data.EvqEvq = cdf['EvqEvq'][...] * 10**(cf/10)
        data.EwiEwi = cdf['EwiEwi'][...] * 10**(cf/10)
        data.EwqEwq = cdf['EwqEwq'][...] * 10**(cf/10)
        #
        data.EuiEvi = cdf['EuiEvi'][...] * 10**(cf/10)
        data.EviEwi = cdf['EviEwi'][...] * 10**(cf/10)
        data.EwiEui = cdf['EwiEui'][...] * 10**(cf/10)
        data.EuqEvq = cdf['EuiEvq'][...] * 10**(cf/10)
        data.EvqEwq = cdf['EviEwq'][...] * 10**(cf/10)
        data.EwqEuq = cdf['EwiEuq'][...] * 10**(cf/10)
        #
        data.EuiEvq = cdf['EuiEvq'][...] * 10**(cf/10)
        data.EuqEvi = cdf['EuqEvi'][...] * 10**(cf/10)
        data.EviEwq = cdf['EviEwq'][...] * 10**(cf/10)
        data.EvqEwi = cdf['EvqEwi'][...] * 10**(cf/10)
        data.EwiEuq = cdf['EwiEuq'][...] * 10**(cf/10)
        data.EwqEui = cdf['EwqEui'][...] * 10**(cf/10)
        #
        data.EuiEuq = cdf['EuiEuq'][...] * 10**(cf/10)
        data.EviEvq = cdf['EviEvq'][...] * 10**(cf/10)
        data.EwiEwq = cdf['EwiEwq'][...] * 10**(cf/10)
        #
        data.EuEu = data.EuiEui + data.EuqEuq
        data.EvEv = data.EviEvi + data.EvqEvq
        data.EwEw = data.EwiEwi + data.EwqEwq
        data.EuEv_re = data.EuiEvi + data.EuqEvq
        data.EvEw_re = data.EviEwi + data.EvqEwq
        data.EwEu_re = data.EwiEui + data.EwqEuq
        data.EuEv_im = -data.EuiEvq + data.EuqEvi     # why?
        data.EvEw_im = -data.EviEwq + data.EviEvq     # why?
        data.EwEu_im = -data.EwiEuq + data.EwqEui     # why?
        #
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
        #
        data.E_I_3d = data.EuEu + data.EvEv + data.EwEw
        data.E_Q_3d = data.EuiEvi - data.EuqEuq + data.EviEvi - data.EvqEvq + data.EwiEwi - data.EwqEwq
        data.E_U_3d = 2. * (data.EuiEuq + data.EviEvq + data.EwiEwq)
        data.E_Vu_3d = -2. * (data.EviEwq - data.EvqEwi)
        data.E_Vv_3d = -2. * (data.EwiEuq - data.EwqEui)
        data.E_Vw_3d = -2. * (data.EuiEvq - data.EuqEvi)
        data.E_DoP_3d, data.E_DoL_3d, data.E_DoC_3d, data.E_ANG_3d, data.E_k_lon, data.E_k_lat = \
            juice_math.get_pol_3D(data.E_I_3d, data.E_Q_3d, data.E_U_3d, data.E_Vu_3d, data.E_Vv_3d, data.E_Vw_3d)

    return data
