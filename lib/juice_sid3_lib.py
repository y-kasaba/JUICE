"""
    JUICE RPWI HF SID3 (Full): L1a QL -- 2024/8/31
"""
import numpy as np
# import juice_spec_lib as juice_spec

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
    data.U_selected  = cdf['U_selected'][...];  data.V_selected = cdf['V_selected'][...];  data.W_selected = cdf['W_selected'][...]
    data.complex     = cdf['complex'][...]
    data.cal_signal  = cdf['cal_signal'][...]
    data.sweep_table = cdf['sweep_table'][...]  # (fixed: not defined in V.2)
    data.onboard_cal = cdf['onboard_cal'][...]  # (not used)
    data.BG_subtract = cdf['BG_subtract'][...]
    data.BG_select   = cdf['BG_select'][...]
    data.FFT_window  = cdf['FFT_window'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    data.Pol_sep_thres = cdf['Pol_sep_thres'][...]
    data.Pol_sep_SW  = cdf['Pol_sep_SW'][...]
    data.overflow_U  = cdf['overflow_U'][...]   # (fixed: not defined in V.2)
    data.overflow_V  = cdf['overflow_V'][...]   # (fixed: not defined in V.2)
    data.overflow_W  = cdf['overflow_W'][...]   # (fixed: not defined in V.2)
    data.proc_param0 = cdf['proc_param0'][...];  data.proc_param1 = cdf['proc_param1'][...]
    data.proc_param2 = cdf['proc_param2'][...];  data.proc_param3 = cdf['proc_param3'][...]
    data.BG_downlink = cdf['BG_downlink'][...]
    data.N_block     = cdf['N_block'][...]
    data.T_RWI_CH1   = np.float16(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float16(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float16(cdf['T_HF_FPGA'][...])
    # Header
    data.N_samp      = cdf['N_samp'][...];     data.N_step    = cdf['N_step'][...]
    data.decimation  = cdf['decimation'][...]; data.pol       = cdf['pol'][...]
    data.B0_startf   = cdf['B0_startf'][...];  data.B0_stopf  = cdf['B0_stopf'][...];  data.B0_step = cdf['B0_step'][...]
    data.B0_repeat   = cdf['B0_repeat'][...];  data.B0_subdiv = cdf['B0_subdiv'][...]
    data.B1_startf   = cdf['B1_startf'][...];  data.B1_stopf  = cdf['B1_stopf'][...];  data.B1_step = cdf['B1_step'][...]
    data.B1_repeat   = cdf['B1_repeat'][...];  data.B1_subdiv = cdf['B1_subdiv'][...]
    data.B2_startf   = cdf['B2_startf'][...];  data.B2_stopf  = cdf['B2_stopf'][...];  data.B2_step = cdf['B2_step'][...]
    data.B2_repeat   = cdf['B2_repeat'][...];  data.B2_subdiv = cdf['B2_subdiv'][...]
    data.B3_startf   = cdf['B3_startf'][...];  data.B3_stopf  = cdf['B3_stopf'][...];  data.B3_step = cdf['B3_step'][...]
    data.B3_repeat   = cdf['B3_repeat'][...];  data.B3_subdiv = cdf['B3_subdiv'][...]
    data.B4_startf   = cdf['B4_startf'][...];  data.B4_stopf  = cdf['B4_stopf'][...];  data.B4_step = cdf['B4_step'][...]
    data.B4_repeat   = cdf['B4_repeat'][...];  data.B4_subdiv = cdf['B4_subdiv'][...]
    # Data
    data.frequency   = cdf['frequency'][...];  data.freq_step = cdf['freq_step'][...]; data.freq_width  = cdf['freq_width'][...]
    data.epoch       = cdf['Epoch'][...];      data.scet      = cdf['SCET'][...]
    # complex < 2:     # Power
    data.EuEu        = cdf['EuEu'][...];       data.EvEv       = cdf['EvEv'][...];       data.EwEw = cdf['EwEw'][...]
    # complex == 1:    # Matrix
    data.EuEv_re     = cdf['EuEv_re'][...];    data.EvEw_re    = cdf['EvEw_re'][...];    data.EwEu_re    = cdf['EwEu_re'][...];    
    data.EuEv_im     = cdf['EuEv_im'][...];    data.EvEw_im    = cdf['EvEw_im'][...];    data.EwEu_im    = cdf['EwEu_im'][...]
    # complex == 2:    # Matrix - N/R/L-separated
    # *** NC
    data.EuEu_NC     = cdf['EuEu_NC'][...];    data.EvEv_NC    = cdf['EvEv_NC'][...];    data.EwEw_NC    = cdf['EwEw_NC'][...]
    data.EuEv_re_NC  = cdf['EuEv_re_NC'][...]; data.EvEw_re_NC = cdf['EvEw_re_NC'][...]; data.EwEu_re_NC = cdf['EwEu_re_NC'][...]
    data.EuEv_im_NC  = cdf['EuEv_im_NC'][...]; data.EvEw_im_NC = cdf['EvEw_im_NC'][...]; data.EwEu_im_NC = cdf['EwEu_im_NC'][...]
    # *** RC
    data.EuEu_RC     = cdf['EuEu_RC'][...];    data.EvEv_RC    = cdf['EvEv_RC'][...];    data.EwEw_RC    = cdf['EwEw_RC'][...]
    data.EuEv_re_RC  = cdf['EuEv_re_RC'][...]; data.EvEw_re_RC = cdf['EvEw_re_RC'][...]; data.EwEu_re_RC = cdf['EwEu_re_RC'][...]
    data.EuEv_im_RC  = cdf['EuEv_im_RC'][...]; data.EvEw_im_RC = cdf['EvEw_im_RC'][...]; data.EwEu_im_RC = cdf['EwEu_im_RC'][...]
    # *** LC
    data.EuEu_LC     = cdf['EuEu_LC'][...];    data.EvEv_LC    = cdf['EvEv_LC'][...];    data.EwEw_LC    = cdf['EwEw_LC'][...]
    data.EuEv_re_LC  = cdf['EuEv_re_LC'][...]; data.EvEw_re_LC = cdf['EvEw_re_LC'][...]; data.EwEu_re_LC = cdf['EwEu_re_LC'][...]
    data.EuEv_im_LC  = cdf['EuEv_im_LC'][...]; data.EvEw_im_LC = cdf['EvEw_im_LC'][...]; data.EwEu_im_LC = cdf['EwEu_im_LC'][...]
    #
    data.num_NC      = cdf['num_NC'][...];     data.num_RC     = cdf['num_RC'][...];     data.num_LC     = cdf['num_LC'][...]
    # complex == 3:    # 3D-matrix
    data.EuiEui      = cdf['EuiEui'][...];     data.EuqEuq     = cdf['EuqEuq'][...]
    data.EviEvi      = cdf['EviEvi'][...];     data.EvqEvq     = cdf['EvqEvq'][...]
    data.EwiEwi      = cdf['EwiEwi'][...];     data.EwqEwq     = cdf['EwqEwq'][...]
    #
    data.EuiEvi      = cdf['EuiEvi'][...];     data.EviEwi     = cdf['EviEwi'][...]
    data.EwiEui      = cdf['EwiEui'][...];     data.EuqEvq     = cdf['EuqEvq'][...]
    data.EvqEwq      = cdf['EvqEwq'][...];     data.EwqEuq     = cdf['EwqEuq'][...]
    #
    data.EuiEvq      = cdf['EuiEvq'][...];     data.EuqEvi     = cdf['EuqEvi'][...]
    data.EviEwq      = cdf['EviEwq'][...];     data.EvqEwi     = cdf['EvqEwi'][...]
    data.EwiEuq      = cdf['EwiEuq'][...];     data.EwqEui     = cdf['EwqEui'][...]
    #
    data.EuiEuq      = cdf['EuiEuq'][...];     data.EviEvq     = cdf['EviEvq'][...];    data.EwiEwq     = cdf['EwiEwq'][...]
    #
    data.BG_Eu       = cdf['BG_Eu'][...];      data.BG_Ev      = cdf['BG_Ev'][...];     data.BG_Ew      = cdf['BG_Ew'][...]
    return data


def hf_sid3_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # AUX
    data.U_selected  = np.r_["0", data.U_selected, data1.U_selected]
    data.V_selected  = np.r_["0", data.V_selected, data1.V_selected]
    data.W_selected  = np.r_["0", data.W_selected, data1.W_selected]
    data.complex     = np.r_["0", data.complex, data1.complex]
    #
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.sweep_table = np.r_["0", data.sweep_table, data1.sweep_table]
    data.onboard_cal = np.r_["0", data.onboard_cal, data1.onboard_cal]
    data.BG_subtract = np.r_["0", data.BG_subtract, data1.BG_subtract]
    data.BG_select   = np.r_["0", data.BG_select, data1.BG_select]
    data.FFT_window  = np.r_["0", data.FFT_window, data1.FFT_window]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    data.Pol_sep_thres = np.r_["0", data.Pol_sep_thres, data1.Pol_sep_thres]
    data.Pol_sep_SW  = np.r_["0", data.Pol_sep_SW, data1.Pol_sep_SW]
    data.overflow_U  = np.r_["0", data.overflow_U, data1.overflow_U]
    data.overflow_V  = np.r_["0", data.overflow_V, data1.overflow_V]
    data.overflow_W  = np.r_["0", data.overflow_W, data1.overflow_W]
    data.proc_param0 = np.r_["0", data.proc_param0, data1.proc_param0]
    data.proc_param1 = np.r_["0", data.proc_param1, data1.proc_param1]
    data.proc_param2 = np.r_["0", data.proc_param2, data1.proc_param2]
    data.proc_param3 = np.r_["0", data.proc_param3, data1.proc_param3]
    data.BG_downlink = np.r_["0", data.BG_downlink, data1.BG_downlink]
    data.N_block     = np.r_["0", data.N_block, data1.N_block]
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.N_samp      = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step      = np.r_["0", data.N_step, data1.N_step]
    data.decimation  = np.r_["0", data.decimation, data1.decimation]
    data.pol         = np.r_["0", data.pol, data1.pol]
    data.B0_startf   = np.r_["0", data.B0_startf, data1.B0_startf]
    data.B0_stopf    = np.r_["0", data.B0_stopf, data1.B0_stopf]
    data.B0_step     = np.r_["0", data.B0_step, data1.B0_step]
    data.B0_repeat   = np.r_["0", data.B0_repeat, data1.B0_repeat]
    data.B0_subdiv   = np.r_["0", data.B0_subdiv, data1.B0_subdiv]
    data.B1_startf   = np.r_["0", data.B1_startf, data1.B1_startf]
    data.B1_stopf    = np.r_["0", data.B1_stopf, data1.B1_stopf]
    data.B1_step     = np.r_["0", data.B1_step, data1.B1_step]
    data.B1_repeat   = np.r_["0", data.B1_repeat, data1.B1_repeat]
    data.B1_subdiv   = np.r_["0", data.B1_subdiv, data1.B1_subdiv]
    data.B2_startf   = np.r_["0", data.B2_startf, data1.B2_startf]
    data.B2_stopf    = np.r_["0", data.B2_stopf, data1.B2_stopf]
    data.B2_step     = np.r_["0", data.B2_step, data1.B2_step]
    data.B2_repeat   = np.r_["0", data.B2_repeat, data1.B2_repeat]
    data.B2_subdiv   = np.r_["0", data.B2_subdiv, data1.B2_subdiv]
    data.B3_startf   = np.r_["0", data.B3_startf, data1.B3_startf]
    data.B3_stopf    = np.r_["0", data.B3_stopf, data1.B3_stopf]
    data.B3_step     = np.r_["0", data.B3_step, data1.B3_step]
    data.B3_repeat   = np.r_["0", data.B3_repeat, data1.B3_repeat]
    data.B3_subdiv   = np.r_["0", data.B3_subdiv, data1.B3_subdiv]
    data.B4_startf   = np.r_["0", data.B4_startf, data1.B4_startf]
    data.B4_stopf    = np.r_["0", data.B4_stopf, data1.B4_stopf]
    data.B4_step     = np.r_["0", data.B4_step, data1.B4_step]
    data.B4_repeat   = np.r_["0", data.B4_repeat, data1.B4_repeat]
    data.B4_subdiv   = np.r_["0", data.B4_subdiv, data1.B4_subdiv]
    # Data
    data.epoch       = np.r_["0", data.epoch, data1.epoch]
    data.scet        = np.r_["0", data.scet, data1.scet]
    data.frequency   = np.r_["0", data.frequency, data1.frequency]
    data.freq_step   = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width  = np.r_["0", data.freq_width, data1.freq_width]
    # complex < 2:     # Power
    data.EuEu        = np.r_["0", data.EuEu, data1.EuEu]
    data.EvEv        = np.r_["0", data.EvEv, data1.EvEv]
    data.EwEw        = np.r_["0", data.EwEw, data1.EwEw]
    # complex == 1:    # Matrix
    data.EuEv_re     = np.r_["0", data.EuEv_re, data1.EuEv_re];       data.EvEw_re = np.r_["0", data.EvEw_re, data1.EvEw_re]
    data.EwEu_re     = np.r_["0", data.EwEu_re, data1.EwEu_re];       data.EuEv_im = np.r_["0", data.EuEv_im, data1.EuEv_im]
    data.EvEw_im     = np.r_["0", data.EvEw_im, data1.EvEw_im];       data.EwEu_im = np.r_["0", data.EwEu_im, data1.EwEu_im]
    # complex == 2:    # Matrix - N/R/L-separated
    # *** NC
    data.EuEu_NC     = np.r_["0", data.EuEu_NC, data1.EuEu_NC]
    data.EvEv_NC     = np.r_["0", data.EvEv_NC, data1.EvEv_NC]
    data.EwEw_NC     = np.r_["0", data.EwEw_NC, data1.EwEw_NC]
    data.EuEv_re_NC  = np.r_["0", data.EuEv_re_NC, data1.EuEv_re_NC]; data.EvEw_re_NC = np.r_["0", data.EvEw_re_NC, data1.EvEw_re_NC]
    data.EwEu_re_NC  = np.r_["0", data.EwEu_re_NC, data1.EwEu_re_NC]; data.EuEv_im_NC = np.r_["0", data.EuEv_im_NC, data1.EuEv_im_NC]
    data.EvEw_im_NC  = np.r_["0", data.EvEw_im_NC, data1.EvEw_im_NC]; data.EwEu_im_NC = np.r_["0", data.EwEu_im_NC, data1.EwEu_im_NC]
    # *** RC
    data.EuEu_RC     = np.r_["0", data.EuEu_RC, data1.EuEu_RC]
    data.EvEv_RC     = np.r_["0", data.EvEv_RC, data1.EvEv_RC]
    data.EwEw_RC     = np.r_["0", data.EwEw_RC, data1.EwEw_RC]
    data.EuEv_re_RC  = np.r_["0", data.EuEv_re_RC, data1.EuEv_re_RC]; data.EvEw_re_RC = np.r_["0", data.EvEw_re_RC, data1.EvEw_re_RC]
    data.EwEu_re_RC  = np.r_["0", data.EwEu_re_RC, data1.EwEu_re_RC]; data.EuEv_im_RC = np.r_["0", data.EuEv_im_RC, data1.EuEv_im_RC]
    data.EvEw_im_RC  = np.r_["0", data.EvEw_im_RC, data1.EvEw_im_RC]; data.EwEu_im_RC = np.r_["0", data.EwEu_im_RC, data1.EwEu_im_RC]
    # *** LC
    data.EuEu_LC     = np.r_["0", data.EuEu_LC, data1.EuEu_LC]
    data.EvEv_LC     = np.r_["0", data.EvEv_LC, data1.EvEv_LC]
    data.EwEw_LC     = np.r_["0", data.EwEw_LC, data1.EwEw_LC]
    data.EuEv_re_LC  = np.r_["0", data.EuEv_re_LC, data1.EuEv_re_LC]; data.EvEw_re_LC = np.r_["0", data.EvEw_re_LC, data1.EvEw_re_LC]
    data.EwEu_re_LC  = np.r_["0", data.EwEu_re_LC, data1.EwEu_re_LC]; data.EuEv_im_LC = np.r_["0", data.EuEv_im_LC, data1.EuEv_im_LC]
    data.EvEw_im_LC  = np.r_["0", data.EvEw_im_LC, data1.EvEw_im_LC]; data.EwEu_im_LC = np.r_["0", data.EwEu_im_LC, data1.EwEu_im_LC]
    #
    data.num_NC      = np.r_["0", data.num_NC, data1.num_NC]
    data.num_RC      = np.r_["0", data.num_RC, data1.num_RC]
    data.num_LC      = np.r_["0", data.num_LC, data1.num_LC]
    # complex == 3:    # 3D-matrix
    data.EuiEui      = np.r_["0", data.EuiEui, data1.EuiEui];         data.EuqEuq = np.r_["0", data.EuqEuq, data1.EuqEuq]
    data.EviEvi      = np.r_["0", data.EviEvi, data1.EviEvi];         data.EvqEvq = np.r_["0", data.EvqEvq, data1.EvqEvq]
    data.EwiEwi      = np.r_["0", data.EwiEwi, data1.EwiEwi];         data.EwqEwq = np.r_["0", data.EwqEwq, data1.EwqEwq]
    #
    data.EuiEvi      = np.r_["0", data.EuiEvi, data1.EuiEvi];         data.EviEwi = np.r_["0", data.EviEwi, data1.EviEwi]
    data.EwiEui      = np.r_["0", data.EwiEui, data1.EwiEui];         data.EuqEvq = np.r_["0", data.EuqEvq, data1.EuqEvq]
    data.EvqEwq      = np.r_["0", data.EvqEwq, data1.EvqEwq];         data.EwqEuq = np.r_["0", data.EwqEuq, data1.EwqEuq]
    #
    data.EuiEvq      = np.r_["0", data.EuiEvq, data1.EuiEvq];         data.EuqEvi = np.r_["0", data.EuqEvi, data1.EuqEvi]
    data.EviEwq      = np.r_["0", data.EviEwq, data1.EviEwq];         data.EvqEwi = np.r_["0", data.EvqEwi, data1.EvqEwi]
    data.EwiEuq      = np.r_["0", data.EwiEuq, data1.EwiEuq];         data.EwqEui = np.r_["0", data.EwqEui, data1.EwqEui]
    #
    data.EuiEuq      = np.r_["0", data.EuiEuq, data1.EuiEuq]
    data.EviEvq      = np.r_["0", data.EviEvq, data1.EviEvq]
    data.EwiEwq      = np.r_["0", data.EwiEwq, data1.EwiEwq]
    #
    data.BG_Eu       = np.r_["0", data.BG_Eu, data1.BG_Eu]
    data.BG_Ev       = np.r_["0", data.BG_Ev, data1.BG_Ev]
    data.BG_Ew       = np.r_["0", data.BG_Ew, data1.BG_Ew]
    return data


def hf_sid3_shaping(data, cal_mode, N_ch, comp_mode):
    """
    input:  data
            cal_mode    [Power]     0: background          1: CAL           2: all
            N_ch0       [channel]   2: 2-ch    3: 3-ch                   0,>3: any
            comp_mode   [Complex]   0: Poweer  1: Matrix   3: Matrix-2D    >3: any   
    return: data
    """
    # CUT -- Ver.1
    n_num = data.B0_step[0]
    if n_num == 255:
        data.EuEu = data.EuEu[:, 0:n_num];  data.EvEv = data.EvEv[:, 0:n_num];  data.EwEw = data.EwEw[:, 0:n_num]
        data.frequency  = data.frequency[:, 0:n_num]
        data.freq_step  = data.freq_step[:, 0:n_num]
        data.freq_width = data.freq_width[:, 0:n_num]
        print("Mode: Ver.1")

    # Background / CAL only
    n_time = data.EuEu.shape[0];  n_freq = data.EuEu.shape[1]
    print("  org:", data.EuEu.shape, n_time, "x", n_freq, "[", n_time*n_freq, "]")
    N_ch0 = data.U_selected + data.V_selected + data.W_selected
    if cal_mode < 2 or N_ch < 4 or comp_mode < 4:
        if cal_mode < 2:
            if N_ch < 4:
                if comp_mode < 4:
                    index = np.where( (data.cal_signal == cal_mode) & (N_ch0 == N_ch) & (comp_mode == data.complex) )
                else:
                    index = np.where( (data.cal_signal == cal_mode) & (N_ch0 == N_ch)                               )
            else:
                if comp_mode < 4:
                    index = np.where( (data.cal_signal == cal_mode) &                   (comp_mode == data.complex) )
                else:
                    index = np.where( (data.cal_signal == cal_mode)                                                 )
        else:
            if N_ch < 4:
                if comp_mode < 4:
                    index = np.where(                                 (N_ch0 == N_ch) & (comp_mode == data.complex) )
                else:
                    index = np.where(                                 (N_ch0 == N_ch)                               )
            else:
                index     = np.where(                                                   (comp_mode == data.complex) )
        # AUX
        data.U_selected  = data.U_selected[index[0]];  data.V_selected  = data.V_selected[index[0]];  data.W_selected  = data.W_selected[index[0]]
        data.complex     = data.complex[index[0]]
        #
        data.cal_signal  = data.cal_signal[index[0]]
        data.sweep_table = data.sweep_table[index[0]]
        data.onboard_cal = data.onboard_cal[index[0]]
        data.BG_subtract = data.BG_subtract[index[0]]
        data.BG_select   = data.BG_select[index[0]]
        data.FFT_window  = data.FFT_window[index[0]]
        data.RFI_rejection = data.RFI_rejection[index[0]]
        data.Pol_sep_thres = data.Pol_sep_thres[index[0]]
        data.Pol_sep_SW  = data.Pol_sep_SW[index[0]]
        data.overflow_U  = data.overflow_U[index[0]]
        data.overflow_V  = data.overflow_V[index[0]]
        data.overflow_W  = data.overflow_W[index[0]]
        data.proc_param0 = data.proc_param0[index[0]];  data.proc_param1 = data.proc_param1[index[0]]
        data.proc_param2 = data.proc_param2[index[0]];  data.proc_param3 = data.proc_param3[index[0]]
        data.BG_downlink = data.BG_downlink[index[0]]
        data.N_block     = data.N_block[index[0]]
        data.T_RWI_CH1   = data.T_RWI_CH1[index[0]]
        data.T_RWI_CH2   = data.T_RWI_CH2[index[0]]
        data.T_HF_FPGA   = data.T_HF_FPGA[index[0]]
        # Header
        data.N_samp      = data.N_samp[index[0]]
        data.N_step      = data.N_step[index[0]]
        data.decimation  = data.decimation[index[0]]
        data.pol         = data.pol[index[0]]
        data.B0_startf   = data.B0_startf[index[0]];  data.B0_stopf  = data.B0_stopf[index[0]];  data.B0_step = data.B0_step[index[0]]
        data.B0_repeat   = data.B0_repeat[index[0]];  data.B0_subdiv = data.B0_subdiv[index[0]]
        data.B1_startf   = data.B1_startf[index[0]];  data.B1_stopf  = data.B1_stopf[index[0]];  data.B1_step = data.B1_step[index[0]]
        data.B1_repeat   = data.B1_repeat[index[0]];  data.B1_subdiv = data.B1_subdiv[index[0]]
        data.B2_startf   = data.B2_startf[index[0]];  data.B2_stopf  = data.B2_stopf[index[0]];  data.B2_step = data.B2_step[index[0]]
        data.B2_repeat   = data.B2_repeat[index[0]];  data.B2_subdiv = data.B2_subdiv[index[0]]
        data.B3_startf   = data.B3_startf[index[0]];  data.B3_stopf  = data.B3_stopf[index[0]];  data.B3_step = data.B3_step[index[0]]
        data.B3_repeat   = data.B3_repeat[index[0]];  data.B3_subdiv = data.B3_subdiv[index[0]]
        data.B4_startf   = data.B4_startf[index[0]];  data.B4_stopf  = data.B4_stopf[index[0]];  data.B4_step = data.B4_step[index[0]]
        data.B4_repeat   = data.B4_repeat[index[0]];  data.B4_subdiv = data.B4_subdiv[index[0]]
        # Data
        data.epoch       = data.epoch[index[0]]
        data.scet        = data.scet[index[0]]
        data.frequency   = data.frequency[index[0]]
        data.freq_step   = data.freq_step[index[0]]
        data.freq_width  = data.freq_width[index[0]]
        # complex < 2:     # Power
        data.EuEu        = data.EuEu[index[0]];       data.EvEv       = data.EvEv[index[0]];       data.EwEw       = data.EwEw[index[0]]
        # complex == 1:    # Matrix
        data.EuEv_re     = data.EuEv_re[index[0]];    data.EvEw_re    = data.EvEw_re[index[0]];    data.EwEu_re    = data.EwEu_re[index[0]]
        data.EuEv_im     = data.EuEv_im[index[0]];    data.EvEw_im    = data.EvEw_im[index[0]];    data.EwEu_im    = data.EwEu_im[index[0]]
        # complex == 2:    # Matrix - N/R/L-separated
        data.EuEu_NC     = data.EuEu_NC[index[0]];    data.EvEv_NC    = data.EvEv_NC[index[0]];    data.EwEw_NC    = data.EwEw_NC[index[0]]
        data.EuEv_re_NC  = data.EuEv_re_NC[index[0]]; data.EvEw_re_NC = data.EvEw_re_NC[index[0]]; data.EwEu_re_NC = data.EwEu_re_NC[index[0]]
        data.EuEv_im_NC  = data.EuEv_im_NC[index[0]]; data.EvEw_im_NC = data.EvEw_im_NC[index[0]]; data.EwEu_im_NC = data.EwEu_im_NC[index[0]]
        #
        data.EuEu_RC     = data.EuEu_RC[index[0]];    data.EvEv_RC    = data.EvEv_RC[index[0]];    data.EwEw_RC    = data.EwEw_RC[index[0]]
        data.EuEv_re_RC  = data.EuEv_re_RC[index[0]]; data.EvEw_re_RC = data.EvEw_re_RC[index[0]]; data.EwEu_re_RC = data.EwEu_re_RC[index[0]]
        data.EuEv_im_RC  = data.EuEv_im_RC[index[0]]; data.EvEw_im_RC = data.EvEw_im_RC[index[0]]; data.EwEu_im_RC = data.EwEu_im_RC[index[0]]
        #
        data.EuEu_LC     = data.EuEu_LC[index[0]];    data.EvEv_LC    = data.EvEv_LC[index[0]];    data.EwEw_LC    = data.EwEw_LC[index[0]]
        data.EuEv_re_LC  = data.EuEv_re_LC[index[0]]; data.EvEw_re_LC = data.EvEw_re_LC[index[0]]; data.EwEu_re_LC = data.EwEu_re_LC[index[0]]
        data.EuEv_im_LC  = data.EuEv_im_LC[index[0]]; data.EvEw_im_LC = data.EvEw_im_LC[index[0]]; data.EwEu_im_LC = data.EwEu_im_LC[index[0]]
        #
        data.num_NC      = data.num_NC[index[0]];     data.num_RC     = data.num_RC[index[0]];     data.num_LC     = data.num_LC[index[0]]
        # complex == 3:    # 3D-matrix
        data.EuiEui      = data.EuiEui[index[0]];     data.EuqEuq     = data.EuqEuq[index[0]]
        data.EviEvi      = data.EviEvi[index[0]];     data.EvqEvq     = data.EvqEvq[index[0]]
        data.EwiEwi      = data.EwiEwi[index[0]];     data.EwqEwq     = data.EwqEwq[index[0]]
        #
        data.EuiEvi      = data.EuiEvi[index[0]];     data.EviEwi     = data.EviEwi[index[0]]
        data.EwiEui      = data.EwiEui[index[0]];     data.EuqEvq     = data.EuqEvq[index[0]]
        data.EvqEwq      = data.EvqEwq[index[0]];     data.EwqEuq     = data.EwqEuq[index[0]]
        #
        data.EuiEvq      = data.EuiEvq[index[0]];     data.EuqEvi     = data.EuqEvi[index[0]]
        data.EviEwq      = data.EviEwq[index[0]];     data.EvqEwi     = data.EvqEwi[index[0]]
        data.EwiEuq      = data.EwiEuq[index[0]];     data.EwqEui     = data.EwqEui[index[0]]
        #
        data.EuiEuq      = data.EuiEuq[index[0]];     data.EviEvq     = data.EviEvq[index[0]];     data.EwiEwq     = data.EwiEwq[index[0]]
        #
        data.BG_Eu       = data.BG_Eu[index[0]];      data.BG_Ev      = data.BG_Ev[index[0]];      data.BG_Ew      = data.BG_Ew[index[0]]

        n_time = data.EuEu.shape[0]
        if cal_mode < 2:
            if N_ch < 4:
                if comp_mode < 4:
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch, " comp_mode:", comp_mode)
                else:
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch)
            else:
                if comp_mode < 4:
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " comp_mode:", comp_mode)
                else:
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode)
        else:
            if N_ch < 4:
                if comp_mode < 4:
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> N_ch:", N_ch, " comp_mode:", comp_mode)
                else:
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> N_ch:", N_ch)
            else:
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> comp_mode:", comp_mode)

    # complex-2&3 data ==> complex-1 data ***
    for i in range(n_time):
        if data.complex[i] == 2: # Matrix - N/R/L-separated
            for j in range(n_freq):
                if   data.Pol_sep_SW[i] == 0:
                    flux_NC = data.EuEu_NC[i][j] + data.EvEv_NC[i][j];  flux_RC = data.EuEu_RC[i][j] + data.EvEv_RC[i][j];  flux_LC = data.EuEu_LC[i][j] + data.EvEv_LC[i][j]
                elif data.Pol_sep_SW[i] == 1:
                    flux_NC = data.EvEv_NC[i][j] + data.EwEw_NC[i][j];  flux_RC = data.EvEv_RC[i][j] + data.EwEw_RC[i][j];  flux_LC = data.EvEv_LC[i][j] + data.EwEw_LC[i][j]
                else:
                    flux_NC = data.EwEw_NC[i][j] + data.EuEu_NC[i][j];  flux_RC = data.EwEw_RC[i][j] + data.EuEu_RC[i][j];  flux_LC = data.EwEw_LC[i][j] + data.EuEu_LC[i][j]
                if   flux_NC >= flux_RC and flux_NC >= flux_LC:
                    data.EuEu[i][j]    = data.EuEu_NC[i][j];     data.EvEv[i][j]    = data.EvEv_NC[i][j];     data.EwEw[i][j]    = data.EwEw_NC[i][j]
                    data.EuEv_re[i][j] = data.EuEv_re_NC[i][j];  data.EvEw_re[i][j] = data.EvEw_re_NC[i][j];  data.EwEu_re[i][j] = data.EwEu_re_NC[i][j]
                    data.EuEv_im[i][j] = data.EuEv_im_NC[i][j];  data.EvEw_im[i][j] = data.EvEw_im_NC[i][j];  data.EwEu_im[i][j] = data.EwEu_im_NC[i][j]
                elif flux_RC >= flux_NC and flux_RC >= flux_LC:
                    data.EuEu[i][j]    = data.EuEu_RC[i][j];     data.EvEv[i][j]    = data.EvEv_RC[i][j];     data.EwEw[i][j]    = data.EwEw_RC[i][j]
                    data.EuEv_re[i][j] = data.EuEv_re_RC[i][j];  data.EvEw_re[i][j] = data.EvEw_re_RC[i][j];  data.EwEu_re[i][j] = data.EwEu_re_RC[i][j]
                    data.EuEv_im[i][j] = data.EuEv_im_RC[i][j];  data.EvEw_im[i][j] = data.EvEw_im_RC[i][j];  data.EwEu_im[i][j] = data.EwEu_im_RC[i][j]
                else:
                    data.EuEu[i][j]    = data.EuEu_LC[i][j];     data.EvEv[i][j]    = data.EvEv_LC[i][j];     data.EwEw[i][j]    = data.EwEw_LC[i][j]
                    data.EuEv_re[i][j] = data.EuEv_re_LC[i][j];  data.EvEw_re[i][j] = data.EvEw_re_LC[i][j];  data.EwEu_re[i][j] = data.EwEu_re_LC[i][j]
                    data.EuEv_im[i][j] = data.EuEv_im_LC[i][j];  data.EvEw_im[i][j] = data.EvEw_im_LC[i][j];  data.EwEu_im[i][j] = data.EwEu_im_LC[i][j]
        if data.complex[i] == 3:
            data.EuEu[i]    =  data.EuiEui[i] + data.EuqEuq[i];  data.EvEv[i]    =  data.EviEvi[i] + data.EvqEvq[i];  data.EwEw[i]    =  data.EwiEwi[i] + data.EwqEwq[i]
            data.EuEv_re[i] =  data.EuiEvi[i] + data.EuqEvq[i];  data.EvEw_re[i] =  data.EviEwi[i] + data.EvqEwq[i];  data.EwEu_re[i] =  data.EwiEui[i] + data.EwqEuq[i]
            data.EuEv_im[i] = -data.EuiEvq[i] + data.EuqEvi[i];  data.EvEw_im[i] = -data.EviEwq[i] + data.EviEvq[i];  data.EwEu_im[i] = -data.EwiEuq[i] + data.EwqEui[i]

    """
    # STOKES
    # *** all
    data.E_Iuv,   data.E_Quv,   data.E_Uuv,   data.E_Vuv   = juice_spec.get_stokes(data.EuEu, data.EvEv, data.EuEv_re, data.EuEv_im)
    data.E_Ivw,   data.E_Qvw,   data.E_Uvw,   data.E_Vvw   = juice_spec.get_stokes(data.EvEv, data.EwEw, data.EvEw_re, data.EvEw_im)
    data.E_Iwu,   data.E_Qwu,   data.E_Uwu,   data.E_Vwu   = juice_spec.get_stokes(data.EwEw, data.EuEu, data.EwEu_re, data.EwEu_im)
    data.E_DoPuv, data.E_DoLuv, data.E_DoCuv, data.E_ANGuv = juice_spec.get_pol(data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv)
    data.E_DoPvw, data.E_DoLvw, data.E_DoCvw, data.E_ANGvw = juice_spec.get_pol(data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw)
    data.E_DoPwu, data.E_DoLwu, data.E_DoCwu, data.E_ANGwu = juice_spec.get_pol(data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu)
    # *** NC
    data.E_Iuv_NC,   data.E_Quv_NC,   data.E_Uuv_NC,   data.E_Vuv_NC   = juice_spec.get_stokes(data.EuEu_NC, data.EvEv_NC, data.EuEv_re_NC, data.EuEv_im_NC)
    data.E_Ivw_NC,   data.E_Qvw_NC,   data.E_Uvw_NC,   data.E_Vvw_NC   = juice_spec.get_stokes(data.EvEv_NC, data.EwEw_NC, data.EvEw_re_NC, data.EvEw_im_NC)
    data.E_Iwu_NC,   data.E_Qwu_NC,   data.E_Uwu_NC,   data.E_Vwu_NC   = juice_spec.get_stokes(data.EwEw_NC, data.EuEu_NC, data.EwEu_re_NC, data.EwEu_im_NC)
    data.E_DoPuv_NC, data.E_DoLuv_NC, data.E_DoCuv_NC, data.E_ANGuv_NC = juice_spec.get_pol(data.E_Iuv_NC, data.E_Quv_NC, data.E_Uuv_NC, data.E_Vuv_NC)
    data.E_DoPvw_NC, data.E_DoLvw_NC, data.E_DoCvw_NC, data.E_ANGvw_NC = juice_spec.get_pol(data.E_Ivw_NC, data.E_Qvw_NC, data.E_Uvw_NC, data.E_Vvw_NC)
    data.E_DoPwu_NC, data.E_DoLwu_NC, data.E_DoCwu_NC, data.E_ANGwu_NC = juice_spec.get_pol(data.E_Iwu_NC, data.E_Qwu_NC, data.E_Uwu_NC, data.E_Vwu_NC)
    # *** RC
    data.E_Iuv_RC,   data.E_Quv_RC,   data.E_Uuv_RC,   data.E_Vuv_RC   = juice_spec.get_stokes(data.EuEu_RC, data.EvEv_RC, data.EuEv_re_RC, data.EuEv_im_RC)
    data.E_Ivw_RC,   data.E_Qvw_RC,   data.E_Uvw_RC,   data.E_Vvw_RC   = juice_spec.get_stokes(data.EvEv_RC, data.EwEw_RC, data.EvEw_re_RC, data.EvEw_im_RC)
    data.E_Iwu_RC,   data.E_Qwu_RC,   data.E_Uwu_RC,   data.E_Vwu_RC   = juice_spec.get_stokes(data.EwEw_RC, data.EuEu_RC, data.EwEu_re_RC, data.EwEu_im_RC)
    data.E_DoPuv_RC, data.E_DoLuv_RC, data.E_DoCuv_RC, data.E_ANGuv_RC = juice_spec.get_pol(data.E_Iuv_RC, data.E_Quv_RC, data.E_Uuv_RC, data.E_Vuv_RC)
    data.E_DoPvw_RC, data.E_DoLvw_RC, data.E_DoCvw_RC, data.E_ANGvw_RC = juice_spec.get_pol(data.E_Ivw_RC, data.E_Qvw_RC, data.E_Uvw_RC, data.E_Vvw_RC)
    data.E_DoPwu_RC, data.E_DoLwu_RC, data.E_DoCwu_RC, data.E_ANGwu_RC = juice_spec.get_pol(data.E_Iwu_RC, data.E_Qwu_RC, data.E_Uwu_RC, data.E_Vwu_RC)
    # *** LC
    data.E_Iuv_LC,   data.E_Quv_LC,   data.E_Uuv_LC,   data.E_Vuv_LC   = juice_spec.get_stokes(data.EuEu_LC, data.EvEv_LC, data.EuEv_re_LC, data.EuEv_im_LC)
    data.E_Ivw_LC,   data.E_Qvw_LC,   data.E_Uvw_LC,   data.E_Vvw_LC   = juice_spec.get_stokes(data.EvEv_LC, data.EwEw_LC, data.EvEw_re_LC, data.EvEw_im_LC)
    data.E_Iwu_LC,   data.E_Qwu_LC,   data.E_Uwu_LC,   data.E_Vwu_LC   = juice_spec.get_stokes(data.EwEw_LC, data.EuEu_LC, data.EwEu_re_LC, data.EwEu_im_LC)
    data.E_DoPuv_LC, data.E_DoLuv_LC, data.E_DoCuv_LC, data.E_ANGuv_LC = juice_spec.get_pol(data.E_Iuv_LC, data.E_Quv_LC, data.E_Uuv_LC, data.E_Vuv_LC)
    data.E_DoPvw_LC, data.E_DoLvw_LC, data.E_DoCvw_LC, data.E_ANGvw_LC = juice_spec.get_pol(data.E_Ivw_LC, data.E_Qvw_LC, data.E_Uvw_LC, data.E_Vvw_LC)
    data.E_DoPwu_LC, data.E_DoLwu_LC, data.E_DoCwu_LC, data.E_ANGwu_LC = juice_spec.get_pol(data.E_Iwu_LC, data.E_Qwu_LC, data.E_Uwu_LC, data.E_Vwu_LC)
    # *** 3D
    data.E_I_3d = data.EuiEui + data.EuqEuq + data.EviEvi + data.EvqEvq + data.EwiEwi + data.EwqEwq
    data.E_Q_3d = data.EuiEvi - data.EuqEuq + data.EviEvi - data.EvqEvq + data.EwiEwi - data.EwqEwq
    data.E_U_3d = 2. * (data.EuiEuq + data.EviEvq + data.EwiEwq)
    data.E_Vu_3d = -2. * (data.EviEwq - data.EvqEwi)
    data.E_Vv_3d = -2. * (data.EwiEuq - data.EwqEui)
    data.E_Vw_3d = -2. * (data.EuiEvq - data.EuqEvi)
    data.E_DoP_3d, data.E_DoL_3d, data.E_DoC_3d, data.E_ANG_3d, data.E_k_lon, data.E_k_lat = \
        juice_spec.get_pol_3D(data.E_I_3d, data.E_Q_3d, data.E_U_3d, data.E_Vu_3d, data.E_Vv_3d, data.E_Vw_3d)
    """

    # *** TMP: fill NaN
    """
    for i in range(n_time0):
        if data.EuEu[i][0]    < -1e20: 
            data.EuEu[i]    = math.nan;  data.EuEv_re[i]    = math.nan;  data.EuEv_im[i]    = math.nan;  data.EwEu_re[i]    = math.nan;  data.EwEu_im[i]    = math.nan
        if data.EvEv[i][0]    < -1e20: 
            data.EvEv[i]    = math.nan;  data.EuEv_re[i]    = math.nan;  data.EuEv_im[i]    = math.nan;  data.EvEw_re[i]    = math.nan;  data.EvEw_im[i]    = math.nan
        if data.EwEw[i][0]    < -1e20:
            data.EwEw[i]    = math.nan;  data.EvEw_re[i]    = math.nan;  data.EvEw_im[i]    = math.nan;  data.EwEu_re[i]    = math.nan;  data.EwEu_im[i]    = math.nan
        if data.EuEu_NC[i][0] < -1e20: 
            data.EuEu_NC[i] = math.nan;  data.EuEv_re_NC[i] = math.nan;  data.EuEv_im_NC[i] = math.nan;  data.EwEu_re_NC[i] = math.nan;  data.EwEu_im_NC[i] = math.nan
        if data.EvEv_NC[i][0] < -1e20: 
            data.EvEv_NC[i] = math.nan;  data.EuEv_re_NC[i] = math.nan;  data.EuEv_im_NC[i] = math.nan;  data.EvEw_re_NC[i] = math.nan;  data.EvEw_im_NC[i] = math.nan
        if data.EwEw_NC[i][0] < -1e20:
            data.EwEw_NC[i] = math.nan;  data.EvEw_re_NC[i] = math.nan;  data.EvEw_im_NC[i] = math.nan;  data.EwEu_re_NC[i] = math.nan;  data.EwEu_im_NC[i] = math.nan
        if data.EuEu_RC[i][0] < -1e20: 
            data.EuEu_RC[i] = math.nan;  data.EuEv_re_RC[i] = math.nan;  data.EuEv_im_RC[i] = math.nan;  data.EwEu_re_RC[i] = math.nan;  data.EwEu_im_RC[i] = math.nan
        if data.EvEv_RC[i][0] < -1e20: 
            data.EvEv_RC[i] = math.nan;  data.EuEv_re_RC[i] = math.nan;  data.EuEv_im_RC[i] = math.nan;  data.EvEw_re_RC[i] = math.nan;  data.EvEw_im_RC[i] = math.nan
        if data.EwEw_RC[i][0] < -1e20:
            data.EwEw_RC[i] = math.nan;  data.EvEw_re_RC[i] = math.nan;  data.EvEw_im_RC[i] = math.nan;  data.EwEu_re_RC[i] = math.nan;  data.EwEu_im_RC[i] = math.nan
        if data.EuEu_LC[i][0] < -1e20: 
            data.EuEu_LC[i] = math.nan;  data.EuEv_re_LC[i] = math.nan;  data.EuEv_im_LC[i] = math.nan;  data.EwEu_re_LC[i] = math.nan;  data.EwEu_im_LC[i] = math.nan
        if data.EvEv_LC[i][0] < -1e20: 
            data.EvEv_LC[i] = math.nan;  data.EuEv_re_LC[i] = math.nan;  data.EuEv_im_LC[i] = math.nan;  data.EvEw_re_LC[i] = math.nan;  data.EvEw_im_LC[i] = math.nan
        if data.EwEw_LC[i][0] < -1e20:
            data.EwEw_LC[i] = math.nan;  data.EvEw_re_LC[i] = math.nan;  data.EvEw_im_LC[i] = math.nan;  data.EwEu_re_LC[i] = math.nan;  data.EwEu_im_LC[i] = math.nan
    """

    # *** frequncy & width for spec cal
    data.freq   = data.frequency
    data.freq_w = data.freq_width
    return data


