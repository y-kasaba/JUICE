"""
    JUICE RPWI HF SID7 (PSSR3 surv): L1a QL -- 2026/7/22
"""
import glob
import numpy as np
import os
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
        data_name = '*HF*SID7_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    else:
        # *** Flight - Ver.3 ***
        # 202606 -- PC4
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW3/'
        data_list = ['JUICE_L1a_RPWI-HF-SID7_20260716T220726-20260716T220814_V01___RPR1_52000006_2026.197.23.00.12.498.cdf',
                     'JUICE_L1a_RPWI-HF-SID7_20260720T012425-20260720T012513_V01___RPR1_5200000E_2026.201.05.13.34.426.cdf',
                    ]
        """
        """

        # *** Ground Test - Ver.3 ***
        # 202511 -- SAMPLE  Freq = 1.8, 1.85, 1.75, 1.9, 1.7 MHz  Vin = 10mVpp
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID7_20000101T003817-20000101T003904_V01___FFT_20260602-2241.ccs.cdf']
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID7_20000101T000155-20000101T000430_V01___SID7-23_P0_20251113-2224.ccs.cdf']                      
        """
        # 202509 -- SAMPLE  Freq = 1.8, 1.85, 1.75, 1.9, 1.7 MHz  Vin = 10mVpp
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old2/'
        data_list = ['JUICE_L1a_RPWI-HF-SID7_20000101T064546-20000101T064910_V01___SID07-23_20250925-1722_10mVpp.ccs.cdf']
        """
    print(data_dir)
    print(data_list)
    return data_dir, data_list


# ---------------------------------------------------------------------
# --- SID7 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid7_read(cdf):
    """
    input:  CDF
    return: data
    """
    data = struct()

    # Data
    data.auto_corr   = np.float64(cdf['auto_corr'][...])
    data.time_block  = cdf['time_block'][...];      data.time   = np.float64(cdf['time'][...])
    #
    data.EE          = np.float64(cdf['EE'][...]);  data.EE_amp   = np.float64(cdf['EE_amp'][...]);  data.EE_raw = np.float64(cdf['EE_raw'][...])
    data.gain_raw = cdf['gain_raw'][...];           data.df_raw = cdf['df_raw'][...]

    hf_hk.status_read(cdf, data)
    return data


def hf_sid7_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.auto_corr  = np.r_["0", data.auto_corr, data1.auto_corr]
    data.time_block = np.r_["0", data.time_block, data1.time_block];    data.time   = np.r_["0", data.time, data1.time]
    #
    data.EE         = np.r_["0", data.EE, data1.EE]
    data.EE_raw     = np.r_["0", data.EE_raw, data1.EE_raw];            data.EE_amp = np.r_["0", data.EE_amp, data1.EE_amp]
    data.gain_raw   = np.r_["0", data.gain_raw, data1.gain_raw];        data.df_raw = np.r_["0", data.df_raw, data1.df_raw]

    hf_hk.status_add(data, data1)
    return data


def hf_sid7_shaping(data, mode_bg, f_max, f_min):
    """
    input:  data
    return: data
    """
    # Size - original
    data.n_time  = data.auto_corr.shape[0]
    data.n_block = data.N_block[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("     org:", data.auto_corr.shape, data.n_time, data.n_block, data.n_lag)

    # ---------------------------
    # --- frequency selection ---
    # ---------------------------
    index = np.where( (data.frequency > f_min) & (data.frequency < f_max) )

    data.auto_corr   = data.auto_corr [index[0]]
    data.time_block  = data.time_block[index[0]];  data.time   = data.time  [index[0]]
    data.EE          = data.EE        [index[0]]
    data.EE_amp      = data.EE_amp    [index[0]];  data.EE_raw = data.EE_raw[index[0]]
    data.gain_raw    = data.gain_raw  [index[0]];  data.df_raw = data.df_raw[index[0]]
    hf_hk.status_shaping(data, index[0])
    print("cut-freq:", data.auto_corr.shape, data.n_time, data.n_block, data.n_lag, "  frequency in", f_min, "-", f_max, "kHz")

    # ---------------------
    # --- CAL selection ---
    # ---------------------
    if mode_bg < 3:
        if mode_bg < 2: index = np.where(data.cal_signal == mode_bg)
        else:           index = np.where((data.HF_QF & 0x01) == 1)
        data.auto_corr   = data.auto_corr [index[0]]
        data.time_block  = data.time_block[index[0]];  data.time   = data.time  [index[0]]
        data.EE          = data.EE        [index[0]]
        data.EE_amp      = data.EE_amp    [index[0]];  data.EE_raw = data.EE_raw[index[0]]
        data.gain_raw    = data.gain_raw  [index[0]];  data.df_raw = data.df_raw[index[0]]
        hf_hk.status_shaping(data, index[0])
        if    mode_bg == 0: print(" cut-cal:", data.auto_corr.shape, data.n_time, data.n_block, data.n_lag, "  <only BG>")
        elif  mode_bg == 1: print(" cut-cal:", data.auto_corr.shape, data.n_time, data.n_block, data.n_lag, "  <only CAL>")
        else:               print(" cut-cal:", data.auto_corr.shape, data.n_time, data.n_block, data.n_lag, "  <only OFF>")

    # Size - after frequency selection
    data.n_time  = data.auto_corr.shape[0]
    data.n_block = data.N_block[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("     cut:", data.auto_corr.shape, data.n_time, data.n_block, data.n_lag, "  frequency in", f_min, "-", f_max, "kHz")

    return data