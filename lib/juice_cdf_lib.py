# JUICE RPWI HF CDF -- 2023/10/16

import glob
import spacepy.pycdf
import numpy as np

class struct:
    pass

#---------------------------------------------------------------------
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

#---------------------------------------------------------------------
#--- QL --------------------------------------------------------------
#---------------------------------------------------------------------
# Sampling rate [Hz]
def _sample_rate(decimation):
    ret = 296e+3
    if decimation >= 0 and decimation <= 3:
        ret = (296e+3)/(2**decimation)
    return ret

#---------------------------------------------------------------------
# Frequency: linear [kHz]
def _get_frequencies(n_freq, samp, sample_rate):
    fs = 80e3                       # start freq
    fe = 45e6                       # end   freq
    df = (fe - fs) / (n_freq - 1)   # band width

    i_freq = np.arange(0, n_freq)
    freq = np.float32((fs + df * i_freq) / 1000.)
    freq = np.repeat(freq, samp)

    f_step = np.float32((i_freq * 0. + df) / 1000.)
    f_step = np.repeat(f_step, samp)

    f_width = np.float32(
        (i_freq * 0. + sample_rate * 0.7566) / 1000.)
    f_width = np.repeat(f_width, samp)
    return freq, f_step, f_width

#---------------------------------------------------------------------
# power label
def power_label(cal_mode, unit_mode):
    if unit_mode == 0:
        if cal_mode == 0:
            str = 'Power [RAW @ ADC]'
        elif cal_mode == 1:
            str = 'Power [dBm @ ADC]'
        elif cal_mode == 2:
            str = 'Power [V @ HF-in]'
        elif cal_mode == 3:
            str = 'Power [V^2 @ HF-in]'
        elif cal_mode == 4:
            str = 'Power [V^2 @ RWI-in]'
    else:
        if cal_mode == 0:
            str = 'Power [RAW/Hz @ ADC]'
        elif cal_mode == 1:
            str = 'Power [dBm/Hz @ ADC]'
        elif cal_mode == 2:
            str = 'Power [V/Hz @ HF-in]'
        elif cal_mode == 3:
            str = 'Power [V^2/Hz @ HF-in]'
        elif cal_mode == 4:
            str = 'Power [V^2/Hz @ RWI-in]'
    return str
