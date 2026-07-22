"""
    JUICE RPWI HF SID6 (PSSR2-S) & 9 (PSSR2-S-SINGLE) & 22 (PSSR2-R) L1a QL -- 2026/7/22
"""
import glob
import numpy as np
import os
import juice_hf_hk_lib as hf_hk
class struct:
    pass

def datalist(date_str, ver_str, sid):
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
        if   sid == 6:  data_name = '*HF*SID6_*'+ver_str+'.cdf'
        elif sid == 22: data_name = '*HF*SID22_*'+ver_str+'.cdf'    
        elif sid == 9:  data_name = '*HF*SID9_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    elif sid == 22: 	# <<< SID-22 test datas >>>
        # *** Flight - Ver.3 ***
        # 202606 -- PC4
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW3/'
        data_list = ['JUICE_L1a_RPWI-HF-SID22_20260716T215924-20260716T221515_V01___RPW0_62000005_2026.198.19.00.45.441.cdf',
                    ]
        """
        """

        # *** Ground Test - Ver.3 ***
        # 202605-- ASW3 FFT
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID22_20000101T003014-20000101T004605_V01___FFT_20260602-2241.ccs.cdf']
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID22_20000113T003818-20000113T004500_V01___260520FFT_0.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID22_20000113T004654-20000113T005337_V01___260520FFT_1.bin.cdf',
                     #'JUICE_L1a_RPWI-HF-SID22_20000101T004231-20000101T004331_V01___260525FFT_0.bin.cdf',
                     #'JUICE_L1a_RPWI-HF-SID22_20000101T004401-20000101T005208_V01___260525FFT_1.bin.cdf',
                     #'JUICE_L1a_RPWI-HF-SID22_20000101T005252-20000101T005750_V01___260525FFT_2.bin.cdf',
                    ]
        """
        # 202604-- ASW3 test @ system
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/system/'
        data_list = ['JUICE_L1a_RPWI-HF-SID22_20260421T153015-20260421T153145_V01___62000001_3.cdf',]
        """
        # 202601-- ASW3 test
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID22_20260109T171221-20260109T172121_V01___Sec06_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID22_20260414T120343-20260414T121243_V01___Sec06_260416.bin.cdf',
                    ]
        """
        # 202601
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID22_20000101T000044-20000101T001414_V01___SID6-22_20251211-1108.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID22_20000101T000051-20000101T000121_V01___SID6-22_P0_20251212-2236.ccs.cdf',
                     'JUICE_L1a_RPWI-HF-SID22_20000101T000047-20000101T001317_V01___SID6-22_20251213-1846.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID22_20000101T000034-20000101T000104_V01___SID9-22_20260114.dat.cdf',
                    ]
        """
    elif sid == 6:      # <<< SID-06 test datas >>>
        # *** Flight - Ver.3 ***
        """
        # 202606 -- PC4
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW3/'
        data_list = ['JUICE_L1a_RPWI-HF-SID9_20260716T215924-20260716T221515_V01___RPR1_52000006_2026.197.23.00.12.498.cdf',
                    ]
        """

        # 202601-- ASW3 test
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID6_20260109T171221-20260109T172121_V01___Sec06_260118.bin.cdf'
                    ]
        """
        """
        # 202601
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID6_20000101T000044-20000101T001444_V01___SID6-22_20251211-1108.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID6_20000101T000047-20000101T001317_V01___SID6-22_20251213-1846.ccs.cdf',
                     'JUICE_L1a_RPWI-HF-SID6_20000101T000051-20000101T000151_V01___SID6-22_P0_20251212-2236.ccs.cdf',
                    ]
        """

    elif sid == 9:      # <<< SID-09 test datas >>>
        # *** Flight - Ver.3 ***
        # 202606 -- PC4
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW3/'
        data_list = ['JUICE_L1a_RPWI-HF-SID9_20260716T215924-20260716T221515_V01___RPR1_52000006_2026.197.23.00.12.498.cdf',
                     'JUICE_L1a_RPWI-HF-SID9_20260720T011623-20260720T013214_V01___RPR1_5200000E_2026.201.05.13.34.426.cdf',
                     'JUICE_L1a_RPWI-HF-SID9_20260720T050011-20260720T052941_V01___RPR1_52000012_2026.201.05.43.50.470.cdf',
                    ]
        """
        """

        # 202605-- ASW3 FFT
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID9_20000101T003014-20000101T005639_V01___FFT_20260602-2241.ccs.cdf']
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID9_20000113T003818-20000113T004500_V01___260520FFT_0.bin.cdf',
                     #'JUICE_L1a_RPWI-HF-SID9_20000113T004654-20000113T005337_V01___260520FFT_1.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID9_20000101T004231-20000101T004331_V01___260525FFT_0.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID9_20000101T004401-20000101T005238_V01___260525FFT_1.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID9_20000101T005252-20000101T005750_V01___260525FFT_2.bin.cdf',
                    ]
        """
        # 202604-- ASW3 test @ system
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/system/'
        data_list = ['JUICE_L1a_RPWI-HF-SID9_20260421T153015-20260421T153145_V01___52000001_4.cdf']
        """
        # 202601-- ASW3 test
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID9_20260414T120343-20260414T121243_V01___Sec06_260416.bin.cdf']
        """
        # 202601
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID9_20000101T000034-20000101T000104_V01___SID9-22_20260114.dat.cdf',
                    ]
        """

    print(data_dir)
    print(data_list)
    return data_dir, data_list


#---------------------------------------------------------------------
#--- SID22 ------------------------------------------------------------
#---------------------------------------------------------------------
def hf_sid22_read(cdf):
    """
    input:  CDF
    return: data
    """
    data = struct()

    # Data
    data.EE          = np.float64(cdf['EE'][...])
    data.auto_corr   = np.float64(cdf['auto_corr'][...])
    data.frequency  = cdf['frequency'][...];    data.freq_width = cdf['freq_width'][...]
    data.time        = np.float64(cdf['time'][...])
    #
    data.EE_amp = np.float64(cdf['EE_amp'][...]);   data.EE_raw = np.float64(cdf['EE_raw'][...])
    data.gain_raw = cdf['gain_raw'][...];           data.df_raw = cdf['df_raw'][...]

    hf_hk.status_read(cdf, data)
    print("param: ", data.auto_corr.shape, data.N_step[0], data.N_lag[0], data.N_step[0] * data.N_lag[0])
    return data


def hf_sid22_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.EE         = np.r_["0", data.EE, data1.EE]
    data.auto_corr  = np.r_["0", data.auto_corr, data1.auto_corr]
    data.frequency  = np.r_["0", data.frequency, data1.frequency]
    data.freq_width = np.r_["0", data.freq_width, data1.freq_width]
    #
    data.time       = np.r_["0", data.time, data1.time]
    #
    data.EE_raw     = np.r_["0", data.EE_raw, data1.EE_raw];        data.EE_amp     = np.r_["0", data.EE_amp, data1.EE_amp]
    data.gain_raw   = np.r_["0", data.gain_raw, data1.gain_raw];    data.df_raw     = np.r_["0", data.df_raw, data1.df_raw]

    hf_hk.status_add(data, data1)
    return data


def hf_sid22_shaping(data, mode_bg, sid):
    """
    input:  data
    return: data
    """
    # Size - original
    data.n_time  = data.auto_corr.shape[0]
    data.n_step  = data.N_step[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("      org:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag)

    # ---------------------------
    # --- shape-check ---
    # ---------------------------
    index = np.where( (data.N_step == data.n_step) & (data.N_lag == data.n_lag) )
    #
    data.auto_corr = data.auto_corr [index[0]]
    data.EE        = data.EE [index[0]]
    data.time      = data.time [index[0]]
    data.EE_raw    = data.EE_raw  [index[0]];        data.EE_amp = data.EE_amp[index[0]]
    data.gain_raw  = data.gain_raw[index[0]];        data.df_raw = data.df_raw[index[0]]
    hf_hk.status_shaping(data, index[0])
    print("cut-shape:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag, "  <only BG>")

    # ---------------------
    # --- CAL selection ---
    # ---------------------
    if mode_bg < 3:
        if mode_bg < 2: index = np.where(data.cal_signal == mode_bg)
        else:           index = np.where((data.HF_QF & 0x01) == 1)
        data.auto_corr = data.auto_corr [index[0]]
        data.EE        = data.EE [index[0]]
        data.time      = data.time [index[0]]
        data.EE_raw    = data.EE_raw  [index[0]];        data.EE_amp = data.EE_amp[index[0]]
        data.gain_raw  = data.gain_raw[index[0]];        data.df_raw = data.df_raw[index[0]]
        hf_hk.status_shaping(data, index[0])
        if    mode_bg == 0: print(" cut-cal:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag, "  <only BG>")
        elif  mode_bg == 1: print(" cut-cal:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag, "  <only CAL>")
        else:               print(" cut-cal:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag, "  <only OFF>")

    data.n_time    = data.auto_corr.shape[0]
    data.n_step    = data.N_step[data.n_time//2]
    data.n_lag     = data.N_lag[data.n_time//2]
    if sid == 6:  data.n_lag = np.int64(data.n_lag / 16)
    print("      cut:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag)
    
    # *** frequncy & width for spec cal
    data.freq   = data.frequency
    data.freq_w = data.freq_width
    return data
