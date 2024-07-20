"""
    JUICE RPWI HF SID3 (Full): L1a QL -- 2023/12/17
"""
import numpy as np
import juice_math_lib as juice_math


class struct:
    pass


# ---------------------------------------------------------------------
# --- HID3 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid3_read(cdf):
    """
    input:  CDF
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
    data.B1_startf = cdf['B1_startf'][...]
    data.B1_stopf = cdf['B1_stopf'][...]
    data.B1_step = cdf['B1_step'][...]
    data.B1_repeat = cdf['B1_repeat'][...]
    data.B1_subdiv = cdf['B1_subdiv'][...]
    data.B2_startf = cdf['B2_startf'][...]
    data.B2_stopf = cdf['B2_stopf'][...]
    data.B2_step = cdf['B2_step'][...]
    data.B2_repeat = cdf['B2_repeat'][...]
    data.B2_subdiv = cdf['B2_subdiv'][...]
    data.B3_startf = cdf['B3_startf'][...]
    data.B3_stopf = cdf['B3_stopf'][...]
    data.B3_step = cdf['B3_step'][...]
    data.B3_repeat = cdf['B3_repeat'][...]
    data.B3_subdiv = cdf['B3_subdiv'][...]
    data.B4_startf = cdf['B4_startf'][...]
    data.B4_stopf = cdf['B4_stopf'][...]
    data.B4_step = cdf['B4_step'][...]
    data.B4_repeat = cdf['B4_repeat'][...]
    data.B4_subdiv = cdf['B4_subdiv'][...]

    # Data
    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]
    #
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]

    if data.complex[0] < 2:     # Power
        data.EuEu = cdf['EuEu'][...]
        data.EvEv = cdf['EvEv'][...]
        data.EwEw = cdf['EwEw'][...]
    #
    if data.complex[0] == 1:    # Matrix
        data.EuEv_re = cdf['EuEv_re'][...]
        data.EvEw_re = cdf['EvEw_re'][...]
        data.EwEu_re = cdf['EwEu_re'][...]
        data.EuEv_im = cdf['EuEv_im'][...]
        data.EvEw_im = cdf['EvEw_im'][...]
        data.EwEu_im = cdf['EwEu_im'][...]

        data.E_Iuv,   data.E_Quv,   data.E_Uuv,   data.E_Vuv   = juice_math.get_stokes(data.EuEu, data.EvEv, data.EuEv_re, data.EuEv_im)
        data.E_Ivw,   data.E_Qvw,   data.E_Uvw,   data.E_Vvw   = juice_math.get_stokes(data.EvEv, data.EwEw, data.EvEw_re, data.EvEw_im)
        data.E_Iwu,   data.E_Qwu,   data.E_Uwu,   data.E_Vwu   = juice_math.get_stokes(data.EwEw, data.EuEu, data.EwEu_re, data.EwEu_im)
        data.E_DoPuv, data.E_DoLuv, data.E_DoCuv, data.E_ANGuv = juice_math.get_pol(data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv)
        data.E_DoPvw, data.E_DoLvw, data.E_DoCvw, data.E_ANGvw = juice_math.get_pol(data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw)
        data.E_DoPwu, data.E_DoLwu, data.E_DoCwu, data.E_ANGwu = juice_math.get_pol(data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu)
    #
    if data.complex[0] == 2:    # Matrix - N/R/L-separated
        # *** NC
        data.EuEu_NC = cdf['EuEu_NC'][...]
        data.EvEv_NC = cdf['EvEv_NC'][...]
        data.EwEw_NC = cdf['EwEw_NC'][...]
        data.EuEv_re_NC = cdf['EuEv_re_NC'][...]
        data.EvEw_re_NC = cdf['EvEw_re_NC'][...]
        data.EwEu_re_NC = cdf['EwEu_re_NC'][...]
        data.EuEv_im_NC = cdf['EuEv_im_NC'][...]
        data.EvEw_im_NC = cdf['EvEw_im_NC'][...]
        data.EwEu_im_NC = cdf['EwEu_im_NC'][...]
        data.E_Iuv_NC,   data.E_Quv_NC,   data.E_Uuv_NC,   data.E_Vuv_NC   = juice_math.get_stokes(data.EuEu_NC, data.EvEv_NC, data.EuEv_re_NC, data.EuEv_im_NC)
        data.E_Ivw_NC,   data.E_Qvw_NC,   data.E_Uvw_NC,   data.E_Vvw_NC   = juice_math.get_stokes(data.EvEv_NC, data.EwEw_NC, data.EvEw_re_NC, data.EvEw_im_NC)
        data.E_Iwu_NC,   data.E_Qwu_NC,   data.E_Uwu_NC,   data.E_Vwu_NC   = juice_math.get_stokes(data.EwEw_NC, data.EuEu_NC, data.EwEu_re_NC, data.EwEu_im_NC)
        data.E_DoPuv_NC, data.E_DoLuv_NC, data.E_DoCuv_NC, data.E_ANGuv_NC = juice_math.get_pol(data.E_Iuv_NC, data.E_Quv_NC, data.E_Uuv_NC, data.E_Vuv_NC)
        data.E_DoPvw_NC, data.E_DoLvw_NC, data.E_DoCvw_NC, data.E_ANGvw_NC = juice_math.get_pol(data.E_Ivw_NC, data.E_Qvw_NC, data.E_Uvw_NC, data.E_Vvw_NC)
        data.E_DoPwu_NC, data.E_DoLwu_NC, data.E_DoCwu_NC, data.E_ANGwu_NC = juice_math.get_pol(data.E_Iwu_NC, data.E_Qwu_NC, data.E_Uwu_NC, data.E_Vwu_NC)

        # *** RC
        data.EuEu_RC = cdf['EuEu_RC'][...]
        data.EvEv_RC = cdf['EvEv_RC'][...]
        data.EwEw_RC = cdf['EwEw_RC'][...]
        data.EuEv_re_RC = cdf['EuEv_re_RC'][...]
        data.EvEw_re_RC = cdf['EvEw_re_RC'][...]
        data.EwEu_re_RC = cdf['EwEu_re_RC'][...]
        data.EuEv_im_RC = cdf['EuEv_im_RC'][...]
        data.EvEw_im_RC = cdf['EvEw_im_RC'][...]
        data.EwEu_im_RC = cdf['EwEu_im_RC'][...]
        data.E_Iuv_RC,   data.E_Quv_RC,   data.E_Uuv_RC,   data.E_Vuv_RC   = juice_math.get_stokes(data.EuEu_RC, data.EvEv_RC, data.EuEv_re_RC, data.EuEv_im_RC)
        data.E_Ivw_RC,   data.E_Qvw_RC,   data.E_Uvw_RC,   data.E_Vvw_RC   = juice_math.get_stokes(data.EvEv_RC, data.EwEw_RC, data.EvEw_re_RC, data.EvEw_im_RC)
        data.E_Iwu_RC,   data.E_Qwu_RC,   data.E_Uwu_RC,   data.E_Vwu_RC   = juice_math.get_stokes(data.EwEw_RC, data.EuEu_RC, data.EwEu_re_RC, data.EwEu_im_RC)
        data.E_DoPuv_RC, data.E_DoLuv_RC, data.E_DoCuv_RC, data.E_ANGuv_RC = juice_math.get_pol(data.E_Iuv_RC, data.E_Quv_RC, data.E_Uuv_RC, data.E_Vuv_RC)
        data.E_DoPvw_RC, data.E_DoLvw_RC, data.E_DoCvw_RC, data.E_ANGvw_RC = juice_math.get_pol(data.E_Ivw_RC, data.E_Qvw_RC, data.E_Uvw_RC, data.E_Vvw_RC)
        data.E_DoPwu_RC, data.E_DoLwu_RC, data.E_DoCwu_RC, data.E_ANGwu_RC = juice_math.get_pol(data.E_Iwu_RC, data.E_Qwu_RC, data.E_Uwu_RC, data.E_Vwu_RC)
        #
        # *** LC
        data.EuEu_LC = cdf['EuEu_LC'][...]
        data.EvEv_LC = cdf['EvEv_LC'][...]
        data.EwEw_LC = cdf['EwEw_LC'][...]
        data.EuEv_re_LC = cdf['EuEv_re_LC'][...]
        data.EvEw_re_LC = cdf['EvEw_re_LC'][...]
        data.EwEu_re_LC = cdf['EwEu_re_LC'][...]
        data.EuEv_im_LC = cdf['EuEv_im_LC'][...]
        data.EvEw_im_LC = cdf['EvEw_im_LC'][...]
        data.EwEu_im_LC = cdf['EwEu_im_LC'][...]
        data.E_Iuv_LC,   data.E_Quv_LC,   data.E_Uuv_LC,   data.E_Vuv_LC   = juice_math.get_stokes(data.EuEu_LC, data.EvEv_LC, data.EuEv_re_LC, data.EuEv_im_LC)
        data.E_Ivw_LC,   data.E_Qvw_LC,   data.E_Uvw_LC,   data.E_Vvw_LC   = juice_math.get_stokes(data.EvEv_LC, data.EwEw_LC, data.EvEw_re_LC, data.EvEw_im_LC)
        data.E_Iwu_LC,   data.E_Qwu_LC,   data.E_Uwu_LC,   data.E_Vwu_LC   = juice_math.get_stokes(data.EwEw_LC, data.EuEu_LC, data.EwEu_re_LC, data.EwEu_im_LC)
        data.E_DoPuv_LC, data.E_DoLuv_LC, data.E_DoCuv_LC, data.E_ANGuv_LC = juice_math.get_pol(data.E_Iuv_LC, data.E_Quv_LC, data.E_Uuv_LC, data.E_Vuv_LC)
        data.E_DoPvw_LC, data.E_DoLvw_LC, data.E_DoCvw_LC, data.E_ANGvw_LC = juice_math.get_pol(data.E_Ivw_LC, data.E_Qvw_LC, data.E_Uvw_LC, data.E_Vvw_LC)
        data.E_DoPwu_LC, data.E_DoLwu_LC, data.E_DoCwu_LC, data.E_ANGwu_LC = juice_math.get_pol(data.E_Iwu_LC, data.E_Qwu_LC, data.E_Uwu_LC, data.E_Vwu_LC)

        data.num_NC = cdf['num_NC'][...]
        data.num_RC = cdf['num_RC'][...]
        data.num_LC = cdf['num_LC'][...]

        # *** temporary values by NC
        # data.EuEu = data.EuEu_NC;        data.EvEv = data.EvEv_NC;        data.EwEw = data.EwEw_NC
        # data.EuEv_re = data.EuEv_re_NC;  data.EvEw_re = data.EvEw_re_NC;  data.EwEu_re = data.EwEu_re_NC
        # data.EuEv_im = data.EuEv_im_NC;  data.EvEw_im = data.EvEw_im_NC;  data.EwEu_im = data.EwEu_im_NC
        # data.E_Iuv = data.E_Iuv_NC;      data.E_Quv = data.E_Quv_NC;      data.E_Uuv = data.E_Uuv_NC;      data.E_Vuv = data.E_Vuv_NC
        # data.E_Ivw = data.E_Ivw_NC;      data.E_Qvw = data.E_Qvw_NC;      data.E_Uvw = data.E_Uvw_NC;      data.E_Vvw = data.E_Vvw_NC
        # data.E_Iwu = data.E_Iwu_NC;      data.E_Qwu = data.E_Qwu_NC;      data.E_Uwu = data.E_Uwu_NC;      data.E_Vwu = data.E_Vwu_NC
        # data.E_DoPuv = data.E_DoPuv_NC;  data.E_DoLuv = data.E_DoLuv_NC;  data.E_DoCuv = data.E_DoCuv_NC;  data.E_ANGuv = data.E_ANGuv_NC
        # data.E_DoPvw = data.E_DoPvw_NC;  data.E_DoLvw = data.E_DoLvw_NC;  data.E_DoCvw = data.E_DoCvw_NC;  data.E_ANGvw = data.E_ANGvw_NC
        # data.E_DoPwu = data.E_DoPwu_NC;  data.E_DoLwu = data.E_DoLwu_NC;  data.E_DoCwu = data.E_DoCwu_NC;  data.E_ANGwu = data.E_ANGwu_NC
        # ****TMP: Ratio adoption is needed ****
        data.EuEu = data.EuEu_NC + data.EuEu_RC + data.EuEu_LC
        data.EvEv = data.EvEv_NC + data.EvEv_RC + data.EvEv_LC
        data.EwEw = data.EwEw_NC + data.EwEw_RC + data.EwEw_LC
        data.EuEv_re = data.EuEv_re_NC + data.EuEv_re_RC + data.EuEv_re_LC
        data.EvEw_re = data.EvEw_re_NC + data.EvEw_re_RC + data.EvEw_re_LC
        data.EwEu_re = data.EwEu_re_NC + data.EwEu_re_RC + data.EwEu_re_LC
        data.EuEv_im = data.EuEv_im_NC + data.EuEv_im_RC + data.EuEv_im_LC
        data.EvEw_im = data.EvEw_im_NC + data.EvEw_im_RC + data.EvEw_im_LC
        data.EwEu_im = data.EwEu_im_NC + data.EwEu_im_RC + data.EwEu_im_LC
        data.E_Iuv,   data.E_Quv,   data.E_Uuv,   data.E_Vuv   = juice_math.get_stokes(data.EuEu, data.EvEv, data.EuEv_re, data.EuEv_im)
        data.E_Ivw,   data.E_Qvw,   data.E_Uvw,   data.E_Vvw   = juice_math.get_stokes(data.EvEv, data.EwEw, data.EvEw_re, data.EvEw_im)
        data.E_Iwu,   data.E_Qwu,   data.E_Uwu,   data.E_Vwu   = juice_math.get_stokes(data.EwEw, data.EuEu, data.EwEu_re, data.EwEu_im)
        data.E_DoPuv, data.E_DoLuv, data.E_DoCuv, data.E_ANGuv = juice_math.get_pol(data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv)
        data.E_DoPvw, data.E_DoLvw, data.E_DoCvw, data.E_ANGvw = juice_math.get_pol(data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw)
        data.E_DoPwu, data.E_DoLwu, data.E_DoCwu, data.E_ANGwu = juice_math.get_pol(data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu)
        # ****TMP****
    #
    if data.complex[0] == 3:    # 3D-matrix
        data.EuiEui = cdf['EuiEui'][...]
        data.EuqEuq = cdf['EuqEuq'][...]
        data.EviEvi = cdf['EviEvi'][...]
        data.EvqEvq = cdf['EvqEvq'][...]
        data.EwiEwi = cdf['EwiEwi'][...]
        data.EwqEwq = cdf['EwqEwq'][...]
        #
        data.EuiEvi = cdf['EuiEvi'][...]
        data.EviEwi = cdf['EviEwi'][...]
        data.EwiEui = cdf['EwiEui'][...]
        data.EuqEvq = cdf['EuqEvq'][...]
        data.EvqEwq = cdf['EvqEwq'][...]
        data.EwqEuq = cdf['EwqEuq'][...]
        #
        data.EuiEvq = cdf['EuiEvq'][...]
        data.EuqEvi = cdf['EuqEvi'][...]
        data.EviEwq = cdf['EviEwq'][...]
        data.EvqEwi = cdf['EvqEwi'][...]
        data.EwiEuq = cdf['EwiEuq'][...]
        data.EwqEui = cdf['EwqEui'][...]
        #
        data.EuiEuq = cdf['EuiEuq'][...]
        data.EviEvq = cdf['EviEvq'][...]
        data.EwiEwq = cdf['EwiEwq'][...]
        #
        data.EuEu    =  data.EuiEui + data.EuqEuq
        data.EvEv    =  data.EviEvi + data.EvqEvq
        data.EwEw    =  data.EwiEwi + data.EwqEwq
        data.EuEv_re =  data.EuiEvi + data.EuqEvq
        data.EvEw_re =  data.EviEwi + data.EvqEwq
        data.EwEu_re =  data.EwiEui + data.EwqEuq
        data.EuEv_im = -data.EuiEvq + data.EuqEvi
        data.EvEw_im = -data.EviEwq + data.EviEvq
        data.EwEu_im = -data.EwiEuq + data.EwqEui
        #
        data.E_Iuv,   data.E_Quv,   data.E_Uuv,   data.E_Vuv   = juice_math.get_stokes(data.EuEu, data.EvEv, data.EuEv_re, data.EuEv_im)
        data.E_Ivw,   data.E_Qvw,   data.E_Uvw,   data.E_Vvw   = juice_math.get_stokes(data.EvEv, data.EwEw, data.EvEw_re, data.EvEw_im)
        data.E_Iwu,   data.E_Qwu,   data.E_Uwu,   data.E_Vwu   = juice_math.get_stokes(data.EwEw, data.EuEu, data.EwEu_re, data.EwEu_im)
        data.E_DoPuv, data.E_DoLuv, data.E_DoCuv, data.E_ANGuv = juice_math.get_pol(data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv)
        data.E_DoPvw, data.E_DoLvw, data.E_DoCvw, data.E_ANGvw = juice_math.get_pol(data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw)
        data.E_DoPwu, data.E_DoLwu, data.E_DoCwu, data.E_ANGwu = juice_math.get_pol(data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu)
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
    data.BG_Eu = cdf['BG_Eu'][...]
    data.BG_Ev = cdf['BG_Ev'][...]
    data.BG_Ew = cdf['BG_Ew'][...]

    # CUT -- Ver.1
    n_num = data.B0_step[0]  # data.EuEu.shape[1]
    if n_num == 255:
        data.EuEu = data.EuEu[:, 0:n_num]
        data.EvEv = data.EvEv[:, 0:n_num]
        data.EwEw = data.EwEw[:, 0:n_num]
        data.frequency = data.frequency[:, 0:n_num]
        data.freq_step = data.freq_step[:, 0:n_num]
        data.freq_width = data.freq_width[:, 0:n_num]
        # print("Mode: Ver.1")

    return data


def hf_sid3_add(data, data1):
    """
    input:  data, data1
    return: data
    """

    # AUX
    data.U_selected = np.r_["0", data.U_selected, data1.U_selected]
    data.V_selected = np.r_["0", data.V_selected, data1.V_selected]
    data.W_selected = np.r_["0", data.W_selected, data1.W_selected]
    data.complex = np.r_["0", data.complex, data1.complex]
    #
    data.cal_signal = np.r_["0", data.cal_signal, data1.cal_signal]
    data.sweep_table = np.r_["0", data.sweep_table, data1.sweep_table]
    data.onboard_cal = np.r_["0", data.onboard_cal, data1.onboard_cal]
    data.BG_subtract = np.r_["0", data.BG_subtract, data1.BG_subtract]
    data.BG_select = np.r_["0", data.BG_select, data1.BG_select]
    data.FFT_window = np.r_["0", data.FFT_window, data1.FFT_window]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    data.Pol_sep_thres = np.r_["0", data.Pol_sep_thres, data1.Pol_sep_thres]
    data.Pol_sep_SW = np.r_["0", data.Pol_sep_SW, data1.Pol_sep_SW]
    data.overflow_U = np.r_["0", data.overflow_U, data1.overflow_U]
    data.overflow_V = np.r_["0", data.overflow_V, data1.overflow_V]
    data.overflow_W = np.r_["0", data.overflow_W, data1.overflow_W]
    data.proc_param0 = np.r_["0", data.proc_param0, data1.proc_param0]
    data.proc_param1 = np.r_["0", data.proc_param1, data1.proc_param1]
    data.proc_param2 = np.r_["0", data.proc_param2, data1.proc_param2]
    data.proc_param3 = np.r_["0", data.proc_param3, data1.proc_param3]
    data.BG_downlink = np.r_["0", data.BG_downlink, data1.BG_downlink]
    data.N_block = np.r_["0", data.N_block, data1.N_block]
    data.T_RWI_CH1 = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2 = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]

    # Header
    data.N_samp = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step = np.r_["0", data.N_step, data1.N_step]
    data.decimation = np.r_["0", data.decimation, data1.decimation]
    data.pol = np.r_["0", data.pol, data1.pol]
    data.B0_startf = np.r_["0", data.B0_startf, data1.B0_startf]
    data.B0_stopf = np.r_["0", data.B0_stopf, data1.B0_stopf]
    data.B0_step = np.r_["0", data.B0_step, data1.B0_step]
    data.B0_repeat = np.r_["0", data.B0_repeat, data1.B0_repeat]
    data.B0_subdiv = np.r_["0", data.B0_subdiv, data1.B0_subdiv]
    data.B1_startf = np.r_["0", data.B1_startf, data1.B1_startf]
    data.B1_stopf = np.r_["0", data.B1_stopf, data1.B1_stopf]
    data.B1_step = np.r_["0", data.B1_step, data1.B1_step]
    data.B1_repeat = np.r_["0", data.B1_repeat, data1.B1_repeat]
    data.B1_subdiv = np.r_["0", data.B1_subdiv, data1.B1_subdiv]
    data.B2_startf = np.r_["0", data.B2_startf, data1.B2_startf]
    data.B2_stopf = np.r_["0", data.B2_stopf, data1.B2_stopf]
    data.B2_step = np.r_["0", data.B2_step, data1.B2_step]
    data.B2_repeat = np.r_["0", data.B2_repeat, data1.B2_repeat]
    data.B2_subdiv = np.r_["0", data.B2_subdiv, data1.B2_subdiv]
    data.B3_startf = np.r_["0", data.B3_startf, data1.B3_startf]
    data.B3_stopf = np.r_["0", data.B3_stopf, data1.B3_stopf]
    data.B3_step = np.r_["0", data.B3_step, data1.B3_step]
    data.B3_repeat = np.r_["0", data.B3_repeat, data1.B3_repeat]
    data.B3_subdiv = np.r_["0", data.B3_subdiv, data1.B3_subdiv]
    data.B4_startf = np.r_["0", data.B4_startf, data1.B4_startf]
    data.B4_stopf = np.r_["0", data.B4_stopf, data1.B4_stopf]
    data.B4_step = np.r_["0", data.B4_step, data1.B4_step]
    data.B4_repeat = np.r_["0", data.B4_repeat, data1.B4_repeat]
    data.B4_subdiv = np.r_["0", data.B4_subdiv, data1.B4_subdiv]

    # Data
    data.epoch = np.r_["0", data.epoch, data1.epoch]
    data.scet = np.r_["0", data.scet, data1.scet]
    #
    data.frequency = np.r_["0", data.frequency, data1.frequency]
    data.freq_step = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width = np.r_["0", data.freq_width, data1.freq_width]
    #
    data.EuEu = np.r_["0", data.EuEu, data1.EuEu]
    data.EvEv = np.r_["0", data.EvEv, data1.EvEv]
    data.EwEw = np.r_["0", data.EwEw, data1.EwEw]
    #
    if data.complex[0] > 0:     # Power
        data.EuEv_re = np.r_["0", data.EuEv_re, data1.EuEv_re]
        data.EvEw_re = np.r_["0", data.EvEw_re, data1.EvEw_re]
        data.EwEu_re = np.r_["0", data.EwEu_re, data1.EwEu_re]
        data.EuEv_im = np.r_["0", data.EuEv_im, data1.EuEv_im]
        data.EvEw_im = np.r_["0", data.EvEw_im, data1.EvEw_im]
        data.EwEu_im = np.r_["0", data.EwEu_im, data1.EwEu_im]
        #
        data.E_Iuv = np.r_["0", data.E_Iuv, data1.E_Iuv]
        data.E_Quv = np.r_["0", data.E_Quv, data1.E_Quv]
        data.E_Uuv = np.r_["0", data.E_Uuv, data1.E_Uuv]
        data.E_Vuv = np.r_["0", data.E_Vuv, data1.E_Vuv]
        data.E_Ivw = np.r_["0", data.E_Ivw, data1.E_Ivw]
        data.E_Qvw = np.r_["0", data.E_Qvw, data1.E_Qvw]
        data.E_Uvw = np.r_["0", data.E_Uvw, data1.E_Uvw]
        data.E_Vvw = np.r_["0", data.E_Vvw, data1.E_Vvw]
        data.E_Iwu = np.r_["0", data.E_Iwu, data1.E_Iwu]
        data.E_Qwu = np.r_["0", data.E_Qwu, data1.E_Qwu]
        data.E_Uwu = np.r_["0", data.E_Uwu, data1.E_Uwu]
        data.E_Vwu = np.r_["0", data.E_Vwu, data1.E_Vwu]
        #
        data.E_DoPuv = np.r_["0", data.E_DoPuv, data1.E_DoPuv]
        data.E_DoLuv = np.r_["0", data.E_DoLuv, data1.E_DoLuv]
        data.E_DoCuv = np.r_["0", data.E_DoCuv, data1.E_DoCuv]
        data.E_ANGuv = np.r_["0", data.E_ANGuv, data1.E_ANGuv]
        data.E_DoPvw = np.r_["0", data.E_DoPvw, data1.E_DoPvw]
        data.E_DoLvw = np.r_["0", data.E_DoLvw, data1.E_DoLvw]
        data.E_DoCvw = np.r_["0", data.E_DoCvw, data1.E_DoCvw]
        data.E_ANGvw = np.r_["0", data.E_ANGvw, data1.E_ANGvw]
        data.E_DoPwu = np.r_["0", data.E_DoPwu, data1.E_DoPwu]
        data.E_DoLwu = np.r_["0", data.E_DoLwu, data1.E_DoLwu]
        data.E_DoCwu = np.r_["0", data.E_DoCwu, data1.E_DoCwu]
        data.E_ANGwu = np.r_["0", data.E_ANGwu, data1.E_ANGwu]
    #
    if data.complex[0] == 2:    # Matrix - N/R/L-separated
        # *** NC
        data.EuEu_NC = np.r_["0", data.EuEu_NC, data1.EuEu_NC]
        data.EvEv_NC = np.r_["0", data.EvEv_NC, data1.EvEv_NC]
        data.EwEw_NC = np.r_["0", data.EwEw_NC, data1.EwEw_NC]
        data.EuEv_re_NC = np.r_["0", data.EuEv_re_NC, data1.EuEv_re_NC]
        data.EvEw_re_NC = np.r_["0", data.EvEw_re_NC, data1.EvEw_re_NC]
        data.EwEu_re_NC = np.r_["0", data.EwEu_re_NC, data1.EwEu_re_NC]
        data.EuEv_im_NC = np.r_["0", data.EuEv_im_NC, data1.EuEv_im_NC]
        data.EvEw_im_NC = np.r_["0", data.EvEw_im_NC, data1.EvEw_im_NC]
        data.EwEu_im_NC = np.r_["0", data.EwEu_im_NC, data1.EwEu_im_NC]
        #
        data.E_Iuv_NC = np.r_["0", data.E_Iuv_NC, data1.E_Iuv_NC]
        data.E_Quv_NC = np.r_["0", data.E_Quv_NC, data1.E_Quv_NC]
        data.E_Uuv_NC = np.r_["0", data.E_Uuv_NC, data1.E_Uuv_NC]
        data.E_Vuv_NC = np.r_["0", data.E_Vuv_NC, data1.E_Vuv_NC]
        data.E_Ivw_NC = np.r_["0", data.E_Ivw_NC, data1.E_Ivw_NC]
        data.E_Qvw_NC = np.r_["0", data.E_Qvw_NC, data1.E_Qvw_NC]
        data.E_Uvw_NC = np.r_["0", data.E_Uvw_NC, data1.E_Uvw_NC]
        data.E_Vvw_NC = np.r_["0", data.E_Vvw_NC, data1.E_Vvw_NC]
        data.E_Iwu_NC = np.r_["0", data.E_Iwu_NC, data1.E_Iwu_NC]
        data.E_Qwu_NC = np.r_["0", data.E_Qwu_NC, data1.E_Qwu_NC]
        data.E_Uwu_NC = np.r_["0", data.E_Uwu_NC, data1.E_Uwu_NC]
        data.E_Vwu_NC = np.r_["0", data.E_Vwu_NC, data1.E_Vwu_NC]
        #
        data.E_DoPuv_NC = np.r_["0", data.E_DoPuv_NC, data1.E_DoPuv_NC]
        data.E_DoLuv_NC = np.r_["0", data.E_DoLuv_NC, data1.E_DoLuv_NC]
        data.E_DoCuv_NC = np.r_["0", data.E_DoCuv_NC, data1.E_DoCuv_NC]
        data.E_ANGuv_NC = np.r_["0", data.E_ANGuv_NC, data1.E_ANGuv_NC]
        data.E_DoPvw_NC = np.r_["0", data.E_DoPvw_NC, data1.E_DoPvw_NC]
        data.E_DoLvw_NC = np.r_["0", data.E_DoLvw_NC, data1.E_DoLvw_NC]
        data.E_DoCvw_NC = np.r_["0", data.E_DoCvw_NC, data1.E_DoCvw_NC]
        data.E_ANGvw_NC = np.r_["0", data.E_ANGvw_NC, data1.E_ANGvw_NC]
        data.E_DoPwu_NC = np.r_["0", data.E_DoPwu_NC, data1.E_DoPwu_NC]
        data.E_DoLwu_NC = np.r_["0", data.E_DoLwu_NC, data1.E_DoLwu_NC]
        data.E_DoCwu_NC = np.r_["0", data.E_DoCwu_NC, data1.E_DoCwu_NC]
        data.E_ANGwu_NC = np.r_["0", data.E_ANGwu_NC, data1.E_ANGwu_NC]
        #
        # *** RC
        data.EuEu_RC = np.r_["0", data.EuEu_RC, data1.EuEu_RC]
        data.EvEv_RC = np.r_["0", data.EvEv_RC, data1.EvEv_RC]
        data.EwEw_RC = np.r_["0", data.EwEw_RC, data1.EwEw_RC]
        data.EuEv_re_RC = np.r_["0", data.EuEv_re_RC, data1.EuEv_re_RC]
        data.EvEw_re_RC = np.r_["0", data.EvEw_re_RC, data1.EvEw_re_RC]
        data.EwEu_re_RC = np.r_["0", data.EwEu_re_RC, data1.EwEu_re_RC]
        data.EuEv_im_RC = np.r_["0", data.EuEv_im_RC, data1.EuEv_im_RC]
        data.EvEw_im_RC = np.r_["0", data.EvEw_im_RC, data1.EvEw_im_RC]
        data.EwEu_im_RC = np.r_["0", data.EwEu_im_RC, data1.EwEu_im_RC]
        #
        data.E_Iuv_RC = np.r_["0", data.E_Iuv_RC, data1.E_Iuv_RC]
        data.E_Quv_RC = np.r_["0", data.E_Quv_RC, data1.E_Quv_RC]
        data.E_Uuv_RC = np.r_["0", data.E_Uuv_RC, data1.E_Uuv_RC]
        data.E_Vuv_RC = np.r_["0", data.E_Vuv_RC, data1.E_Vuv_RC]
        data.E_Ivw_RC = np.r_["0", data.E_Ivw_RC, data1.E_Ivw_RC]
        data.E_Qvw_RC = np.r_["0", data.E_Qvw_RC, data1.E_Qvw_RC]
        data.E_Uvw_RC = np.r_["0", data.E_Uvw_RC, data1.E_Uvw_RC]
        data.E_Vvw_RC = np.r_["0", data.E_Vvw_RC, data1.E_Vvw_RC]
        data.E_Iwu_RC = np.r_["0", data.E_Iwu_RC, data1.E_Iwu_RC]
        data.E_Qwu_RC = np.r_["0", data.E_Qwu_RC, data1.E_Qwu_RC]
        data.E_Uwu_RC = np.r_["0", data.E_Uwu_RC, data1.E_Uwu_RC]
        data.E_Vwu_RC = np.r_["0", data.E_Vwu_RC, data1.E_Vwu_RC]
        #
        data.E_DoPuv_RC = np.r_["0", data.E_DoPuv_RC, data1.E_DoPuv_RC]
        data.E_DoLuv_RC = np.r_["0", data.E_DoLuv_RC, data1.E_DoLuv_RC]
        data.E_DoCuv_RC = np.r_["0", data.E_DoCuv_RC, data1.E_DoCuv_RC]
        data.E_ANGuv_RC = np.r_["0", data.E_ANGuv_RC, data1.E_ANGuv_RC]
        data.E_DoPvw_RC = np.r_["0", data.E_DoPvw_RC, data1.E_DoPvw_RC]
        data.E_DoLvw_RC = np.r_["0", data.E_DoLvw_RC, data1.E_DoLvw_RC]
        data.E_DoCvw_RC = np.r_["0", data.E_DoCvw_RC, data1.E_DoCvw_RC]
        data.E_ANGvw_RC = np.r_["0", data.E_ANGvw_RC, data1.E_ANGvw_RC]
        data.E_DoPwu_RC = np.r_["0", data.E_DoPwu_RC, data1.E_DoPwu_RC]
        data.E_DoLwu_RC = np.r_["0", data.E_DoLwu_RC, data1.E_DoLwu_RC]
        data.E_DoCwu_RC = np.r_["0", data.E_DoCwu_RC, data1.E_DoCwu_RC]
        data.E_ANGwu_RC = np.r_["0", data.E_ANGwu_RC, data1.E_ANGwu_RC]
        #
        # *** LC
        data.EuEu_LC = np.r_["0", data.EuEu_LC, data1.EuEu_LC]
        data.EvEv_LC = np.r_["0", data.EvEv_LC, data1.EvEv_LC]
        data.EwEw_LC = np.r_["0", data.EwEw_LC, data1.EwEw_LC]
        data.EuEv_re_LC = np.r_["0", data.EuEv_re_LC, data1.EuEv_re_LC]
        data.EvEw_re_LC = np.r_["0", data.EvEw_re_LC, data1.EvEw_re_LC]
        data.EwEu_re_LC = np.r_["0", data.EwEu_re_LC, data1.EwEu_re_LC]
        data.EuEv_im_LC = np.r_["0", data.EuEv_im_LC, data1.EuEv_im_LC]
        data.EvEw_im_LC = np.r_["0", data.EvEw_im_LC, data1.EvEw_im_LC]
        data.EwEu_im_LC = np.r_["0", data.EwEu_im_LC, data1.EwEu_im_LC]
        #
        data.E_Iuv_LC = np.r_["0", data.E_Iuv_LC, data1.E_Iuv_LC]
        data.E_Quv_LC = np.r_["0", data.E_Quv_LC, data1.E_Quv_LC]
        data.E_Uuv_LC = np.r_["0", data.E_Uuv_LC, data1.E_Uuv_LC]
        data.E_Vuv_LC = np.r_["0", data.E_Vuv_LC, data1.E_Vuv_LC]
        data.E_Ivw_LC = np.r_["0", data.E_Ivw_LC, data1.E_Ivw_LC]
        data.E_Qvw_LC = np.r_["0", data.E_Qvw_LC, data1.E_Qvw_LC]
        data.E_Uvw_LC = np.r_["0", data.E_Uvw_LC, data1.E_Uvw_LC]
        data.E_Vvw_LC = np.r_["0", data.E_Vvw_LC, data1.E_Vvw_LC]
        data.E_Iwu_LC = np.r_["0", data.E_Iwu_LC, data1.E_Iwu_LC]
        data.E_Qwu_LC = np.r_["0", data.E_Qwu_LC, data1.E_Qwu_LC]
        data.E_Uwu_LC = np.r_["0", data.E_Uwu_LC, data1.E_Uwu_LC]
        data.E_Vwu_LC = np.r_["0", data.E_Vwu_LC, data1.E_Vwu_LC]
        #
        data.E_DoPuv_LC = np.r_["0", data.E_DoPuv_LC, data1.E_DoPuv_LC]
        data.E_DoLuv_LC = np.r_["0", data.E_DoLuv_LC, data1.E_DoLuv_LC]
        data.E_DoCuv_LC = np.r_["0", data.E_DoCuv_LC, data1.E_DoCuv_LC]
        data.E_ANGuv_LC = np.r_["0", data.E_ANGuv_LC, data1.E_ANGuv_LC]
        data.E_DoPvw_LC = np.r_["0", data.E_DoPvw_LC, data1.E_DoPvw_LC]
        data.E_DoLvw_LC = np.r_["0", data.E_DoLvw_LC, data1.E_DoLvw_LC]
        data.E_DoCvw_LC = np.r_["0", data.E_DoCvw_LC, data1.E_DoCvw_LC]
        data.E_ANGvw_LC = np.r_["0", data.E_ANGvw_LC, data1.E_ANGvw_LC]
        data.E_DoPwu_LC = np.r_["0", data.E_DoPwu_LC, data1.E_DoPwu_LC]
        data.E_DoLwu_LC = np.r_["0", data.E_DoLwu_LC, data1.E_DoLwu_LC]
        data.E_DoCwu_LC = np.r_["0", data.E_DoCwu_LC, data1.E_DoCwu_LC]
        data.E_ANGwu_LC = np.r_["0", data.E_ANGwu_LC, data1.E_ANGwu_LC]
        #
        data.num_NC = np.r_["0", data.num_NC, data1.num_NC]
        data.num_RC = np.r_["0", data.num_RC, data1.num_RC]
        data.num_LC = np.r_["0", data.num_LC, data1.num_LC]

    if data.complex[0] == 3:    # 3D-matrix
        data.EuiEui = np.r_["0", data.EuiEui, data1.EuiEui]
        data.EuqEuq = np.r_["0", data.EuqEuq, data1.EuqEuq]
        data.EviEvi = np.r_["0", data.EviEvi, data1.EviEvi]
        data.EvqEvq = np.r_["0", data.EvqEvq, data1.EvqEvq]
        data.EwiEwi = np.r_["0", data.EwiEwi, data1.EwiEwi]
        data.EwqEwq = np.r_["0", data.EwqEwq, data1.EwqEwq]
        #
        data.EuiEvi = np.r_["0", data.EuiEvi, data1.EuiEvi]
        data.EviEwi = np.r_["0", data.EviEwi, data1.EviEwi]
        data.EwiEui = np.r_["0", data.EwiEui, data1.EwiEui]
        data.EuqEvq = np.r_["0", data.EuqEvq, data1.EuqEvq]
        data.EvqEwq = np.r_["0", data.EvqEwq, data1.EvqEwq]
        data.EwqEuq = np.r_["0", data.EwqEuq, data1.EwqEuq]
        #
        data.EuiEvq = np.r_["0", data.EuiEvq, data1.EuiEvq]
        data.EuqEvi = np.r_["0", data.EuqEvi, data1.EuqEvi]
        data.EviEwq = np.r_["0", data.EviEwq, data1.EviEwq]
        data.EvqEwi = np.r_["0", data.EvqEwi, data1.EvqEwi]
        data.EwiEuq = np.r_["0", data.EwiEuq, data1.EwiEuq]
        data.EwqEui = np.r_["0", data.EwqEui, data1.EwqEui]
        #
        data.EuiEuq = np.r_["0", data.EuiEuq, data1.EuiEuq]
        data.EviEvq = np.r_["0", data.EviEvq, data1.EviEvq]
        data.EwiEwq = np.r_["0", data.EwiEwq, data1.EwiEwq]
        #
        data.E_I_3d = np.r_["0", data.E_I_3d, data1.E_I_3d]
        data.E_Q_3d = np.r_["0", data.E_Q_3d, data1.E_Q_3d]
        data.E_U_3d = np.r_["0", data.E_U_3d, data1.E_U_3d]
        data.E_Vu_3d = np.r_["0", data.E_Vu_3d, data1.E_Vu_3d]
        data.E_Vv_3d = np.r_["0", data.E_Vv_3d, data1.E_Vv_3d]
        data.E_Vw_3d = np.r_["0", data.E_Vw_3d, data1.E_Vw_3d]
        #
        data.E_DoP_3d = np.r_["0", data.E_DoP_3d, data1.E_DoP_3d]
        data.E_DoL_3d = np.r_["0", data.E_DoL_3d, data1.E_DoL_3d]
        data.E_DoC_3d = np.r_["0", data.E_DoC_3d, data1.E_DoC_3d]
        data.E_ANG_3d = np.r_["0", data.E_ANG_3d, data1.E_ANG_3d]
        data.E_k_lon = np.r_["0", data.E_k_lon, data1.E_k_lon]
        data.E_k_lat = np.r_["0", data.E_k_lat, data1.E_k_lat]
    #
    data.BG_Eu = np.r_["0", data.BG_Eu, data1.BG_Eu]
    data.BG_Ev = np.r_["0", data.BG_Ev, data1.BG_Ev]
    data.BG_Ew = np.r_["0", data.BG_Ew, data1.BG_Ew]
        
    return data