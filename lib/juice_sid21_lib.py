"""
    JUICE RPWI HF SID21 (PSSR1 rich): L1a QL -- 2025/7/5
"""
import numpy as np
import math
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

    # Data
    data.EuEu    = np.float64(cdf['EuEu'][...]);     data.EvEv = np.float64(cdf['EvEv'][...]);        data.EwEw = np.float64(cdf['EwEw'][...])
    data.EuEv_re = np.float64(cdf['EuEv_re'][...]);  data.EuEv_im = np.float64(cdf['EuEv_im'][...])  
    data.EvEw_re = np.float64(cdf['EvEw_re'][...]);  data.EvEw_im = np.float64(cdf['EvEw_im'][...])  
    data.EwEu_re = np.float64(cdf['EwEu_re'][...]);  data.EwEu_im = np.float64(cdf['EwEu_im'][...])
    data.frequency  = cdf['frequency'][...];   data.freq_step = cdf['freq_step'][...]; data.freq_width = cdf['freq_width'][...]
    data.epoch      = cdf['Epoch'][...];       data.scet      = cdf['SCET'][...]
    # AUX
    data.complex     = cdf['complex'][...]
    data.ch_selected = cdf['ch_selected'][...]      # [0:U  1:V  2:W]
    data.cal_signal  = cdf['cal_signal'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    #
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    # Header
    data.N_step      = np.int64(cdf['N_step'][...])
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]
    data.ISW_ver     = cdf['ISW_ver'][...]

    return data


def hf_sid21_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.EuEu          = np.r_["0", data.EuEu, data1.EuEu]
    data.EvEv          = np.r_["0", data.EvEv, data1.EvEv]
    data.EwEw          = np.r_["0", data.EwEw, data1.EwEw]
    data.EuEv_re       = np.r_["0", data.EuEv_re, data1.EuEv_re];    data.EuEv_im = np.r_["0", data.EuEv_im, data1.EuEv_im]
    data.EvEw_re       = np.r_["0", data.EvEw_re, data1.EvEw_re];    data.EvEw_im = np.r_["0", data.EvEw_im, data1.EvEw_im]
    data.EwEu_re       = np.r_["0", data.EwEu_re, data1.EwEu_re];    data.EwEu_im = np.r_["0", data.EwEu_im, data1.EwEu_im]
    data.frequency     = np.r_["0", data.frequency, data1.frequency]
    data.freq_step     = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width    = np.r_["0", data.freq_width, data1.freq_width]
    data.epoch         = np.r_["0", data.epoch, data1.epoch]
    data.scet          = np.r_["0", data.scet, data1.scet]
    # AUX
    data.complex       = np.r_["0", data.complex, data1.complex]
    data.ch_selected   = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal    = np.r_["0", data.cal_signal, data1.cal_signal]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    #
    data.T_RWI_CH1     = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2     = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA     = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.N_step        = np.r_["0", data.N_step, data1.N_step]
    data.ADC_ovrflw    = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver       = np.r_["0", data.ISW_ver, data1.ISW_ver]
    return data


