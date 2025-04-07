"""
    JUICE RPWI HF SID4 & 20: L1a QL -- 2025/4/6
"""
import numpy as np
import math

class struct:
    pass

# ---------------------------------------------------------------------
# --- SID20 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid20_read(cdf, sid, RPWI_FSW_version):
    """
    input:  cdf, sid, FSW version
    return: data
    """
    data = struct()
    data.RPWI_FSW_version = RPWI_FSW_version

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
    data.proc_param0 = cdf['proc_param0'][...];  data.proc_param1 = cdf['proc_param1'][...]
    data.proc_param2 = cdf['proc_param2'][...];  data.proc_param3 = cdf['proc_param3'][...]
    data.BG_downlink = cdf['BG_downlink'][...]
    data.N_block     = np.int64(cdf['N_block'][...])
    data.Rich_flag   = np.int64(cdf['Rich_data_flag'][...])
    data.T_RWI_CH1   = np.float64(cdf['T_RWI_CH1'][...])    
    data.T_RWI_CH2   = np.float64(cdf['T_RWI_CH2'][...])  
    data.T_HF_FPGA   = np.float64(cdf['T_HF_FPGA'][...])

    # Header
    data.N_samp      = np.int64(cdf['N_samp'][...])
    data.N_step      = np.int64(cdf['N_step'][...])
    data.decimation  = cdf['decimation'][...];   data.pol       = cdf['pol'][...]
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...];   data.ISW_ver   = cdf['ISW_ver'][...]
    data.B0_startf   = cdf['B0_startf'][...];    data.B0_stopf  = cdf['B0_stopf'][...];  data.B0_step = cdf['B0_step'][...]
    data.B0_repeat   = cdf['B0_repeat'][...];    data.B0_subdiv = cdf['B0_subdiv'][...]
    if (sid==20):
        data.B1_startf = cdf['B1_startf'][...];  data.B1_stopf  = cdf['B1_stopf'][...];  data.B1_step = cdf['B1_step'][...]
        data.B1_repeat = cdf['B1_repeat'][...];  data.B1_subdiv = cdf['B1_subdiv'][...]
        data.B2_startf = cdf['B2_startf'][...];  data.B2_stopf  = cdf['B2_stopf'][...];  data.B2_step = cdf['B2_step'][...]
        data.B2_repeat = cdf['B2_repeat'][...];  data.B2_subdiv = cdf['B2_subdiv'][...]
        data.B3_startf = cdf['B3_startf'][...];  data.B3_stopf  = cdf['B3_stopf'][...];  data.B3_step = cdf['B3_step'][...]
        data.B3_repeat = cdf['B3_repeat'][...];  data.B3_subdiv = cdf['B3_subdiv'][...]
        data.B4_startf = cdf['B4_startf'][...];  data.B4_stopf  = cdf['B4_stopf'][...];  data.B4_step = cdf['B4_step'][...]
        data.B4_repeat = cdf['B4_repeat'][...];  data.B4_subdiv = cdf['B4_subdiv'][...]

    # Data
    data.frequency   = cdf['frequency'][...];    data.freq_step = cdf['freq_step'][...]; data.freq_width  = cdf['freq_width'][...]
    data.epoch       = cdf['Epoch'][...];        data.scet      = cdf['SCET'][...]
    # complex < 2:     # Power
    data.EuEu        = np.float64(cdf['EuEu'][...]);     data.EvEv    = np.float64(cdf['EvEv'][...]);     data.EwEw    = np.float64(cdf['EwEw'][...])
    # complex == 1:    # Matrix
    data.EuEv_re     = np.float64(cdf['EuEv_re'][...]);  data.EvEw_re = np.float64(cdf['EvEw_re'][...]);  data.EwEu_re = np.float64(cdf['EwEu_re'][...])
    data.EuEv_im     = np.float64(cdf['EuEv_im'][...]);  data.EvEw_im = np.float64(cdf['EvEw_im'][...]);  data.EwEu_im = np.float64(cdf['EwEu_im'][...])
    # complex == 3:    # 3D-matrix
    data.EuiEui      = np.float64(cdf['EuiEui'][...]);   data.EuqEuq  = np.float64(cdf['EuqEuq'][...])
    data.EviEvi      = np.float64(cdf['EviEvi'][...]);   data.EvqEvq  = np.float64(cdf['EvqEvq'][...])
    data.EwiEwi      = np.float64(cdf['EwiEwi'][...]);   data.EwqEwq  = np.float64(cdf['EwqEwq'][...])
    #
    data.EuiEvi      = np.float64(cdf['EuiEvi'][...]);   data.EviEwi  = np.float64(cdf['EviEwi'][...])
    data.EwiEui      = np.float64(cdf['EwiEui'][...]);   data.EuqEvq  = np.float64(cdf['EuqEvq'][...])
    data.EvqEwq      = np.float64(cdf['EvqEwq'][...]);   data.EwqEuq  = np.float64(cdf['EwqEuq'][...])
    #
    data.EuiEvq      = np.float64(cdf['EuiEvq'][...]);   data.EuqEvi  = np.float64(cdf['EuqEvi'][...])
    data.EviEwq      = np.float64(cdf['EviEwq'][...]);   data.EvqEwi  = np.float64(cdf['EvqEwi'][...])
    data.EwiEuq      = np.float64(cdf['EwiEuq'][...]);   data.EwqEui  = np.float64(cdf['EwqEui'][...])
    #
    data.EuiEuq      = np.float64(cdf['EuiEuq'][...]);   data.EviEvq  = np.float64(cdf['EviEvq'][...]);  data.EwiEwq = np.float64(cdf['EwiEwq'][...])
    return data