# [MEMO: ASW1 data]  *** Flight - Ver.1
# *** Flight - Ver. 1 ***
"""
data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/2023/'        # CDF data folder

# *** 2023/4/20 before deployment of MAG-BOOM
data_name_list = ['04/20/SID3_20230420T103558-20230420T103800.cdf']

# *** 2023/5/23 before deployment of RWI
data_name_list = ['05/23/SID3_20230523T090033-20230523T091021.cdf',
                  '05/23/SID3_20230523T092629-20230523T093617.cdf',
                  '05/23/SID3_20230523T095226-20230523T100214.cdf',
                  '05/23/SID3_20230523T102036-20230523T102247.cdf',
                 ]
# *** 2023/5/23 after X deployment of RWI
data_name_list = ['05/23/SID3_20230523T102431-20230523T102647.cdf',
                  '05/23/SID3_20230523T104536-20230523T104747.cdf',
                 ]
# *** 2023/5/23 after Z deployment of RWI
data_name_list = ['05/23/SID3_20230523T104931-20230523T105148.cdf',
                  '05/23/SID3_20230523T110537-20230523T110749.cdf',
                 ]
# *** 2023/5/23 after Y deployment of RWI
data_name_list = ['05/23/SID3_20230523T110933-20230523T111149.cdf']

# *** 2023/5/23 background
data_name_list = ['05/23/SID3_20230523T121538-20230523T122526.cdf',
                  '05/23/SID3_20230523T124134-20230523T125122.cdf',
                  '05/23/SID3_20230523T125738-20230523T130726.cdf',
                 ]
"""

