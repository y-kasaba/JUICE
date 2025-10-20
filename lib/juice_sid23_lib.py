"""
    JUICE RPWI HF SID23 (PSSR3 rich): L1a QL -- 2025/10/20
"""
import glob
import numpy          as np
import scipy.stats    as stats
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
        base_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/'
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        data_name = '*HF*SID23_*'+ver_str+'.cdf'
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
        data_list = ['JUICE_L1a_RPWI-HF-SID23_20000101T064546-20000101T064910_V01___SID07-23_20250925-1722_10mVpp.ccs.cdf']
        # 202411 -- SAMPLE -- SG: 1.75MHz 100mVpp 90/0/0deg
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old/'
        data_list = ['JUICE_L1a_RPWI-HF-SID23_20000101T000512-20000101T000512_V01___SID07-23_20241125-1321_PSSR3_asw3.ccs.cdf']    
        """
        """

        # *** Ground Test - Ver.2 ***
        """
        # 202310 -- SAMPLE -- SG: 0/0/10mVpp 
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/old/'
        data_list = ['JUICE_L1a_RPWI-HF-SID23_20000101T000322-20000101T000322_V01___SID07-23_20231024-0011.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20000101T000047-20000101T000047_V01___SID07-23_20231024-0024.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20000101T001030-20000101T001030_V01___SID07-23_20231024-0034.ccs.cdf',
                         ]
        """

        # *** Flight - Ver.2 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID23_20240126T092930-20240126T094732_V01___RPR2_62000006_2024.026.11.53.48.449.cdf',
                     #'JUICE_L1a_RPWI-HF-SID23_20240126T094802-20240126T100504_V01___RPR2_62000007_2024.026.12.58.18.441.cdf',
                     #'JUICE_L1a_RPWI-HF-SID23_20240706T023200-20240706T023440_V01___RPR2_62000001_2024.190.16.56.50.659.cdf',
                     #'JUICE_L1a_RPWI-HF-SID23_20240706T124753-20240706T130347_V01___RPR2_62000002_2024.190.19.50.21.637.cdf',
                     #'JUICE_L1a_RPWI-HF-SID23_20240706T130407-20240706T130904_V01___RPR2_62000003_2024.190.22.47.44.640.cdf',
                     #'JUICE_L1a_RPWI-HF-SID23_20240819T210319-20240819T211856_V01___RPR2_62000004_2024.235.10.15.04.518.cdf',
                     'JUICE_L1a_RPWI-HF-SID23_20240819T211916-20240819T212356_V01___RPR2_62000005_2024.235.12.58.11.564.cdf',
                     #'JUICE_L1a_RPWI-HF-SID23_20240822T024109-20240822T024134_V01___RPR2_62000006_2024.236.10.07.45.514.cdf',
                    ]
        """
        """

    print(data_dir)
    print(data_list)
    return data_dir, data_list


# ---------------------------------------------------------------------
# --- SID23 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid23_read(cdf): # RPWI_FSW_version):
    """
    input:  CDF
    return: data
    """
    data = struct()
    data.RPWI_FSW_version = cdf['ISW_ver'][...]
    data.RPWI_FSW_version = data.RPWI_FSW_version[0]

    # Data
    data.Eu_i        = np.float64(cdf['Eu_i'][...]);       data.Eu_q = np.float64(cdf['Eu_q'][...])
    data.Ev_i        = np.float64(cdf['Ev_i'][...]);       data.Ev_q = np.float64(cdf['Ev_q'][...])
    data.Ew_i        = np.float64(cdf['Ew_i'][...]);       data.Ew_q = np.float64(cdf['Ew_q'][...])
    data.time_block  = np.float64(cdf['time_block'][...]); data.time = np.float64(cdf['time'][...])

    hf_hk.status_read(cdf, data, 23)
    """
    data.epoch       = cdf['Epoch'][...];                  data.scet = cdf['SCET'][...]
    # AUX
    data.N_block     = np.int16(cdf['N_block'][...])
    data.N_feed      = np.int16(cdf['N_feed'][...])
    data.cal_signal  = cdf['cal_signal'][...]
    data.freq_center = cdf['freq_center'][...]
    #
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    # Header
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]
    data.ISW_ver     = cdf['ISW_ver'][...]
    data.HF_QF       = cdf['HF_QF'][...]    # Quality flag: b0:RWI-off b1:Cal b2-3:Ovrflw b4:RIME b5-7:n/a (b0-1=3:error)'
    """

    return data


