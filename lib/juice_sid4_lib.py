"""
    JUICE RPWI HF SID4 (Burst surv): L1a QL -- 2024/7/22
"""
import numpy as np
import juice_math_lib as juice_math


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID4 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid4_read(cdf):
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

    # complex < 2:     # Power
    data.EuEu = cdf['EuEu'][...]
    data.EvEv = cdf['EvEv'][...]
    data.EwEw = cdf['EwEw'][...]
    #
    # complex == 1:    # Matrix
    data.EuEv_re = cdf['EuEv_re'][...]
    data.EvEw_re = cdf['EvEw_re'][...]
    data.EwEu_re = cdf['EwEu_re'][...]
    data.EuEv_im = cdf['EuEv_im'][...]
    data.EvEw_im = cdf['EvEw_im'][...]
    data.EwEu_im = cdf['EwEu_im'][...]
    #
    # complex[0] == 3:    # 3D-matrix
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

    return data


def hf_sid4_add(data, data1):
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
    # data.complex > 0:     # Power
    data.EuEv_re = np.r_["0", data.EuEv_re, data1.EuEv_re]
    data.EvEw_re = np.r_["0", data.EvEw_re, data1.EvEw_re]
    data.EwEu_re = np.r_["0", data.EwEu_re, data1.EwEu_re]
    data.EuEv_im = np.r_["0", data.EuEv_im, data1.EuEv_im]
    data.EvEw_im = np.r_["0", data.EvEw_im, data1.EvEw_im]
    data.EwEu_im = np.r_["0", data.EwEu_im, data1.EwEu_im]
    #
    # complex == 3:    # 3D-matrix
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
        
    return data


def hf_sid4_shaping(data):
    """
    input:  data
    return: data
    """
    # CUT
    if data.EuEu.shape[1] != 72:
        print("Mode: **** error ****")

    # *** TMP: complex-2&3 data ==> complex-1 data ***
    n_time0 = data.EuEu.shape[0]
    for i in range(n_time0):
        if data.complex[i] == 3:    # Matrix - N/R/L-separated
            data.EuEu[i]    =  data.EuiEui[i] + data.EuqEuq[i]
            data.EvEv[i]    =  data.EviEvi[i] + data.EvqEvq[i]
            data.EwEw[i]    =  data.EwiEwi[i] + data.EwqEwq[i]
            data.EuEv_re[i] =  data.EuiEvi[i] + data.EuqEvq[i]
            data.EvEw_re[i] =  data.EviEwi[i] + data.EvqEwq[i]
            data.EwEu_re[i] =  data.EwiEui[i] + data.EwqEuq[i]
            data.EuEv_im[i] = -data.EuiEvq[i] + data.EuqEvi[i]
            data.EvEw_im[i] = -data.EviEwq[i] + data.EviEvq[i]
            data.EwEu_im[i] = -data.EwiEuq[i] + data.EwqEui[i]

    # STOKES
    # *** all
    data.E_Iuv,   data.E_Quv,   data.E_Uuv,   data.E_Vuv   = juice_math.get_stokes(data.EuEu, data.EvEv, data.EuEv_re, data.EuEv_im)
    data.E_Ivw,   data.E_Qvw,   data.E_Uvw,   data.E_Vvw   = juice_math.get_stokes(data.EvEv, data.EwEw, data.EvEw_re, data.EvEw_im)
    data.E_Iwu,   data.E_Qwu,   data.E_Uwu,   data.E_Vwu   = juice_math.get_stokes(data.EwEw, data.EuEu, data.EwEu_re, data.EwEu_im)
    data.E_DoPuv, data.E_DoLuv, data.E_DoCuv, data.E_ANGuv = juice_math.get_pol(data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv)
    data.E_DoPvw, data.E_DoLvw, data.E_DoCvw, data.E_ANGvw = juice_math.get_pol(data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw)
    data.E_DoPwu, data.E_DoLwu, data.E_DoCwu, data.E_ANGwu = juice_math.get_pol(data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu)

    # *** 3D
    data.E_I_3d = data.EuiEui + data.EuqEuq + data.EviEvi + data.EvqEvq + data.EwiEwi + data.EwqEwq
    data.E_Q_3d = data.EuiEvi - data.EuqEuq + data.EviEvi - data.EvqEvq + data.EwiEwi - data.EwqEwq
    data.E_U_3d = 2. * (data.EuiEuq + data.EviEvq + data.EwiEwq)
    data.E_Vu_3d = -2. * (data.EviEwq - data.EvqEwi)
    data.E_Vv_3d = -2. * (data.EwiEuq - data.EwqEui)
    data.E_Vw_3d = -2. * (data.EuiEvq - data.EuqEvi)
    data.E_DoP_3d, data.E_DoL_3d, data.E_DoC_3d, data.E_ANG_3d, data.E_k_lon, data.E_k_lat = \
        juice_math.get_pol_3D(data.E_I_3d, data.E_Q_3d, data.E_U_3d, data.E_Vu_3d, data.E_Vv_3d, data.E_Vw_3d)

    return data