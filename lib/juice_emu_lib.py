"""
    JUICE RPWI HF Emulation and Comparison: L1a for all SIDs -- 2026/7/20
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import medfilt

import juice_cdf_lib  as juice_cdf

def datalist(asw, space, mode_bg):
    # dummy
    cdf_sid20= '';  cdf_sid4 = ''
    cdf_sid21= '';  cdf_sid5 = ''
    cdf_sid22= '';  cdf_sid6 = '';  cdf_sid9 = ''
    cdf_sid23= '';  cdf_sid7 = '';  cdf_sid8 = ''
    if asw == 3:
        if space == 1:
            # **************************
            # ASW3      flight
            # **************************
            data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW3/'
            cdf_sid2  = data_dir + 'JUICE_L1a_RPWI-HF-SID2_20260716T213019-20260716T213737_V01___RPR1_52000006_2026.197.23.00.12.498.cdf'
            cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20260716T213754-20260716T215104_V01___RPR1_52000006_2026.197.23.00.12.498.cdf'
            cdf_sid4  = data_dir + 'JUICE_L1a_RPWI-HF-SID4_20260716T215148-20260716T215217_V01___RPR1_52000006_2026.197.23.00.12.498.cdf'
            cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20260716T215148-20260716T215217_V01___RPW0_62000005_2026.198.19.00.45.441.cdf'
            cdf_sid5  = data_dir + 'JUICE_L1a_RPWI-HF-SID5_20260716T215226-20260716T215839_V01___RPR1_52000006_2026.197.23.00.12.498.cdf'
            cdf_sid21 = data_dir + 'JUICE_L1a_RPWI-HF-SID21_20260716T215226-20260716T215839_V01___RPW0_62000005_2026.198.19.00.45.441.cdf'
            # cdf_sid6  = data_dir + ''
            cdf_sid9  = data_dir + 'JUICE_L1a_RPWI-HF-SID9_20260716T215924-20260716T221515_V01___RPR1_52000006_2026.197.23.00.12.498.cdf'
            cdf_sid22 = data_dir + 'JUICE_L1a_RPWI-HF-SID22_20260716T215924-20260716T221515_V01___RPW0_62000005_2026.198.19.00.45.441.cdf'
            cdf_sid7  = data_dir + 'JUICE_L1a_RPWI-HF-SID7_20260716T220726-20260716T220814_V01___RPR1_52000006_2026.197.23.00.12.498.cdf'
            cdf_sid8  = data_dir + 'JUICE_L1a_RPWI-HF-SID8_20260716T220620-20260716T220708_V01___RPR1_52000006_2026.197.23.00.12.498.cdf'
            cdf_sid23 = data_dir + 'JUICE_L1a_RPWI-HF-SID23_20260716T220620-20260716T220814_V01___RPW0_62000005_2026.198.19.00.45.441.cdf'
        else:
            # **************************
            # ASW3      ground - EM3
            # **************************
            data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
            cdf_sid2  = data_dir + 'JUICE_L1a_RPWI-HF-SID2_20000101T000110-20000101T000828_V01___FFT_20260602-2241.ccs.cdf'
            cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20000101T000844-20000101T002155_V01___FFT_20260602-2241.ccs.cdf'
            cdf_sid4  = data_dir + 'JUICE_L1a_RPWI-HF-SID4_20000101T002239-20000101T002307_V01___FFT_20260602-2241.ccs.cdf'
            cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20000101T002239-20000101T002307_V01___FFT_20260602-2241.ccs.cdf'
            cdf_sid5  = data_dir + 'JUICE_L1a_RPWI-HF-SID5_20000101T002317-20000101T002929_V01___FFT_20260602-2241.ccs.cdf'
            cdf_sid21 = data_dir + 'JUICE_L1a_RPWI-HF-SID21_20000101T002317-20000101T002929_V01___FFT_20260602-2241.ccs.cdf'
            cdf_sid6  = data_dir + 'JUICE_L1a_RPWI-HF-SID6_20000101T000047-20000101T001317_V01___SID6-22_20251213-1846.ccs.cdf'
            cdf_sid9  = data_dir + 'JUICE_L1a_RPWI-HF-SID9_20000101T003014-20000101T005639_V01___FFT_20260602-2241.ccs.cdf'
            cdf_sid22 = data_dir + 'JUICE_L1a_RPWI-HF-SID22_20000101T003014-20000101T004605_V01___FFT_20260602-2241.ccs.cdf'
            cdf_sid7  = data_dir + 'JUICE_L1a_RPWI-HF-SID7_20000101T003817-20000101T003904_V01___FFT_20260602-2241.ccs.cdf'
            cdf_sid8  = data_dir + 'JUICE_L1a_RPWI-HF-SID8_20000101T003711-20000101T003758_V01___FFT_20260602-2241.ccs.cdf'
            cdf_sid23 = data_dir + 'JUICE_L1a_RPWI-HF-SID23_20000101T003711-20000101T003904_V01___FFT_20260602-2241.ccs.cdf'

            # **************************
            # ASW3      ground - FS 
            # **************************
            """
            data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
            # SID-2     20251123     10mV, interval=40 [s]  freq_set = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1] [MHz]
            cdf_sid2  = data_dir + 'JUICE_L1a_RPWI-HF-SID2_20000101T000043-20000101T001413_V01___SID2_20251123-1005.ccs.cdf'
            # SID-3     20251123    2d matix, RFI rejection OFF), new sweep table (Beff=62.5%)
            #                       int=40 [s]		               f = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1 [MHz]
            cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20000101T001555-20000101T002925_V01___SID3_C1_20251123-1021.ccs.cdf'
            # cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20000101T003123-20000101T004453_V01___SID3_C2_20251123-1037.ccs.cdf'
            # SID-20    20251123    sweep 0.02-2MHz 5s		Vin=10 mVpp     .2s(10s)>.5s(10s)>1s(20s)>2s(30s))  f = 1.8 [MHz]
            cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20000101T000046-20000101T000506_V01___SID4-20_20251123-1107.ccs.cdf'
            cdf_sid4  = data_dir + 'JUICE_L1a_RPWI-HF-SID4_20000101T000046-20000101T000420_V01___SID4-20_20251123-1107.ccs.cdf'
            # SID-21  COMP-1 20250926    1.5MHz  Vin=10mVpp, Phase=[0 45 90 135 180 225 270 315 0] deg (V-ch) 
            cdf_sid21 = data_dir + 'JUICE_L1a_RPWI-HF-SID21_20000101T002158-20000101T002658_V01___SID5-21_20251123-1129.ccs.cdf'
            cdf_sid5  = data_dir + 'JUICE_L1a_RPWI-HF-SID5_20000101T002158-20000101T002628_V01___SID5-21_20251123-1129.ccs.cdf'
            # SID-22 
            cdf_sid22 = data_dir + 'JUICE_L1a_RPWI-HF-SID22_20000101T000047-20000101T001317_V01___SID6-22_20251213-1846.ccs.cdf'
            cdf_sid6  = data_dir + 'JUICE_L1a_RPWI-HF-SID6_20000101T000047-20000101T001317_V01___SID6-22_20251213-1846.ccs.cdf'
            cdf_sid9  = data_dir + 'JUICE_L1a_RPWI-HF-SID9_20000101T000034-20000101T000104_V01___SID9-22_20260114.dat.cdf'
            # SID-23
            cdf_sid23 = data_dir + 'JUICE_L1a_RPWI-HF-SID23_20000101T000049-20000101T000708_V01___SID7-23_P1_20251204-0844.ccs.cdf'
            cdf_sid7  = data_dir + 'JUICE_L1a_RPWI-HF-SID7_20000101T000049-20000101T000300_V01___SID7-23_P1_20251204-0844.ccs.cdf'
            cdf_sid8  = data_dir + 'JUICE_L1a_RPWI-HF-SID8_20000101T000504-20000101T000708_V01___SID7-23_P1_20251204-0844.ccs.cdf'
            """

    if asw == 2:
        if space == 1:
            # **************************
            # *** Flight - ASW2 ***
            # **************************
            data_dir  = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
            # SID-2  ASW2   20260223   nrm / CAL + off
            cdf_sid2  = data_dir + 'JUICE_L1a_RPWI-HF-SID2_20260223T003941-20260223T004236_V01___RPR1_52000001_2026.062.08.07.27.435.cdf'
            # SID-3  ASW2   20260223   nrm / CAL
            cdf_sid3 = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20260223T004250-20260223T004427_V01___RPR1_52000001_2026.062.08.07.27.435.cdf' # Normal
            # SID-20 ASW2   20260223   nrm / CAL
            cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20260223T004451-20260223T004640_V01___RPR2_62000001_2026.054.09.35.22.426.cdf'
            cdf_sid4  = data_dir + 'JUICE_L1a_RPWI-HF-SID4_20260223T004501-20260223T004630_V01___RPR1_52000001_2026.062.08.07.27.435.cdf'
            # SID-21 ASW2   20260223   nrm / CAL
            cdf_sid21 = data_dir + 'JUICE_L1a_RPWI-HF-SID21_20260223T004655-20260223T004831_V01___RPR2_62000001_2026.054.09.35.22.426.cdf'
            cdf_sid5  = data_dir + 'JUICE_L1a_RPWI-HF-SID5_20260223T004655-20260223T004831_V01___RPR1_52000001_2026.062.08.07.27.435.cdf'
            # SID-23 ASW2   20240822   nrm
            cdf_sid23 = data_dir + 'JUICE_L1a_RPWI-HF-SID23_20240822T024109-20240822T024134_V01___RPR2_62000006_2024.236.10.07.45.514.cdf'
        else:
            # **************************
            # *** Ground Test - ASW2 ***
            # **************************
            data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
            # SID-2    ASW2        SG - 1.0MHz 10mVpp 90/0/0deg
            cdf_sid2  = data_dir + 'JUICE_L1a_RPWI-HF-SID2_20000101T000154-20000101T000454_V01___SID02_20241021-1026.ccs.cdf'
            # SID-3    ASW2        10/10/10mV, 90/0/0deg,  1.55MHz
            cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20000101T000055-20000101T001033_V01___SID03_20241010-1027_RadioFull_comp1.ccs.cdf'
            # cdf_sid3  = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20000101T000511-20000101T000855_V01___SID03_20241009-1806_RadioFull_comp2.ccs.cdf'
            # SID-20   ASW2
            cdf_sid20 = data_dir + 'JUICE_L1a_RPWI-HF-SID20_20000101T000102-20000101T000123_V01___SID04-20_20241016-1156-Radioburst.ccs.cdf'
            cdf_sid4  = data_dir + 'JUICE_L1a_RPWI-HF-SID4_20000101T000112-20000101T000123_V01___SID04-20_20241016-1156-Radioburst.ccs.cdf'
            # SID-21   ASW2
            cdf_sid21 = data_dir + 'old/JUICE_L1a_RPWI-HF-SID21_20000101T000044-20000101T000144_V01___SID05-21_20231117-1611.ccs.cdf'
            cdf_sid5  = data_dir + 'old/JUICE_L1a_RPWI-HF-SID5_20000101T000044-20000101T000144_V01___SID05-21_20231117-1611.ccs.cdf'
            # SID-23   ASW3
            cdf_sid23 = data_dir + 'old/JUICE_L1a_RPWI-HF-SID23_20000101T000047-20000101T000047_V01___SID07-23_20231024-0024.ccs.cdf'

    if asw == 1:
        if space == 1:
            # **************************
            # *** Flight - Ver.1 ***
            # **************************
            data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW1/'
            # SID-2  ASW1       20230530   normal + CAL
            cdf_sid2 = data_dir + 'JUICE_L1a_RPWI-HF-SID2_20230530T100330-20230530T100930_V01___RPR1_52000010_2023.150.10.40.53.663.cdf' # 230530 background & CAL
            # SID-3  ASW1       20250523   normal + CAL
            cdf_sid3 = data_dir + 'JUICE_L1a_RPWI-HF-SID3_20230523T110938-20230523T111154_V01___RPR1_52000003_2023.143.11.14.17.500.cdf' # 230523 after Y deployment: with CAL
            
    print('[SID-02]', cdf_sid2 );  print('[SID-03]', cdf_sid3)
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


def spec_shaping_EuEu(spec_sid, str_SID, n_sweep1, n_sweep2, mode_bg):
    #           [RAW^2/Hz]            [RAW^2]
    # MAX       spec_sid.EuEu_max     spec_sid.EuEu_a_max
    # Median    spec_sid.EuEu_med     spec_sid.EuEu_a_med
    spec_sid.EuEu      = spec_sid.EuEu    [n_sweep1:n_sweep2];  spec_sid.n_time   = spec_sid.EuEu.shape[0]
    spec_sid.EuEu_raw  = spec_sid.EuEu_raw[n_sweep1:n_sweep2];  spec_sid.EuEu_amp = spec_sid.EuEu_amp[n_sweep1:n_sweep2]
    spec_sid.epoch     = spec_sid.epoch   [n_sweep1:n_sweep2]
    if spec_sid.sid == 20:  spec_sid = spec_shaping_EuEu_sid20(spec_sid)
    freq1   = spec_sid.freq  [n_sweep1:n_sweep2];   spec_sid.freq1     = freq1  [(n_sweep2-n_sweep1)//2]
    freq_w1 = spec_sid.freq_w[n_sweep1:n_sweep2];   spec_sid.freq_w1   = freq_w1[(n_sweep2-n_sweep1)//2]
    if spec_sid.sid != 2:   spec_sid.freq2 = spec_sid.freq1

    # RAW^2/Hz -> RAW^2
    spec_sid.df_freq      = spec_sid.freq_w1   * 1000.              # kHz -> Hz
    spec_sid.EuEu_max     = np.nanmax(spec_sid.EuEu, axis=0)   
    spec_sid.EuEu_a_max   = spec_sid.EuEu_max * spec_sid.df_freq * 2.0; # spec_sid.EuEu_a_max   = np.convolve(spec_sid.EuEu_a_max,   [1,1,1], mode='same')
    spec_sid.EuEu_amp_max = np.nanmax(spec_sid.EuEu_amp, axis=0);       # spec_sid.EuEu_amp_max = np.convolve(spec_sid.EuEu_amp_max, [1,1,1], mode='same')
    
    # Median except large amplitude parts (< amp_max)
    if mode_bg != 1:  amp_max = 1e+6
    else:             amp_max = 1e+10
    if spec_sid.sid != 8:  spec_sid.time_EuEu_amp_med = np.nanmedian(spec_sid.EuEu_amp, axis=1)
    else:                  spec_sid.time_EuEu_amp_med = spec_sid.EuEu_amp
    index = np.where( spec_sid.time_EuEu_amp_med < amp_max )
    spec_sid.EuEu_med     = np.nanmedian(spec_sid.EuEu[index[0]],     axis=0)
    spec_sid.EuEu_raw_med = np.nanmedian(spec_sid.EuEu_raw[index[0]], axis=0)

    # peak
    peak_f = np.nanargmax(spec_sid.EuEu_a_max);  print('\n'+str_SID+' [peak-MAX]', spec_sid.EuEu_max.shape, spec_sid.freq.shape, peak_f)
    if spec_sid.sid != 7 and spec_sid.sid != 8 and spec_sid.sid != 23:
        spec_sid.peak_f     = spec_sid.freq1     [peak_f]
    if spec_sid.EuEu_max.size > 1:
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
    peak_f = np.nanargmax(spec_sid.EuEu_amp_max)
    if spec_sid.EuEu_amp_max.size > 1:
        spec_sid.peak_amp_max = spec_sid.EuEu_amp_max[peak_f];  spec_sid.peaks_amp_max = np.sum(spec_sid.EuEu_amp_max[peak_f-1:peak_f+2])
    else:
        spec_sid.peak_amp_max = spec_sid.EuEu_amp_max;          spec_sid.peaks_amp_max = spec_sid.EuEu_amp_max
    if spec_sid.sid != 7 and spec_sid.sid != 8 and spec_sid.sid != 23:
        print('[Peak - '+str_SID+' RAW-AMP in TLM  ]  EuEu:', '{:.2e}kHz            -- (peak)'.format(spec_sid.freq1[peak_f]),                  '{:.2e}'.format(spec_sid.peak_amp_max), '{:.2e}'.format(spec_sid.peak_amp_max**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_amp_max), '{:.2e}'.format(spec_sid.peaks_amp_max**.5) )
    else:
        print(spec_sid.peak_max)
        print(spec_sid.peaks_max)

        print('[Peak - '+str_SID+' RAW-AMP in TLM  ]  EuEu:')
        print(f'{spec_sid.peak_amp_max:.2e}')
        print('{:.2e}'.format(spec_sid.peak_amp_max))
        print('{:.2e}'.format(spec_sid.peak_amp_max**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_amp_max))
        print('{:.2e}'.format(spec_sid.peaks_amp_max**.5) )

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
def plot_data_Eu(data_sid, str_SID, mode_dump, mode_str, work_dir):
    fig = plt.figure(figsize=(16, 2));  ax1 = fig.add_subplot(3, 1, (1,2));  ax2 = fig.add_subplot(3, 1, 3)
    ax1.plot(np.ravel(data_sid.Eu_i[:][:]), '-r', linewidth=.5, label=str_SID+' Eu_i')
    ax1.plot(np.ravel(data_sid.Eu_q[:][:]), ':g', linewidth=.5, label=str_SID+' Eu_q');  ax1.set_ylabel(str_SID+' Eu (RAW)'); ax1.legend(loc='upper right')
    p_max = np.ceil(np.log10(np.nanmax([np.nanmax(data_sid.Eu_i), np.nanmax(data_sid.Eu_q)]))*5)/5
    xlim=[0, len(np.ravel(data_sid.Eu_i[:][:]))];   ax1.set_xlim(xlim)
    ylim=[-10**(p_max), 10**(p_max)];  ax1.set_ylim(ylim)

    ax2.plot(np.ravel(data_sid.epoch[:]), '.');     ax2.set_ylabel('Epoch')
    xlim=[0, data_sid.n_time];                      ax2.set_xlim(xlim)

    fig.subplots_adjust(hspace=0);  fig.show
    if mode_dump == 1:
        png_fname = work_dir+'EMU_raw_'+str_SID+mode_str+'.png'
        fig.savefig(png_fname)


def plot_data_EuEu(data_sid, str_SID, mode_dump, mode_str, work_dir):
    if data_sid.sid != 7 and data_sid.sid != 8 and data_sid.sid != 23:  fig = plt.figure(figsize=(16, 2))  
    else:                                                               fig = plt.figure(figsize=(16, 6.5))
    ax1 = fig.add_subplot(3, 1, (1,2));  ax2 = fig.add_subplot(3, 1, 3)

    ax1.plot(np.ravel(data_sid.EuEu    [:][:]), '-r', linewidth=.5, label=str_SID+' EuEu');  
    ax1.plot(np.ravel(data_sid.EuEu_raw[:][:]), ':g', linewidth=.5, label=str_SID+' EuEu_raw')
    ax1.plot(np.ravel(data_sid.EuEu_amp[:][:]), ':b', linewidth=.5, label=str_SID+' EuEu_amp');  ax1.set_ylabel(str_SID+' EuEu (RAW^2)'); ax1.legend(loc='upper right')
    xlim=[0, len(np.ravel(data_sid.EuEu[:][:]))];   ax1.set_xlim(xlim)

    p_max = np.ceil(np.log10( np.nanmax( [np.nanmax(data_sid.EuEu), np.nanmax(data_sid.EuEu_raw), np.nanmax(data_sid.EuEu_amp)] ) )*5)/5+.5
    p_min = np.ceil(np.log10( np.nanmin( [np.nanmin(data_sid.EuEu), np.nanmin(data_sid.EuEu_raw), np.nanmin(data_sid.EuEu_amp)] ) )*5)/5-.5
    ylim=[10**(p_min), 10**(p_max)]
    ylim=[10**(-3.5), 10**(9)]
    ax1.set_ylim(ylim);  ax1.set_yscale('log')    

    ax2.plot(np.ravel(data_sid.epoch[:]), '.');  ax2.set_ylabel('Epoch')
    xlim=[0, data_sid.n_time];                   ax2.set_xlim(xlim)

    fig.subplots_adjust(hspace=0);  fig.show
    if mode_dump == 1:
        png_fname = work_dir+'EMU_raw_'+str_SID+mode_str+'.png'
        fig.savefig(png_fname)


def plot_spec_EuEu(spec_sid, str_SID, mode_freq, mode_dump, mode_str, work_dir):
    lw = 1;  ms = 5
    fig = plt.figure(figsize=(16, 6.5));  ax1 = fig.add_subplot(1, 1, 1)

    ax1.plot(spec_sid.freq1, spec_sid.EuEu_a_max,   '.y', linewidth=lw, ms=ms, label=str_SID+' EuEu Amp-max')
    ax1.plot(spec_sid.freq2, spec_sid.EuEu_amp_max, '-r', linewidth=lw, ms=ms, label=str_SID+' EuEu Amp-max [RAW]')
    ax1.plot(spec_sid.freq1, spec_sid.EuEu_med,     '.c', linewidth=lw, ms=ms, label=str_SID+' EuEu med')
    ax1.plot(spec_sid.freq2, spec_sid.EuEu_raw_med, '-g', linewidth=lw, ms=ms, label=str_SID+' EuEu med [RAW]')

    ax1.set_ylabel(str_SID+' EuEu (RAW^2)');  ax1.legend(loc='upper left', fontsize=8); 
    ax1.set_yscale('log')
    if mode_freq == 1:  ax1.set_xscale('log')

    # xlim=[np.nanmin(spec_sid.freq), np.nanmax(spec_sid.freq)];  
    xlim=[19.5, 44789.5];        ax1.set_xlim(xlim)
    ylim=[10**(-3.5), 10**(9)];  ax1.set_ylim(ylim)

    fig.show
    if mode_dump == 1:
        png_fname = work_dir+'EMU_spec_'+str_SID+mode_str+'.png'
        fig.savefig(png_fname)