"""
# *** 20230525 
data_name_list = ['05/25/SID3_20230525T130149-20230525T131137.cdf',
                  '05/25/SID3_20230525T150435-20230525T151423.cdf',
                  '05/25/SID3_20230525T165313-20230525T170301.cdf',
                 ]

# *** ALL ***
data_name_list = ['04/20/SID3_20230420T103558-20230420T103800.cdf',
                  '05/23/SID3_20230523T090033-20230523T091021.cdf',
                  '05/23/SID3_20230523T092629-20230523T093617.cdf',
                  '05/23/SID3_20230523T095226-20230523T100214.cdf',
                  '05/23/SID3_20230523T102036-20230523T102247.cdf',
                  '05/23/SID3_20230523T102431-20230523T102647.cdf',
                  '05/23/SID3_20230523T104536-20230523T104747.cdf',
                  '05/23/SID3_20230523T104931-20230523T105148.cdf',
                  '05/23/SID3_20230523T110537-20230523T110749.cdf',
                  '05/23/SID3_20230523T110933-20230523T111149.cdf',
                  '05/23/SID3_20230523T121538-20230523T122526.cdf',
                  '05/23/SID3_20230523T124134-20230523T125122.cdf',
                  '05/23/SID3_20230523T125738-20230523T130726.cdf',
                  '05/25/SID3_20230525T130149-20230525T131137.cdf',
                  '05/25/SID3_20230525T150435-20230525T151423.cdf',
                  '05/25/SID3_20230525T165313-20230525T170301.cdf',
                 ]
"""

