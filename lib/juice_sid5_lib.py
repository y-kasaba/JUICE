"""
    JUICE RPWI HF SID5 (PSSR1 surv): L1a QL -- 2026/3/4
"""
import glob
import math
import numpy as np
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
        data_name = '*HF*SID5_*'+ver_str+'.cdf'
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
        data_list = ['JUICE_L1a_RPWI-HF-SID5_20260109T165736-20260109T170606_V01___Sec05_260118.bin.cdf',
                    ]
        # 202511 -- SAMPLE  Vin=10 mVpp     	interval=40 [s]			freq_set = [1.1 1.2 1.4 1.6 1.8] [MHz]
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID5_20000101T002158-20000101T002628_V01___SID5-21_20251123-1129.ccs.cdf',
                     'JUICE_L1a_RPWI-HF-SID5_20000101T003031-20000101T003531_V01___SID5-21_20251113-1746.ccs.cdf',
                      ]
        """

        # *** Ground Test - Ver.2 ***
        # 202510 -- PCW4 emulation
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID5_20251003T080925-20251003T081100_V01___PC4-1_00001.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID5_20251003T080938-20251003T081113_V01___TMIDX_00001.bin.cdf',
                     ]
        """
        """
        # 202503 -- Flight
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = ['JUICE_L1a_RPWI-HF-SID5_20250331T033821-20250331T034222_V01___RPR1_52000005_2025.091.16.38.56.448.cdf']
        """

    print(data_dir)
    print(data_list)
    return data_dir, data_list


# ---------------------------------------------------------------------
# --- SID5 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid5_read(cdf):
    """
    Input:  cdf
    Output: data
    """
    data = struct()

    # Data
    data.EE = np.float64(cdf['EE'][...])
    data.frequency  = cdf['frequency'][...];   data.freq_step = cdf['freq_step'][...]; data.freq_width = cdf['freq_width'][...]
    #
    data.EE_amp = np.float64(cdf['EE_amp'][...]);   data.EE_raw = np.float64(cdf['EE_raw'][...])
    data.gain_raw = cdf['gain_raw'][...];           data.df_raw = cdf['df_raw'][...]

    hf_hk.status_read(cdf, data)
    return data


def hf_sid5_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.EE         = np.r_["0", data.EE, data1.EE]
    data.frequency  = np.r_["0", data.frequency, data1.frequency]
    data.freq_step  = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width = np.r_["0", data.freq_width, data1.freq_width]
    #
    data.EE_raw     = np.r_["0", data.EE_raw, data1.EE_raw];        data.EE_amp     = np.r_["0", data.EE_amp, data1.EE_amp]
    data.gain_raw   = np.r_["0", data.gain_raw, data1.gain_raw];    data.df_raw     = np.r_["0", data.df_raw, data1.df_raw]

    hf_hk.status_add(data, data1)
    return data


def hf_sid5_shaping(data, cal_mode):
    """
    input:  data
            cal_mode    [Power]     0: background          1: CAL           2: all
    return: data
    """
    n_time = data.EE.shape[0];  n_freq = data.EE.shape[1]
    print("  org:", data.EE.shape, n_time, "x", n_freq, "[", n_time*n_freq, "]")

    if cal_mode < 2:
        index = np.where( (data.cal_signal == cal_mode)                                                 )
        print("  cut:", data.EE.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode)

        # Data
        data.EE          = data.EE        [index[0]]
        data.frequency   = data.frequency [index[0]]
        data.freq_step   = data.freq_step [index[0]]
        data.freq_width  = data.freq_width[index[0]]
        #
        data.EE_raw   = data.EE_raw  [index[0]];    data.EE_amp = data.EE_amp[index[0]]
        data.gain_raw = data.gain_raw[index[0]];    data.df_raw = data.df_raw[index[0]]
        
        hf_hk.status_shaping(data, index[0])
    
        n_time = data.EE.shape[0]
        if cal_mode < 2:
            print("  cut:", data.EE.shape, n_time, "x", n_freq, "===> cal-mode:", cal_mode)
            if cal_mode == 0:   print("<only BG>")
            else:               print("<only CAL>")

    data.n_time = data.EE.shape[0]
    data.n_step = data.N_step[data.n_time//2]

    # *** frequncy & width for spec cal
    data.freq   = data.frequency
    data.freq_w = data.freq_width
    return data


def spec_nan(data, i):
    data.EE[i]     = math.nan;  data.EE_raw[i] = math.nan;  data.EE_amp[i] = math.nan
    
    hf_hk.status_nan(data, i, 5)