def hf_sid20_add(data, data1, sid):
    """
    input:  data, data1, sid
    return: data
    """
    # AUX
    data.U_selected  = np.r_["0", data.U_selected, data1.U_selected]
    data.V_selected  = np.r_["0", data.V_selected, data1.V_selected]
    data.W_selected  = np.r_["0", data.W_selected, data1.W_selected]
    data.complex     = np.r_["0", data.complex, data1.complex]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.sweep_table = np.r_["0", data.sweep_table, data1.sweep_table]
    data.onboard_cal = np.r_["0", data.onboard_cal, data1.onboard_cal]
    data.BG_subtract = np.r_["0", data.BG_subtract, data1.BG_subtract]
    data.BG_select   = np.r_["0", data.BG_select, data1.BG_select]
    data.FFT_window  = np.r_["0", data.FFT_window, data1.FFT_window]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    data.Pol_sep_thres = np.r_["0", data.Pol_sep_thres, data1.Pol_sep_thres]
    data.Pol_sep_SW  = np.r_["0", data.Pol_sep_SW, data1.Pol_sep_SW]
    #data.overflow_U  = np.r_["0", data.overflow_U, data1.overflow_U]
    #data.overflow_V  = np.r_["0", data.overflow_V, data1.overflow_V]
    #data.overflow_W  = np.r_["0", data.overflow_W, data1.overflow_W]
    data.proc_param0 = np.r_["0", data.proc_param0, data1.proc_param0]
    data.proc_param1 = np.r_["0", data.proc_param1, data1.proc_param1]
    data.proc_param2 = np.r_["0", data.proc_param2, data1.proc_param2]
    data.proc_param3 = np.r_["0", data.proc_param3, data1.proc_param3]
    data.BG_downlink = np.r_["0", data.BG_downlink, data1.BG_downlink]
    data.N_block     = np.r_["0", data.N_block, data1.N_block]
    data.Rich_flag   = np.r_["0", data.Rich_flag, data1.Rich_flag]
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.N_samp      = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step      = np.r_["0", data.N_step, data1.N_step]
    data.decimation  = np.r_["0", data.decimation, data1.decimation]
    data.pol         = np.r_["0", data.pol, data1.pol]
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver     = np.r_["0", data.ISW_ver, data1.ISW_ver]
    data.B0_startf   = np.r_["0", data.B0_startf, data1.B0_startf]
    data.B0_stopf    = np.r_["0", data.B0_stopf, data1.B0_stopf]
    data.B0_step     = np.r_["0", data.B0_step, data1.B0_step]
    data.B0_repeat   = np.r_["0", data.B0_repeat, data1.B0_repeat]
    data.B0_subdiv   = np.r_["0", data.B0_subdiv, data1.B0_subdiv]
    if (sid==20):
        data.B1_startf = np.r_["0", data.B1_startf, data1.B1_startf]
        data.B1_stopf  = np.r_["0", data.B1_stopf,  data1.B1_stopf]
        data.B1_step   = np.r_["0", data.B1_step,   data1.B1_step]
        data.B1_repeat = np.r_["0", data.B1_repeat, data1.B1_repeat]
        data.B1_subdiv = np.r_["0", data.B1_subdiv, data1.B1_subdiv]
        data.B2_startf = np.r_["0", data.B2_startf, data1.B2_startf]
        data.B2_stopf  = np.r_["0", data.B2_stopf,  data1.B2_stopf]
        data.B2_step   = np.r_["0", data.B2_step,   data1.B2_step]
        data.B2_repeat = np.r_["0", data.B2_repeat, data1.B2_repeat]
        data.B2_subdiv = np.r_["0", data.B2_subdiv, data1.B2_subdiv]
        data.B3_startf = np.r_["0", data.B3_startf, data1.B3_startf]
        data.B3_stopf  = np.r_["0", data.B3_stopf,  data1.B3_stopf]
        data.B3_step   = np.r_["0", data.B3_step,   data1.B3_step]
        data.B3_repeat = np.r_["0", data.B3_repeat, data1.B3_repeat]
        data.B3_subdiv = np.r_["0", data.B3_subdiv, data1.B3_subdiv]
        data.B4_startf = np.r_["0", data.B4_startf, data1.B4_startf]
        data.B4_stopf  = np.r_["0", data.B4_stopf,  data1.B4_stopf]
        data.B4_step   = np.r_["0", data.B4_step,   data1.B4_step]
        data.B4_repeat = np.r_["0", data.B4_repeat, data1.B4_repeat]
        data.B4_subdiv = np.r_["0", data.B4_subdiv, data1.B4_subdiv]
    # Data
    data.epoch       = np.r_["0", data.epoch,      data1.epoch]
    data.scet        = np.r_["0", data.scet,       data1.scet]
    data.frequency   = np.r_["0", data.frequency,  data1.frequency]
    data.freq_step   = np.r_["0", data.freq_step,  data1.freq_step]
    data.freq_width  = np.r_["0", data.freq_width, data1.freq_width]
    # complex < 2:     # Power
    data.EuEu        = np.r_["0", data.EuEu, data1.EuEu]
    data.EvEv        = np.r_["0", data.EvEv, data1.EvEv]
    data.EwEw        = np.r_["0", data.EwEw, data1.EwEw]
    # complex == 1:    # Matrix
    data.EuEv_re     = np.r_["0", data.EuEv_re, data1.EuEv_re];  data.EvEw_re = np.r_["0", data.EvEw_re, data1.EvEw_re]
    data.EwEu_re     = np.r_["0", data.EwEu_re, data1.EwEu_re];  data.EuEv_im = np.r_["0", data.EuEv_im, data1.EuEv_im]
    data.EvEw_im     = np.r_["0", data.EvEw_im, data1.EvEw_im];  data.EwEu_im = np.r_["0", data.EwEu_im, data1.EwEu_im]
    # complex == 3:    # 3D-matrix
    data.EuiEui      = np.r_["0", data.EuiEui, data1.EuiEui];    data.EuqEuq  = np.r_["0", data.EuqEuq, data1.EuqEuq]
    data.EviEvi      = np.r_["0", data.EviEvi, data1.EviEvi];    data.EvqEvq  = np.r_["0", data.EvqEvq, data1.EvqEvq]
    data.EwiEwi      = np.r_["0", data.EwiEwi, data1.EwiEwi];    data.EwqEwq  = np.r_["0", data.EwqEwq, data1.EwqEwq]
    #
    data.EuiEvi      = np.r_["0", data.EuiEvi, data1.EuiEvi];    data.EviEwi  = np.r_["0", data.EviEwi, data1.EviEwi]
    data.EwiEui      = np.r_["0", data.EwiEui, data1.EwiEui];    data.EuqEvq  = np.r_["0", data.EuqEvq, data1.EuqEvq]
    data.EvqEwq      = np.r_["0", data.EvqEwq, data1.EvqEwq];    data.EwqEuq  = np.r_["0", data.EwqEuq, data1.EwqEuq]
    #
    data.EuiEvq      = np.r_["0", data.EuiEvq, data1.EuiEvq];    data.EuqEvi  = np.r_["0", data.EuqEvi, data1.EuqEvi]
    data.EviEwq      = np.r_["0", data.EviEwq, data1.EviEwq];    data.EvqEwi  = np.r_["0", data.EvqEwi, data1.EvqEwi]
    data.EwiEuq      = np.r_["0", data.EwiEuq, data1.EwiEuq];    data.EwqEui  = np.r_["0", data.EwqEui, data1.EwqEui]
    #
    data.EuiEuq      = np.r_["0", data.EuiEuq, data1.EuiEuq]
    data.EviEvq      = np.r_["0", data.EviEvq, data1.EviEvq]
    data.EwiEwq      = np.r_["0", data.EwiEwq, data1.EwiEwq]
    return data