# [MEMO: ASW1 data]  *** Ground Test - Ver.1 ***
# *** Ground Test - Ver.1 ***
"""
# *** 202105
data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202105/'        # CDF data folder
data_name_list = ['SID3_20210531_SCPFM_PTR_RPWI_2_day4_xid32813.cdf']
data_name_list = ['SID3_20210531_SCPFM_PTR_RPWI_2_day5_xid32814.cdf']

# *** 202106 ***
data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202106/'        # CDF data folder
data_name_list = ['SID3_SCTBTV_Phase3_xid32776.cdf']
data_name_list = ['SID3_SCTBTV_Phase5_xid32794.cdf']
data_name_list = ['SID3_SCTBTV_Phase11_xid32836.cdf']
data_name_list = ['SID3_SCTBTV_Phase13_xid32848.cdf']
                  
# *** 202111 ***
data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202111/'        # CDF data folder
data_name_list = ['SID3_SCPFM_PTR_RPWI_delta.RPWI_SCM_TEST_xid32816.cdf',
                  'SID3_SCPFM_PTR_RPWI_delta.RPWI_SCM_TEST_xid32817.cdf',
                  'SID3_SCPFM_PTR_RPWI_delta.RPWI_SCM_TEST_xid32818.cdf',
                 ]

# *** 202204 ***
data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202204/'        # CDF data folder
data_name_list = ['SID3_20220400_SCPFM_EMCR.Phase4_xid32994.cdf',
                  'SID3_20220400_SCPFM_EMCR.Phase4_xid32995.cdf',
                  'SID3_20220400_SCPFM_EMCR.Phase4_xid32996.cdf',
                  'SID3_20220400_SCPFM_EMCR.Phase4_xid32997.cdf',
                  'SID3_20220400_SCPFM_EMCR.Phase4_xid32998.cdf',
                  'SID3_20220400_SCPFM_EMCR.Phase4_xid32999.cdf',
                  'SID3_20220400_SCPFM_EMCR.Phase4_xid33000.cdf',
                  'SID3_20220400_SCPFM_EMCR.Phase4_xid33001.cdf',
                  'SID3_20220400_SCPFM_EMCR.Phase4_xid33002.cdf',
                  'SID3_20220400_SCPFM_EMCR.Phase4_xid33003.cdf',
                  'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32798.cdf',
                  'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32799.cdf',
                  'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32800.cdf',
                  'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32801.cdf',
                  'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32802.cdf',
                  'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32803.cdf',
                  'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32804.cdf',
                 ] 
                
# *** 202211 ***
data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202211/'        # CDF data folder
data_name_list = ['SID3_20221115_Mission_Test_GCO500_1RPR_4.cdf',
                  'SID3_20221115_Mission_Test_GCO500_1RPR_6.cdf',
                  ]

# *** 202301 ***
data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202301/'        # CDF data folder
data_name_list = ['SID3_20230113_Mission_Test_CSW3.2.1_SCOP020_1RPR_4.cdf',
                  'SID3_20230113_Mission_Test_CSW3.2.1_SCOP020_1RPR_6.cdf',
                  ]
"""