"""
    JUICE RPWI HF SID4 & 20: L1a QL -- 2025/10/24
"""
import glob
import numpy as np
import math
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
        if sid == 4:  data_name = '*HF*SID4_*'+ver_str+'.cdf'
        else:         data_name = '*HF*SID20_*'+ver_str+'.cdf'    
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    elif sid == 20:     # <<< SID-20 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202509 -- SAMPLE  sweep 0.02-2MHz 5s		Vin=10 mVpp
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID20_20000101T031404-20000101T031417_V01___SID04-20_0.2s_20250925-1500_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID20_20000101T051458-20000101T051512_V01___SID04-20_0.5s_20250925-1701_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID20_20000101T051753-20000101T051806_V01___SID04-20_1.0s_20250925-1704_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID20_20000101T052137-20000101T052201_V01___SID04-20_2.0s_20250925-1708_10mVpp.ccs.cdf',
                    ]
        # 202411 -- SAMPLE  1.75MHz  (100mVpp, 10mVpp, 100mVpp, 10mVpp, 100mVpp)  (0,0,0),(90,0,0),(0,90,0),(0,0,90)
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID20_20000101T000057-20000101T000114_V01___SID04-20_20241125-1517_RadioBurst_comp0_asw3.ccs.cdf',
                     'JUICE_L1a_RPWI-HF-SID20_20000101T000214-20000101T000228_V01___SID04-20_20241125-1520_RadioBurst_comp1_asw3.ccs.cdf',
                    ]                   # SG - 1.5MHz 10mVpp 90/0/0deg
        """
        # *** Ground Test - Ver.2 ***
        # 202510 -- PCW4 emulation
        data_dir = '/Users/user/G-Univ/TU/TU_C_staffs/C-Space/JUICE/data/test-TMIDX/251003_PCW4_test/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID20_20251003T080724-20251003T080912_V01___TMIDX_00001.bin.cdf']
        # 202310 -- SAMPLE
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID20_20000101T000102-20000101T000123_V01___SID04-20_20241016-1156-Radioburst.ccs.cdf',
                     #'old/JUICE_L1a_RPWI-HF-SID20_20000101T001825-20000101T001852_V01___SID04-20_20231024-0042.ccs.cdf',
                     #'old/JUICE_L1a_RPWI-HF-SID20_20000101T000046-20000101T000127_V01___SID04-20-comp0-20231117-1529.ccs.cdf',
                     #'old/JUICE_L1a_RPWI-HF-SID20_20000101T000050-20000101T000147_V01___SID04-20-comp1-20231117-1532.ccs.cdf',
                    ]
        """
        # *** Flight data: Ver.2 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = ['JUICE_L1a_RPWI-HF-SID20_20240126T113714-20240126T114759_V01___RPR2_62000007_2024.026.12.58.18.441.cdf',
                     'JUICE_L1a_RPWI-HF-SID20_20240126T114800-20240126T123719_V01___RPR2_62000008_2024.026.13.54.26.469.cdf',
                     'JUICE_L1a_RPWI-HF-SID20_20240706T121424-20240706T125428_V01___RPR2_62000002_2024.190.19.50.21.637.cdf',
                     'JUICE_L1a_RPWI-HF-SID20_20240819T203013-20240819T210936_V01___RPR2_62000004_2024.235.10.15.04.518.cdf',
                    ]
        """
        """

    else:     # <<< SID-4 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202509 -- SAMPLE  sweep 0.02-2MHz 5s		Vin=10 mVpp
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID4_20000101T031404-20000101T031414_V01___SID04-20_0.2s_20250925-1500_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID4_20000101T051505-20000101T051505_V01___SID04-20_0.5s_20250925-1701_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID4_20000101T051756-20000101T051756_V01___SID04-20_1.0s_20250925-1704_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID4_20000101T052137-20000101T052159_V01___SID04-20_2.0s_20250925-1708_10mVpp.ccs.cdf',
                    ]
        # 202411 -- SAMPLE  0.2-2MHz, 10mVpp, 0/90/0deg
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID4_20000101T000106-20000101T000106_V01___SID04-20_20241125-1517_RadioBurst_comp0_asw3.ccs.cdf',
                     'JUICE_L1a_RPWI-HF-SID4_20000101T000226-20000101T000226_V01___SID04-20_20241125-1520_RadioBurst_comp1_asw3.ccs.cdf',
                    ]
        """
        # *** Ground Test - Ver.2 ***
        # 202510 -- PCW4 emulation
        data_dir = '/Users/user/G-Univ/TU/TU_C_staffs/C-Space/JUICE/data/test-TMIDX/251003_PCW4_test/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID4_20251003T080734-20251003T080910_V01___TMIDX_00001.bin.cdf']
        """
        # 202310 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID4_20000101T000112-20000101T000123_V01___SID04-20_20241016-1156-Radioburst.ccs.cdf',
                          'old/JUICE_L1a_RPWI-HF-SID4_20000101T000057-20000101T000119_V01___SID04-20-comp0-20231117-1529.ccs.cdf',
                          'old/JUICE_L1a_RPWI-HF-SID4_20000101T000100-20000101T000144_V01___SID04-20-comp1-20231117-1532.ccs.cdf',
                          'old/JUICE_L1a_RPWI-HF-SID4_20000101T001837-20000101T001848_V01___SID04-20_20231024-0042.ccs.cdf',
                         ]
        """
        # *** Flight data: Ver.2 ***
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = ['JUICE_L1a_RPWI-HF-SID4_20240126T113727-20240126T123719_V01___RPR1_52000013_2024.026.13.22.14.423.cdf',
                     'JUICE_L1a_RPWI-HF-SID4_20240706T121439-20240706T125422_V01___RPR1_52000002_2024.190.14.59.43.630.cdf',
                     'JUICE_L1a_RPWI-HF-SID4_20240819T203025-20240819T210933_V01___RPR1_52000003_2024.233.02.43.43.102.cdf',
                    ]
        """

    print(data_dir)
    print(data_list)
    return data_dir, data_list