def hf_sid23_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.Eu_i        = np.r_["0", data.Eu_i, data1.Eu_i];              data.Eu_q = np.r_["0", data.Eu_q, data1.Eu_q]
    data.Ev_i        = np.r_["0", data.Ev_i, data1.Ev_i];              data.Ev_q = np.r_["0", data.Ev_q, data1.Ev_q]
    data.Ew_i        = np.r_["0", data.Ew_i, data1.Ew_i];              data.Ew_q = np.r_["0", data.Ew_q, data1.Ew_q]
    data.time_block  = np.r_["0", data.time_block, data1.time_block];  data.time        = np.r_["0", data.time, data1.time]

    hf_hk.status_add(data, data1, 23)
    """
    data.epoch       = np.r_["0", data.epoch, data1.epoch];            data.scet = np.r_["0", data.scet, data1.scet]
    # AUX
    data.N_block     = np.r_["0", data.N_block, data1.N_block]
    data.N_feed      = np.r_["0", data.N_feed, data1.N_feed]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.freq_center = np.r_["0", data.freq_center, data1.freq_center]
    #
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver     = np.r_["0", data.ISW_ver, data1.ISW_ver]
    data.HF_QF       = np.r_["0", data.HF_QF, data1.HF_QF]
    """
    return data


def hf_sid23_shaping(data, f_max, f_min):
    """
    input:  data, f_max, f_min
    return: data
    """
    # Size - original
    data.n_time = data.Eu_i.shape[0]
    data.n_block = data.N_block[data.n_time//2]
    data.n_feed = data.N_feed[data.n_time//2]
    print("    org:", data.Eu_i.shape, data.n_time, data.n_block, data.n_feed)

    # ---------------------------
    # --- shape-check ---
    # ---------------------------
    index = np.where( (data.N_block == data.n_block) & (data.N_feed == data.n_feed) )
    # Data
    data.Eu_i        = data.Eu_i [index[0]];       data.Eu_q = data.Eu_q [index[0]]
    data.Ev_i        = data.Ev_i [index[0]];       data.Ev_q = data.Ev_q [index[0]]
    data.Ew_i        = data.Ew_i [index[0]];       data.Ew_q = data.Ew_q [index[0]]
    data.time_block  = data.time_block [index[0]]; data.time        = data.time [index[0]]

    hf_hk.status_shaping(data, index[0])
    """
    data.epoch       = data.epoch[index[0]];       data.scet = data.scet[index[0]]
    # AUX
    data.N_block     = data.N_block [index[0]]
    data.N_feed      = data.N_feed  [index[0]]
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
    data.n_time = data.Eu_i.shape[0]
    data.n_block = data.N_block[data.n_time//2]
    data.n_feed = data.N_feed[data.n_time//2]
    print("   cut1:", data.Eu_i.shape, data.n_time, data.n_block, data.n_feed)

    # ---------------------------
    # --- frequency selection ---
    # ---------------------------
    index = np.where( (data.freq_center > f_min) & (data.freq_center < f_max) )
    # Data
    data.Eu_i        = data.Eu_i [index[0]];       data.Eu_q = data.Eu_q [index[0]]
    data.Ev_i        = data.Ev_i [index[0]];       data.Ev_q = data.Ev_q [index[0]]
    data.Ew_i        = data.Ew_i [index[0]];       data.Ew_q = data.Ew_q [index[0]]
    data.time_block  = data.time_block [index[0]]; data.time        = data.time [index[0]]

    hf_hk.status_shaping(data, index[0])
    """
    data.epoch       = data.epoch[index[0]];       data.scet = data.scet[index[0]]
    # AUX
    data.N_block     = data.N_block [index[0]]
    data.N_feed      = data.N_feed  [index[0]]
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
    data.n_time = data.Eu_i.shape[0]
    data.n_block = data.N_block[data.n_time//2]
    data.n_feed = data.N_feed[data.n_time//2]
    print("  cut2:", data.Eu_i.shape, data.n_time, data.n_block, data.n_feed, "   frequency in", f_min, "-", f_max, "kHz")


    # -------------------------------------
    # Reshape to "3D: n_time * n_block * n_feed"
    # -------------------------------------
    """
    data.Eu_i = np.array(data.Eu_i).reshape(data.n_time, data.n_block, data.n_feed*128)
    data.Eu_q = np.array(data.Eu_q).reshape(data.n_time, data.n_block, data.n_feed*128)
    data.Ev_i = np.array(data.Ev_i).reshape(data.n_time, data.n_block, data.n_feed*128)
    data.Ev_q = np.array(data.Ev_q).reshape(data.n_time, data.n_block, data.n_feed*128)
    data.Ew_i = np.array(data.Ew_i).reshape(data.n_time, data.n_block, data.n_feed*128)
    data.Ew_q = np.array(data.Ew_q).reshape(data.n_time, data.n_block, data.n_feed*128)
    data.time = np.array(data.time).reshape(data.n_time, data.n_block, data.n_feed*128)
    print(" sort:", data.Eu_i.shape, data.n_time, data.n_block, data.n_feed)
    """

    return data


# ---------------------------------------------------------------------
def hf_sid23_getauto(data):
    """
    input:  data
    return: auto
    """
    # Spec formation
    auto = struct()
    auto.EuEu = np.zeros(data.n_time*data.n_block*data.n_feed*128)
    auto.EvEv = np.zeros(data.n_time*data.n_block*data.n_feed*128)
    auto.EwEw = np.zeros(data.n_time*data.n_block*data.n_feed*128)
    auto.EE   = np.zeros(data.n_time*data.n_block*data.n_feed*128)
    auto.EuEu = auto.EuEu.reshape(data.n_time, data.n_block, data.n_feed*128)
    auto.EvEv = auto.EvEv.reshape(data.n_time, data.n_block, data.n_feed*128)
    auto.EwEw = auto.EwEw.reshape(data.n_time, data.n_block, data.n_feed*128)
    auto.EE   = auto.EE.reshape(data.n_time, data.n_block, data.n_feed*128)

    for i in range(data.n_time):
        for j in range(data.n_block):
            EuEu = data.Eu_i[i][j]**2 + data.Eu_q[i][j]**2  
            EvEv = data.Ev_i[i][j]**2 + data.Ev_q[i][j]**2  
            EwEw = data.Ew_i[i][j]**2 + data.Ew_q[i][j]**2  
            EE = EuEu + EvEv + EwEw
            EuEu = stats.zscore(EuEu); EvEv = stats.zscore(EvEv); EwEw = stats.zscore(EwEw); EE = stats.zscore(EE)

            EuEu_auto = np.correlate(EuEu, EuEu, mode='full')
            EuEu_auto = EuEu_auto[EuEu_auto.shape[0]//2:]
            EuEu_auto /= len(EuEu_auto)
            auto.EuEu[i][j] = EuEu_auto

            EvEv_auto = np.correlate(EvEv, EvEv, mode='full')
            EvEv_auto = EvEv_auto[EvEv_auto.shape[0]//2:]
            EvEv_auto /= len(EvEv_auto)
            auto.EvEv[i][j] = EvEv_auto

            EwEw_auto = np.correlate(EwEw, EwEw, mode='full')
            EwEw_auto = EwEw_auto[EwEw_auto.shape[0]//2:]
            EwEw_auto /= len(EwEw_auto)
            auto.EwEw[i][j] = EwEw_auto

            EE_auto   = np.correlate(EE, EE, mode='full')
            EE_auto   = EE_auto[EE_auto.shape[0]//2:]
            EE_auto   /= len(EE_auto)
            auto.EE[i][j] = EE_auto

            auto.EuEu[i][j][0] = 0
            auto.EvEv[i][j][0] = 0
            auto.EwEw[i][j][0] = 0
            auto.EE[i][j][0] = 0
            auto.EuEu[i][j][1] = 0
            auto.EvEv[i][j][1] = 0
            auto.EwEw[i][j][1] = 0
            auto.EE[i][j][1] = 0
    return auto


# ---------------------------------------------------------------------
def hf_sid23_rime_detect(data):
    data.EuEu = (data.Eu_i * data.Eu_i + data.Eu_q * data.Eu_q) ** .5
    data.EvEv = (data.Ev_i * data.Ev_i + data.Ev_q * data.Ev_q) ** .5
    data.EwEw = (data.Ew_i * data.Ew_i + data.Ew_q * data.Ew_q) ** .5

    k0 = 0
    for i in range(data.n_time):
        for j in range(data.n_block):
            for k in range(data.n_feed*128):
                if data.EuEu[i][j][k] >= 1000:
                    if k-k0 > 80:
                        print(k0, k)
                        data.EuEu[i][j][k:k0-1] = 10000
                        k0 = k
    return data
