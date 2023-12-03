# JUICE RPWI HF CDF lib -- 2023/12/2

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
    bw_eff = bw_eff * 0.75 / const.UNIT_KHZ
    for i in range(step):
        f_mid = start + f_step * i
        f_div = bw_eff / sdiv
        f_low = f_mid - bw_eff * 0.5
        for j in range(sdiv):
            freq_band[i*sdiv + j] = f_low + f_div*j + f_div*0.5
            freq_step[i*sdiv + j] = f_step / sdiv
            freq_width[i*sdiv + j] = f_div
    return freq_band, freq_step, freq_width


# ---------------------------------------------------------------------
# --- CAL --------------------------------------------------------------
# ---------------------------------------------------------------------
def cal_factors(unit_mode, cal_mode, cal, p_raw_max, p_raw_min):
    """
    *** Conversion factor
    unit_mode       0: sum    1: /Hz
    cal_mode        0: raw    1: dBm＠ADC  2: V@HF   3:V2@HF   4:V2@RWI
    cal             0: background     1: CAL
    """
    cf = 0.0                                # Conversion Factor: RAW

    # ******************************************************
    # [EM2-0]
    # "1-bit" = -104.1 dBm = -114.1 dB V  = 1.97E-6 V    ==> "20-bit": 2.06 Vpp
    # "HF input"  +15dB(AMP) -3dB(50-ohm) = "+12dB"      ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    # [EM2-3 / FM / FS]
    # "1-bit" = -110.1 dBm = -110.1 dB V  = 0.99E-7 V "  ==> "20-bit": 1.03 Vpp
    # "HF input"  +9dB(AMP)  -3dB(50-ohm) = "+6dB"       ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    if cal_mode == 1:
        cf = -104.1                         # dBm @ ADC 
    elif cal_mode == 2:
        cf = -104.1 - 10.00 - 15.0          # V(amplitude) @ HF -- in EM2-1: HF-gain +15dB, ADC: 2Vpp  ==> EM2-3 & later: same [-6dB + 6dB]
    elif cal_mode == 3:
        cf = -104.1 - 13.01 - 15.0          # V^2 @ HF (EM2-0 case)
    elif cal_mode == 4:
        cf = -104.1 - 13.01 - 15.0 - 5.0    # V^2 @ RWIin -- temporary

    # *** Max / Min in plots ***
    p_max = p_raw_max + cf/10
    p_min = p_raw_min + cf/10

    # *** Unit mode: Bandwidth is needed.
    if unit_mode == 1:
        p_max = p_max - 4.5
        p_min = p_min - 4.5

    return cf, p_max, p_min


# power label
def power_label(cal_mode, unit_mode):
    """
    Input:  cal_mode, unit_mode
    Outout: str
    """
    if unit_mode == 0:
        if cal_mode == 0:
            str = 'Power [RAW^2 @ADC]'
        elif cal_mode == 1:
            str = 'Power [dBm @ADC]'
        elif cal_mode == 2:
            str = 'Power [V^2peak @HF]'
        elif cal_mode == 3:
            str = 'Power [V^2 @HF]'
        elif cal_mode == 4:
            str = 'Power [V^2 @RWI]'
    else:
        if cal_mode == 0:
            str = 'Power [RAW^2/Hz @ADC]'
        elif cal_mode == 1:
            str = 'Power [dBm/Hz @ADC]'
        elif cal_mode == 2:
            str = 'Power [V^2peak/Hz @HF]'
        elif cal_mode == 3:
            str = 'Power [V^2/Hz @HF]'
        elif cal_mode == 4:
            str = 'Power [V^2/Hz @RWI]'
    return str
