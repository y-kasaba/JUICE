"""
    JUICE RPWI HF Emulation and Comparison: L1a for all SIDs -- 2025/10/17
"""
# import copy
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import medfilt

def datalist():
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

    # *** Flight - Ver.2 ***
    """
    # SID-2  ASW2        20250331    OFF & CAL
    cdf_sid2 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID2_20250331T005104-20250331T233757_V01___RPR1_52000005_2025.091.16.38.56.448.cdf'
    # SID-3  ASW2 COMP-1 20250331    
    cdf_sid3 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID3_20250331T030012-20250331T201834_V01___RPR1_52000005_2025.091.16.38.56.448.cdf'
    # SID-20 ASW2 COMP-1 20240706
    cdf_sid20= '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID20_20240819T203025-20240819T210933_V01___RPR1_52000003_2024.233.02.43.43.102.cdf'
    # SID-4  ASW2 COMP-1 20240706
    cdf_sid4 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID4_20240706T121439-20240706T125422_V01___RPR1_52000002_2024.190.14.59.43.630.cdf'
    # SID-21 ASW2 COMP-1 20250331
    cdf_sid21= '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID21_20250331T033821-20250331T034222_V01___RPR2_62000007_2025.091.16.40.05.450.cdf'
    # SID-5  ASW2        20250331
    cdf_sid5 = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/JUICE_L1a_RPWI-HF-SID5_20250331T033821-20250331T034222_V01___RPR2_62000007_2025.091.16.40.05.450.cdf'
    """

    print('[SID-02]', cdf_sid2)
    print('[SID-03]', cdf_sid3)
    print('[SID-20]', cdf_sid20)
    print('[SID-04]', cdf_sid4)
    print('[SID-21]', cdf_sid21)
    print('[SID-05]', cdf_sid5)
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
    print("[Peak - '+str_SID+' Wave]  Eu:", '{:.2e} '.format(wave_sid.peak))
    return wave_sid


def wave_shaping_EuEu(data_sid, str_SID, n_sweep1, n_sweep2):
    class struct:
        pass
    wave_sid = struct()
    wave_sid.EuEu   = data_sid.EuEu [n_sweep1:n_sweep2]
    wave_sid.epoch  = data_sid.epoch[n_sweep1:n_sweep2]
    wave_sid.n_time = wave_sid.EuEu.shape[0]

    peak = np.ravel(wave_sid.EuEu); wave_sid.peak = np.nanmax(peak)
    print('[Peak - '+str_SID+' Wave]  EuEu:', '{:.2e} '.format(wave_sid.peak), '{:.2e}'.format(wave_sid.peak**.5))
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
    return spec_sid