def hf_sid21_shaping(data, cal_mode, N_ch, comp_mode):
    """
    input:  data
            cal_mode    [Power]     0: background          1: CAL           2: all
            N_ch0       [channel]   2: 2-ch                                >3: any
            comp_mode   [Complex]   0: Poweer  1: Matrix                   >3: any   
    return: data
    """

    """
    if data.complex[0] > 0:    # Matrix
        data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv = juice_spec.get_stokes(data.EuEu, data.EvEv, data.EuEv_re, data.EuEv_im)
        data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw = juice_spec.get_stokes(data.EvEv, data.EwEw, data.EvEw_re, data.EvEw_im)
        data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu = juice_spec.get_stokes(data.EwEw, data.EuEu, data.EwEu_re, data.EwEu_im)
        data.E_DoPuv, data.E_DoLuv, data.E_DoCuv, data.E_ANGuv = juice_spec.get_pol(data.E_Iuv, data.E_Quv, data.E_Uuv, data.E_Vuv)
        data.E_DoPvw, data.E_DoLvw, data.E_DoCvw, data.E_ANGvw = juice_spec.get_pol(data.E_Ivw, data.E_Qvw, data.E_Uvw, data.E_Vvw)
        data.E_DoPwu, data.E_DoLwu, data.E_DoCwu, data.E_ANGwu = juice_spec.get_pol(data.E_Iwu, data.E_Qwu, data.E_Uwu, data.E_Vwu)
    """
    n_time = data.EuEu.shape[0];  n_freq = data.EuEu.shape[1]
    print("  org:", data.EuEu.shape, n_time, "x", n_freq)
    data.U_selected = (data.ch_selected & 0b1   ) 
    data.V_selected = (data.ch_selected & 0b10  ) >> 1
    data.W_selected = (data.ch_selected & 0b100 ) >> 2
    N_ch0 = data.U_selected[0] + data.V_selected[0] + data.W_selected[0]

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

        # Data
        data.EuEu        = data.EuEu      [index[0]]; data.EvEv       = data.EvEv      [index[0]]; data.EwEw       = data.EwEw      [index[0]]
        data.EuEv_re     = data.EuEv_re   [index[0]]; data.EvEw_re    = data.EvEw_re   [index[0]]; data.EwEu_re    = data.EwEu_re   [index[0]]
        data.EuEv_im     = data.EuEv_im   [index[0]]; data.EvEw_im    = data.EvEw_im   [index[0]]; data.EwEu_im    = data.EwEu_im   [index[0]]
        data.frequency   = data.frequency [index[0]]
        data.freq_step   = data.freq_step [index[0]]
        data.freq_width  = data.freq_width[index[0]]
        data.epoch       = data.epoch     [index[0]]
        data.scet        = data.scet      [index[0]]
        # AUX
        data.complex     = data.complex[index[0]]
        data.ch_selected = data.ch_selected[index[0]]
        data.cal_signal  = data.cal_signal[index[0]]
        data.RFI_rejection = data.RFI_rejection[index[0]]
        #
        data.T_RWI_CH1   = data.T_RWI_CH1[index[0]]
        data.T_RWI_CH2   = data.T_RWI_CH2[index[0]]
        data.T_HF_FPGA   = data.T_HF_FPGA[index[0]]
        # Header
        data.N_step      = data.N_step    [index[0]]
        data.ADC_ovrflw  = data.ADC_ovrflw[index[0]]
        data.ISW_ver     = data.ISW_ver   [index[0]]

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

    data.U_selected = (data.ch_selected & 0b1   ) 
    data.V_selected = (data.ch_selected & 0b10  ) >> 1
    data.W_selected = (data.ch_selected & 0b100 ) >> 2
    N_ch0 = data.U_selected[0] + data.V_selected[0] + data.W_selected[0]

    # NAN
    index = np.where(data.complex == 0)
    data.EuEv_re[index[0]] = math.nan; data.EvEw_re[index[0]] = math.nan; data.EwEu_re[index[0]] = math.nan
    data.EuEv_im[index[0]] = math.nan; data.EvEw_im[index[0]] = math.nan; data.EwEu_im[index[0]] = math.nan
    #
    index = np.where(data.ch_selected & 0b1 == 0) 
    data.EuEu   [index[0]] = math.nan
    data.EuEv_re[index[0]] = math.nan; data.EwEu_re[index[0]] = math.nan; data.EuEv_im[index[0]] = math.nan; data.EwEu_im[index[0]] = math.nan
    index = np.where(data.ch_selected & 0b10 == 0)
    data.EvEv   [index[0]] = math.nan
    data.EvEw_re[index[0]] = math.nan; data.EwEu_re[index[0]] = math.nan; data.EvEw_im[index[0]] = math.nan; data.EwEu_im[index[0]] = math.nan
    index = np.where(data.ch_selected & 0b100 == 0)
    data.EwEw   [index[0]] = math.nan
    data.EvEw_re[index[0]] = math.nan; data.EwEu_re[index[0]] = math.nan; data.EvEw_im[index[0]] = math.nan; data.EwEu_im[index[0]] = math.nan

    """
    # Masked
    for i in range(n_time):
        index = np.where(data.EuEu[i] < 1) 
        data.EuEu   [i][index[0]] = math.nan; data.EvEv   [i][index[0]] = math.nan; data.EwEw   [i][index[0]] = math.nan
        data.EuEv_re[i][index[0]] = math.nan; data.EvEw_re[i][index[0]] = math.nan; data.EwEu_re[i][index[0]] = math.nan 
        data.EuEv_im[i][index[0]] = math.nan; data.EvEw_im[i][index[0]] = math.nan; data.EwEu_im[i][index[0]] = math.nan
    """

    data.n_time = data.EuEu.shape[0]
    data.n_step = data.N_step[data.n_time//2]

    # *** frequncy & width for spec cal
    data.freq   = data.frequency
    data.freq_w = data.freq_width
    return data


def spec_nan(data, i):
    data.EuEu      [i] = math.nan; data.EvEv      [i] = math.nan; data.EwEw      [i] = math.nan
    data.EuEv_re   [i] = math.nan; data.EvEw_re   [i] = math.nan; data.EwEu_re   [i] = math.nan
    data.EuEv_im   [i] = math.nan; data.EvEw_im   [i] = math.nan; data.EwEu_im   [i] = math.nan