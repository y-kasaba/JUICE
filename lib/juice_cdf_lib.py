# JUICE RPWI HF CDF lib -- 2024/3/31

import glob
import spacepy.pycdf
import numpy as np


class struct:
    pass


# ---------------------------------------------------------------------
# --- Read CDF --------------------------------------------------------------
# ---------------------------------------------------------------------
def juice_read_cdfs(date_str, label, ver_str="01", base_dir="/db/JUICE/juice/datasets/"):

    yr_str = date_str[0:4]
    mn_str = date_str[4:6]
    dy_str = date_str[6:8]
    search_path = base_dir+yr_str+'/'+mn_str+'/'+dy_str + \
        '/JUICE_LU_RPWI-PPTD-'+label+'_'+date_str+'T??????_V'+ver_str+'.cdf'

    fname = glob.glob(search_path)
    if len(fname) > 0:
        err = 0
        ret = spacepy.pycdf.concatCDF([
            spacepy.pycdf.CDF(f) for f in glob.glob(search_path)])
    else:
        err = 1
        ret = 0

    return ret, err


# ---------------------------------------------------------------------
# --- QL --------------------------------------------------------------
# ---------------------------------------------------------------------
# Sampling rate [Hz]
def _sample_rate(decimation):
    ret = 296e+3
    if decimation >= 0 and decimation <= 3:
        ret = (296e+3)/(2**decimation)
    return ret


# ---------------------------------------------------------------------
# --- Frequency -------------------------------------------------------
# ---------------------------------------------------------------------
# Frequency: linear [kHz]
# output: freq, f_step, f_width
# Frequency: linear [kHz]
def _get_frequencies(sample_rate, n_freq, samp):
    fs = 80e3                       # start freq
    fe = 45e6                       # end   freq
    df = (fe - fs) / (n_freq - 1)   # band width

    i_freq = np.arange(0, n_freq)
    freq = np.float32((fs + df * i_freq) / 1000.)
    step = np.float32((i_freq * 0. + df) / 1000.)
    width = np.float32(
        (i_freq * 0. + sample_rate * 0.7566) / 1000.,
    )

    freq = np.repeat(freq, samp)
    step = np.repeat(step, samp)
    width = np.repeat(width, samp)
    return freq, step, width


# Frequency: Band
# Output: freq, step, width
def _get_frequencies_band(sample_rate, b_num, b_start, b_stop,
                          b_step, b_repeat, b_sdiv, samp):
    freq = []
    step = []
    width = []
    for i in range(b_num):
        f_freq, f_step, f_width = _get_band(
            b_start[i], b_stop[i], b_step[i], b_sdiv[i], sample_rate,
        )
        freq.extend(f_freq)
        step.extend(f_step)
        width.extend(f_width)

    freq = np.repeat(freq, samp)
    step = np.repeat(step, samp)
    width = np.repeat(width, samp)
    return freq, step, width


# Frequency: Band
# Output: freq, step, width
def _get_band(start, stop, step, sdiv, bw_eff):
    freq_band = np.float32(np.repeat(-10 ** 30, step * sdiv))
    freq_step = np.float32(np.repeat(-10 ** 30, step * sdiv))
    freq_width = np.float32(np.repeat(-10 ** 30, step * sdiv))
    f_step = (stop - start) / step
    bw_eff = bw_eff * 0.75 / 1000.
    for i in range(step):
        f_mid = start + f_step * i
        f_div = bw_eff / sdiv
        f_low = f_mid - bw_eff * 0.5
        for j in range(sdiv):
            freq_band[i*sdiv + j] = f_low + f_div*j + f_div*0.5
            freq_step[i*sdiv + j] = f_step / sdiv
            freq_width[i*sdiv + j] = f_div
    return freq_band, freq_step, freq_width


# Frequency: SID-2
# Output: freq, f_step, f_width
def _frequency_sid2(asw_ver):
    # ASW2
    decimation = 0
    N_step = 202
    b_num = 1
    b_start = [191, 0, 0, 0, 0]
    b_stop = [45111, 0, 0, 0, 0]
    b_step = [202, 0, 0, 0, 0]
    b_repeat = [1, 0, 0, 0, 0]
    b_sdiv = [1, 0, 0, 0, 0]
    N_samp = 128
    sample_rate = _sample_rate(decimation)
    freq, f_step, f_width = _get_frequencies_band(sample_rate, b_num, b_start, b_stop, b_step, b_repeat, b_sdiv, 1)
    return freq, f_step, f_width


# Frequency: SID-3
# Output: freq, f_step, f_width
def _frequency_sid3(asw_ver):
    if asw_ver == 1:
        # ASW1
        decimation = 0
        N_step = 512
        b_num = 1
        b_start = [80, 0, 0, 0, 0]
        b_stop = [45000, 0, 0, 0, 0]
        b_step = [255, 0, 0, 0, 0]
        b_repeat = [1, 0, 0, 0, 0]
        b_sdiv = [1, 0, 0, 0, 0]
        N_samp = 1
        sample_rate = _sample_rate(decimation)
        freq, f_step, f_width = _get_frequencies(sample_rate, N_step, 1)
    else:
        # ASW2
        decimation = 0
        N_step = 238
        b_num = 5
        b_start = [191, 413, 635, 1079, 2189]
        b_stop = [413, 635, 1079, 2189, 45035]
        b_step = [1, 1, 2, 5, 193]
        b_repeat = [16, 8, 4, 2, 1]
        b_sdiv = [24, 12, 6, 3, 1]
        N_samp = 1
        sample_rate = _sample_rate(decimation)
        freq, f_step, f_width = _get_frequencies_band(sample_rate, b_num, b_start, b_stop, b_step, b_repeat, b_sdiv, N_samp)
    return freq, f_step, f_width


