"""
    JUICE RPWI HF SID4 & 20: L1a QL -- 2026/3/4
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
        base_dir = '/Users/D-Univ/data/data-JUICE/datasets/'         # ASW2
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
        # 202601-- ASW3 test
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID20_20260109T153335-20260109T154241_V01___Sec01_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID20_20260109T155142-20260109T160048_V01___Sec02_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID20_20260109T230757-20260109T231704_V01___Sec16_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID20_20260109T233814-20260109T234720_V01___Sec18_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID20_20260109T235245-20260110T000148_V01___Sec19_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID20_20260110T000730-20260110T001635_V01___Sec20_260118.bin.cdf',
                    ]
        # 202511 -- SAMPLE  sweep 0.02-2MHz 5s		Vin=10 mVpp
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID20_20000101T000046-20000101T000506_V01___SID4-20_20251123-1107.ccs.cdf',         # .2s(10s)>.5s(10s)>1s(20s)>2s(30s))  f = 1.8 [MHz]
                     #'JUICE_L1a_RPWI-HF-SID20_20000101T000718-20000101T001159_V01___SID4-20_20251123-1345.ccs.cdf',         # .2s(10s)>.5s(10s)>1s(20s)>2s(30s))  int=1 [s]	 f = 0.02 0.1 0.5 1.1 1.8 [MHz]
                     #'JUICE_L1a_RPWI-HF-SID20_20000101T000823-20000101T001238_V01___SID4-20_20251123-1114.ccs.cdf',         # .2s(10s)>.5s(10s)>1s(20s)>2s(30s))  int=1 [s]	 f = 0.02 0.1 0.5 1.1 1.8 [MHz]
                     #'JUICE_L1a_RPWI-HF-SID20_20000101T002118-20000101T002307_V01___SID4-20_0.5s_20251113-1736.ccs.cdf',    # int=1[s]	f = 0.02 0.1 0.5 1.1 1.8 [MHz]
                     #'JUICE_L1a_RPWI-HF-SID20_20000101T002515-20000101T002833_V01___SID4-20_20251113-1741.ccs.cdf',			#           f = 1.8 [MHz]
                    ]
        """
        # 202509 -- SAMPLE  sweep 0.02-2MHz 5s		Vin=10 mVpp
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old2/'
        data_list = ['JUICE_L1a_RPWI-HF-SID20_20000101T031404-20000101T031417_V01___SID04-20_0.2s_20250925-1500_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID20_20000101T051458-20000101T051512_V01___SID04-20_0.5s_20250925-1701_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID20_20000101T051753-20000101T051806_V01___SID04-20_1.0s_20250925-1704_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID20_20000101T052137-20000101T052201_V01___SID04-20_2.0s_20250925-1708_10mVpp.ccs.cdf',
                    ]
        """
        # *** Ground Test - Ver.2 ***
        """
        # 202510 -- PCW4 emulation
        data_dir = '/Users/user/G-Univ/TU/TU_C_staffs/C-Space/JUICE/data/test-TMIDX/251003_PCW4_test/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID20_20251003T080724-20251003T080912_V01___TMIDX_00001.bin.cdf']
        # 202310 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID20_20000101T000102-20000101T000123_V01___SID04-20_20241016-1156-Radioburst.ccs.cdf',
                     #'old/JUICE_L1a_RPWI-HF-SID20_20000101T001825-20000101T001852_V01___SID04-20_20231024-0042.ccs.cdf',
                     #'old/JUICE_L1a_RPWI-HF-SID20_20000101T000046-20000101T000127_V01___SID04-20-comp0-20231117-1529.ccs.cdf',
                     #'old/JUICE_L1a_RPWI-HF-SID20_20000101T000050-20000101T000147_V01___SID04-20-comp1-20231117-1532.ccs.cdf',
                    ]
        """
        # *** Flight data: Ver.2 ***
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID20_20240126T113714-20240126T114759_V01___RPR2_62000007_2024.026.12.58.18.441.cdf',
                     #'JUICE_L1a_RPWI-HF-SID20_20240126T114800-20240126T123719_V01___RPR2_62000008_2024.026.13.54.26.469.cdf',
                     #'JUICE_L1a_RPWI-HF-SID20_20240706T121424-20240706T125428_V01___RPR2_62000002_2024.190.19.50.21.637.cdf',
                     'JUICE_L1a_RPWI-HF-SID20_20240819T203013-20240819T210936_V01___RPR2_62000004_2024.235.10.15.04.518.cdf',
                    ]
        """

    else:     # <<< SID-4 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202601-- ASW3 test
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID4_20260109T153335-20260109T154240_V01___Sec01_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID4_20260109T155142-20260109T160047_V01___Sec02_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID4_20260109T230757-20260109T231704_V01___Sec16_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID4_20260109T233814-20260109T234719_V01___Sec18_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID4_20260109T235245-20260110T000147_V01___Sec19_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID4_20260110T000730-20260110T001635_V01___Sec20_260118.bin.cdf',
                    ]
        # 202511 -- SAMPLE  sweep 0.02-2MHz 5s		Vin=10 mVpp
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID4_20000101T000046-20000101T000420_V01___SID4-20_20251123-1107.ccs.cdf',         # .2s(10s)>.5s(10s)>1s(20s)>2s(30s))  f = 1.8 [MHz]
                     #'JUICE_L1a_RPWI-HF-SID4_20000101T000718-20000101T001114_V01___SID4-20_20251123-1345.ccs.cdf',         # .2s(10s)>.5s(10s)>1s(20s)>2s(30s))  int=1 [s]	 f = 0.02 0.1 0.5 1.1 1.8 [MHz]
                     #'JUICE_L1a_RPWI-HF-SID4_20000101T002127-20000101T002138_V01___SID4-20_0.5s_20251113-1736.ccs.cdf',    # int=1[s]	f = 0.02 0.1 0.5 1.1 1.8 [MHz]
                     #'JUICE_L1a_RPWI-HF-SID4_20000101T002522-20000101T002759_V01___SID4-20_20251113-1741.ccs.cdf',		   #           f = 1.8 [MHz]
                    ]
        """
        # 202509 -- SAMPLE  sweep 0.02-2MHz 5s		Vin=10 mVpp
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old2/'
        data_list = ['JUICE_L1a_RPWI-HF-SID4_20000101T031404-20000101T031414_V01___SID04-20_0.2s_20250925-1500_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID4_20000101T051505-20000101T051505_V01___SID04-20_0.5s_20250925-1701_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID4_20000101T051756-20000101T051756_V01___SID04-20_1.0s_20250925-1704_10mVpp.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID4_20000101T052137-20000101T052159_V01___SID04-20_2.0s_20250925-1708_10mVpp.ccs.cdf',
                    ]
        """
        # *** Ground Test - Ver.2 ***
        """
        # 202510 -- PCW4 emulation
        data_dir = '/Users/user/G-Univ/TU/TU_C_staffs/C-Space/JUICE/data/test-TMIDX/251003_PCW4_test/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID4_20251003T080734-20251003T080910_V01___TMIDX_00001.bin.cdf']
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
    #
    data.EuEu_amp = np.float64(cdf['EuEu_amp'][...]);   data.EuEu_raw = np.float64(cdf['EuEu_raw'][...])
    data.EvEv_amp = np.float64(cdf['EvEv_amp'][...]);   data.EvEv_raw = np.float64(cdf['EvEv_raw'][...])
    data.EwEw_amp = np.float64(cdf['EwEw_amp'][...]);   data.EwEw_raw = np.float64(cdf['EwEw_raw'][...])
    data.gain_raw = cdf['gain_raw'][...];               data.df_raw = cdf['df_raw'][...]
    #
    data.frequency = cdf['frequency'][...];  data.freq_step = cdf['freq_step'][...]; data.freq_width  = cdf['freq_width'][...]

    hf_hk.status_read(cdf, data)
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
    #
    data.EuEu_raw   = np.r_["0", data.EuEu_raw, data1.EuEu_raw];    data.EuEu_amp   = np.r_["0", data.EuEu_amp, data1.EuEu_amp]
    data.EvEv_raw   = np.r_["0", data.EvEv_raw, data1.EvEv_raw];    data.EvEv_amp   = np.r_["0", data.EvEv_amp, data1.EvEv_amp]
    data.EwEw_raw   = np.r_["0", data.EwEw_raw, data1.EwEw_raw];    data.EwEw_amp   = np.r_["0", data.EwEw_amp, data1.EwEw_amp]
    data.gain_raw   = np.r_["0", data.gain_raw, data1.gain_raw];    data.df_raw     = np.r_["0", data.df_raw, data1.df_raw]
    #
    data.frequency  = np.r_["0", data.frequency,  data1.frequency]
    data.freq_step  = np.r_["0", data.freq_step,  data1.freq_step]
    data.freq_width = np.r_["0", data.freq_width, data1.freq_width]

    hf_hk.status_add(data, data1)
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
    if data.sid in [20]:
        data.n_block = data.N_block[data.n_time//2]
    else:
        data.n_block = 1
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
        data.EuEu_raw = data.EuEu_raw[:, 0:n_num]; data.EvEv_raw = data.EvEv_raw[:, 0:n_num]; data.EwEw_raw = data.EwEw_raw[:, 0:n_num]
        data.EuEu_amp = data.EuEu_amp[:, 0:n_num]; data.EvEv_amp = data.EvEv_amp[:, 0:n_num]; data.EwEw_amp = data.EwEw_amp[:, 0:n_num]
        #
        data.n_time  = data.EuEu.shape[0]
        data.n_freq  = data.EuEu.shape[1]
        data.n_step  = data.N_step [data.n_time//2]
        if data.sid in [20]:
            data.n_block = data.N_block[data.n_time//2]
        else:
            data.n_block = 1
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
        #
        data.EuEu_raw = data.EuEu_raw[index[0]]; data.EvEv_raw = data.EvEv_raw[index[0]]; data.EwEw_raw = data.EwEw_raw[index[0]]
        data.EuEu_amp = data.EuEu_amp[index[0]]; data.EvEv_amp = data.EvEv_amp[index[0]]; data.EwEw_amp = data.EwEw_amp[index[0]]
        data.gain_raw = data.gain_raw[index[0]]; data.df_raw   = data.df_raw  [index[0]]

        hf_hk.status_shaping(data, index[0])

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

    # *** frequncy & width for spec cal
    data.freq   = data.frequency
    data.freq_w = data.freq_width

    # Size
    data.n_time  = data.EuEu.shape[0]
    data.n_freq  = data.EuEu.shape[1]
    data.n_step  = data.N_step [data.n_time//2]
    if data.sid in [20]:
        data.n_block = data.N_block[data.n_time//2]
    else:
        data.n_block = 1

    return data


def spec_nan(data, i):
    data.EuEu      [i] = math.nan; data.EvEv      [i] = math.nan; data.EwEw      [i] = math.nan
    data.EuEv_re   [i] = math.nan; data.EvEw_re   [i] = math.nan; data.EwEu_re   [i] = math.nan
    data.EuEv_im   [i] = math.nan; data.EvEw_im   [i] = math.nan; data.EwEu_im   [i] = math.nan
    #
    data.EuEu_raw  [i] = math.nan; data.EvEv_raw  [i] = math.nan; data.EwEw_raw  [i] = math.nan
    data.EuEu_amp  [i] = math.nan; data.EvEv_amp  [i] = math.nan; data.EwEw_amp  [i] = math.nan
    
    hf_hk.status_nan(data, i)
