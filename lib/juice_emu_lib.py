"""
    JUICE RPWI HF Emulation and Comparison: L1a for all SIDs -- 2025/11/11
"""
# import copy
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import medfilt
#
import juice_cdf_lib  as juice_cdf

def datalist(asw, space, cal_mode):
    if asw == 3:
        if space == 0:
            # *** Ground Test - Ver.3 ***
            # SID-2    ASW3        20251010    1.5MHz  OFF->10mVpp->100mVpp->500mVpp->OFF (500mVpp - saturated)
            cdf_sid2 = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/JUICE_L1a_RPWI-HF-SID2_20000101T000327-20000101T000857_V01___SID02_20251010-1729.ccs.cdf'
            # SID-3    ASW3  COMP-1 20250925    1.5MHz  Vin=10mVpp  Phase=[0 45 90 135 180 225 270 315 0] deg (V-ch)
            cdf_sid3 = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/JUICE_L1a_RPWI-HF-SID3_20000101T000151-20000101T000731_V01___SID03-comp1_20250925-1148_10mVpp.ccs.cdf'
            # SID-20   ASW3  COMP-1 20250925    0.02-2MHz 5s  Vin=10 mVpp
            cdf_sid20= '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/JUICE_L1a_RPWI-HF-SID20_20000101T031404-20000101T031417_V01___SID04-20_0.2s_20250925-1500_10mVpp.ccs.cdf'
            # SID-20   ASW3  COMP-1 20250925    0.02-2MHz 5s	 Vin=10 mVpp
            cdf_sid4 = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/JUICE_L1a_RPWI-HF-SID4_20000101T031404-20000101T031414_V01___SID04-20_0.2s_20250925-1500_10mVpp.ccs.cdf'
            # SID-21   ASW3  COMP-1 20250926    1.5MHz  Vin=10mVpp, Phase=[0 45 90 135 180 225 270 315 0] deg (V-ch) 
            cdf_sid21= '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/JUICE_L1a_RPWI-HF-SID21_20000101T002153-20000101T004523_V01___SID05-21_20250926-0820_10mVpp.ccs.cdf'
            # SID-5    ASW3         20250926    1.5MHz  Vin=10mVpp, Phase=[0 45 90 135 180 225 270 315 0] deg (V-ch) 
            cdf_sid5 = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/JUICE_L1a_RPWI-HF-SID5_20000101T002153-20000101T004523_V01___SID05-21_20250926-0820_10mVpp.ccs.cdf'

    if asw == 2:
        if space == 1:
            # *** Flight - Ver.2 ***
            # SID-2  ASW2        20250331   normal + OFF + CAL
            cdf_sid2 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID2_20250331T005104-20250331T233757_V01___RPR1_52000005_2025.091.16.38.56.448.cdf'
            # SID-3  ASW2 COMP-1 20250331   normal + CAL
            if cal_mode == 1:  # CAL
                cdf_sid3 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID3_20240822T095914-20240822T182844_V01___RPR1_52000004_2024.236.08.13.31.519.cdf' # CAL
            else:
                cdf_sid3 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID3_20250331T030012-20250331T201834_V01___RPR1_52000005_2025.091.16.38.56.448.cdf' # Normal
            # SID-20 ASW2 COMP-1 20240706   normal
            cdf_sid20= '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID20_20240706T121424-20240706T125428_V01___RPR2_62000002_2024.190.19.50.21.637.cdf'
            # SID-4  ASW2 COMP-1 20240706   normal
            cdf_sid4 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID4_20240706T121439-20240706T125422_V01___RPR1_52000002_2024.190.14.59.43.630.cdf'
            # SID-21 ASW2 COMP-1 20250331   nornal & CAL
            cdf_sid21= '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID21_20250331T033821-20250331T034222_V01___RPR2_62000007_2025.091.16.40.05.450.cdf'
            # SID-5  ASW2        20250331   nornal & CAL
            cdf_sid5 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID5_20250331T033821-20250331T034222_V01___RPR1_52000005_2025.091.16.38.56.448.cdf'

    if asw == 1:
        if space == 1:
            # *** Flight - Ver.1 ***
            # SID-2  ASW1       20230530   normal + CAL
            cdf_sid2 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW1/JUICE_L1a_RPWI-HF-SID2_20230530T100330-20230530T100930_V01___RPR1_52000010_2023.150.10.40.53.663.cdf' # 230530 background & CAL
            # SID-3  ASW1       20250523   normal + CAL
            cdf_sid3 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW1/JUICE_L1a_RPWI-HF-SID3_20230523T110938-20230523T111154_V01___RPR1_52000003_2023.143.11.14.17.500.cdf' # 230523 after Y deployment: with CAL
            # dummy
            cdf_sid20= ''
            cdf_sid4 = ''
            cdf_sid21= ''
            cdf_sid5 = ''
            
    print('[SID-02]', cdf_sid2)
    print('[SID-03]', cdf_sid3)
    print('[SID-20]', cdf_sid20);  print('[SID-04]', cdf_sid4)
    print('[SID-21]', cdf_sid21);  print('[SID-05]', cdf_sid5)
    return cdf_sid2, cdf_sid3, cdf_sid20, cdf_sid4, cdf_sid21, cdf_sid5


