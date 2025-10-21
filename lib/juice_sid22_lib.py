"""
    JUICE RPWI HF SID6 & 22 (PSSR2): L1a QL -- 2025/10/21
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
        base_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/'         # ASW2
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        if sid == 6:  data_name = '*HF*SID6_*'+ver_str+'.cdf'
        else:         data_name = '*HF*SID22_*'+ver_str+'.cdf'    
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    elif sid == 6: 	# <<< SID-22 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202509 -- SAMPLE  Freq = 0.3, 0.35, 0.4, 0.45 MHz       Vin = 10mVpp
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID22_20000101T065212-20000101T065612_V01___SID06-22_20250925-1838_10mVpp.ccs.cdf', ]
        """
        # 202411 -- SAMPLE -- 1.75MHz, 100mVpp
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old/'
        data_list = ['JUICE_L1a_RPWI-HF-SID22_20000101T000055-20000101T000255_V01___SID06-22_20241125-1325_PSSR2_asw3.ccs.cdf']
        # SG - 1.5MHz 10mVpp 90/0/0deg
        """

    else:               # <<< SID-06 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202509 -- SAMPLE  Freq = 0.3, 0.35, 0.4, 0.45 MHz       Vin = 10mVpp
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID6_20000101T065212-20000101T065612_V01___SID06-22_20250925-1838_10mVpp.ccs.cdf']
        """
        # 202411 -- SAMPLE -- 1.75MHz, 100mVpp
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old/'
        data_list = ['JUICE_L1a_RPWI-HF-SID6_20000101T000055-20000101T000255_V01___SID06-22_20241125-1325_PSSR2_asw3.ccs.cdf']
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
    data.E_i         = np.float64(cdf['E_i'][...]);  data.E_q            = np.float64(cdf['E_q'][...])
    data.auto_corr   = np.float64(cdf['auto_corr'][...])
    data.frequency   = cdf['frequency'][...]
    data.time        = np.float64(cdf['time'][...])

    hf_hk.status_read(cdf, data)
    """
    data.RPWI_FSW_version = cdf['ISW_ver'][...]
    data.RPWI_FSW_version = data.RPWI_FSW_version[0]
    data.epoch       = cdf['Epoch'][...];        data.scet      = cdf['SCET'][...]
    # AUX
    data.ch_selected = cdf['ch_selected'][...]      # [0:U  1:V  2:W]
    data.cal_signal  = cdf['cal_signal'][...]
    data.N_lag       = np.int64(cdf['N_lag'][...])
    #
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    # Header
    data.N_step      = np.int64(cdf['N_step'][...])
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]
    data.ISW_ver   = cdf['ISW_ver'][...]
    """

    return data


def hf_sid22_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.E_i         = np.r_["0", data.E_i, data1.E_i]
    data.E_q         = np.r_["0", data.E_q, data1.E_q]
    data.auto_corr   = np.r_["0", data.auto_corr, data1.auto_corr]
    data.frequency   = np.r_["0", data.frequency, data1.frequency]
    data.time        = np.r_["0", data.time, data1.time]

    hf_hk.status_add(data, data1)
    """
    data.epoch       = np.r_["0", data.epoch, data1.epoch]
    data.scet        = np.r_["0", data.scet, data1.scet]
    # AUX
    data.ch_selected = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.N_lag       = np.r_["0", data.N_lag, data1.N_lag]
    #
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.N_step      = np.r_["0", data.N_step, data1.N_step]
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver     = np.r_["0", data.ISW_ver, data1.ISW_ver]
    """

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
    data.E_i         = data.E_i [index[0]];        data.E_q = data.E_q [index[0]]
    data.frequency   = data.frequency [index[0]];  data.time        = data.time [index[0]]

    hf_hk.status_shaping(data, index[0])
    """
    data.epoch       = data.epoch[index[0]];       data.scet = data.scet[index[0]]
    # AUX
    data.ch_selected = data.ch_selected[index[0]]
    data.cal_signal  = data.cal_signal [index[0]]
    data.N_lag       = data.N_lag [index[0]]
    #
    data.T_RWI_CH1   = data.T_RWI_CH1[index[0]]
    data.T_RWI_CH2   = data.T_RWI_CH2[index[0]]
    data.T_HF_FPGA   = data.T_HF_FPGA[index[0]]
    # Header
    data.N_step      = data.N_step    [index[0]]
    data.ADC_ovrflw  = data.ADC_ovrflw[index[0]]
    data.ISW_ver     = data.ISW_ver   [index[0]]
    """

    data.n_time  = data.auto_corr.shape[0]
    data.n_step  = data.N_step[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("    cut:", data.auto_corr.shape, data.n_time, data.n_step, data.n_lag)
    
    return data