# ---------------------------------------------------------------------
# --- SID20 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid20_read(cdf):
    """
    input:  cdf
    return: data
    """
    data = struct()

    # Data
    # complex < 2:     # Power
    data.EuEu    = np.float64(cdf['EuEu'][...]);    data.EvEv    = np.float64(cdf['EvEv'][...]);    data.EwEw    = np.float64(cdf['EwEw'][...])
    # complex == 1:    # Matrix
    data.EuEv_re = np.float64(cdf['EuEv_re'][...]); data.EvEw_re = np.float64(cdf['EvEw_re'][...]); data.EwEu_re = np.float64(cdf['EwEu_re'][...])
    data.EuEv_im = np.float64(cdf['EuEv_im'][...]); data.EvEw_im = np.float64(cdf['EvEw_im'][...]); data.EwEu_im = np.float64(cdf['EwEu_im'][...])
    """
    # complex == 3:    # 3D-matrix
    data.EuiEui  = np.float64(cdf['EuiEui'][...]);  data.EviEvi  = np.float64(cdf['EviEvi'][...]);  data.EwiEwi  = np.float64(cdf['EwiEwi'][...]);   
    data.EuqEuq  = np.float64(cdf['EuqEuq'][...]);  data.EvqEvq  = np.float64(cdf['EvqEvq'][...]);  data.EwqEwq  = np.float64(cdf['EwqEwq'][...])
    data.EuiEvi  = np.float64(cdf['EuiEvi'][...]);  data.EviEwi  = np.float64(cdf['EviEwi'][...]);  data.EwiEui  = np.float64(cdf['EwiEui'][...]);   data.EuqEvq  = np.float64(cdf['EuqEvq'][...])
    data.EuqEvq  = np.float64(cdf['EuqEvq'][...]);  data.EvqEwq  = np.float64(cdf['EvqEwq'][...]);  data.EwqEuq  = np.float64(cdf['EwqEuq'][...]);  
    data.EuiEvq  = np.float64(cdf['EuiEvq'][...]);  data.EviEwq  = np.float64(cdf['EviEwq'][...]);  data.EwiEuq  = np.float64(cdf['EwiEuq'][...]);   
    data.EuqEvi  = np.float64(cdf['EuqEvi'][...]);  data.EvqEwi  = np.float64(cdf['EvqEwi'][...]);  data.EwqEui  = np.float64(cdf['EwqEui'][...])
    data.EuiEuq  = np.float64(cdf['EuiEuq'][...]);  data.EviEvq  = np.float64(cdf['EviEvq'][...]);  data.EwiEwq = np.float64(cdf['EwiEwq'][...])
    """
    #
    data.frequency = cdf['frequency'][...];  data.freq_step = cdf['freq_step'][...]; data.freq_width  = cdf['freq_width'][...]

    hf_hk.status_read(cdf, data)
    """
    data.epoch   = cdf['Epoch'][...];        data.scet      = cdf['SCET'][...]
    # AUX
    data.ch_selected = cdf['ch_selected'][...]
    data.complex     = cdf['complex'][...]
    data.cal_signal  = cdf['cal_signal'][...]
    data.N_block     = np.int64(cdf['N_block'][...])
    #
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])    
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])  
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    # Header
    data.N_step      = np.int64(cdf['N_step'][...])
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...];   
    data.ISW_ver     = cdf['ISW_ver'][...]
    """
    return data