# *****************
# **** SHAPING ****
# *****************
def wave_shaping_Eu(data_sid, str_SID, n_sweep1, n_sweep2):
    class struct:
        pass
    wave_sid = struct()
    wave_sid.Eu_i   = data_sid.Eu_i [n_sweep1:n_sweep2]
    wave_sid.Eu_q   = data_sid.Eu_q [n_sweep1:n_sweep2]
    wave_sid.epoch  = data_sid.epoch[n_sweep1:n_sweep2]
    wave_sid.n_time = wave_sid.Eu_i.shape[0]

    peak = np.ravel(wave_sid.Eu_i); wave_sid.peak = np.nanmax(peak)
    print('[Peak - '+str_SID+' Wave in RAW     ]    Eu:', '                       -- (peak)                                    {:.2e} '.format(wave_sid.peak))
    return wave_sid


def wave_shaping_EuEu(data_sid, str_SID, n_sweep1, n_sweep2):
    class struct:
        pass
    wave_sid = struct()
    wave_sid.EuEu   = data_sid.EuEu [n_sweep1:n_sweep2]
    wave_sid.epoch  = data_sid.epoch[n_sweep1:n_sweep2]
    wave_sid.n_time = wave_sid.EuEu.shape[0]
    wave_sid.HF_ID  = data_sid.HF_ID
    wave_sid.sid    = data_sid.sid

    peak = np.ravel(wave_sid.EuEu); wave_sid.peak = np.nanmax(peak)
    print('[Peak - '+str_SID+' Wave in RAW^2   ]  EuEu:', '                       -- (peak) {:.2e} '.format(wave_sid.peak), '{:.2e}'.format(wave_sid.peak**.5))
    return wave_sid


