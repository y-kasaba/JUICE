"""
    JUICE RPWI HF SID23 (PSSR3 rich) and SID8 (PSSR3 survey RAW): L1a QL -- 2026/3/4
"""
import glob
import numpy          as np
import scipy.stats    as stats
import juice_hf_hk_lib as hf_hk
import juice_cdf_lib   as hk_cdf
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
        base_dir = '/Users/D-Univ/data/data-JUICE/datasets/'
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        data_name = '*HF*SID23_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    elif sid == 23: 	# <<< SID-23 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202601-- ASW3 test
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID23_20260109T172713-20260109T173543_V01___Sec07_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID23_20260109T174710-20260109T175540_V01___Sec08_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID23_20260109T180233-20260109T181103_V01___Sec09_260118.bin.cdf',
                    ]    
        # 202511 -- SAMPLE
        # HF_20251113-2224	PSSR3 (param0 = 0)	    1.75 1.8 1.85 [MHz]   Vin = 10mVpp
        # HF_20251204-0844  PSSR3 (param0 = 1->0)	1.75 1.8 1.85 [MHz]   Vin = 10mVpp
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = [# 'JUICE_L1a_RPWI-HF-SID23_20000101T000155-20000101T000503_V01___SID7-23_P0_20251113-2224.ccs.cdf'
                     'JUICE_L1a_RPWI-HF-SID23_20000101T000049-20000101T000708_V01___SID7-23_P1_20251204-0844.ccs.cdf',
                    ]
        """
        # 202509 -- SAMPLE  Freq = 1.8, 1.85, 1.75, 1.9, 1.7 MHz  Vin = 10mVpp
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old2/'
        data_list = ['JUICE_L1a_RPWI-HF-SID23_20000101T064546-20000101T064910_V01___SID07-23_20250925-1722_10mVpp.ccs.cdf']
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
        """
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

    else:               # <<< SID-08 test datas >>>
        # 202601-- ASW3 test
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID8_20260109T172713-20260109T173543_V01___Sec07_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID8_20260109T174710-20260109T175540_V01___Sec08_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID8_20260109T180233-20260109T181103_V01___Sec09_260118.bin.cdf'
                    ]
        # 202512 -- SAMPLE
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID8_20000101T000504-20000101T000708_V01___SID7-23_P1_20251204-0844.ccs.cdf',
        ]
        """

    print(data_dir)
    print(data_list)
    return data_dir, data_list


# ---------------------------------------------------------------------
# --- SID23 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid23_read(cdf):
    """
    input:  CDF
    return: data
    """
    data = struct()
    #data.RPWI_FSW_version = cdf['ISW_ver'][...]
    #data.RPWI_FSW_version = data.RPWI_FSW_version[0]

    # Data
    data.Eu_i        = np.float64(cdf['Eu_i'][...]);       data.Eu_q = np.float64(cdf['Eu_q'][...])
    data.Ev_i        = np.float64(cdf['Ev_i'][...]);       data.Ev_q = np.float64(cdf['Ev_q'][...])
    data.Ew_i        = np.float64(cdf['Ew_i'][...]);       data.Ew_q = np.float64(cdf['Ew_q'][...])
    data.time_block  = np.float64(cdf['time_block'][...]); data.time = np.float64(cdf['time'][...])

    # Spectrum Data
    data.spec_EuEu = np.float64(cdf['EuEu_raw'][...])
    data.spec_EvEv = np.float64(cdf['EvEv_raw'][...])
    data.spec_EwEw = np.float64(cdf['EwEw_raw'][...])
    data.spec_EuEu_amp = np.float64(cdf['EuEu_amp'][...]);  data.spec_EuEu_raw = np.float64(cdf['EuEu_raw'][...])
    data.spec_EvEv_amp = np.float64(cdf['EvEv_amp'][...]);  data.spec_EvEv_raw = np.float64(cdf['EvEv_raw'][...])
    data.spec_EwEw_amp = np.float64(cdf['EwEw_amp'][...]);  data.spec_EwEw_raw = np.float64(cdf['EwEw_raw'][...])
    data.gain_raw = cdf['gain_raw'][...];      data.df_raw = cdf['df_raw'][...]

    hf_hk.status_read(cdf, data)
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

    # Spectrum Data
    data.spec_EuEu   = np.r_["0", data.spec_EuEu,   data1.spec_EuEu]
    data.spec_EvEv   = np.r_["0", data.spec_EvEv,   data1.spec_EvEv]
    data.spec_EwEw   = np.r_["0", data.spec_EwEw,   data1.spec_EwEw]
    data.spec_EuEu_amp = np.r_["0", data.spec_EuEu_amp, data1.spec_EuEu_amp]
    data.spec_EvEv_amp = np.r_["0", data.spec_EvEv_amp, data1.spec_EvEv_amp]
    data.spec_EwEw_amp = np.r_["0", data.spec_EwEw_amp, data1.spec_EwEw_amp]
    data.spec_EuEu_raw = np.r_["0", data.spec_EuEu_raw, data1.spec_EuEu_raw]
    data.spec_EvEv_raw = np.r_["0", data.spec_EvEv_raw, data1.spec_EvEv_raw]
    data.spec_EwEw_raw = np.r_["0", data.spec_EwEw_raw, data1.spec_EwEw_raw]
    data.gain_raw   = np.r_["0", data.gain_raw, data1.gain_raw]
    data.df_raw     = np.r_["0", data.df_raw,   data1.df_raw]

    hf_hk.status_add(data, data1)
    return data


def hf_sid23_shaping(data, f_max, f_min):
    """
    input:  data, f_max, f_min
    return: data
    """
    # Size - original
    data.n_time = data.Eu_i.shape[0]
    data.n_block = data.Eu_i.shape[1]  # data.N_block[data.n_time//2]
    data.n_samp = data.N_samp[data.n_time//2]
    print("    org:", data.Eu_i.shape, data.n_time, data.n_block, data.n_samp)

    """
    # -------------------
    # --- shape-check ---
    # -------------------
    index = np.where( (data.N_block == data.n_block) & (data.N_samp == data.n_samp) )
    # Data
    data.Eu_i        = data.Eu_i [index[0]];       data.Eu_q = data.Eu_q [index[0]]
    data.Ev_i        = data.Ev_i [index[0]];       data.Ev_q = data.Ev_q [index[0]]
    data.Ew_i        = data.Ew_i [index[0]];       data.Ew_q = data.Ew_q [index[0]]
    data.time_block  = data.time_block [index[0]]; data.time = data.time [index[0]]

    data.spec_EuEu_amp = data.spec_EuEu_amp[index[0]];  data.spec_EuEu_raw = data.spec_EuEu_raw[index[0]]
    data.spec_EvEv_amp = data.spec_EvEv_amp[index[0]];  data.spec_EvEv_raw = data.spec_EvEv_raw[index[0]]
    data.spec_EwEw_amp = data.spec_EwEw_amp[index[0]];  data.spec_EwEw_raw = data.spec_EwEw_raw[index[0]]
    data.gain_raw  = data.gain_raw[index[0]];           data.df_raw     = data.df_raw[index[0]]

    hf_hk.status_shaping(data, index[0])
    #
    # Size - after frequency selection
    data.n_time = data.Eu_i.shape[0]
    data.n_block = data.N_block[data.n_time//2]
    data.n_samp = data.N_samp[data.n_time//2]
    print("   cut1:", data.Eu_i.shape, data.n_time, data.n_block, data.n_samp)
    """

    # ---------------------------
    # --- frequency selection ---
    # ---------------------------
    index = np.where( (data.freq_center > f_min) & (data.freq_center < f_max) )
    # Data
    data.Eu_i        = data.Eu_i [index[0]];       data.Eu_q = data.Eu_q [index[0]]
    data.Ev_i        = data.Ev_i [index[0]];       data.Ev_q = data.Ev_q [index[0]]
    data.Ew_i        = data.Ew_i [index[0]];       data.Ew_q = data.Ew_q [index[0]]
    data.time_block  = data.time_block [index[0]]; data.time = data.time [index[0]]

    hf_hk.status_shaping(data, index[0])
    #
    # Size - after frequency selection
    data.n_time = data.Eu_i.shape[0]
    data.n_block = data.Eu_i.shape[1]  # data.N_block[data.n_time//2]
    data.n_samp = data.N_samp[data.n_time//2]
    print("  cut2:", data.Eu_i.shape, data.n_time, data.n_block, data.n_samp, "   frequency in", f_min, "-", f_max, "kHz")
    return data


# ---------------------------------------------------------------------
def hf_sid23_getauto(data):
    """
    input:  data
    return: auto
    """
    # Spec formation
    auto = struct()
    auto.EuEu = np.zeros(data.n_time*data.n_block*data.n_samp)
    auto.EvEv = np.zeros(data.n_time*data.n_block*data.n_samp)
    auto.EwEw = np.zeros(data.n_time*data.n_block*data.n_samp)
    auto.EE   = np.zeros(data.n_time*data.n_block*data.n_samp)
    auto.EuEu = auto.EuEu.reshape(data.n_time, data.n_block, data.n_samp)
    auto.EvEv = auto.EvEv.reshape(data.n_time, data.n_block, data.n_samp)
    auto.EwEw = auto.EwEw.reshape(data.n_time, data.n_block, data.n_samp)
    auto.EE   = auto.EE.reshape(data.n_time, data.n_block, data.n_samp)

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
            print(i, j, "EuEu_auto shape:", EuEu_auto.shape, "EuEu shape:", EuEu.shape, auto.EuEu.shape)
            # 0 0 EuEu_auto shape: (3328,) EuEu shape: (3328,) (8, 45, 0)
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
            for k in range(data.n_samp):
                if data.EuEu[i][j][k] >= 1000:
                    if k-k0 > 80:
                        print(k0, k)
                        data.EuEu[i][j][k:k0-1] = 10000
                        k0 = k
    return data