# Frequency: SID-4 & SID-20
# Output: freq, f_step, f_width
def _frequency_sid4_sid20():
    decimation = 3
    b_num = 1
    b_start = [80, 0, 0, 0, 0]
    b_stop = [2096, 0, 0, 0, 0]
    b_step = [72, 0, 0, 0, 0]
    b_repeat = [1, 0, 0, 0, 0]
    b_sdiv = [1, 0, 0, 0, 0]
    N_samp = 1
    sample_rate = _sample_rate(decimation)
    freq, f_step, f_width = _get_frequencies_band(sample_rate, b_num, b_start, b_stop, b_step, b_repeat, b_sdiv, N_samp)
    return freq, f_step, f_width


# Frequency: SID-5 & SID-21
# Output: freq, f_step, f_width
def _frequency_sid5_sid21():
    decimation = 0
    b_num = 1
    b_start = [191, 0, 0, 0, 0]
    b_stop = [10181, 0, 0, 0, 0]
    b_step = [45, 0, 0, 0, 0]
    b_repeat = [1, 0, 0, 0, 0]
    b_sdiv = [96, 0, 0, 0, 0]
    N_samp = 1
    sample_rate = _sample_rate(decimation)
    freq, f_step, f_width = _get_frequencies_band(sample_rate, b_num, b_start, b_stop, b_step, b_repeat, b_sdiv, N_samp)
    return freq, f_step, f_width


# Frequency: MASK frequency matching
# Output: tbl_sid2_to_data
def _frequency_sid2_to_data(freq, f_step, freq_sid2):
    n_freq = len(freq)
    n_freq_sid2 = len(freq_sid2)
    # print(n_freq, n_freq_sid2)
    tbl_freq_to_data = np.zeros((n_freq, 3), dtype = int)

    j = 0
    for i in range(n_freq):
        f_min = freq[i] - f_step[i]/2
        f_max = freq[i] + f_step[i]/2
        while freq_sid2[j] < f_min:
            j = j+1
            if j>=n_freq_sid2:
                j = n_freq_sid2-1
                break
        if freq_sid2[j] >= f_min:
            tbl_freq_to_data[i][0] = j
        while freq_sid2[j] < f_max:
            j = j+1
            if j>=n_freq_sid2:
                j = n_freq_sid2-1
                break
        if j==n_freq_sid2-1:
            tbl_freq_to_data[i][1] = j
        elif freq_sid2[j-1] <= f_max:
            tbl_freq_to_data[i][1] = j-1
        tbl_freq_to_data[i][2] = tbl_freq_to_data[i][1] - tbl_freq_to_data[i][0] + 1 
        if tbl_freq_to_data[i][2] == 0:
            tbl_freq_to_data[i][1] = -1
            tbl_freq_to_data[i][0] = -1

    return tbl_freq_to_data


# ---------------------------------------------------------------------
# --- CAL --------------------------------------------------------------
# ---------------------------------------------------------------------
# power label
def power_label(band_mode, unit_mode):
    """
    Input:  cal_mode, unit_mode
    Outout: str
    """
    if band_mode == 0:
        if unit_mode == 0:
            str = 'Power [RAW^2 @ADC]'
        elif unit_mode == 1:
            str = 'Power [dBm @ADC]'
        elif unit_mode == 2:
            str = 'Power [V^2peak @HF]'
        elif unit_mode == 3:
            str = 'Power [V^2 @HF]'
        elif unit_mode == 4:
            str = 'Power [V^2 @RWI]'
    else:
        if unit_mode == 0:
            str = 'Power [RAW^2/Hz @ADC]'
        elif unit_mode == 1:
            str = 'Power [dBm/Hz @ADC]'
        elif unit_mode == 2:
            str = 'Power [V^2peak/Hz @HF]'
        elif unit_mode == 3:
            str = 'Power [V^2/Hz @HF]'
        elif unit_mode == 4:
            str = 'Power [V^2/Hz @RWI]'
    return str


def cal_factors(unit_mode, p_raw_max, p_raw_min):
    """
    Input:  unit_mode   0: raw   1: dBm＠ADC   2: V@HF   3:V2@HF   4:V2@RWI
    Output: cf, p_max, p_min
    """
    # ******************************************************
    # [EM2-0]
    # "1-bit" = -104.1 dBm = -114.1 dB V  = 1.97E-6 V    ==> "20-bit": 2.06 Vpp
    # "HF input"  +15dB(AMP) -3dB(50-ohm) = "+12dB"      ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    # [EM2-3 / FM / FS]
    # "1-bit" = -110.1 dBm = -110.1 dB V  = 0.99E-7 V "  ==> "20-bit": 1.03 Vpp
    # "HF input"  +9dB(AMP)  -3dB(50-ohm) = "+6dB"       ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    cf = 0.0                                # Conversion Factor: RAW

    if   unit_mode == 1:
        cf = -104.1                         # dBm @ ADC 
    elif unit_mode == 2:
        cf = -104.1 - 10.00 - 15.0          # V(amplitude) @ HF -- in EM2-1: HF-gain +15dB, ADC: 2Vpp  ==> EM2-3 & later: same [-6dB + 6dB]
    elif unit_mode == 3:
        cf = -104.1 - 13.01 - 15.0          # V^2 @ HF (EM2-0 case)
    elif unit_mode == 4:
        cf = -104.1 - 13.01 - 15.0 - 5.0    # V^2 @ RWIin

    # *** Max / Min in plots ***
    p_max = p_raw_max + cf/10
    p_min = p_raw_min + cf/10

    return cf, p_max, p_min