def hf_sid20_shaping(data, sid, cal_mode, N_ch, comp_mode):
    """
    input:  data, sid
            cal_mode    [Power]     0: background          1: CAL           2: all
            N_ch0       [channel]   2: 2-ch    3: 3-ch                   0,>3: any
            comp_mode   [Complex]   0: Poweer  1: Matrix   3: Matrix-2D    >3: any   
    return: data
    """
    # Size
    n_time = data.EuEu.shape[0];  n_freq = data.EuEu.shape[1]
    print("  org:", data.EuEu.shape, n_time, "x", n_freq, "[", n_time*n_freq, "]")
    if   data.EuEu.shape[1] != 72  and sid == 4:
        print("      [SID]", sid, "  *** size error ***", data.EuEu.shape[1], ", not 72")
    elif data.EuEu.shape[1] != 360 and sid == 20:
        print("      [SID]", sid, "  *** size error ***", data.EuEu.shape[1], ", not 360")
    else:
        print("  org:[SID]", sid, "  size:", data.EuEu.shape, n_time, "x", n_freq, "[", n_time*n_freq, "]")
    N_ch0 = data.U_selected + data.V_selected + data.W_selected
    if cal_mode < 2 or N_ch < 4 or comp_mode < 4:
        if cal_mode < 2:
            if N_ch < 4:
                if comp_mode < 4:
                    index = np.where( (data.cal_signal == cal_mode) & (N_ch0 == N_ch) & (comp_mode == data.complex) )
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch, " comp_mode:", comp_mode)
                else:
                    index = np.where( (data.cal_signal == cal_mode) & (N_ch0 == N_ch)                               )
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch)
            else:
                if comp_mode < 4:
                    index = np.where( (data.cal_signal == cal_mode) &                   (comp_mode == data.complex) )
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " comp_mode:", comp_mode)
                else:
                    index = np.where( (data.cal_signal == cal_mode)                                                 )
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode)
        else:
            if N_ch < 4:
                if comp_mode < 4:
                    index = np.where(                                 (N_ch0 == N_ch) & (comp_mode == data.complex) )
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> N_ch:", N_ch, " comp_mode:", comp_mode)
                else:
                    index = np.where(                                 (N_ch0 == N_ch)                               )
                    print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> N_ch:", N_ch)
            else:
                index     = np.where(                                                   (comp_mode == data.complex) )
                print(    "  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> comp_mode:", comp_mode)

        # AUX
        data.U_selected  = data.U_selected[index[0]];  data.V_selected  = data.V_selected[index[0]];  data.W_selected  = data.W_selected[index[0]]
        data.complex     = data.complex[index[0]]
        data.cal_signal  = data.cal_signal[index[0]]
        data.sweep_table = data.sweep_table[index[0]]
        data.onboard_cal = data.onboard_cal[index[0]]
        data.BG_subtract = data.BG_subtract[index[0]]
        data.BG_select   = data.BG_select [index[0]]
        data.FFT_window  = data.FFT_window[index[0]]
        data.RFI_rejection = data.RFI_rejection[index[0]]
        data.Pol_sep_thres = data.Pol_sep_thres[index[0]]
        data.Pol_sep_SW  = data.Pol_sep_SW[index[0]]
        #data.overflow_U  = data.overflow_U[index[0]]
        #data.overflow_V  = data.overflow_V[index[0]]
        #data.overflow_W  = data.overflow_W[index[0]]
        data.proc_param0 = data.proc_param0[index[0]];  data.proc_param1 = data.proc_param1[index[0]]
        data.proc_param2 = data.proc_param2[index[0]];  data.proc_param3 = data.proc_param3[index[0]]
        data.BG_downlink = data.BG_downlink[index[0]]
        data.N_block     = data.N_block    [index[0]]
        data.Rich_flag   = data.Rich_flag  [index[0]]
        data.T_RWI_CH1   = data.T_RWI_CH1 [index[0]]
        data.T_RWI_CH2   = data.T_RWI_CH2 [index[0]]
        data.T_HF_FPGA   = data.T_HF_FPGA [index[0]]
        # Header
        data.N_samp      = data.N_samp    [index[0]]
        data.N_step      = data.N_step    [index[0]]
        data.decimation  = data.decimation[index[0]]
        data.pol         = data.pol       [index[0]]
        data.ADC_ovrflw  = data.ADC_ovrflw[index[0]]
        data.ISW_ver     = data.ISW_ver   [index[0]]
        data.B0_startf   = data.B0_startf [index[0]];  data.B0_stopf   = data.B0_stopf[index[0]];  data.B0_step = data.B0_step[index[0]]
        data.B0_repeat   = data.B0_repeat [index[0]];  data.B0_subdiv  = data.B0_subdiv[index[0]]
        if (sid==20):
            data.B1_startf = data.B1_startf[index[0]];  data.B1_stopf  = data.B1_stopf[index[0]];  data.B1_step = data.B1_step[index[0]]
            data.B1_repeat = data.B1_repeat[index[0]];  data.B1_subdiv = data.B1_subdiv[index[0]]
            data.B2_startf = data.B2_startf[index[0]];  data.B2_stopf  = data.B2_stopf[index[0]];  data.B2_step = data.B2_step[index[0]]
            data.B2_repeat = data.B2_repeat[index[0]];  data.B2_subdiv = data.B2_subdiv[index[0]]
            data.B3_startf = data.B3_startf[index[0]];  data.B3_stopf  = data.B3_stopf[index[0]];  data.B3_step = data.B3_step[index[0]]
            data.B3_repeat = data.B3_repeat[index[0]];  data.B3_subdiv = data.B3_subdiv[index[0]]
            data.B4_startf = data.B4_startf[index[0]];  data.B4_stopf  = data.B4_stopf[index[0]];  data.B4_step = data.B4_step[index[0]]
            data.B4_repeat = data.B4_repeat[index[0]];  data.B4_subdiv = data.B4_subdiv[index[0]]
        # Data
        data.epoch       = data.epoch     [index[0]]
        data.scet        = data.scet      [index[0]]
        data.frequency   = data.frequency [index[0]]
        data.freq_step   = data.freq_step [index[0]]
        data.freq_width  = data.freq_width[index[0]]
        # complex < 2:     # Power
        data.EuEu        = data.EuEu      [index[0]]; data.EvEv       = data.EvEv      [index[0]]; data.EwEw       = data.EwEw      [index[0]]
        # complex == 1:    # Matrix
        data.EuEv_re     = data.EuEv_re   [index[0]]; data.EvEw_re    = data.EvEw_re   [index[0]]; data.EwEu_re    = data.EwEu_re   [index[0]]
        data.EuEv_im     = data.EuEv_im   [index[0]]; data.EvEw_im    = data.EvEw_im   [index[0]]; data.EwEu_im    = data.EwEu_im   [index[0]]
        # complex == 3:    # 3D-matrix
        data.EuiEui      = data.EuiEui    [index[0]]; data.EviEvi     = data.EviEvi    [index[0]]; data.EwiEwi     = data.EwiEwi    [index[0]]
        data.EuqEuq      = data.EuqEuq    [index[0]]; data.EvqEvq     = data.EvqEvq    [index[0]]; data.EwqEwq     = data.EwqEwq    [index[0]]
        data.EuiEvi      = data.EuiEvi    [index[0]]; data.EviEwi     = data.EviEwi    [index[0]]; data.EwiEui     = data.EwiEui    [index[0]]
        data.EuqEvq      = data.EuqEvq    [index[0]]; data.EvqEwq     = data.EvqEwq    [index[0]]; data.EwqEuq     = data.EwqEuq    [index[0]]
        data.EuiEvq      = data.EuiEvq    [index[0]]; data.EviEwq     = data.EviEwq    [index[0]]; data.EwiEuq     = data.EwiEuq    [index[0]]
        data.EuqEvi      = data.EuqEvi    [index[0]]; data.EvqEwi     = data.EvqEwi    [index[0]]; data.EwqEui     = data.EwqEui    [index[0]]
        data.EuiEuq      = data.EuiEuq    [index[0]]; data.EviEvq     = data.EviEvq    [index[0]]; data.EwiEwq     = data.EwiEwq    [index[0]]

        n_time = data.EuEu.shape[0]
        if cal_mode < 2:
            if N_ch < 4:
                if comp_mode < 4: print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch, " comp_mode:", comp_mode)
                else:             print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch)
            else:
                if comp_mode < 4: print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " comp_mode:", comp_mode)
                else:             print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode)
        else:
            if N_ch < 4:
                if comp_mode < 4: print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> N_ch:", N_ch, " comp_mode:", comp_mode)
                else:             print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> N_ch:", N_ch)
            else:                 print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> comp_mode:", comp_mode)
        if cal_mode == 0:         print("<only BG>")
        else:                     print("<only CAL>")

    # NAN
    index = np.where(data.complex == 0)
    data.EuEv_re   [index[0]] = math.nan; data.EvEw_re   [index[0]] = math.nan; data.EwEu_re   [index[0]] = math.nan
    data.EuEv_im   [index[0]] = math.nan; data.EvEw_im   [index[0]] = math.nan; data.EwEu_im   [index[0]] = math.nan
    #
    index = np.where(data.complex != 3)
    data.EuiEui    [index[0]] = math.nan; data.EviEvi    [index[0]] = math.nan; data.EwiEwi    [index[0]] = math.nan
    data.EuqEuq    [index[0]] = math.nan; data.EvqEvq    [index[0]] = math.nan; data.EwqEwq    [index[0]] = math.nan
    data.EuiEvi    [index[0]] = math.nan; data.EviEwi    [index[0]] = math.nan; data.EwiEui    [index[0]] = math.nan
    data.EuqEvq    [index[0]] = math.nan; data.EvqEwq    [index[0]] = math.nan; data.EwqEuq    [index[0]] = math.nan
    data.EuiEvq    [index[0]] = math.nan; data.EviEwq    [index[0]] = math.nan; data.EwiEuq    [index[0]] = math.nan
    data.EuqEvi    [index[0]] = math.nan; data.EvqEwi    [index[0]] = math.nan; data.EwqEui    [index[0]] = math.nan
    data.EuiEuq    [index[0]] = math.nan; data.EviEvq    [index[0]] = math.nan; data.EwiEwq    [index[0]] = math.nan
    #
    index = np.where(data.U_selected == 0) 
    data.EuEu      [index[0]] = math.nan
    data.EuEv_re   [index[0]] = math.nan; data.EwEu_re   [index[0]] = math.nan; data.EuEv_im   [index[0]] = math.nan; data.EwEu_im   [index[0]] = math.nan
    data.EuiEui    [index[0]] = math.nan; data.EuqEuq    [index[0]] = math.nan; data.EuiEuq    [index[0]] = math.nan
    data.EuiEvi    [index[0]] = math.nan; data.EwiEui    [index[0]] = math.nan; data.EuqEvq    [index[0]] = math.nan; data.EwqEuq    [index[0]] = math.nan
    data.EuiEvq    [index[0]] = math.nan; data.EwiEuq    [index[0]] = math.nan; data.EuqEvi    [index[0]] = math.nan; data.EwqEui    [index[0]] = math.nan
    index = np.where(data.V_selected == 0)
    data.EvEv      [index[0]] = math.nan
    data.EvEw_re   [index[0]] = math.nan; data.EwEu_re   [index[0]] = math.nan; data.EvEw_im   [index[0]] = math.nan; data.EwEu_im   [index[0]] = math.nan
    data.EviEvi    [index[0]] = math.nan; data.EvqEvq    [index[0]] = math.nan; data.EviEvq    [index[0]] = math.nan
    data.EuiEvi    [index[0]] = math.nan; data.EviEwi    [index[0]] = math.nan; data.EuqEvq    [index[0]] = math.nan; data.EvqEwq    [index[0]] = math.nan
    data.EuiEvq    [index[0]] = math.nan; data.EviEwq    [index[0]] = math.nan; data.EuqEvi    [index[0]] = math.nan; data.EvqEwi    [index[0]] = math.nan
    index = np.where(data.W_selected == 0)
    data.EwEw      [index[0]] = math.nan
    data.EvEw_re   [index[0]] = math.nan; data.EwEu_re   [index[0]] = math.nan; data.EvEw_im   [index[0]] = math.nan; data.EwEu_im   [index[0]] = math.nan
    data.EwiEwi    [index[0]] = math.nan; data.EwqEwq    [index[0]] = math.nan; data.EwiEwq    [index[0]] = math.nan
    data.EviEwi    [index[0]] = math.nan; data.EwiEui    [index[0]] = math.nan; data.EvqEwq    [index[0]] = math.nan; data.EwqEuq    [index[0]] = math.nan
    data.EviEwq    [index[0]] = math.nan; data.EwiEuq    [index[0]] = math.nan; data.EvqEwi    [index[0]] = math.nan; data.EwqEui    [index[0]] = math.nan

    # *** complex-3 data ==> complex-1 data ***
    for i in range(n_time):
        if data.complex[i] == 3:
            # TMP: "/2" ?
            data.EuEu[i]    =  data.EuiEui[i] + data.EuqEuq[i]; data.EvEv[i]    =  data.EviEvi[i] + data.EvqEvq[i]; data.EwEw[i]    =  data.EwiEwi[i] + data.EwqEwq[i]
            data.EuEv_re[i] =  data.EuiEvi[i] + data.EuqEvq[i]; data.EvEw_re[i] =  data.EviEwi[i] + data.EvqEwq[i]; data.EwEu_re[i] =  data.EwiEui[i] + data.EwqEuq[i]
            data.EuEv_im[i] = -data.EuiEvq[i] + data.EuqEvi[i]; data.EvEw_im[i] = -data.EviEwq[i] + data.EviEvq[i]; data.EwEu_im[i] = -data.EwiEuq[i] + data.EwqEui[i]

    # *** frequncy & width for spec cal
    data.freq   = data.frequency
    data.freq_w = data.freq_width
    return data