# **************
# **** SPEC ****
# **************
def spec_data2spec(data_sid):
    class struct:
        pass
    spec_sid = struct()
    spec_sid.EuEu   = data_sid.EuEu
    spec_sid.epoch  = data_sid.epoch
    spec_sid.freq   = data_sid.freq
    spec_sid.freq_w = data_sid.freq_w
    spec_sid.HF_ID  = data_sid.HF_ID
    spec_sid.sid    = data_sid.sid
    if spec_sid.sid == 20:
        spec_sid.n_block = data_sid.N_block[spec_sid.EuEu.shape[0]//2]
        spec_sid.n_step  = data_sid.N_step [spec_sid.EuEu.shape[0]//2]

    ##################################################################
    # GAIN correction -- tentative
    ##################################################################
    if data_sid.RPWI_FSW_version == 1:
        if spec_sid.sid == 3:
            spec_sid.EuEu *= 1.                                     # TBC

    if data_sid.RPWI_FSW_version == 2:
        if spec_sid.sid == 3:
            spec_sid.EuEu /=  5000.             # TBC
        if spec_sid.sid == 4 or spec_sid.sid == 20:
            spec_sid.freq_w /= 2                # TBC --
        if spec_sid.sid == 5:
            spec_sid.EuEu   /= (5000. * 2.828)  # TBC -- 2.828 = sqrt(8)
            spec_sid.freq_w /= (8     * 2.828)  # TBC --
        if spec_sid.sid == 21:
            spec_sid.EuEu /=  5000.             # TBC

    if data_sid.RPWI_FSW_version == 3:
        if spec_sid.sid == 3:
            spec_sid.EuEu /=   1.8              # TBC
        if spec_sid.sid == 4 or spec_sid.sid == 20:
            spec_sid.EuEu /=   1.2              # TBC
        #    spec_sid.freq_w /= 2.              # TBC --
        if spec_sid.sid == 5:
            spec_sid.EuEu /=  (1.8 * 2.828 )    # TBC -- 2.828 = sqrt(8)
        if spec_sid.sid == 21:
            spec_sid.EuEu /=   1.8              # TBC
    ##################################################################
    # GAIN correction -- tentative
    ##################################################################

    return spec_sid


def spec_shaping_EuEu(spec_sid, str_SID, n_sweep1, n_sweep2, n_median):
    # [TLM]                 [RAW^2/Hz]              [RAW^2]
    # spec_sid.EuEu_max     pec_sid.EuEu_s_max      spec_sid.EuEu_a_max     *** MAX *** 
    # spec_sid.EuEu_med     spec_sid.EuEu_s_med     spec_sid.EuEu_a_med     *** median ***
    # spec_sid.EuEu_cln     spec_sid.EuEu_s_cln     spec_sid.EuEu_a_cln     *** clean (background) ***
    spec_sid.EuEu      = spec_sid.EuEu  [n_sweep1:n_sweep2]  
    spec_sid.epoch     = spec_sid.epoch [n_sweep1:n_sweep2]
    spec_sid.n_time    = spec_sid.EuEu.shape[0]
    spec_sid.freq      = spec_sid.freq  [spec_sid.n_time//2]
    spec_sid.freq_w    = spec_sid.freq_w[spec_sid.n_time//2]
    if spec_sid.sid == 20:  spec_shaping_EuEu_sid20(spec_sid)

    # df -- bandwidth in original (kHz)
    #    ret = 37          # SID-4/20      simple sum
    #    ret = 296         # SID-6/22/7    296 or 148 kHz
    #    ret = 2.3125      # SID-2/3/5/21  296kHz / 128(N_samp) 
    #    ret = 0.08894     # SID-23        296kHz / 128(N_samp) / 26(N_feed)
    spec_sid.df      = juice_cdf._df_org(spec_sid.HF_ID) * 1000.  # kHz -> Hz
    spec_sid.df_freq = spec_sid.freq_w                   * 1000.  # kHz -> Hz
    if (str_SID=='SID-2_Wsum' or str_SID=='SID-2_Fsum'):
        spec_sid.df = spec_sid.freq_w[0] * 1000.
    # print(f"**** SID:{spec_sid.sid}  df_org:{spec_sid.df}kHz  df:{spec_sid.df_freq}")

    # TLM, RAW/Hz^2, Sum
    spec_sid.EuEu_max   = np.nanmax(spec_sid.EuEu, axis=0);        spec_sid.EuEu_med   = np.nanmedian(spec_sid.EuEu, axis=0);     spec_sid.EuEu_cln   = medfilt(spec_sid.EuEu_med,   n_median)
    spec_sid.EuEu_s_max = spec_sid.EuEu_max   / spec_sid.df;       spec_sid.EuEu_s_med = spec_sid.EuEu_med   / spec_sid.df;       spec_sid.EuEu_s_cln = medfilt(spec_sid.EuEu_s_med, n_median)
    spec_sid.EuEu_a_max = spec_sid.EuEu_s_max * spec_sid.df_freq;  spec_sid.EuEu_a_med = spec_sid.EuEu_s_med * spec_sid.df_freq;  spec_sid.EuEu_a_cln = medfilt(spec_sid.EuEu_a_med, n_median)

    # peak
    peak_f = np.nanargmax(spec_sid.EuEu_max);           spec_sid.peak_f      = spec_sid.freq      [peak_f]
    spec_sid.peak_max   = spec_sid.EuEu_max[peak_f];    spec_sid.peaks_max   = np.sum(spec_sid.EuEu_max[peak_f-1:peak_f+2])
    spec_sid.peak_s_max = spec_sid.EuEu_s_max[peak_f];  spec_sid.peaks_s_max = np.sum(spec_sid.EuEu_s_max[peak_f-1:peak_f+2])
    spec_sid.peak_a_max = spec_sid.EuEu_a_max[peak_f];  spec_sid.peaks_a_max = np.sum(spec_sid.EuEu_a_max[peak_f-1:peak_f+2])

    print('[Peak - '+str_SID+' Spec in TLM     ]  EuEu:', '{:.2e}kHz            -- (peak)'.format(spec_sid.peak_f), '{:.2e}'.format(spec_sid.peak_max), '{:.2e}'.format(spec_sid.peak_max**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_max), '{:.2e}'.format(spec_sid.peaks_max**.5))
    print('[Peak - '+str_SID+' Spec in RAW^2/Hz]  EuEu:', '{:.2e}'.format(spec_sid.peak_f), '({:.2e})kHz -- (peak)'.format(spec_sid.df/1000), '{:.2e}'.format(spec_sid.peak_s_max), '{:.2e}'.format(spec_sid.peak_s_max**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_s_max), '{:.2e}'.format(spec_sid.peaks_s_max**.5))
    print('[Peak - '+str_SID+' Spec in RAW^2   ]  EuEu:', '{:.2e}'.format(spec_sid.peak_f), '({:.2e})kHz -- (peak)'.format(spec_sid.df/1000), '{:.2e}'.format(spec_sid.peak_a_max), '{:.2e}'.format(spec_sid.peak_a_max**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_a_max), '{:.2e}'.format(spec_sid.peaks_a_max**.5))
    return spec_sid


def spec_shaping_EuEu_sid20(spec_sid):
    from datetime import timedelta

    # Epoch -- Time resoution: 1/n_block [sec]
    Epoch = spec_sid.epoch.tolist();   Epoch_1d = []
    for i in range(spec_sid.n_block):
        Epoch_1d += Epoch
    for i in range(spec_sid.n_time):
        for j in range(spec_sid.n_block):
            Epoch_1d[i * spec_sid.n_block + j] = Epoch[i] + timedelta(seconds = j/spec_sid.n_block)
    spec_sid.epoch = Epoch

    # Frequency
    spec_sid.freq   = spec_sid.freq  [0:spec_sid.n_step]
    spec_sid.freq_w = spec_sid.freq_w[0:spec_sid.n_step]

    # EuEu
    spec_sid.EuEu   = spec_sid.EuEu.reshape(spec_sid.n_time * spec_sid.n_block, spec_sid.n_step)
    spec_sid.n_time = spec_sid.EuEu.shape[0]
    return spec_sid


# **************
# **** PLOT ****
# **************
def plot_data_Eu(data_sid, str_SID, dump_mode, str_mode, work_dir):
    fig = plt.figure(figsize=(16, 5));  ax1 = fig.add_subplot(3, 1, (1,2));  ax2 = fig.add_subplot(3, 1, 3)
    ax1.plot(np.ravel(data_sid.Eu_i[:][:]), '-r', linewidth=.5, label=str_SID+' Eu_i')
    ax1.plot(np.ravel(data_sid.Eu_q[:][:]), ':g', linewidth=.5, label=str_SID+' Eu_q');  ax1.set_ylabel(str_SID+' Eu (RAW)'); ax1.legend(loc='upper right')
    p_max = np.ceil(np.log10(np.nanmax([np.nanmax(data_sid.Eu_i), np.nanmax(data_sid.Eu_q)]))*5)/5
    ylim=[-10**(p_max), 10**(p_max)];  ax1.set_ylim(ylim)

    ax2.plot(np.ravel(data_sid.epoch[:]), '.');     ax2.set_ylabel('Epoch')
    xlim=[0, len(np.ravel(data_sid.Eu_i[:][:])) - 1];   ax1.set_xlim(xlim)
    xlim=[0, data_sid.n_time];                  ax2.set_xlim(xlim)

    fig.subplots_adjust(hspace=0);  fig.show
    if dump_mode > 1:
        png_fname = work_dir+'EMU_raw_'+str_SID+str_mode+'.png'
        fig.savefig(png_fname)


def plot_data_EuEu(data_sid, str_SID, dump_mode, str_mode, work_dir):
    fig = plt.figure(figsize=(16, 5));  ax1 = fig.add_subplot(3, 1, (1,2));  ax2 = fig.add_subplot(3, 1, 3)
    ax1.plot(np.ravel(data_sid.EuEu[:][:]), '-r', linewidth=.5, label=str_SID+' EuEu');  ax1.set_ylabel(str_SID+' EuEu (RAW^2)'); ax1.legend(loc='upper right')
    xlim=[0, len(np.ravel(data_sid.EuEu[:][:])) - 1];   ax1.set_xlim(xlim);  # ax1.set_yscale('log')
    p_max = np.ceil(np.log10(np.nanmax(data_sid.EuEu))*5)/5
    p_min = np.ceil(np.log10(np.nanmin(data_sid.EuEu))*5)/5
    ylim=[10**(p_min), 10**(p_max)];  ax1.set_ylim(ylim)

    ax2.plot(np.ravel(data_sid.epoch[:]), '.');         ax2.set_ylabel('Epoch')
    xlim=[0, data_sid.n_time];                      ax2.set_xlim(xlim)

    fig.subplots_adjust(hspace=0);  fig.show
    if dump_mode > 1:
        png_fname = work_dir+'EMU_raw_'+str_SID+str_mode+'.png'
        fig.savefig(png_fname)


def plot_spec_EuEu(spec_sid, n_sweep1, n_sweep2, n_sweep3, str_SID, f_mode, dump_mode, str_mode, work_dir):
    fig = plt.figure(figsize=(16, 11));  ax1 = fig.add_subplot(1, 1, 1)
    #ax1.plot(spec_sid.freq, spec_sid.EuEu[n_sweep1], '-r', linewidth=.2, label=str_SID+' EuEu {:d}'.format(n_sweep1))
    #ax1.plot(spec_sid.freq, spec_sid.EuEu[n_sweep2], '-g', linewidth=.2, label=str_SID+' EuEu {:d}'.format(n_sweep2))
    #ax1.plot(spec_sid.freq, spec_sid.EuEu[n_sweep3], '-b', linewidth=.2, label=str_SID+' EuEu {:d}'.format(n_sweep3))
    ax1.plot(spec_sid.freq, spec_sid.EuEu_max,       '-k', linewidth=1,  label=str_SID+' EuEu max (TLM)')
    ax1.plot(spec_sid.freq, spec_sid.EuEu_med,       '-g', linewidth=1,  label=str_SID+' EuEu med (TLM)')
    ax1.plot(spec_sid.freq, spec_sid.EuEu_cln,       '-r', linewidth=1,  label=str_SID+' EuEu cln (TLM)')
    ax1.plot(spec_sid.freq, spec_sid.EuEu_a_max,     ':k', linewidth=1,  label=str_SID+' EuEu Amp max (RAW^2)')
    ax1.plot(spec_sid.freq, spec_sid.EuEu_a_med,     ':g', linewidth=1,  label=str_SID+' EuEu Amp med (RAW^2)')
    ax1.plot(spec_sid.freq, spec_sid.EuEu_a_cln,     ':r', linewidth=1,  label=str_SID+' EuEu Amp cln (RAW^2)')
    ax1.plot(spec_sid.freq, spec_sid.EuEu_s_max,     '.k', linewidth=1,  label=str_SID+' EuEu max (RAW^2/Hz)')
    ax1.plot(spec_sid.freq, spec_sid.EuEu_s_med,     '.g', linewidth=1,  label=str_SID+' EuEu med (RAW^2/Hz)')
    ax1.plot(spec_sid.freq, spec_sid.EuEu_s_cln,     '.r', linewidth=1,  label=str_SID+' EuEu cln (RAW^2/Hz)')


    ax1.set_ylabel(str_SID+' EuEu (RAW^2)');  ax1.legend(loc='upper right', fontsize=8); 
    ax1.set_yscale('log')
    if f_mode == 1:
        ax1.set_xscale('log')

    xlim=[np.nanmin(spec_sid.freq), np.nanmax(spec_sid.freq)]
    ax1.set_xlim(xlim)
    #ylim=[10**(p_min), 10**(p_max)]
    #ax1.set_ylim(ylim)

    fig.show
    if dump_mode > 0:
        png_fname = work_dir+'EMU_spec_'+str_SID+str_mode+'.png'
        fig.savefig(png_fname)
