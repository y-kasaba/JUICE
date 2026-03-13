"""
    JUICE RPWI HF SID21 (PSSR1 rich): L1a QL -- 2026/3/11
"""
import glob
import numpy as np
import math
import juice_hf_hk_lib as hf_hk
class struct:
    pass


def datalist(date_str, ver_str):
    """
    input:  date_str        yyyymmdd: group read    others: file list
    return: data_dir
            data_list
    """
    yr_format = date_str[0:2]
    yr_str    = date_str[0:4]
    mn_str    = date_str[4:6]
    dy_str    = date_str[6:8]
    
    # *** Group read
    if yr_format=='20':
        base_dir = '/Users/D-Univ/data/data-JUICE/datasets/'         # ASW2
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        data_name = '*HF*SID21_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    else:

        # *** Ground Test - Ver.3 ***
        # 202601-- ASW3 test
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID21_20260109T165736-20260109T170606_V01___Sec05_260118.bin.cdf',
                    ]
        # 202511 -- SAMPLE  Vin=10 mVpp     	interval=40 [s]			freq_set = [1.1 1.2 1.4 1.6 1.8] [MHz]
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID21_20000101T002158-20000101T002658_V01___SID5-21_20251123-1129.ccs.cdf',
                     'JUICE_L1a_RPWI-HF-SID21_20000101T003031-20000101T003642_V01___SID5-21_20251113-1746.ccs.cdf',
                      ]
        """

        # *** Ground Test - Ver.2 ***
        # 202510 -- PCW4 emulation
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID21_20251003T080925-20251003T081100_V01___PC4-1_00001.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID21_20251003T080938-20251003T081113_V01___TMIDX_00001.bin.cdf',
                     ]
        """
        # 202311 -- SAMPLE -- SG 1.55MHz, 10mVpp, [90.0, 0.0, 0.0]    20231117-1611: with RFI-mitigation
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/old/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID21_20000101T002245-20000101T002330_V01___SID05-21_20231024-0046.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID21_20000101T000128-20000101T000213_V01___SID05-21_20231117-1603.ccs.cdf',
                     'JUICE_L1a_RPWI-HF-SID21_20000101T000044-20000101T000144_V01___SID05-21_20231117-1611.ccs.cdf',
                     ]
        """

        # 202503 -- Flight
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = ['JUICE_L1a_RPWI-HF-SID21_20250331T033821-20250331T034222_V01___RPR2_62000007_2025.091.16.40.05.450.cdf',
                     'JUICE_L1a_RPWI-HF-SID21_20260223T004655-20260223T004831_V01___RPR2_62000001_2026.054.09.35.22.426.cdf',
                     'JUICE_L1a_RPWI-HF-SID21_20260223T082205-20260223T082341_V01___RPR2_62000001_2026.054.09.35.22.426.cdf',
                    ]
        """

    print(data_dir)
    print(data_list)
    return data_dir, data_list


# ---------------------------------------------------------------------
# --- SID21 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid21_read(cdf):
    """
    input:  CDF
    return: data
    """
    data = struct()

    # Data
    data.EuEu    = np.float64(cdf['EuEu'][...]);     data.EvEv = np.float64(cdf['EvEv'][...]);        data.EwEw = np.float64(cdf['EwEw'][...])
    data.EuEv_re = np.float64(cdf['EuEv_re'][...]);  data.EuEv_im = np.float64(cdf['EuEv_im'][...])  
    data.EvEw_re = np.float64(cdf['EvEw_re'][...]);  data.EvEw_im = np.float64(cdf['EvEw_im'][...])  
    data.EwEu_re = np.float64(cdf['EwEu_re'][...]);  data.EwEu_im = np.float64(cdf['EwEu_im'][...])
    data.frequency  = cdf['frequency'][...];   data.freq_step = cdf['freq_step'][...]; data.freq_width = cdf['freq_width'][...]
    #
    data.EuEu_amp = np.float64(cdf['EuEu_amp'][...]);   data.EuEu_raw = np.float64(cdf['EuEu_raw'][...])
    data.EvEv_amp = np.float64(cdf['EvEv_amp'][...]);   data.EvEv_raw = np.float64(cdf['EvEv_raw'][...])
    data.EwEw_amp = np.float64(cdf['EwEw_amp'][...]);   data.EwEw_raw = np.float64(cdf['EwEw_raw'][...])
    data.gain_raw = cdf['gain_raw'][...];               data.df_raw = cdf['df_raw'][...]

    hf_hk.status_read(cdf, data)

    return data


