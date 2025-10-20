"""
    JUICE RPWI HF SID2 (RAW): L1a read -- 2025/10/20
"""
import glob
import numpy as np
import math
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
        data_name = '*HF*SID2_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    else:
        # *** Ground Test - Ver.3 ***
        # 202509 -- SAMPLE --1.5MHz	OFF-> 10mVpp->100mVpp->500mVpp-> OFF (500mVpp - saturated)
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID2_20000101T000327-20000101T000857_V01___SID02_20251010-1729.ccs.cdf']
        """
        # 202411 -- SAMPLE -- SG - 1.75MHz 100mVpp 90/0/0deg
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old/'
        data_list = ['JUICE_L1a_RPWI-HF-SID2_20000101T000129-20000101T000229_V01___SID02_20241125-1316_asw3.ccs.cdf']
        """

        # *** Ground Test - Ver.2 ***
        # 202410 -- SAMPLE -- SG - 1.0MHz 10mVpp 90/0/0deg
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID2_20000101T000154-20000101T000454_V01___SID02_20241021-1026.ccs.cdf',                     
                     #'old/JUICE_L1a_RPWI-HF-SID2_20000101T000413-20000101T000513_V01___SID02_20231117-1607.ccs.cdf',
                     #'old/JUICE_L1a_RPWI-HF-SID2_20000101T001617-20000101T001647_V01___SID02_20231007-0349.ccs.cdf',
                   ]
        """

        # *** Flight - Ver.2 ***
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID2_20240125T112327-20240125T113141_V01___RPR1_52000011_2024.025.15.57.21.441.cdf',    # f_max: 44888.625
                     #'JUICE_L1a_RPWI-HF-SID2_20240125T152238-20240125T152330_V01___RPR1_52000012_2024.025.16.07.08.425.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20240822T023129-20240822T023713_V01___RPR1_52000003_2024.235.03.19.13.483.cdf',    # f_max: 44813.
                     #'JUICE_L1a_RPWI-HF-SID2_20240822T023715-20240822T023953_V01___RPR1_52000004_2024.236.08.13.31.519.cdf',
                     'JUICE_L1a_RPWI-HF-SID2_20250331T005104-20250331T233757_V01___RPR1_52000005_2025.091.16.38.56.448.cdf',    # CAL
        ]
        """

        # [MEMO: ASW1 data]  *** Flight - Ver.1
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW1/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID2_20230419T135855-20230419T141235_V01___RPR1_52000000_2023.109.16.17.21.607.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230419T141237-20230419T141408_V01___RPR1_52000001_2023.109.17.51.54.600.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230530T100330-20230530T100930_V01___RPR1_52000010_2023.150.10.40.53.663.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230530T100932-20230530T100942_V01___RPR1_52000011_2023.150.10.41.53.508.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230601T120804-20230601T120902_V01___RPR1_52000015_2023.152.12.32.12.471.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230601T121440-20230601T121538_V01___RPR1_52000016_2023.152.13.14.38.473.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230601T122143-20230601T122241_V01___RPR1_52000017_2023.152.13.55.02.539.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230601T122712-20230601T122810_V01___RPR1_52000018_2023.152.14.35.37.467.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230601T123421-20230601T123519_V01___RPR1_52000019_2023.152.15.15.55.483.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T090437-20230712T093851_V01___RPR1_52000001_2023.193.10.24.57.479.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T093945-20230712T101359_V01___RPR1_52000002_2023.194.08.38.36.474.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T101453-20230712T104151_V01___RPR1_52000003_2023.194.10.18.44.478.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T104153-20230712T232410_V01___RPR1_52000004_2023.194.11.15.35.498.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T232412-20230712T235200_V01___RPR1_52000005_2023.195.09.10.17.486.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T235202-20230713T001858_V01___RPR1_52000006_2023.195.10.28.57.506.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T001900-20230713T004648_V01___RPR1_52000007_2023.195.11.42.37.540.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T004652-20230713T011346_V01___RPR1_52000008_2023.195.12.39.02.479.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T011440-20230713T014138_V01___RPR1_52000009_2023.195.13.03.08.470.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T014140-20230713T020928_V01___RPR1_5200000A_2023.195.13.25.22.477.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T020932-20230713T023721_V01___RPR1_5200000B_2023.195.13.47.46.500.cdf',
                     # 'JUICE_L1a_RPWI-HF-SID2_20230713T023723-20230713T030419_V01___RPR1_5200000C_2023.195.14.10.35.574.cdf',
                     'JUICE_L1a_RPWI-HF-SID2_20230713T030513-20230713T033211_V01___RPR1_5200000D_2023.195.14.33.20.470.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T033213-20230713T040003_V01___RPR1_5200000E_2023.195.14.55.41.474.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T040005-20230713T042755_V01___RPR1_5200000F_2023.195.15.18.00.472.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T042757-20230713T045453_V01___RPR1_52000010_2023.195.15.40.11.470.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T045547-20230713T050921_V01___RPR1_52000011_2023.195.16.14.20.468.cdf',
                    ]
        """

    print(data_dir)
    print(data_list)
    return data_dir, data_list


# ---------------------------------------------------------------------
# --- SID2 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid2_read(cdf):
    """
    input:  CDF, FSW version
    return: data
    """
    data = struct()

    # Data
    data.Eu_i      = np.float64(cdf['Eu_i'][...]);  data.Eu_q = np.float64(cdf['Eu_q'][...])
    data.Ev_i      = np.float64(cdf['Ev_i'][...]);  data.Ev_q = np.float64(cdf['Ev_q'][...])
    data.Ew_i      = np.float64(cdf['Ew_i'][...]);  data.Ew_q = np.float64(cdf['Ew_q'][...])
    data.frequency = cdf['frequency'][...];  data.freq_step = cdf['freq_step'][...]; data.freq_width = cdf['freq_width'][...]
    data.time      = cdf['time'][...];       

    hf_hk.status_read(cdf, data, 2)
    """
    data.epoch     = cdf['Epoch'][...];     data.scet      = cdf['SCET'][...]
    # AUX
    data.ch_selected = cdf['ch_selected'][...]
    data.cal_signal  = cdf['cal_signal'][...]
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    # Header
    data.N_samp      = np.int64(cdf['N_samp'][...])
    data.N_step      = np.int64(cdf['N_step'][...])
    data.decimation  = cdf['decimation'][...]
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...] 
    data.ISW_ver     = cdf['ISW_ver'][...]
    data.HF_QF       = cdf['HF_QF'][...]    # Quality flag: b0:RWI-off b1:Cal b2-3:Ovrflw b4:RIME b5-7:n/a (b0-1=3:error)'
    """

    # ### ASW1: SPECIAL: data shift -16
    date = data.epoch[0];  month = date.strftime('%Y%m')
    if month == "202304" or month == "202305" or month == "202307":
        data.Eu_i = np.roll(data.Eu_i, -16);  data.Eu_q = np.roll(data.Eu_q, -16)
        data.Ev_i = np.roll(data.Ev_i, -16);  data.Ev_q = np.roll(data.Ev_q, -16)
        data.Ew_i = np.roll(data.Ew_i, -16);  data.Ew_q = np.roll(data.Ew_q, -16)
        print("-16 shift in ASW1 data")
    return data


def hf_sid2_add(data, data1):
    # Data
    data.Eu_i        = np.r_["0", data.Eu_i, data1.Eu_i]
    data.Eu_q        = np.r_["0", data.Eu_q, data1.Eu_q]
    data.Ev_i        = np.r_["0", data.Ev_i, data1.Ev_i]
    data.Ev_q        = np.r_["0", data.Ev_q, data1.Ev_q]
    data.Ew_i        = np.r_["0", data.Ew_i, data1.Ew_i]
    data.Ew_q        = np.r_["0", data.Ew_q, data1.Ew_q]
    #
    data.frequency   = np.r_["0", data.frequency, data1.frequency]
    data.freq_step   = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width  = np.r_["0", data.freq_width, data1.freq_width]
    data.time        = np.r_["0", data.time, data1.time]

    hf_hk.status_add(data, data1, 2)
    """
    data.epoch       = np.r_["0", data.epoch, data1.epoch]
    data.scet        = np.r_["0", data.scet,  data1.scet]
    # AUX
    data.ch_selected = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.N_samp      = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step      = np.r_["0", data.N_step, data1.N_step]
    data.decimation  = np.r_["0", data.decimation, data1.decimation]
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver     = np.r_["0", data.ISW_ver, data1.ISW_ver]
    data.HF_QF       = np.r_["0", data.HF_QF, data1.HF_QF]
    """
    return data


def hf_sid2_shaping(data, cal_mode):
    """
    input:  data, cal_mode
    return: data
    """
    data.n_time = data.Eu_i.shape[0]
    data.n_step = data.N_step[data.n_time//2]
    data.n_samp = data.N_samp[data.n_time//2]
    n_num = data.n_step * data.n_samp
    print("  org:", data.Eu_i.shape, data.n_time, "x", data.n_step, "x", data.n_samp, "[", n_num, "]")

    # N_step selection
    index = np.where(data.N_step != data.n_step);  print(" [error packets]", index[0], data.N_step[index[0]], data.epoch[index[0]])
    index = np.where(data.N_step == data.n_step);  data = hf_sid2_select_time(data, index);  data.n_time = data.Eu_i.shape[0]
    print(" cut0:", data.Eu_i.shape, data.n_time, "  <n_step selection>")
    # N_samp selection
    index = np.where(data.N_samp != data.n_samp);  print(" [error packets]", index[0], data.N_step[index[0]], data.epoch[index[0]])
    index = np.where(data.N_samp == data.n_samp);  data = hf_sid2_select_time(data, index);  data.n_time = data.Eu_i.shape[0]
    print(" cut0:", data.Eu_i.shape, data.n_time, "  <n_samp selection>")

    # CUT & Shaping: less packet length
    if n_num < data.Eu_i.shape[1]:
        data.Eu_i = data.Eu_i[:, 0:n_num];  data.Eu_q = data.Eu_q[:, 0:n_num]
        data.Ev_i = data.Ev_i[:, 0:n_num];  data.Ev_q = data.Ev_q[:, 0:n_num]
        data.Ew_i = data.Ew_i[:, 0:n_num];  data.Ew_q = data.Ew_q[:, 0:n_num]
        data.frequency  = data.frequency [:, 0:n_num];   data.freq_step  = data.freq_step [:, 0:n_num]
        data.freq_width = data.freq_width[:, 0:n_num];   data.time       = data.time      [:, 0:n_num]
        print(" cut1:", data.Eu_i.shape, data.n_time, "  <n_freq*n_samp selection>")

    # Reshape from "2D: n_time * (n_freq * n_samp)" to "3D: n_time * n_freq * n_samp"
    data.Eu_i       = np.array(data.Eu_i).reshape      (data.n_time, data.n_step, data.n_samp)
    data.Eu_q       = np.array(data.Eu_q).reshape      (data.n_time, data.n_step, data.n_samp)
    data.Ev_i       = np.array(data.Ev_i).reshape      (data.n_time, data.n_step, data.n_samp)
    data.Ev_q       = np.array(data.Ev_q).reshape      (data.n_time, data.n_step, data.n_samp)
    data.Ew_i       = np.array(data.Ew_i).reshape      (data.n_time, data.n_step, data.n_samp)
    data.Ew_q       = np.array(data.Ew_q).reshape      (data.n_time, data.n_step, data.n_samp)
    data.frequency  = np.array(data.frequency).reshape (data.n_time, data.n_step, data.n_samp)
    data.freq_step  = np.array(data.freq_step).reshape (data.n_time, data.n_step, data.n_samp)
    data.freq_width = np.array(data.freq_width).reshape(data.n_time, data.n_step, data.n_samp)
    data.time       = np.array(data.time).reshape      (data.n_time, data.n_step, data.n_samp)
    print(" sort:", data.Eu_i.shape, data.n_time, "x", data.n_step, "x", data.n_samp)

    # ### ASW1: data shift -16 for error packets in 2023
    date = data.epoch[0];  month = date.strftime('%Y%m')
    if month == "202304" or month == "202305" or month == "202307":
        data.Eu_i[:, -1, data.n_samp//2:data.n_samp] = 0.;  data.Eu_q[:, -1, data.n_samp//2:data.n_samp] = 0.
        data.Ev_i[:, -1, data.n_samp//2:data.n_samp] = 0.;  data.Ev_q[:, -1, data.n_samp//2:data.n_samp] = 0.
        data.Ew_i[:, -1, data.n_samp//2:data.n_samp] = 0.;  data.Ew_q[:, -1, data.n_samp//2:data.n_samp] = 0.

    # ### CAL
    # ASW1: CAL flag
    if data.cal_signal[0] == 255:
        power = data.Eu_i[:,-1]**2 + data.Eu_q[:,-1]**2 + data.Ev_i[:,-1]**2 + data.Ev_q[:,-1]**2 + data.Ew_i[:,-1]**2 + data.Ew_q[:,-1]**2
        power = np.mean(power, axis=1)
        index = np.where(power > 1e4)
        data.cal_signal[:] = 0
        data.cal_signal[index[0]] = 1
    # Selection: CAL
    if cal_mode < 2:
        index  = np.where(data.cal_signal == cal_mode);    data = hf_sid2_select_time(data, index);  data.n_time = data.Eu_i.shape[0]
        if cal_mode == 0: print("  cut:", data.Eu_i.shape, data.n_time, "x", data.n_step, "x", data.n_samp, "  <only BG>")
        else:             print("  cut:", data.Eu_i.shape, data.n_time, "x", data.n_step, "x", data.n_samp, "  <only CAL>")

    # NAN -- no data channels
    index = np.where(data.ch_selected & 0b1   == 0);  data.Eu_i[index[0]] = math.nan;  data.Eu_q[index[0]] = math.nan
    index = np.where(data.ch_selected & 0b10  == 0);  data.Ev_i[index[0]] = math.nan;  data.Ev_q[index[0]] = math.nan
    index = np.where(data.ch_selected & 0b100 == 0);  data.Ew_i[index[0]] = math.nan;  data.Ew_q[index[0]] = math.nan

    return data


def hf_sid2_select_time(data, index):
    # Data
    data.Eu_i      = data.Eu_i     [index[0]];   data.Eu_q = data.Eu_q[index[0]]
    data.Ev_i      = data.Ev_i     [index[0]];   data.Ev_q = data.Ev_q[index[0]]
    data.Ew_i      = data.Ew_i     [index[0]];   data.Ew_q = data.Ew_q[index[0]]
    data.frequency = data.frequency[index[0]];   data.freq_step = data.freq_step[index[0]];  data.freq_width = data.freq_width[index[0]]
    data.time      = data.time     [index[0]]
    # data.epoch     = data.epoch    [index[0]];  data.scet       = data.scet      [index[0]]

    hf_hk.status_shaping(data, index[0])
    """
    # AUX
    data.T_RWI_CH1 = data.T_RWI_CH1[index[0]];   data.T_RWI_CH2 = data.T_RWI_CH2[index[0]];  data.T_HF_FPGA  = data.T_HF_FPGA [index[0]]
    data.ch_selected = data.ch_selected[index[0]]; data.cal_signal= data.cal_signal [index[0]]
    # Header
    data.N_step    = data.N_step    [index[0]];  data.N_samp  = data.N_samp [index[0]]; 
    data.decimation= data.decimation[index[0]]
    data.ADC_ovrflw= data.ADC_ovrflw[index[0]];  data.ISW_ver = data.ISW_ver[index[0]]
    """
    return data


def hf_sid2_spec_nan(data, i):
    data.EE        [i] = math.nan; 
    data.EuEu      [i] = math.nan; data.EvEv      [i] = math.nan; data.EwEw      [i] = math.nan
    data.EuEv_re   [i] = math.nan; data.EvEw_re   [i] = math.nan; data.EwEu_re   [i] = math.nan
    data.EuEv_im   [i] = math.nan; data.EvEw_im   [i] = math.nan; data.EwEu_im   [i] = math.nan

    hf_hk.status_nan(data, i, 2)


"""
import csv
with open("sid2-f.csv", 'w') as f:
    writer = csv.writer(f)
    for i in range(n_freq1):
        writer.writerow([ i, freq_1d[i], freq_w_1d[i]])
print(n_freq1, spec.freq.shape)
"""

"""
import csv
with open("sid2-f-org.csv", 'w') as f:
    writer = csv.writer(f)
    for i in range(n_freq0):
        writer.writerow([ i, data.frequency[1][i][0], data.freq_width[1][i][0], data.freq_step[1][i][0]])
print(n_freq0, data.frequency.shape)
"""
