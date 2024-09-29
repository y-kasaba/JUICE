"""
    JUICE RPWI HF SID21 (PSSR1 rich): L1a QL -- 2024/9/28
"""
import numpy as np
import juice_spec_lib as juice_spec


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID21 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid21_read(cdf, RPWI_FSW_version):
    """
    input:  CDF, cf:conversion factor
    return: data
    """
    data = struct()
    data.RPWI_FSW_version = RPWI_FSW_version

    # AUX
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    data.complex    = cdf['complex'][...]
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
    data.N_samp = np.int64(cdf['N_samp'][...])
    data.N_step = np.int64(cdf['N_step'][...])
    data.decimation = cdf['decimation'][...]
    data.pol       = cdf['pol'][...]
    data.B0_startf = cdf['B0_startf'][...]
    data.B0_stopf  = cdf['B0_stopf'][...]
    data.B0_step   = cdf['B0_step'][...]
    data.B0_repeat = cdf['B0_repeat'][...]
    data.B0_subdiv = cdf['B0_subdiv'][...]

    # Data
    data.frequency  = cdf['frequency'][...]
    data.freq_step  = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]
    #
    data.epoch = cdf['Epoch'][...]
    data.scet  = cdf['SCET'][...]
    #
    data.EuEu = np.float64(cdf['EuEu'][...])
    data.EvEv = np.float64(cdf['EvEv'][...])
    data.EwEw = np.float64(cdf['EwEw'][...])
    if data.complex[0] > 0:    # Matrix
        data.EuEv_re = np.float64(cdf['EuEv_re'][...])
        data.EuEv_im = np.float64(cdf['EuEv_im'][...])
        data.EvEw_re = np.float64(cdf['EvEw_re'][...])
        data.EvEw_im = np.float64(cdf['EvEw_im'][...])
        data.EwEu_re = np.float64(cdf['EwEu_re'][...])
        data.EwEu_im = np.float64(cdf['EwEu_im'][...])

    return data


def hf_sid5_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # AUX
    data.U_selected    = np.r_["0", data.U_selected, data1.U_selected]
    data.V_selected    = np.r_["0", data.V_selected, data1.V_selected]
    data.W_selected    = np.r_["0", data.W_selected, data1.W_selected]
    data.complex       = np.r_["0", data.complex, data1.complex]
    #
    data.cal_signal    = np.r_["0", data.cal_signal, data1.cal_signal]
    data.sweep_table   = np.r_["0", data.sweep_table, data1.sweep_table]
    data.onboard_cal   = np.r_["0", data.onboard_cal, data1.onboard_cal]
    data.BG_subtract   = np.r_["0", data.BG_subtract, data1.BG_subtract]
    data.BG_select     = np.r_["0", data.BG_select, data1.BG_select]
    data.FFT_window    = np.r_["0", data.FFT_window, data1.FFT_window]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    data.Pol_sep_thres = np.r_["0", data.Pol_sep_thres, data1.Pol_sep_thres]
    data.Pol_sep_SW    = np.r_["0", data.Pol_sep_SW, data1.Pol_sep_SW]
    data.overflow_U    = np.r_["0", data.overflow_U, data1.overflow_U]
    data.overflow_V    = np.r_["0", data.overflow_V, data1.overflow_V]
    data.overflow_W    = np.r_["0", data.overflow_W, data1.overflow_W]
    data.proc_param0   = np.r_["0", data.proc_param0, data1.proc_param0]
    data.proc_param1   = np.r_["0", data.proc_param1, data1.proc_param1]
    data.proc_param2   = np.r_["0", data.proc_param2, data1.proc_param2]
    data.proc_param3   = np.r_["0", data.proc_param3, data1.proc_param3]
    data.freq_start    = np.r_["0", data.freq_start, data1.freq_start]

    # Header
    data.N_samp        = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step        = np.r_["0", data.N_step, data1.N_step]
    data.decimation    = np.r_["0", data.decimation, data1.decimation]
    data.pol           = np.r_["0", data.pol, data1.pol]
    data.B0_startf     = np.r_["0", data.B0_startf, data1.B0_startf]
    data.B0_stopf      = np.r_["0", data.B0_stopf, data1.B0_stopf]
    data.B0_step       = np.r_["0", data.B0_step, data1.B0_step]
    data.B0_repeat     = np.r_["0", data.B0_repeat, data1.B0_repeat]
    data.B0_subdiv     = np.r_["0", data.B0_subdiv, data1.B0_subdiv]

    # Data
    data.epoch         = np.r_["0", data.epoch, data1.epoch]
    data.scet          = np.r_["0", data.scet, data1.scet]
    #
    data.frequency     = np.r_["0", data.frequency, data1.frequency]
    data.freq_step     = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width    = np.r_["0", data.freq_width, data1.freq_width]
    #
    data.EuEu          = np.r_["0", data.EuEu, data1.EuEu]
    data.EvEv          = np.r_["0", data.EvEv, data1.EvEv]
    data.EwEw          = np.r_["0", data.EwEw, data1.EwEw]
    if data.complex[0] > 0:    # Matrix
        data.EuEv_re = np.r_["0", data.EuEv_re, data1.EuEv_re]
        data.EvEw_re = np.r_["0", data.EvEw_re, data1.EvEw_re]
        data.EwEu_re = np.r_["0", data.EwEu_re, data1.EwEu_re]
        data.EuEv_im = np.r_["0", data.EuEv_im, data1.EuEv_im]
        data.EvEw_im = np.r_["0", data.EvEw_im, data1.EvEw_im]
        data.EwEu_im = np.r_["0", data.EwEu_im, data1.EwEu_im]
        
    return data



def hf_sid21_shaping(data):
    """
    input:  data
    return: data
    """
    if data.complex[0] > 0:    # Matrix
        data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv = juice_spec.get_stokes(data.EuEu, data.EvEv, data.EuEv_re, data.EuEv_im)
        data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw = juice_spec.get_stokes(data.EvEv, data.EwEw, data.EvEw_re, data.EvEw_im)
        data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu = juice_spec.get_stokes(data.EwEw, data.EuEu, data.EwEu_re, data.EwEu_im)
        data.E_DoPuv, data.E_DoLuv, data.E_DoCuv, data.E_ANGuv = juice_spec.get_pol(data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv)
        data.E_DoPvw, data.E_DoLvw, data.E_DoCvw, data.E_ANGvw = juice_spec.get_pol(data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw)
        data.E_DoPwu, data.E_DoLwu, data.E_DoCwu, data.E_ANGwu = juice_spec.get_pol(data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu)

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

    data.freq   = data.frequency
    data.freq_w = data.freq_width

    return data