def spec_nan(data, i):
    data.EuEu      [i] = math.nan; data.EvEv      [i] = math.nan; data.EwEw      [i] = math.nan
    data.EuEv_re   [i] = math.nan; data.EvEw_re   [i] = math.nan; data.EwEu_re   [i] = math.nan
    data.EuEv_im   [i] = math.nan; data.EvEw_im   [i] = math.nan; data.EwEu_im   [i] = math.nan
    data.EuiEui    [i] = math.nan; data.EviEvi    [i] = math.nan; data.EwiEwi    [i] = math.nan
    data.EuqEuq    [i] = math.nan; data.EvqEvq    [i] = math.nan; data.EwqEwq    [i] = math.nan
    data.EuiEvi    [i] = math.nan; data.EviEwi    [i] = math.nan; data.EwiEui    [i] = math.nan
    data.EuqEvq    [i] = math.nan; data.EvqEwq    [i] = math.nan; data.EwqEuq    [i] = math.nan
    data.EuiEvq    [i] = math.nan; data.EviEwq    [i] = math.nan; data.EwiEuq    [i] = math.nan
    data.EuqEvi    [i] = math.nan; data.EvqEwi    [i] = math.nan; data.EwqEui    [i] = math.nan
    data.EuiEuq    [i] = math.nan; data.EviEvq    [i] = math.nan; data.EwiEwq    [i] = math.nan