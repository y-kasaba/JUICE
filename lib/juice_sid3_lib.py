"""
    JUICE RPWI HF SID3 (Full): L1a QL -- 2023/11/19
"""
import juice_math_lib as juice_math


class struct:
    pass


# ---------------------------------------------------------------------
# --- HID3 ------------------------------------------------------------
# ---------------------------------------------------------------------
def juice_getdata_hf_sid3(cdf, cf):
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
    data.B1_startf = cdf['B0_startf'][...]
    data.B1_stopf = cdf['B0_stopf'][...]
    data.B1_step = cdf['B0_step'][...]
    data.B1_repeat = cdf['B0_repeat'][...]
    data.B1_subdiv = cdf['B0_subdiv'][...]
    data.B2_startf = cdf['B0_startf'][...]
    data.B2_stopf = cdf['B0_stopf'][...]
    data.B2_step = cdf['B0_step'][...]
    data.B2_repeat = cdf['B0_repeat'][...]
    data.B2_subdiv = cdf['B0_subdiv'][...]
    data.B3_startf = cdf['B0_startf'][...]
    data.B3_stopf = cdf['B0_stopf'][...]
    data.B3_step = cdf['B0_step'][...]
    data.B3_repeat = cdf['B0_repeat'][...]
    data.B3_subdiv = cdf['B0_subdiv'][...]
    data.B4_startf = cdf['B0_startf'][...]
    data.B4_stopf = cdf['B0_stopf'][...]
    data.B4_step = cdf['B0_step'][...]
    data.B4_repeat = cdf['B0_repeat'][...]
    data.B4_subdiv = cdf['B0_subdiv'][...]

    # Data
    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]
    #
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]

    if data.complex[0] < 2:     # Power
        data.EuEu = cdf['EuEu'][...] * 10**(cf/10)
        data.EvEv = cdf['EvEv'][...] * 10**(cf/10)
        data.EwEw = cdf['EwEw'][...] * 10**(cf/10)
    #
    if data.complex[0] == 1:    # Matrix
        data.EuEv_re = cdf['EuEv_re'][...] * 10**(cf/10)
        data.EvEw_re = cdf['EvEw_re'][...] * 10**(cf/10)
        data.EwEu_re = cdf['EwEu_re'][...] * 10**(cf/10)
        data.EuEv_im = cdf['EuEv_im'][...] * 10**(cf/10)
        data.EvEw_im = cdf['EvEw_im'][...] * 10**(cf/10)
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
    if data.complex[0] == 2:    # Matrix - N/R/L-separated
        data.EuEu = data.EuEu_NC = cdf['EuEu_NC'][...] * 10**(cf/10)
        data.EvEv = data.EvEv_NC = cdf['EvEv_NC'][...] * 10**(cf/10)
        data.EwEw = data.EwEw_NC = cdf['EwEw_NC'][...] * 10**(cf/10)
        data.EuEv_re = data.EuEv_re_NC = cdf['EuEv_re_NC'][...] * 10**(cf/10)
        data.EvEw_re = data.EvEw_re_NC = cdf['EvEw_re_NC'][...] * 10**(cf/10)
        data.EwEu_re = data.EwEu_re_NC = cdf['EwEu_re_NC'][...] * 10**(cf/10)
        data.EuEv_im = data.EuEv_im_NC = cdf['EuEv_im_NC'][...] * 10**(cf/10)
        data.EvEw_im = data.EvEw_im_NC = cdf['EvEw_im_NC'][...] * 10**(cf/10)
        data.EwEu_im = data.EwEu_im_NC = cdf['EwEu_im_NC'][...] * 10**(cf/10)
        data.E_Iuv_NC, data.E_Quv_NC, data.E_Uuv_NC, data.E_Vuv_NC = \
            juice_math.get_stokes(data.EuEu_NC, data.EvEv_NC, data.EuEv_re_NC, data.EuEv_im_NC)
        data.E_Ivw_NC, data.E_Qvw_NC, data.E_Uvw_NC, data.E_Vvw_NC = \
            juice_math.get_stokes(data.EvEv_NC, data.EwEw_NC, data.EvEw_re_NC, data.EvEw_im_NC)
        data.E_Iwu_NC, data.E_Qwu_NC, data.E_Uwu_NC, data.E_Vwu_NC = \
            juice_math.get_stokes(data.EwEw_NC, data.EuEu_NC, data.EwEu_re_NC, data.EwEu_im_NC)
        data.E_DoPuv_NC, data.E_DoLuv_NC, data.E_DoCuv_NC, data.E_ANGuv_NC = \
            juice_math.get_pol(data.E_Iuv_NC, data.E_Quv_NC, data.E_Uuv_NC, data.E_Vuv_NC)
        data.E_DoPvw_NC, data.E_DoLvw_NC, data.E_DoCvw_NC, data.E_ANGvw_NC = \
            juice_math.get_pol(data.E_Ivw_NC, data.E_Qvw_NC, data.E_Uvw_NC, data.E_Vvw_NC)
        data.E_DoPwu_NC, data.E_DoLwu_NC, data.E_DoCwu_NC, data.E_ANGwu_NC = juice_math.get_pol(
            data.E_Iwu_NC, data.E_Qwu_NC, data.E_Uwu_NC, data.E_Vwu_NC)
        data.E_Iuv = data.E_Iuv_NC
        data.E_Quv = data.E_Quv_NC
        data.E_Uuv = data.E_Uuv_NC
        data.E_Vuv = data.E_Vuv_NC
        data.E_DoPuv = data.E_DoPuv_NC
        data.E_DoLuv = data.E_DoLuv_NC
        data.E_DoCuv = data.E_DoCuv_NC
        data.E_ANGuv = data.E_ANGuv_NC
        data.E_Ivw = data.E_Ivw_NC
        data.E_Qvw = data.E_Qvw_NC
        data.E_Uvw = data.E_Uvw_NC
        data.E_Vvw = data.E_Vvw_NC
        data.E_DoPvw = data.E_DoPvw_NC
        data.E_DoLvw = data.E_DoLvw_NC
        data.E_DoCvw = data.E_DoCvw_NC
        data.E_ANGvw = data.E_ANGvw_NC
        data.E_Iwu = data.E_Iwu_NC
        data.E_Qwu = data.E_Qwu_NC
        data.E_Uwu = data.E_Uwu_NC
        data.E_Vwu = data.E_Vwu_NC
        data.E_DoPwu = data.E_DoPwu_NC
        data.E_DoLwu = data.E_DoLwu_NC
        data.E_DoCwu = data.E_DoCwu_NC
        data.E_ANGwu = data.E_ANGwu_NC
        #
        data.EuEu_RC = cdf['EuEu_RC'][...] * 10**(cf/10)
        data.EvEv_RC = cdf['EvEv_RC'][...] * 10**(cf/10)
        data.EwEw_RC = cdf['EwEw_RC'][...] * 10**(cf/10)
        data.EuEv_re_RC = cdf['EuEv_re_RC'][...] * 10**(cf/10)
        data.EvEw_re_RC = cdf['EvEw_re_RC'][...] * 10**(cf/10)
        data.EwEu_re_RC = cdf['EwEu_re_RC'][...] * 10**(cf/10)
        data.EuEv_im_RC = cdf['EuEv_im_RC'][...] * 10**(cf/10)
        data.EvEw_im_RC = cdf['EvEw_im_RC'][...] * 10**(cf/10)
        data.EwEu_im_RC = cdf['EwEu_im_RC'][...] * 10**(cf/10)
        data.E_Iuv_RC, data.E_Quv_RC, data.E_Uuv_RC, data.E_Vuv_RC = \
            juice_math.get_stokes(data.EuEu_RC, data.EvEv_RC, data.EuEv_re_RC, data.EuEv_im_RC)
        data.E_Ivw_RC, data.E_Qvw_RC, data.E_Uvw_RC, data.E_Vvw_RC = \
            juice_math.get_stokes(data.EvEv_RC, data.EwEw_RC, data.EvEw_re_RC, data.EvEw_im_RC)
        data.E_Iwu_RC, data.E_Qwu_RC, data.E_Uwu_RC, data.E_Vwu_RC = \
            juice_math.get_stokes(data.EwEw_RC, data.EuEu_RC, data.EwEu_re_RC, data.EwEu_im_RC)
        data.E_DoPuv_RC, data.E_DoLuv_RC, data.E_DoCuv_RC, data.E_ANGuv_RC = \
            juice_math.get_pol(data.E_Iuv_RC, data.E_Quv_RC, data.E_Uuv_RC, data.E_Vuv_RC)
        data.E_DoPvw_RC, data.E_DoLvw_RC, data.E_DoCvw_RC, data.E_ANGvw_RC = \
            juice_math.get_pol(data.E_Ivw_RC, data.E_Qvw_RC, data.E_Uvw_RC, data.E_Vvw_RC)
        data.E_DoPwu_RC, data.E_DoLwu_RC, data.E_DoCwu_RC, data.E_ANGwu_RC = \
            juice_math.get_pol(data.E_Iwu_RC, data.E_Qwu_RC, data.E_Uwu_RC, data.E_Vwu_RC)
        #
        data.EuEu_LC = cdf['EuEu_LC'][...] * 10**(cf/10)
        data.EvEv_LC = cdf['EvEv_LC'][...] * 10**(cf/10)
        data.EwEw_LC = cdf['EwEw_LC'][...] * 10**(cf/10)
        data.EuEv_re_LC = cdf['EuEv_re_LC'][...] * 10**(cf/10)
        data.EvEw_re_LC = cdf['EvEw_re_LC'][...] * 10**(cf/10)
        data.EwEu_re_LC = cdf['EwEu_re_LC'][...] * 10**(cf/10)
        data.EuEv_im_LC = cdf['EuEv_im_LC'][...] * 10**(cf/10)
        data.EvEw_im_LC = cdf['EvEw_im_LC'][...] * 10**(cf/10)
        data.EwEu_im_LC = cdf['EwEu_im_LC'][...] * 10**(cf/10)
        data.E_Iuv_LC, data.E_Quv_LC, data.E_Uuv_LC, data.E_Vuv_LC = \
            juice_math.get_stokes(data.EuEu_LC, data.EvEv_LC, data.EuEv_re_LC, data.EuEv_im_LC)
        data.E_Ivw_LC, data.E_Qvw_LC, data.E_Uvw_LC, data.E_Vvw_LC = \
            juice_math.get_stokes(data.EvEv_LC, data.EwEw_LC, data.EvEw_re_LC, data.EvEw_im_LC)
        data.E_Iwu_LC, data.E_Qwu_LC, data.E_Uwu_LC, data.E_Vwu_LC = \
            juice_math.get_stokes(data.EwEw_LC, data.EuEu_LC, data.EwEu_re_LC, data.EwEu_im_LC)
        data.E_DoPuv_LC, data.E_DoLuv_LC, data.E_DoCuv_LC, data.E_ANGuv_LC = \
            juice_math.get_pol(data.E_Iuv_LC, data.E_Quv_LC, data.E_Uuv_LC, data.E_Vuv_LC)
        data.E_DoPvw_LC, data.E_DoLvw_LC, data.E_DoCvw_LC, data.E_ANGvw_LC = \
            juice_math.get_pol(data.E_Ivw_LC, data.E_Qvw_LC, data.E_Uvw_LC, data.E_Vvw_LC)
        data.E_DoPwu_LC, data.E_DoLwu_LC, data.E_DoCwu_LC, data.E_ANGwu_LC = \
            juice_math.get_pol(data.E_Iwu_LC, data.E_Qwu_LC, data.E_Uwu_LC, data.E_Vwu_LC)

        data.num_NC = cdf['num_NC'][...]
        data.num_RC = cdf['num_RC'][...]
        data.num_LC = cdf['num_LC'][...]
    #
    if data.complex[0] == 3:    # 3D-matrix
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
        data.EuqEvq = cdf['EuqEvq'][...] * 10**(cf/10)
        data.EvqEwq = cdf['EvqEwq'][...] * 10**(cf/10)
        data.EwqEuq = cdf['EwqEuq'][...] * 10**(cf/10)
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
        data.EuEv_im = -data.EuiEvq + data.EuqEvi
        data.EvEw_im = -data.EviEwq + data.EviEvq
        data.EwEu_im = -data.EwiEuq + data.EwqEui
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
    #
    data.BG_Eu = cdf['BG_Eu'][...] * 10**(cf/10)
    data.BG_Ev = cdf['BG_Ev'][...] * 10**(cf/10)
    data.BG_Ew = cdf['BG_Ew'][...] * 10**(cf/10)

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
    elif n_num == 256:
        print("Mode: Ver.2")
    else:
        print("Mode: **** error ****")
        
    return data
