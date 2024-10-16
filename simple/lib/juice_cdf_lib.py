# JUICE RPWI HF CDF lib -- 2024/9/19

# import glob
# import spacepy.pycdf
import numpy as np
from cdflib import cdfread


class struct:
    pass


# ---------------------------------------------------------------------
# --- Read CDF --------------------------------------------------------------
# ---------------------------------------------------------------------
def _RPWI_FSW_version(cdf_file):
    cdf = cdfread.CDF(cdf_file)
    globalaAttrs = cdf.globalattsget()
    RPWI_FSW_version = globalaAttrs.get("RPWI_FSW_version", "Unknown")
    return(RPWI_FSW_version[0])


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
# output:    freq, f_step, f_width
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
def _frequency_sid3(asw_ver):
    """
    input:  asw_ver     ASW version
    Output: freq, f_step, f_width
    """
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
    """
    Input:  freq, f_step    frequency & step of other SID      
            freq_sid2       frequency of SID2
    Outout: str
    """
    n_freq      = len(freq)
    n_freq_sid2 = len(freq_sid2)
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