def hf_sid20_add(data, data1):
    """
    input:  data, data1, sid
    return: data
    """
    # Data
    # complex < 2:     # Power
    data.EuEu    = np.r_["0", data.EuEu, data1.EuEu]
    data.EvEv    = np.r_["0", data.EvEv, data1.EvEv]
    data.EwEw    = np.r_["0", data.EwEw, data1.EwEw]
    # complex == 1:    # Matrix
    data.EuEv_re = np.r_["0", data.EuEv_re, data1.EuEv_re]; data.EuEv_im = np.r_["0", data.EuEv_im, data1.EuEv_im]
    data.EvEw_re = np.r_["0", data.EvEw_re, data1.EvEw_re]; data.EvEw_im = np.r_["0", data.EvEw_im, data1.EvEw_im]
    data.EwEu_re = np.r_["0", data.EwEu_re, data1.EwEu_re]; data.EwEu_im = np.r_["0", data.EwEu_im, data1.EwEu_im]
    """
    # complex == 3:    # 3D-matrix
    data.EuiEui  = np.r_["0", data.EuiEui, data1.EuiEui];   data.EuqEuq  = np.r_["0", data.EuqEuq, data1.EuqEuq]
    data.EviEvi  = np.r_["0", data.EviEvi, data1.EviEvi];   data.EvqEvq  = np.r_["0", data.EvqEvq, data1.EvqEvq]
    data.EwiEwi  = np.r_["0", data.EwiEwi, data1.EwiEwi];   data.EwqEwq  = np.r_["0", data.EwqEwq, data1.EwqEwq]
    #
    data.EuiEvi  = np.r_["0", data.EuiEvi, data1.EuiEvi];   data.EuqEvq  = np.r_["0", data.EuqEvq, data1.EuqEvq]
    data.EviEwi  = np.r_["0", data.EviEwi, data1.EviEwi];   data.EvqEwq  = np.r_["0", data.EvqEwq, data1.EvqEwq];    
    data.EwiEui  = np.r_["0", data.EwiEui, data1.EwiEui];   data.EwqEuq  = np.r_["0", data.EwqEuq, data1.EwqEuq]
    #
    data.EuiEvq  = np.r_["0", data.EuiEvq, data1.EuiEvq];   data.EuqEvi  = np.r_["0", data.EuqEvi, data1.EuqEvi]
    data.EviEwq  = np.r_["0", data.EviEwq, data1.EviEwq];   data.EvqEwi  = np.r_["0", data.EvqEwi, data1.EvqEwi]
    data.EwiEuq  = np.r_["0", data.EwiEuq, data1.EwiEuq];   data.EwqEui  = np.r_["0", data.EwqEui, data1.EwqEui]
    #
    data.EuiEuq  = np.r_["0", data.EuiEuq, data1.EuiEuq]
    data.EviEvq  = np.r_["0", data.EviEvq, data1.EviEvq]
    data.EwiEwq  = np.r_["0", data.EwiEwq, data1.EwiEwq]
    """
    #
    data.frequency   = np.r_["0", data.frequency,  data1.frequency]
    data.freq_step   = np.r_["0", data.freq_step,  data1.freq_step]
    data.freq_width  = np.r_["0", data.freq_width, data1.freq_width]

    hf_hk.status_add(data, data1)
    """
    data.epoch       = np.r_["0", data.epoch,      data1.epoch]
    data.scet        = np.r_["0", data.scet,       data1.scet]
    # AUX
    data.ch_selected = np.r_["0", data.ch_selected, data1.ch_selected]
    data.complex     = np.r_["0", data.complex, data1.complex]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.N_block     = np.r_["0", data.N_block, data1.N_block]
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


def hf_sid20_shaping(data, cal_mode, comp_mode):
    """
    input:  data, sid
            cal_mode    [Power]     0: background          1: CAL           2: all
            N_ch0       [channel]   2: 2-ch    3: 3-ch                   0,>3: any
            comp_mode   [Complex]   0: Poweer  1: Matrix   3: Matrix-2D    >3: any   
    return: data
    """
    # Size
    data.n_time  = data.EuEu.shape[0]
    data.n_freq  = data.EuEu.shape[1]
    data.n_step  = data.N_step [data.n_time//2]
    data.n_block = data.N_block[data.n_time//2]
    n_num = data.n_step * data.n_block

    if   data.n_freq != 72  and data.sid == 4:
        print("      [SID]", data.sid, "  *** size error ***", data.n_freq, ", not 72")
    elif data.n_freq != 360 and data.sid == 20:
        print("      [SID]", data.sid, "  *** size error ***", data.n_freq, ", not 360")
    print("  org:[SID]", data.sid, "  size:", data.EuEu.shape, data.n_time, "x", data.n_freq, "[", data.n_time*data.n_freq, "]", 
        data.n_time, "x", data.n_block, "x", data.n_step, "[", data.n_time*data.n_block*data.n_step, "]")
    if data.n_freq != n_num:
        data.EuEu    = data.EuEu   [:, 0:n_num]; data.EvEv    = data.EvEv   [:, 0:n_num]; data.EwEw    = data.EwEw   [:, 0:n_num]
        data.EuEv_re = data.EuEv_re[:, 0:n_num]; data.EvEw_re = data.EvEw_re[:, 0:n_num]; data.EwEu_re = data.EwEu_re[:, 0:n_num]
        data.EuEv_im = data.EuEv_im[:, 0:n_num]; data.EvEw_im = data.EvEw_im[:, 0:n_num]; data.EwEu_im = data.EwEu_im[:, 0:n_num]
        data.frequency  = data.frequency [:, 0:n_num]
        data.freq_step  = data.freq_step [:, 0:n_num]
        data.freq_width = data.freq_width[:, 0:n_num]
        #
        data.n_time  = data.EuEu.shape[0]
        data.n_freq  = data.EuEu.shape[1]
        data.n_step  = data.N_step [data.n_time//2]
        data.n_block = data.N_block[data.n_time//2]
        n_num = data.n_step * data.n_block
        print("  cut:[SID]", data.sid, "  size:", data.EuEu.shape, data.n_time, "x", data.n_freq, "[", data.n_time*data.n_freq, "]", 
            data.n_time, "x", data.n_block, "x", data.n_step, "[", data.n_time*data.n_block*data.n_step, "]")

    # CAL & COMP
    if cal_mode < 2 or comp_mode < 4:
        if cal_mode < 2:
            if comp_mode < 4:
                index = np.where( (data.cal_signal == cal_mode) &                   (comp_mode == data.complex) )
                print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> cal-mode:", cal_mode, " comp_mode:", comp_mode)
            else:
                index = np.where( (data.cal_signal == cal_mode)                                                 )
                print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> cal-mode:", cal_mode)
        else:
            index     = np.where(                                                   (comp_mode == data.complex) )
            print(    "  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> comp_mode:", comp_mode)

        # Data
        data.epoch     = data.epoch    [index[0]];  data.scet      = data.scet     [index[0]]
        data.frequency = data.frequency[index[0]];  data.freq_step = data.freq_step[index[0]];  data.freq_width = data.freq_width[index[0]]
        # complex < 2:     # Power
        data.EuEu    = data.EuEu   [index[0]]; data.EvEv    = data.EvEv   [index[0]]; data.EwEw    = data.EwEw   [index[0]]
        # complex == 1:    # Matrix
        data.EuEv_re = data.EuEv_re[index[0]]; data.EvEw_re = data.EvEw_re[index[0]]; data.EwEu_re = data.EwEu_re[index[0]]
        data.EuEv_im = data.EuEv_im[index[0]]; data.EvEw_im = data.EvEw_im[index[0]]; data.EwEu_im = data.EwEu_im[index[0]]
        """
        # complex == 3:    # 3D-matrix
        data.EuiEui  = data.EuiEui [index[0]]; data.EviEvi  = data.EviEvi [index[0]]; data.EwiEwi  = data.EwiEwi [index[0]]
        data.EuqEuq  = data.EuqEuq [index[0]]; data.EvqEvq  = data.EvqEvq [index[0]]; data.EwqEwq  = data.EwqEwq [index[0]]
        data.EuiEvi  = data.EuiEvi [index[0]]; data.EviEwi  = data.EviEwi [index[0]]; data.EwiEui  = data.EwiEui [index[0]]
        data.EuqEvq  = data.EuqEvq [index[0]]; data.EvqEwq  = data.EvqEwq [index[0]]; data.EwqEuq  = data.EwqEuq [index[0]]
        data.EuiEvq  = data.EuiEvq [index[0]]; data.EviEwq  = data.EviEwq [index[0]]; data.EwiEuq  = data.EwiEuq [index[0]]
        data.EuqEvi  = data.EuqEvi [index[0]]; data.EvqEwi  = data.EvqEwi [index[0]]; data.EwqEui  = data.EwqEui [index[0]]
        data.EuiEuq  = data.EuiEuq [index[0]]; data.EviEvq  = data.EviEvq [index[0]]; data.EwiEwq  = data.EwiEwq [index[0]]
        """

        hf_hk.status_shaping(data, index[0])
        """
        # AUX
        data.ch_selected = data.ch_selected[index[0]]; data.complex    = data.complex   [index[0]]
        data.cal_signal  = data.cal_signal[index[0]];  data.N_block    = data.N_block   [index[0]]
        #
        data.T_RWI_CH1   = data.T_RWI_CH1 [index[0]];  data.T_RWI_CH2  = data.T_RWI_CH2 [index[0]];  data.T_HF_FPGA = data.T_HF_FPGA [index[0]]
        # Header
        data.N_step      = data.N_step    [index[0]];  data.ADC_ovrflw = data.ADC_ovrflw[index[0]];  data.ISW_ver   = data.ISW_ver   [index[0]]
        """

        n_time = data.EuEu.shape[0]
        if cal_mode < 2:
            if comp_mode < 4: print("  cut:", data.EuEu.shape, n_time, "x", data.n_freq, "===> cal-mode:", cal_mode, " comp_mode:", comp_mode)
            else:             print("  cut:", data.EuEu.shape, n_time, "x", data.n_freq, "===> cal-mode:", cal_mode)
            if cal_mode == 0: print("<only BG>")
            else:             print("<only CAL>")
        else:                 print("  cut:", data.EuEu.shape, n_time, "x", data.n_freq, "===> comp_mode:", comp_mode)

    # NAN
    index = np.where(data.complex == 0)
    data.EuEv_re   [index[0]] = math.nan; data.EvEw_re   [index[0]] = math.nan; data.EwEu_re   [index[0]] = math.nan
    data.EuEv_im   [index[0]] = math.nan; data.EvEw_im   [index[0]] = math.nan; data.EwEu_im   [index[0]] = math.nan
    #
    """
    index = np.where(data.complex != 3)
    data.EuiEui    [index[0]] = math.nan; data.EviEvi    [index[0]] = math.nan; data.EwiEwi    [index[0]] = math.nan
    data.EuqEuq    [index[0]] = math.nan; data.EvqEvq    [index[0]] = math.nan; data.EwqEwq    [index[0]] = math.nan
    data.EuiEvi    [index[0]] = math.nan; data.EviEwi    [index[0]] = math.nan; data.EwiEui    [index[0]] = math.nan
    data.EuqEvq    [index[0]] = math.nan; data.EvqEwq    [index[0]] = math.nan; data.EwqEuq    [index[0]] = math.nan
    data.EuiEvq    [index[0]] = math.nan; data.EviEwq    [index[0]] = math.nan; data.EwiEuq    [index[0]] = math.nan
    data.EuqEvi    [index[0]] = math.nan; data.EvqEwi    [index[0]] = math.nan; data.EwqEui    [index[0]] = math.nan
    data.EuiEuq    [index[0]] = math.nan; data.EviEvq    [index[0]] = math.nan; data.EwiEwq    [index[0]] = math.nan
    """

    # *** frequncy & width for spec cal
    data.freq   = data.frequency
    data.freq_w = data.freq_width

    # Size
    data.n_time  = data.EuEu.shape[0]
    data.n_freq  = data.EuEu.shape[1]
    data.n_step  = data.N_step [data.n_time//2]
    data.n_block = data.N_block[data.n_time//2]

    return data


def spec_nan(data, i):
    data.EuEu      [i] = math.nan; data.EvEv      [i] = math.nan; data.EwEw      [i] = math.nan
    data.EuEv_re   [i] = math.nan; data.EvEw_re   [i] = math.nan; data.EwEu_re   [i] = math.nan
    data.EuEv_im   [i] = math.nan; data.EvEw_im   [i] = math.nan; data.EwEu_im   [i] = math.nan
    """
    data.EuiEui    [i] = math.nan; data.EviEvi    [i] = math.nan; data.EwiEwi    [i] = math.nan
    data.EuqEuq    [i] = math.nan; data.EvqEvq    [i] = math.nan; data.EwqEwq    [i] = math.nan
    data.EuiEvi    [i] = math.nan; data.EviEwi    [i] = math.nan; data.EwiEui    [i] = math.nan
    data.EuqEvq    [i] = math.nan; data.EvqEwq    [i] = math.nan; data.EwqEuq    [i] = math.nan
    data.EuiEvq    [i] = math.nan; data.EviEwq    [i] = math.nan; data.EwiEuq    [i] = math.nan
    data.EuqEvi    [i] = math.nan; data.EvqEwi    [i] = math.nan; data.EwqEui    [i] = math.nan
    data.EuiEuq    [i] = math.nan; data.EviEvq    [i] = math.nan; data.EwiEwq    [i] = math.nan
    """
    
    hf_hk.status_nan(data, i)