def spec_shaping_EuEu(spec_sid, str_SID, n_sweep1, n_sweep2, n_median):
    spec_sid.EuEu      = spec_sid.EuEu  [n_sweep1:n_sweep2]  
    spec_sid.epoch     = spec_sid.epoch [n_sweep1:n_sweep2]
    spec_sid.n_time    = spec_sid.EuEu.shape[0]
    spec_sid.freq      = spec_sid.freq  [spec_sid.n_time//2]
    spec_sid.df        = spec_sid.freq_w[spec_sid.n_time//2][0] * 1000.  # juice_cdf._sample_rate(data_sid2.decimation[0])
    spec_sid.EuEu_max  = np.nanmax   (spec_sid.EuEu, axis=0);    spec_sid.EuEu_s_max = spec_sid.EuEu_max / spec_sid.df
    spec_sid.EuEu_med  = np.nanmedian(spec_sid.EuEu, axis=0);    spec_sid.EuEu_s_med = spec_sid.EuEu_med / spec_sid.df
    spec_sid.EuEu_cln  = medfilt(spec_sid.EuEu_med,  n_median);  spec_sid.EuEu_s_cln = medfilt(spec_sid.EuEu_s_med, n_median)

    peak_f = np.nanargmax(spec_sid.EuEu_max);        spec_sid.peak_f     = spec_sid.freq      [peak_f]
    spec_sid.peak_max  = spec_sid.EuEu_max[peak_f];  spec_sid.peak_s_max = spec_sid.EuEu_s_max[peak_f]
    spec_sid.peak_med  = spec_sid.EuEu_med[peak_f];  spec_sid.peak_s_med = spec_sid.EuEu_s_med[peak_f]
    spec_sid.peaks_max = spec_sid.EuEu_max[peak_f-1] + spec_sid.EuEu_max[peak_f] + spec_sid.EuEu_max[peak_f+1] 
    spec_sid.peaks_med = spec_sid.EuEu_med[peak_f-1] + spec_sid.EuEu_med[peak_f] + spec_sid.EuEu_med[peak_f+1]
    spec_sid.peaks_max = np.sum(spec_sid.EuEu_max[peak_f-1:peak_f+2])
    spec_sid.peaks_med = np.sum(spec_sid.EuEu_med[peak_f-1:peak_f+2])
    spec_sid.peaks_s_max = np.sum(spec_sid.EuEu_s_max[peak_f-1:peak_f+2])
    spec_sid.peaks_s_med = np.sum(spec_sid.EuEu_s_med[peak_f-1:peak_f+2])
    
    print('[Peak - '+str_SID+' Spec in RAW^2   ]  EuEu:', '{:.2e}kHz               -- (peak)'.format(spec_sid.peak_f), '{:.2e}'.format(spec_sid.peak_max), '{:.2e}'.format(spec_sid.peak_max**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_max), '{:.2e}'.format(spec_sid.peaks_max**.5))
    print('[Med  - '+str_SID+' Spec in RAW^2   ]  EuEu:', '{:.2e}kHz               -- (peak)'.format(spec_sid.peak_f), '{:.2e}'.format(spec_sid.peak_med), '{:.2e}'.format(spec_sid.peak_med**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_med), '{:.2e}'.format(spec_sid.peaks_med**.5))
    print('[Peak - '+str_SID+' Spec in RAW^2/Hz]  EuEu:', '{:.2e}'.format(spec_sid.peak_f), '({:.2e})kHz -- (peak)'.format(spec_sid.df/1000), '{:.2e}'.format(spec_sid.peak_s_max), '{:.2e}'.format(spec_sid.peak_s_max**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_s_max), '{:.2e}'.format(spec_sid.peaks_s_max**.5))
    print('[Med  - '+str_SID+' Spec in RAW^2/Hz]  EuEu:', '{:.2e}'.format(spec_sid.peak_f), '({:.2e})kHz -- (peak)'.format(spec_sid.df/1000), '{:.2e}'.format(spec_sid.peak_s_med), '{:.2e}'.format(spec_sid.peak_s_med**.5), '| (sum) {:.2e}'.format(spec_sid.peaks_s_med), '{:.2e}'.format(spec_sid.peaks_s_med**.5))
    return spec_sid


def spec_shaping_EuEu_sid20(data_sid, spec_sid, n_median):
    from datetime import timedelta

    # Time resoution: 1/n_block [sec]
    Epoch = spec_sid.epoch.tolist();   spec_sid.Epoch_1d = []
    for i in range(data_sid.n_block):
        spec_sid.Epoch_1d += Epoch
    for i in range(spec_sid.n_time):
        for j in range(data_sid.n_block):
            spec_sid.Epoch_1d[i * data_sid.n_block + j] = Epoch[i] + timedelta(seconds = j/data_sid.n_block)
    freq = spec_sid.freq
    spec_sid.freq_1d = freq[0:data_sid.n_step]

    # Time resoution: 1/n_block [sec]
    spec_sid.EuEu_1d     = spec_sid.EuEu.reshape(spec_sid.n_time * data_sid.n_block, data_sid.n_step)
    spec_sid.EuEu_1d_med = np.nanmedian(spec_sid.EuEu_1d, axis=0);    spec_sid.EuEu_1d_med2 = spec_sid.EuEu_1d_med / spec_sid.df
    spec_sid.EuEu_1d_cln = medfilt(spec_sid.EuEu_1d_med,  n_median);  spec_sid.EuEu_1d_cln2 = medfilt(spec_sid.EuEu_1d_med2, n_median)
    f_min0  = spec_sid.freq_1d[0];  f_max0 = spec_sid.freq_1d[-1]
    print("[SID-20]   f_min/MAX:", f_min0, f_max0, "   num of f, step, window:", data_sid.n_step, data_sid.freq_step[0][0], data_sid.freq_width[0][0])

    # Peak
    peak_f = np.nanargmax(spec_sid.EuEu_1d_med);  spec_sid.peak_f = spec_sid.freq_1d[peak_f]
    spec_sid.peak   = spec_sid.EuEu_1d_med [peak_f]
    spec_sid.peak2  = spec_sid.EuEu_1d_med2[peak_f]
    spec_sid.peaks  = spec_sid.EuEu_1d_med [peak_f-1] + spec_sid.EuEu_1d_med [peak_f] + spec_sid.EuEu_1d_med [peak_f+1] 
    spec_sid.peaks2 = spec_sid.EuEu_1d_med2[peak_f-1] + spec_sid.EuEu_1d_med2[peak_f] + spec_sid.EuEu_1d_med2[peak_f+1]
    print('[Peak - SID-20 Spec in RAW^2   ]  EuEu:', '{:.2e} kHz           -- (peak)'.format(spec_sid.peak_f), '{:.2e}'.format(spec_sid.peak), '{:.2e}'.format(spec_sid.peak**.5), '| (sum) {:.2e}'.format(spec_sid.peaks), '{:.2e}'.format(spec_sid.peaks**.5))
    print('[Peak - SID-20 Spec in RAW^2/Hz]  EuEu:',
        '{:.2e}'.format(spec_sid.peak_f), '({:.2e})kHz -- (peak)'.format(spec_sid.df/1000), 
        '{:.2e}'.format(spec_sid.peak2), '{:.2e}'.format(spec_sid.peak2**.5), '| (sum) {:.2e}'.format(spec_sid.peaks2), '{:.2e}'.format(spec_sid.peaks2**.5))

    return spec_sid


# **************
# **** PLOT ****
# **************
def plot_data_Eu(data_sid, str_SID, dump_mode):
    fig = plt.figure(figsize=(16, 11));  ax1 = fig.add_subplot(2, 1, 1);  ax2 = fig.add_subplot(2, 1, 2)
    ax1.plot(np.ravel(data_sid.Eu_i[:][:]), '-r', linewidth=.5, label=str_SID+' Eu_i')
    ax1.plot(np.ravel(data_sid.Eu_q[:][:]), ':g', linewidth=.5, label=str_SID+' Eu_q');  ax1.set_ylabel(str_SID+' Eu (RAW)'); ax1.legend(loc='upper right')
    xlim=[-0.5, len(np.ravel(data_sid.Eu_i[:][:])) -0.5];  ax1.set_xlim(xlim)
    p_max = np.ceil(np.log10(np.nanmax([np.nanmax(data_sid.Eu_i), np.nanmax(data_sid.Eu_q)]))*5)/5
    ylim=[-10**(p_max), 10**(p_max)];  ax1.set_ylim(ylim)

    ax2.plot(np.ravel(data_sid.epoch[:]), '.');   ax2.set_ylabel('Epoch')
    xlim=[-0.5, data_sid.n_time -0.5];            ax2.set_xlim(xlim)

    fig.subplots_adjust(hspace=0);  fig.show
    if dump_mode == 1:
        png_fname = work_dir+'EMU_'+str_SID+'_raw.png'
        fig.savefig(png_fname)


def plot_data_EuEu(data_sid, str_SID, dump_mode):
    fig = plt.figure(figsize=(16, 11));  ax1 = fig.add_subplot(2, 1, 1);  ax2 = fig.add_subplot(2, 1, 2)
    ax1.plot(np.ravel(data_sid.EuEu[:][:]), '-r', linewidth=.5, label=str_SID+' EuEu');  ax1.set_ylabel(str_SID+' EuEu (RAW^2)'); ax1.legend(loc='upper right')
    xlim=[-0.5, len(np.ravel(data_sid.EuEu[:][:])) -0.5];  ax1.set_xlim(xlim);  ax1.set_yscale('log')
    p_max = np.ceil(np.log10(np.nanmax(data_sid.EuEu))*5)/5
    p_min = np.ceil(np.log10(np.nanmin(data_sid.EuEu))*5)/5
    ylim=[10**(p_min), 10**(p_max)];  ax1.set_ylim(ylim)

    ax2.plot(np.ravel(data_sid.epoch[:]), '.');            ax2.set_ylabel('Epoch')
    xlim=[-0.5, data_sid.n_time                    -0.5];  ax2.set_xlim(xlim)

    fig.subplots_adjust(hspace=0);  fig.show
    if dump_mode == 1:
        png_fname = work_dir+'EMU_'+str_SID+'_raw.png'
        fig.savefig(png_fname)


def plot_spec_EuEu(spec_sid, n_sweep1, n_sweep2, n_sweep3, str_SID, f_mode, dump_mode):
    fig = plt.figure(figsize=(16, 11));  ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(spec_sid.freq, spec_sid.EuEu[n_sweep1], '-r', linewidth=.2, label=str_SID+' EuEu {:d}'.format(n_sweep1))
    ax1.plot(spec_sid.freq, spec_sid.EuEu[n_sweep2], '-g', linewidth=.2, label=str_SID+' EuEu {:d}'.format(n_sweep2))
    ax1.plot(spec_sid.freq, spec_sid.EuEu[n_sweep3], '-b', linewidth=.2, label=str_SID+' EuEu {:d}'.format(n_sweep3))
    ax1.plot(spec_sid.freq, spec_sid.EuEu_med,       '-k', linewidth=1,  label=str_SID+' EuEu med')
    ax1.plot(spec_sid.freq, spec_sid.EuEu_cln,       '-r', linewidth=1,  label=str_SID+' EuEu cln')
    ax1.set_ylabel(str_SID+' EuEu (RAW^2)');  ax1.legend(loc='upper right', fontsize=8); 
    ax1.set_yscale('log')
    if f_mode == 1:
        ax1.set_xscale('log')

    xlim=[np.nanmin(spec_sid.freq), np.nanmax(spec_sid.freq)]
    ax1.set_xlim(xlim)
    #ylim=[10**(p_min), 10**(p_max)]
    #ax1.set_ylim(ylim)

    fig.show
    if dump_mode == 1:
        png_fname = work_dir+'EMU_'+str_SID+'_spec.png'