def hf_sid21_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.EuEu     = np.r_["0", data.EuEu, data1.EuEu]
    data.EvEv     = np.r_["0", data.EvEv, data1.EvEv]
    data.EwEw     = np.r_["0", data.EwEw, data1.EwEw]
    data.EuEv_re  = np.r_["0", data.EuEv_re, data1.EuEv_re];    data.EuEv_im = np.r_["0", data.EuEv_im, data1.EuEv_im]
    data.EvEw_re  = np.r_["0", data.EvEw_re, data1.EvEw_re];    data.EvEw_im = np.r_["0", data.EvEw_im, data1.EvEw_im]
    data.EwEu_re  = np.r_["0", data.EwEu_re, data1.EwEu_re];    data.EwEu_im = np.r_["0", data.EwEu_im, data1.EwEu_im]
    #
    data.EuEu_raw = np.r_["0", data.EuEu_raw, data1.EuEu_raw];    data.EuEu_amp = np.r_["0", data.EuEu_amp, data1.EuEu_amp]
    data.EvEv_raw = np.r_["0", data.EvEv_raw, data1.EvEv_raw];    data.EvEv_amp = np.r_["0", data.EvEv_amp, data1.EvEv_amp]
    data.EwEw_raw = np.r_["0", data.EwEw_raw, data1.EwEw_raw];    data.EwEw_amp = np.r_["0", data.EwEw_amp, data1.EwEw_amp]
    data.gain_raw = np.r_["0", data.gain_raw, data1.gain_raw];    data.df_raw   = np.r_["0", data.df_raw,   data1.df_raw]
    #
    data.frequency  = np.r_["0", data.frequency, data1.frequency]
    data.freq_step  = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width = np.r_["0", data.freq_width, data1.freq_width]

    hf_hk.status_add(data, data1)
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
        data.EuEu       = data.EuEu    [index[0]]; data.EvEv     = data.EvEv    [index[0]]; data.EwEw     = data.EwEw    [index[0]]
        data.EuEv_re    = data.EuEv_re [index[0]]; data.EvEw_re  = data.EvEw_re [index[0]]; data.EwEu_re  = data.EwEu_re [index[0]]
        data.EuEv_im    = data.EuEv_im [index[0]]; data.EvEw_im  = data.EvEw_im [index[0]]; data.EwEu_im  = data.EwEu_im [index[0]]
        #
        data.EuEu_raw   = data.EuEu_raw[index[0]]; data.EvEv_raw = data.EvEv_raw[index[0]]; data.EwEw_raw = data.EwEw_raw[index[0]]
        data.EuEu_amp   = data.EuEu_amp[index[0]]; data.EvEv_amp = data.EvEv_amp[index[0]]; data.EwEw_amp = data.EwEw_amp[index[0]]
        data.gain_raw   = data.gain_raw[index[0]]; data.df_raw   = data.df_raw  [index[0]]
        #
        data.frequency  = data.frequency [index[0]]
        data.freq_step  = data.freq_step [index[0]]
        data.freq_width = data.freq_width[index[0]]

        hf_hk.status_shaping(data, index[0])

        n_time = data.EuEu.shape[0]
        if cal_mode < 2:
            if N_ch < 4:
                if comp_mode < 4: print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch, " comp_mode:", comp_mode)
                else:             print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch)
            else:
                if comp_mode < 4: print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode, " comp_mode:", comp_mode)
                else:             print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode)
            if cal_mode == 0:     print("<only BG>")
            else:                 print("<only CAL>")
        else:
            if N_ch < 4:
                if comp_mode < 4: print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> N_ch:", N_ch, " comp_mode:", comp_mode)
                else:             print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> N_ch:", N_ch)
            else:                 print("  cut:", data.EuEu.shape, n_time, "x", n_freq, "===> comp_mode:", comp_mode)

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
    data.EuEu    [index[0]] = math.nan
    data.EuEv_re [index[0]] = math.nan; data.EwEu_re [index[0]] = math.nan; data.EuEv_im[index[0]] = math.nan; data.EwEu_im[index[0]] = math.nan
    data.EuEu_raw[index[0]] = math.nan; data.EuEu_amp[index[0]] = math.nan; 
    index = np.where(data.ch_selected & 0b10 == 0)
    data.EvEv   [index[0]] = math.nan
    data.EvEw_re[index[0]] = math.nan; data.EwEu_re[index[0]] = math.nan; data.EvEw_im[index[0]] = math.nan; data.EwEu_im[index[0]] = math.nan
    data.EvEv_raw[index[0]] = math.nan; data.EvEv_amp[index[0]] = math.nan; 
    index = np.where(data.ch_selected & 0b100 == 0)
    data.EwEw   [index[0]] = math.nan
    data.EvEw_re[index[0]] = math.nan; data.EwEu_re[index[0]] = math.nan; data.EvEw_im[index[0]] = math.nan; data.EwEu_im[index[0]] = math.nan
    data.EwEw_raw[index[0]] = math.nan; data.EwEw_amp[index[0]] = math.nan; 

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
    #
    data.EuEu_raw  [i] = math.nan; data.EvEv_raw  [i] = math.nan; data.EwEw_raw  [i] = math.nan
    data.EuEu_amp  [i] = math.nan; data.EvEv_amp  [i] = math.nan; data.EwEw_amp  [i] = math.nan

    hf_hk.status_nan(data, i, 21)