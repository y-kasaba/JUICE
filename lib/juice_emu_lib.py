"""
    JUICE RPWI HF Emulation and Comparison: L1a for all SIDs -- 2026/3/20
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import medfilt

import juice_cdf_lib  as juice_cdf

def datalist(asw, space, cal_mode):
    # dummy
    cdf_sid20= '';  cdf_sid4 = ''
    cdf_sid21= '';  cdf_sid5 = ''
    cdf_sid22= '';  cdf_sid6 = '';  cdf_sid9 = ''
    cdf_sid23= '';  cdf_sid7 = '';  cdf_sid8 = ''
    if asw == 3:
        if space == 0:
            # *** Ground Test - Ver.3 ***
            data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'

            # SID-2    ASW3        20251123     10mV, interval=40 [s]  freq_set = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1] [MHz]
            # cdf_sid2 = data_dir + 'JUICE_L1a_RPWI-HF-SID2_20000101T000226-20000101T001610_V01___SID2_20251113-1351.ccs.cdf'
            cdf_sid2  = data_dir + 'JUICE_L1a_RPWI-HF-SID2_20000101T000043-20000101T001413_V01___SID2_20251123-1005.ccs.cdf'

            # SID-3    ASW3         20251123
            #   (2d matix, RFI rejection OFF), new sweep table (Beff=62.5%)
            #   int=40 [s]		f = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1 [MHz]
            # cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20000101T001750-20000101T003120_V01___SID3_C1_20251113-1557.ccs.cdf'
            #   (2d matix, RFI rejection OFF), new sweep table (Beff=62.5%)
            #   int=40 [s]		f = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1 [MHz]
            cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20000101T001555-20000101T002925_V01___SID3_C1_20251123-1021.ccs.cdf'
            #   (2d matix, RFI rejection OFF), new sweep table (Beff=62.5%)
            #   int=40 [s]		f = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1 [MHz]
            # cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20000101T000043-20000101T001343_V01___SID3_C2_20251113-1715.ccs.cdf'
            #   (polariztion separation, RFI rejection OFF, noise floor subtraction OFF), new sweep table (Beff=62.5%)
	        #   int=40 [s]		f = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1] [MHz]
            # cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20000101T003123-20000101T004453_V01___SID3_C2_20251123-1037.ccs.cdf'
            # cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20000101T000153-20000101T000323_V01___SID3_20251211-2231.ccs.cdf'

            # SID-20   ASW3         20251123    sweep 0.02-2MHz 5s		Vin=10 mVpp     .2s(10s)>.5s(10s)>1s(20s)>2s(30s))  f = 1.8 [MHz]
            # cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20000101T002118-20000101T002307_V01___SID4-20_0.5s_20251113-1736.ccs.cdf'
            # cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20000101T002515-20000101T002833_V01___SID4-20_20251113-1741.ccs.cdf'
            cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20000101T000046-20000101T000506_V01___SID4-20_20251123-1107.ccs.cdf'
            # cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20000101T000823-20000101T001238_V01___SID4-20_20251123-1114.ccs.cdf'
            # cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20000101T000718-20000101T001159_V01___SID4-20_20251123-1345.ccs.cdf'

            # SID-4    ASW3         20251123    sweep 0.02-2MHz 5s		Vin=10 mVpp     .2s(10s)>.5s(10s)>1s(20s)>2s(30s))  f = 1.8 [MHz]
            # cdf_sid4  = data_dir + 'JUICE_L1a_RPWI-HF-SID4_20000101T002127-20000101T002138_V01___SID4-20_0.5s_20251113-1736.ccs.cdf'
            # df_sid4  = data_dir + 'JUICE_L1a_RPWI-HF-SID4_20000101T002522-20000101T002759_V01___SID4-20_20251113-1741.ccs.cdf'
            cdf_sid4  = data_dir + 'JUICE_L1a_RPWI-HF-SID4_20000101T000046-20000101T000420_V01___SID4-20_20251123-1107.ccs.cdf'
            # cdf_sid4  = data_dir + 'JUICE_L1a_RPWI-HF-SID4_20000101T000718-20000101T001114_V01___SID4-20_20251123-1345.ccs.cdf'

            # SID-21   ASW3  COMP-1 20250926    1.5MHz  Vin=10mVpp, Phase=[0 45 90 135 180 225 270 315 0] deg (V-ch) 
            # cdf_sid21 = data_dir + 'JUICE_L1a_RPWI-HF-SID21_20000101T003031-20000101T003642_V01___SID5-21_20251113-1746.ccs.cdf'
            cdf_sid21 = data_dir + 'JUICE_L1a_RPWI-HF-SID21_20000101T002158-20000101T002658_V01___SID5-21_20251123-1129.ccs.cdf'

            # SID-5    ASW3         20250926    1.5MHz  Vin=10mVpp, Phase=[0 45 90 135 180 225 270 315 0] deg (V-ch) 
            # cdf_sid5  = data_dir + 'JUICE_L1a_RPWI-HF-SID5_20000101T003031-20000101T003531_V01___SID5-21_20251113-1746.ccs.cdf'
            cdf_sid5  = data_dir + 'JUICE_L1a_RPWI-HF-SID5_20000101T002158-20000101T002628_V01___SID5-21_20251123-1129.ccs.cdf'

            # SID-22   ASW3
            # cdf_sid22 = data_dir + 'JUICE_L1a_RPWI-HF-SID22_20000101T000044-20000101T001414_V01___SID6-22_20251211-1108.ccs.cdf'
            # cdf_sid22 = data_dir + 'JUICE_L1a_RPWI-HF-SID22_20000101T000051-20000101T000121_V01___SID6-22_P0_20251212-2236.ccs.cdf'
            cdf_sid22 = data_dir + 'JUICE_L1a_RPWI-HF-SID22_20000101T000047-20000101T001317_V01___SID6-22_20251213-1846.ccs.cdf'
            # cdf_sid22 = data_dir + 'JUICE_L1a_RPWI-HF-SID22_20000101T000034-20000101T000104_V01___SID9-22_20260114.dat.cdf'

            # SID-6    ASW3
            # cdf_sid6  = data_dir + 'JUICE_L1a_RPWI-HF-SID6_20000101T000044-20000101T001444_V01___SID6-22_20251211-1108.ccs.cdf'
            # cdf_sid6  = data_dir + 'JUICE_L1a_RPWI-HF-SID6_20000101T000051-20000101T000151_V01___SID6-22_P0_20251212-2236.ccs.cdf'
            cdf_sid6  = data_dir + 'JUICE_L1a_RPWI-HF-SID6_20000101T000047-20000101T001317_V01___SID6-22_20251213-1846.ccs.cdf'

            # SID-9    ASW3
            cdf_sid9  = data_dir + 'JUICE_L1a_RPWI-HF-SID9_20000101T000034-20000101T000104_V01___SID9-22_20260114.dat.cdf'

            # SID-23   ASW3
            # cdf_sid23 = data_dir + 'JUICE_L1a_RPWI-HF-SID23_20000101T000155-20000101T000503_V01___SID7-23_P0_20251113-2224.ccs.cdf'
            cdf_sid23 = data_dir + 'JUICE_L1a_RPWI-HF-SID23_20000101T000049-20000101T000708_V01___SID7-23_P1_20251204-0844.ccs.cdf'

            # SID-7    ASW3
            cdf_sid7  = data_dir + 'JUICE_L1a_RPWI-HF-SID7_20000101T000155-20000101T000430_V01___SID7-23_P0_20251113-2224.ccs.cdf'
            cdf_sid7  = data_dir + 'JUICE_L1a_RPWI-HF-SID7_20000101T000049-20000101T000300_V01___SID7-23_P1_20251204-0844.ccs.cdf'

            # SID-8    ASW3
            cdf_sid8  = data_dir + 'JUICE_L1a_RPWI-HF-SID8_20000101T000504-20000101T000708_V01___SID7-23_P1_20251204-0844.ccs.cdf'

    if asw == 2:
        if space == 1:
            # *** Flight - Ver.2 ***
            data_dir  = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'

            # SID-2  ASW2        20250331   normal + OFF + CAL
            cdf_sid2  = data_dir + 'JUICE_L1a_RPWI-HF-SID2_20250331T005104-20250331T233757_V01___RPR1_52000005_2025.091.16.38.56.448.cdf'

            # SID-3  ASW2 COMP-1 20250331   normal + CAL
            if cal_mode == 1:    # CAL
                cdf_sid3 = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20240822T095914-20240822T182844_V01___RPR1_52000004_2024.236.08.13.31.519.cdf' # CAL
            else:
                cdf_sid3 = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20250331T030012-20250331T201834_V01___RPR1_52000005_2025.091.16.38.56.448.cdf' # Normal

            # SID-20 ASW2 COMP-1 20240706   normal
            cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20240706T121424-20240706T125428_V01___RPR2_62000002_2024.190.19.50.21.637.cdf'

            # SID-4  ASW2 COMP-1 20240706   normal
            cdf_sid4  = data_dir + 'JUICE_L1a_RPWI-HF-SID4_20240706T121439-20240706T125422_V01___RPR1_52000002_2024.190.14.59.43.630.cdf'

            # SID-21 ASW2 COMP-1 20250331   nornal & CAL
            cdf_sid21 = data_dir + 'JUICE_L1a_RPWI-HF-SID21_20250331T033821-20250331T034222_V01___RPR2_62000007_2025.091.16.40.05.450.cdf'

            # SID-5  ASW2        20250331   nornal & CAL
            cdf_sid5  = data_dir + 'JUICE_L1a_RPWI-HF-SID5_20250331T033821-20250331T034222_V01___RPR1_52000005_2025.091.16.38.56.448.cdf'

            # SID-23   ASW3
            cdf_sid23 = data_dir + 'JUICE_L1a_RPWI-HF-SID23_20240706T130407-20240706T130904_V01___RPR2_62000003_2024.190.22.47.44.640.cdf'

    if asw == 1:
        if space == 1:
            # *** Flight - Ver.1 ***
            data_dir = data_dir + '/Users/user/0-python/JUICE_data/Data-CDF/ASW1/'

            # SID-2  ASW1       20230530   normal + CAL
            cdf_sid2 = data_dir + 'JUICE_L1a_RPWI-HF-SID2_20230530T100330-20230530T100930_V01___RPR1_52000010_2023.150.10.40.53.663.cdf' # 230530 background & CAL
            # SID-3  ASW1       20250523   normal + CAL
            cdf_sid3 = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20230523T110938-20230523T111154_V01___RPR1_52000003_2023.143.11.14.17.500.cdf' # 230523 after Y deployment: with CAL
            
    print('[SID-02]', cdf_sid2);   print('[SID-03]', cdf_sid3)
    print('[SID-20]', cdf_sid20);  print('[SID-04]', cdf_sid4)
    print('[SID-21]', cdf_sid21);  print('[SID-05]', cdf_sid5)
    print('[SID-22]', cdf_sid22);  print('[SID-06]', cdf_sid6);  print('[SID-09]', cdf_sid9)
    print('[SID-23]', cdf_sid23);  print('[SID-07]', cdf_sid7);  print('[SID-08]', cdf_sid8)
    return cdf_sid2, cdf_sid3, cdf_sid20, cdf_sid4, cdf_sid21, cdf_sid5, cdf_sid22, cdf_sid6, cdf_sid9, cdf_sid23, cdf_sid7, cdf_sid8


# *****************
# **** SHAPING ****
# *****************
def wave_shaping_Eu(data_sid, str_SID, n_sweep1, n_sweep2):
    class struct:
        pass
    wave_sid = struct()
    wave_sid.Eu_i     = data_sid.Eu_i    [n_sweep1:n_sweep2];   wave_sid.Eu_q     = data_sid.Eu_q    [n_sweep1:n_sweep2]
    wave_sid.Ev_i     = data_sid.Ev_i    [n_sweep1:n_sweep2];   wave_sid.Ev_q     = data_sid.Ev_q    [n_sweep1:n_sweep2]
    wave_sid.Ew_i     = data_sid.Ew_i    [n_sweep1:n_sweep2];   wave_sid.Ew_q     = data_sid.Ew_q    [n_sweep1:n_sweep2]
    wave_sid.EuEu_amp = data_sid.EuEu_amp[n_sweep1:n_sweep2];   wave_sid.EuEu_raw = data_sid.EuEu_raw[n_sweep1:n_sweep2]
    wave_sid.epoch    = data_sid.epoch   [n_sweep1:n_sweep2]
    wave_sid.n_time   = wave_sid.Eu_i.shape[0]
    #
    wave_sid.RPWI_FSW_version = data_sid.RPWI_FSW_version
    wave_sid.decimation = data_sid.decimation
    wave_sid.frequency  = data_sid.frequency;   wave_sid.freq_width  = data_sid.freq_width

    peak = np.ravel(wave_sid.Eu_i); wave_sid.peak = np.nanmax(peak)
    print('[Peak - '+str_SID+' Wave in RAW     ]    Eu:', '                       -- (peak)                                    {:.2e} '.format(wave_sid.peak))
    return wave_sid


# **************
# **** SPEC ****
# **************
def spec_data2spec(data_sid):
    class struct:
        pass
    spec_sid = struct()
    spec_sid.EuEu  = data_sid.EuEu;   spec_sid.EuEu_raw = data_sid.EuEu_raw;  spec_sid.EuEu_amp = data_sid.EuEu_amp
    spec_sid.epoch = data_sid.epoch;  spec_sid.freq = data_sid.freq;   spec_sid.freq_w = data_sid.freq_w
    spec_sid.HF_ID = data_sid.HF_ID;  spec_sid.sid  = data_sid.sid;    spec_sid.df_raw = data_sid.df_raw  
    if spec_sid.sid == 20:
        spec_sid.n_block = data_sid.N_block[spec_sid.EuEu.shape[0]//2]
        spec_sid.n_step  = data_sid.N_step [spec_sid.EuEu.shape[0]//2]
    return spec_sid


def spec_shaping_EuEu(spec_sid, str_SID, n_sweep1, n_sweep2):
    #           [RAW^2/Hz]            [RAW^2]
    # MAX       spec_sid.EuEu_max     spec_sid.EuEu_a_max
    # Median    spec_sid.EuEu_med     spec_sid.EuEu_a_med
    spec_sid.EuEu      = spec_sid.EuEu    [n_sweep1:n_sweep2];  spec_sid.n_time   = spec_sid.EuEu.shape[0]
    spec_sid.EuEu_raw  = spec_sid.EuEu_raw[n_sweep1:n_sweep2];  spec_sid.EuEu_amp = spec_sid.EuEu_amp[n_sweep1:n_sweep2]
    spec_sid.epoch     = spec_sid.epoch   [n_sweep1:n_sweep2]
    if spec_sid.sid == 20:  spec_sid = spec_shaping_EuEu_sid20(spec_sid)
    spec_sid.freq1     = spec_sid.freq    [spec_sid.n_time//2]; spec_sid.freq_w1   = spec_sid.freq_w  [spec_sid.n_time//2]
    if spec_sid.sid != 2:   spec_sid.freq2 = spec_sid.freq1

    # RAW^2/Hz -> RAW^2
    spec_sid.df_freq      = spec_sid.freq_w1   * 1000.              # kHz -> Hz
    spec_sid.EuEu_max     = np.nanmax(spec_sid.EuEu, axis=0)   
    spec_sid.EuEu_a_max   = spec_sid.EuEu_max * spec_sid.df_freq;   spec_sid.EuEu_med     = np.nanmedian(spec_sid.EuEu, axis=0)
    spec_sid.EuEu_amp_max = np.nanmax(spec_sid.EuEu_amp, axis=0);   spec_sid.EuEu_raw_med = np.nanmedian(spec_sid.EuEu_raw, axis=0)

    # peak
    peak_f = np.nanargmax(spec_sid.EuEu_a_max);  print('\n'+str_SID+' [peak-MAX]', spec_sid.EuEu_max.shape, spec_sid.freq.shape, peak_f)
    if spec_sid.sid != 7 and spec_sid.sid != 8 and spec_sid.sid != 23:
        spec_sid.peak_f     = spec_sid.freq1     [peak_f]
    if spec_sid.sid != 8:
        spec_sid.peak_max   = spec_sid.EuEu_max  [peak_f];  spec_sid.peaks_max   = np.sum(spec_sid.EuEu_max[peak_f-1:peak_f+2])
        spec_sid.peak_a_max = spec_sid.EuEu_a_max[peak_f];  spec_sid.peaks_a_max = np.sum(spec_sid.EuEu_a_max[peak_f-1:peak_f+2])
    else:
        spec_sid.peak_max   = spec_sid.EuEu_max;            spec_sid.peaks_max   = spec_sid.EuEu_max
        spec_sid.peak_a_max = spec_sid.EuEu_a_max;          spec_sid.peaks_a_max = spec_sid.EuEu_a_max
    if spec_sid.sid != 7 and spec_sid.sid != 8 and spec_sid.sid != 23:
        print('[Peak - '+str_SID+' Spec in RAW^2/Hz]  EuEu:', '{:.2e}kHz            -- (peak)'.format(spec_sid.peak_f),                                   '{:.2e}'.format(spec_sid.peak_max),   '{:.2e}'.format(spec_sid.peak_max**.5),   '| (sum) {:.2e}'.format(spec_sid.peaks_max),   '{:.2e}'.format(spec_sid.peaks_max**.5))
        print('[Peak - '+str_SID+' Spec in RAW^2   ]  EuEu:', '{:.2e}'.format(spec_sid.peak_f), '({:.2e})kHz -- (peak)'.format(spec_sid.df_freq[0]/1000), '{:.2e}'.format(spec_sid.peak_a_max), '{:.2e}'.format(spec_sid.peak_a_max**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_a_max), '{:.2e}'.format(spec_sid.peaks_a_max**.5))
    else:
        print('[Peak - '+str_SID+' Spec in RAW^2/Hz]  EuEu:', '{:.2e}'.format(spec_sid.peak_max),     '{:.2e}'.format(spec_sid.peak_max**.5),     '| (sum) {:.2e}'.format(spec_sid.peaks_max),     '{:.2e}'.format(spec_sid.peaks_max**.5))
        print('[Peak - '+str_SID+' Spec in RAW^2   ]  EuEu:', '{:.2e}'.format(spec_sid.peak_a_max),   '{:.2e}'.format(spec_sid.peak_a_max**.5),   '| (sum) {:.2e}'.format(spec_sid.peaks_a_max),   '{:.2e}'.format(spec_sid.peaks_a_max**.5))

    # RAW & AMP
    peak_f =       np.nanargmax(spec_sid.EuEu_amp_max)
    if spec_sid.sid != 8:
        spec_sid.peak_amp_max = spec_sid.EuEu_amp_max[peak_f];  spec_sid.peaks_amp_max = np.sum(spec_sid.EuEu_amp_max[peak_f-1:peak_f+2])
    else:
        spec_sid.peak_amp_max = spec_sid.EuEu_amp_max;          spec_sid.peaks_amp_max = spec_sid.EuEu_amp_max
    if spec_sid.sid != 7 and spec_sid.sid != 8 and spec_sid.sid != 23:
        print('[Peak - '+str_SID+' RAW-AMP in TLM  ]  EuEu:', '{:.2e}kHz            -- (peak)'.format(spec_sid.freq1[peak_f]),                  '{:.2e}'.format(spec_sid.peak_amp_max), '{:.2e}'.format(spec_sid.peak_amp_max**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_amp_max), '{:.2e}'.format(spec_sid.peaks_amp_max**.5) )
    else:
        print('[Peak - '+str_SID+' RAW-AMP in TLM  ]  EuEu:', '{:.2e}'.format(spec_sid.peak_amp_max), '{:.2e}'.format(spec_sid.peak_amp_max**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_amp_max), '{:.2e}'.format(spec_sid.peaks_amp_max**.5) )
    return spec_sid


def spec_shaping_EuEu_sid20(spec_sid):
    from datetime import timedelta
    if spec_sid.n_block == 1: return spec_sid

    # Epoch -- Time resoution: 1/n_block [sec]
    Epoch_1d = []
    for i in range(spec_sid.n_block):
        Epoch_1d.extend(spec_sid.epoch)
    for i in range(spec_sid.n_time):
        for j in range(spec_sid.n_block):
            Epoch_1d[i * spec_sid.n_block + j] = spec_sid.epoch[i] + timedelta(seconds = j/spec_sid.n_block)
    spec_sid.epoch  = Epoch_1d

    spec_sid.EuEu     = spec_sid.EuEu.reshape    (spec_sid.n_time * spec_sid.n_block, spec_sid.n_step) 
    spec_sid.EuEu_raw = spec_sid.EuEu_raw.reshape(spec_sid.n_time * spec_sid.n_block, spec_sid.n_step)
    spec_sid.EuEu_amp = spec_sid.EuEu_amp.reshape(spec_sid.n_time * spec_sid.n_block, spec_sid.n_step)
    spec_sid.freq     = spec_sid.freq.reshape    (spec_sid.n_time * spec_sid.n_block, spec_sid.n_step)
    spec_sid.freq_w   = spec_sid.freq_w.reshape  (spec_sid.n_time * spec_sid.n_block, spec_sid.n_step)
    spec_sid.n_time = spec_sid.EuEu.shape[0]
    print("SID-20:", spec_sid.n_step, spec_sid.freq.shape, spec_sid.freq_w.shape)
    return spec_sid


# **************
# **** PLOT ****
# **************
def plot_data_Eu(data_sid, str_SID, dump_mode, str_mode, work_dir):
    fig = plt.figure(figsize=(16, 2));  ax1 = fig.add_subplot(3, 1, (1,2));  ax2 = fig.add_subplot(3, 1, 3)
    ax1.plot(np.ravel(data_sid.Eu_i[:][:]), '-r', linewidth=.5, label=str_SID+' Eu_i')
    ax1.plot(np.ravel(data_sid.Eu_q[:][:]), ':g', linewidth=.5, label=str_SID+' Eu_q');  ax1.set_ylabel(str_SID+' Eu (RAW)'); ax1.legend(loc='upper right')
    p_max = np.ceil(np.log10(np.nanmax([np.nanmax(data_sid.Eu_i), np.nanmax(data_sid.Eu_q)]))*5)/5
    ylim=[-10**(p_max), 10**(p_max)];  ax1.set_ylim(ylim)

    ax2.plot(np.ravel(data_sid.epoch[:]), '.');     ax2.set_ylabel('Epoch')
    xlim=[0, len(np.ravel(data_sid.Eu_i[:][:])) - 1];   ax1.set_xlim(xlim)
    xlim=[0, data_sid.n_time];                      ax2.set_xlim(xlim)

    fig.subplots_adjust(hspace=0);  fig.show
    if dump_mode == 1:
        png_fname = work_dir+'EMU_raw_'+str_SID+str_mode+'.png'
        fig.savefig(png_fname)


def plot_data_EuEu(data_sid, str_SID, dump_mode, str_mode, work_dir):
    if data_sid.sid != 7 and data_sid.sid != 8 and data_sid.sid != 23:  fig = plt.figure(figsize=(16, 2))  
    else:                                                               fig = plt.figure(figsize=(16, 6.5))
    ax1 = fig.add_subplot(3, 1, (1,2));  ax2 = fig.add_subplot(3, 1, 3)

    ax1.plot(np.ravel(data_sid.EuEu    [:][:]), '-r', linewidth=.5, label=str_SID+' EuEu');  
    ax1.plot(np.ravel(data_sid.EuEu_raw[:][:]), ':g', linewidth=.5, label=str_SID+' EuEu_raw')
    ax1.plot(np.ravel(data_sid.EuEu_amp[:][:]), ':b', linewidth=.5, label=str_SID+' EuEu_amp');  ax1.set_ylabel(str_SID+' EuEu (RAW^2)'); ax1.legend(loc='upper right')
    xlim=[0, len(np.ravel(data_sid.EuEu[:][:])) - 1];   ax1.set_xlim(xlim)

    p_max = np.ceil(np.log10( np.nanmax( [np.nanmax(data_sid.EuEu), np.nanmax(data_sid.EuEu_raw), np.nanmax(data_sid.EuEu_amp)] ) )*5)/5+.5
    p_min = np.ceil(np.log10( np.nanmin( [np.nanmin(data_sid.EuEu), np.nanmin(data_sid.EuEu_raw), np.nanmin(data_sid.EuEu_amp)] ) )*5)/5-.5
    ylim=[10**(p_min), 10**(p_max)]
    ylim=[10**(-3.5), 10**(9)]
    ax1.set_ylim(ylim);  ax1.set_yscale('log')    

    ax2.plot(np.ravel(data_sid.epoch[:]), '.');  ax2.set_ylabel('Epoch')
    xlim=[0, data_sid.n_time];                   ax2.set_xlim(xlim)

    fig.subplots_adjust(hspace=0);  fig.show
    if dump_mode == 1:
        png_fname = work_dir+'EMU_raw_'+str_SID+str_mode+'.png'
        fig.savefig(png_fname)


def plot_spec_EuEu(spec_sid, n_sweep1, n_sweep2, n_sweep3, str_SID, f_mode, dump_mode, str_mode, work_dir):
    fig = plt.figure(figsize=(16, 6.5));  ax1 = fig.add_subplot(1, 1, 1)

    ax1.plot(spec_sid.freq1, spec_sid.EuEu_a_max,     '.r', linewidth=2, ms=10, label=str_SID+' EuEu Amp max (RAW^2)')
    ax1.plot(spec_sid.freq2, spec_sid.EuEu_amp_max,   '-g', linewidth=1, ms=2,  label='RAW EuEu Amp max')
    ax1.plot(spec_sid.freq1, spec_sid.EuEu_med,       '.r', linewidth=2, ms=10, label=str_SID+' EuEu med (TLM)')
    ax1.plot(spec_sid.freq2, spec_sid.EuEu_raw_med,   ':g', linewidth=1, ms=2,  label='RAW EuEu Raw med')

    ax1.set_ylabel(str_SID+' EuEu (RAW^2)');  ax1.legend(loc='upper right', fontsize=8); 
    ax1.set_yscale('log')
    if f_mode == 1:  ax1.set_xscale('log')

    xlim=[np.nanmin(spec_sid.freq), np.nanmax(spec_sid.freq)];  ax1.set_xlim(xlim)
    ylim=[10**(-3.5), 10**(9)];                                 ax1.set_ylim(ylim)

    fig.show
    if dump_mode > 0:
        png_fname = work_dir+'EMU_spec_'+str_SID+str_mode+'.png'
        fig.savefig(png_fname)