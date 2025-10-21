"""
    JUICE RPWI HF SID7 (PSSR3 surv): L1a QL -- 2025/10/21
"""
import glob
import numpy as np
import juice_hf_hk_lib as hf_hk
import juice_cdf_lib   as hk_cdf
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
        data_name = '*HF*SID07_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    else:
        # *** Ground Test - Ver.3 ***
        # 202509 -- SAMPLE  Freq = 1.8, 1.85, 1.75, 1.9, 1.7 MHz  Vin = 10mVpp
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID7_20000101T064546-20000101T064910_V01___SID07-23_20250925-1722_10mVpp.ccs.cdf']
        # 202411 -- SAMPLE -- SG: 1.75MHz 100mVpp 90/0/0deg
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old/'
        data_list = ['JUICE_L1a_RPWI-HF-SID7_20000101T000512-20000101T000512_V01___SID07-23_20241125-1321_PSSR3_asw3.ccs.cdf']    
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
    data.E_i         = np.float64(cdf['E_i'][...]);  data.E_q         = np.float64(cdf['E_q'][...])
    data.time_block  = cdf['time_block'][...];       data.time        = np.float64(cdf['time'][...])

    hf_hk.status_read(cdf, data)
    """
    data.RPWI_FSW_version = cdf['ISW_ver'][...]
    data.RPWI_FSW_version = data.RPWI_FSW_version[0]
    data.epoch       = cdf['Epoch'][...];            data.scet      = cdf['SCET'][...]
    # AUX
    data.N_block     = np.int16(cdf['N_block'][...])
    data.N_lag       = np.int16(cdf['N_lag'][...])
    data.ch_selected = cdf['ch_selected'][...]
    data.cal_signal  = cdf['cal_signal'][...]
    data.freq_center = cdf['freq_center'][...]
    #
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    # Header
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]; 
    data.ISW_ver     = cdf['ISW_ver'][...]
    """

    return data


def hf_sid7_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.auto_corr   = np.r_["0", data.auto_corr, data1.auto_corr]
    data.E_i         = np.r_["0", data.E_i, data1.E_i];               data.E_q  = np.r_["0", data.E_q, data1.E_q]
    data.time_block  = np.r_["0", data.time_block, data1.time_block]; data.time = np.r_["0", data.time, data1.time]

    hf_hk.status_add(data, data1, 7)
    """
    data.epoch      = np.r_["0", data.epoch, data1.epoch];            data.scet = np.r_["0", data.scet, data1.scet]
    # AUX
    data.N_block     = np.r_["0", data.N_block, data1.N_block]
    data.N_lag       = np.r_["0", data.N_lag, data1.N_lag]
    data.ch_selected = np.r_["0", data.ch_selected, data1.U_selected]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.freq_center = np.r_["0", data.freq_center, data1.freq_center]
    #
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver     = np.r_["0", data.ISW_ver, data1.ISW_ver]
    """
    return data


def hf_sid7_shaping(data, f_max, f_min):
    """
    input:  data
    return: data
    """
    # Size - original
    data.n_time  = data.auto_corr.shape[0]
    data.n_block = data.N_block[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("    org:", data.auto_corr.shape, data.n_time, data.n_block, data.n_lag)

    # ---------------------------
    # --- shape-check ---
    # ---------------------------
    index = np.where( (data.N_block == data.n_block) & (data.N_lag == data.n_lag) )
    # Data
    data.auto_corr   = data.auto_corr [index[0]]
    data.E_i         = data.E_i [index[0]];        data.E_q = data.E_q [index[0]]
    data.time_block  = data.time_block [index[0]]; data.time        = data.time [index[0]]

    hf_hk.status_shaping(data, index[0])
    """
    data.epoch       = data.epoch[index[0]];       data.scet = data.scet[index[0]]
    # AUX
    data.N_block     = data.N_block [index[0]]
    data.N_lag       = data.N_lag [index[0]]
    data.ch_selected = data.ch_selected[index[0]]
    data.cal_signal  = data.cal_signal [index[0]]
    data.freq_center = data.freq_center[index[0]]
    #
    data.T_RWI_CH1   = data.T_RWI_CH1[index[0]]
    data.T_RWI_CH2   = data.T_RWI_CH2[index[0]]
    data.T_HF_FPGA   = data.T_HF_FPGA[index[0]]
    # Header
    data.ADC_ovrflw  = data.ADC_ovrflw[index[0]]
    data.ISW_ver     = data.ISW_ver   [index[0]]
    """

    data.n_time  = data.auto_corr.shape[0]
    data.n_block = data.N_block[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("   cut1:", data.auto_corr.shape, data.n_time, data.n_block, data.n_lag)

    # ---------------------------
    # --- frequency selection ---
    # ---------------------------
    index = np.where( (data.freq_center > f_min) & (data.freq_center < f_max) )
    # Data
    data.auto_corr   = data.auto_corr [index[0]]
    data.E_i         = data.E_i [index[0]];        data.E_q = data.E_q [index[0]]
    data.time_block  = data.time_block [index[0]]; data.time        = data.time [index[0]]

    hf_hk.status_shaping(data, index[0])
    """
    data.epoch       = data.epoch[index[0]];       data.scet = data.scet[index[0]]
    # AUX
    data.N_block     = data.N_block [index[0]]
    data.N_lag       = data.N_lag [index[0]]
    data.ch_selected = data.ch_selected[index[0]]
    data.cal_signal  = data.cal_signal [index[0]]
    data.freq_center = data.freq_center[index[0]]
    #
    data.T_RWI_CH1   = data.T_RWI_CH1[index[0]]
    data.T_RWI_CH2   = data.T_RWI_CH2[index[0]]
    data.T_HF_FPGA   = data.T_HF_FPGA[index[0]]
    # Header
    data.ADC_ovrflw  = data.ADC_ovrflw[index[0]]
    data.ISW_ver     = data.ISW_ver   [index[0]]
    """
    #
    # Size - after frequency selection
    data.n_time  = data.auto_corr.shape[0]
    data.n_block = data.N_block[data.n_time//2]
    data.n_lag   = data.N_lag[data.n_time//2]
    print("   cut1:", data.auto_corr.shape, data.n_time, data.n_block, data.n_lag, "   frequency in", f_min, "-", f_max, "kHz")

    return data