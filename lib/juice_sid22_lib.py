"""
    JUICE RPWI HF SID6 & 22 (PSSR2): L1a QL -- 2026/3/4
"""
import glob
import numpy as np
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
        if sid == 6:  data_name = '*HF*SID6_*'+ver_str+'.cdf'
        else:         data_name = '*HF*SID22_*'+ver_str+'.cdf'    
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    elif sid == 22: 	# <<< SID-22 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202601-- ASW3 test
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID22_20260109T171221-20260109T172121_V01___Sec06_260118.bin.cdf',
                    ]
        # 202601
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID22_20000101T000034-20000101T000104_V01___SID9-22_20260114.dat.cdf',
                     #'JUICE_L1a_RPWI-HF-SID22_20000101T000051-20000101T000121_V01___SID6-22_P0_20251212-2236.ccs.cdf',
        ]
        """

    elif sid == 9:  # <<< SID-09 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202601
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID9_20000101T000034-20000101T000104_V01___SID9-22_20260114.dat.cdf',
        ]

    else:               # <<< SID-06 test datas >>>
        # 202601
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID6_20000101T000051-20000101T000151_V01___SID6-22_P0_20251212-2236.ccs.cdf',
        ]

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
    data.frequency   = cdf['frequency'][...]
    data.time        = np.float64(cdf['time'][...])
    data.gain_raw = cdf['gain_raw'][...];       data.df_raw = cdf['df_raw'][...]

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
    data.time       = np.r_["0", data.time, data1.time]
    data.gain_raw   = np.r_["0", data.gain_raw, data1.gain_raw]
    data.df_raw     = np.r_["0", data.df_raw,   data1.df_raw]

    hf_hk.status_add(data, data1)

    return data


def hf_sid22_shaping(data):
    """
    input:  data
    return: data
    """

    # Size - original
    data.n_time  = data.auto_corr.shape[0]
    data.n_step  = data.N_step[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("    org:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag)

    # ---------------------------
    # --- shape-check ---
    # ---------------------------
    index = np.where( (data.N_step == data.n_step) & (data.N_lag == data.n_lag) )
    # Data
    data.auto_corr   = data.auto_corr [index[0]]
    data.EE          = data.EE [index[0]]
    data.frequency   = data.frequency [index[0]];  data.time        = data.time [index[0]]

    hf_hk.status_shaping(data, index[0])

    data.n_time  = data.auto_corr.shape[0]
    data.n_step  = data.N_step[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("    cut:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag)
    
    return data
