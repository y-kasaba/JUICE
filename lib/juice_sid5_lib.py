"""
    JUICE RPWI HF SID5 (PSSR1 surv): L1a QL -- 2025/10/21
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
        base_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/'         # ASW2
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
        # 202509 -- SAMPLE
        #	(1) Freq=1.5MHz                                       Vin = [0.01 0.02 0.05 0.1 0.2 0.5 1 2 5 10 20 50 100 200 500] mVpp
	    #   (2) Freq=[0.02 0.05 0.1 0.2 0.5 1.1 2.1 5.1 9.1] MHz  Vin=10mVpp
	    #   (3) Freq=1.5MHz                                       Vin=10mVpp, Phase (y ch) = [0 45 90 135 180 225 270 315 0] deg
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID5_20000101T002153-20000101T004523_V01___SID05-21_20250926-0820_10mVpp.ccs.cdf', ]
        # 202411 -- SAMPLE -- SG 1.75MHz, 100mVpp  --- comp0 & comp1
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID5_20000101T000119-20000101T000149_V01___SID05-21_20241125-1341_PSSR1_comp0_asw3.ccs.cdf',
                     'JUICE_L1a_RPWI-HF-SID5_20000101T000100-20000101T000200_V01___SID05-21_20241125-1335_PSSR1_comp1_asw3.ccs.cdf',
                    ]
        """
        # *** Ground Test - Ver.2 ***
        """
        # 202310 -- SAMPLE -- 1.55MHz, 10mVpp, 90/0/0deg -- 1611 - wo RF, 1603 -- with RFI
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/old/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID5_20000101T002245-20000101T002315_V01___SID05-21_20231024-0046.ccs.cdf',
                          #'JUICE_L1a_RPWI-HF-SID5_20000101T000128-20000101T000213_V01___SID05-21_20231117-1603.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID5_20000101T000044-20000101T000144_V01___SID05-21_20231117-1611.ccs.cdf',
                    ]
        """
        # 202503 -- Flight
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = ['JUICE_L1a_RPWI-HF-SID5_20250331T033821-20250331T034222_V01___RPR2_62000007_2025.091.16.40.05.450.cdf']
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

    hf_hk.status_read(cdf, data)
    """
    data.RPWI_FSW_version = cdf['ISW_ver'][...]
    data.RPWI_FSW_version = data.RPWI_FSW_version[0]
    data.epoch       = cdf['Epoch'][...];      data.scet      = cdf['SCET'][...]
    # AUX
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
    """
    return data


def hf_sid5_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.EE           = np.r_["0", data.EE, data1.EE]
    data.frequency    = np.r_["0", data.frequency, data1.frequency]
    data.freq_step    = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width   = np.r_["0", data.freq_width, data1.freq_width]

    hf_hk.status_add(data, data1, 5)
    """
    data.epoch        = np.r_["0", data.epoch, data1.epoch]
    data.scet         = np.r_["0", data.scet, data1.scet]
    # AUX
    data.ch_selected   = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal    = np.r_["0", data.cal_signal, data1.cal_signal]
    data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
    #
    data.T_RWI_CH1     = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2     = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA     = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.N_step       = np.r_["0", data.N_step, data1.N_step]
    data.ADC_ovrflw   = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver      = np.r_["0", data.ISW_ver, data1.ISW_ver]
    """
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

        hf_hk.status_shaping(data, index[0], 5)
        """
        data.epoch       = data.epoch     [index[0]]
        data.scet        = data.scet      [index[0]]
        # AUX
        data.ch_selected = data.ch_selected[index[0]]
        data.cal_signal  = data.cal_signal[index[0]]
        data.RFI_rejection = data.RFI_rejection[index[0]]
        #
        data.T_RWI_CH1   = data.T_RWI_CH1 [index[0]]
        data.T_RWI_CH2   = data.T_RWI_CH2 [index[0]]
        data.T_HF_FPGA   = data.T_HF_FPGA [index[0]]
        # Header
        data.N_samp      = data.N_samp    [index[0]]
        data.ADC_ovrflw  = data.ADC_ovrflw[index[0]]
        data.ISW_ver     = data.ISW_ver   [index[0]]
        """
    
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
    data.EE[i] = math.nan

    hf_hk.status_nan(data, i, 5)