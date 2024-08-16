# JUICE RPWI HF CDF lib -- 2024/8/8

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


# ---------------------------------------------------------------------
# --- CAL --------------------------------------------------------------
# ---------------------------------------------------------------------
# power label
"""
def power_label(band_mode, unit_mode):
    #Input:  cal_mode
    #        unit_mode      0: raw     1: V＠ADC     2: V@HF    3: V@RWI
    #Outout: str
    if band_mode == 0:
        if   unit_mode == 0:
            str = 'Power [dB RAW]'
        elif unit_mode == 1:
            str = 'Power [dB V @ADC]'
        elif unit_mode == 2:
            str = 'Power [dB V @HF]'
        elif unit_mode == 3:
            str = 'Power [dB V @RWI]'
    else:
        if  unit_mode == 0:
            str = 'Power [dB RAW/Hz]'
        elif unit_mode == 1:
            str = 'Power [dB V/Hz @ADC]'
        elif unit_mode == 2:
            str = 'Power [dB V/Hz @HF]'
        elif unit_mode == 3:
            str = 'Power [dB V/Hz @RWI]'
    return str
"""


"""
def cal_factors(unit_mode, p_raw_max, p_raw_min):
    #Input:  unit_mode      0: raw     1: V@ADC     2: V@HF(tmp)   3: V@RWI(tmp)
    #Output: cf, p_max, p_min
    # ******************************************************
    # [EM2-0]
    # "1-bit" = -104.1 dBm = -114.1 dB V  = 1.97E-6 V    ==> "20-bit": 2.06 Vpp
    # "HF input"  +15dB(AMP) -3dB(50-ohm) = "+12dB"      ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    # [EM2-3 / FM / FS]
    # "1-bit" = -110.1 dBm = -110.1 dB V  = 0.99E-7 V "  ==> "20-bit": 1.03 Vpp
    # "HF input"  +9dB(AMP)  -3dB(50-ohm) = "+6dB"       ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    cf = 0.0;          str = '[RAW]';       cf_gain = 0.0
    
    if   unit_mode == 1:
        cf = -120.4;   str = '[V @ADC]';    cf_gain = 0.0
    elif unit_mode == 2:
        cf = -128.3;   str = '[V @HF]';     cf_gain = 7.9
    elif unit_mode == 3:
        cf = -138.3;   str = '[V @RWI]';    cf_gain = 17.9

    # *** Max / Min in plots ***
    p_max = p_raw_max + cf/10
    p_min = p_raw_min + cf/10

    return cf, p_max, p_min, str, cf_gain
"""


"""
def cal_gain_phase(freq, mode, T_HF, T_RWI):
    #Input:  freq[0:n_freq]  frequency (kHz)    
    #        unit_mode       1: ADC     2: HF     3: RWI
    #        T_HF, RWI_HF    HF & RWI temperature (degC)
    #Output: CAL_gain [0:freq][0:3 - U/V/W]      gain  (dB)
    #        CAL_phase[0:freq][0:3 - U/V/W]      phase (deg)
    # ******************************************************
    # [EM2-0]
    # "1-bit" = -104.1 dBm = -114.1 dB V  = 1.97E-6 V    ==> "20-bit": 2.06 Vpp
    # "HF input"  +15dB(AMP) -3dB(50-ohm) = "+12dB"      ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    # [EM2-3 / FM / FS]
    # "1-bit" = -110.1 dBm = -110.1 dB V  = 0.99E-7 V "  ==> "20-bit": 1.03 Vpp
    # "HF input"  +9dB(AMP)  -3dB(50-ohm) = "+6dB"       ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    cf = 0.0;          str = '[RAW]'

    n_freq = freq.shape[0]
    CAL_gain  = np.zeros((3, n_freq))
    CAL_phase = np.zeros((3, n_freq))

    if mode == 1:   
        # ADC
        for i in range(3):
            CAL_gain [i] = CAL_gain [i] + 0.0
            CAL_phase[i] = CAL_phase[i] + 0.0

    if mode == 2:
        # 20kHz - 35.5MHz
        g0_l = -2.56147E-02 + 7.9;  g1_l = +9.72892E-03;  g2_l = -5.01061E-03;  g3_l = +1.08353E-03;  g4_l = -1.19770E-04
        g5_l = +7.30311E-06;  g6_l = -2.47328E-07;  g7_l = +4.33832E-09;  g8_l = -3.06838E-11
        p0_l = +1.45013E-02;  p1_l = -6.79809E+00;  p2_l = +1.32584E-02;  p3_l = -2.94140E-03;  p4_l = +2.38078E-04
        p5_l = -1.15806E-05;  p6_l = +2.73704E-07;  p7_l = -2.60940E-09;  p8_l = +1.18267E-12

        # 35.5 - 45 MHz
        g0_h = -7.56455E+02 + 7.9;  g1_h = +0.00000E+00;  g2_h = +0.00000E+00;  g3_h = +5.93628E-01;  g4_h = -5.30853E-02
        g5_h = +2.01301E-03;  g6_h = -3.94992E-05;  g7_h = +3.95919E-07;  g8_h = -1.60963E-09
        p0_h = -1.19846E+02;  p1_h = +0.00000E+00;  p2_h = +0.00000E+00;  p3_h = +4.04944E-01;  p4_h = -4.99625E-02
        p5_h = +2.42086E-03;  p6_h = -5.81059E-05;  p7_h = +6.91408E-07;  p8_h = -3.26259E-09

        for i in range(3):
            for j in range(n_freq):
                f = freq[j]/1000.
                if f < 35.5:
                    CAL_gain [i][j] = g0_l + g1_l * f + g2_l * f**2 + g3_l * f**3 + g4_l * f**4 + g5_l * f**5 + g6_l * f**6 + g7_l * f**7 + g8_l * f**8
                    CAL_phase[i][j] = p0_l + p1_l * f + p2_l * f**2 + p3_l * f**3 + p4_l * f**4 + p5_l * f**5 + p6_l * f**6 + p7_l * f**7 + p8_l * f**8
                else:
                    CAL_gain [i][j] = g0_h + g1_h * f + g2_h * f**2 + g3_h * f**3 + g4_h * f**4 + g5_h * f**5 + g6_h * f**6 + g7_h * f**7 + g8_h * f**8
                    CAL_phase[i][j] = p0_h + p1_h * f + p2_h * f**2 + p3_h * f**3 + p4_h * f**4 + p5_h * f**5 + p6_h * f**6 + p7_h * f**7 + p8_h * f**8
 
    if mode == 3:
        # Gain [RWI - harness - HF]
        # for i in range(3):
        #   CAL_gain [i]  = CAL_gain [i]  - 138.3
        #   CAL_phase[i]  = CAL_phase[i]  +   0.0    

        # RWI temperature (degC) 
        g_tmp0 = [ 15.70226060, -2.044197E-02, -7.640780E-05, -1.562152E-06, -6.620953E-09 ]
        g_tmp1 = [ -1.22544328, -2.428311E-04,  3.869358E-05,  5.149496E-07,  1.726930E-09 ]
        g_tmp2 = [ -0.81571010,  1.503548E-02, -1.999807E-06, -1.812614E-06, -7.821654E-09 ]
        g_tmp3 = [ -0.71374875,	-8.299497E-04,  1.493876E-05, -3.903649E-07, -2.818792E-09 ]
        g_tmp4 = [ -3.02304099,	-3.070438E-02, -3.540418E-05,  2.903294E-06,  1.255253E-08 ]
        g_tmp5 = [ 0.92912903,   4.171481E-04,  1.964224E-05,  6.550603E-07,  3.354454E-09 ]
        g_tmp6 = [ 2.33609583,   1.730226E-02, -1.294253E-05, -1.922596E-06, -7.870634E-09 ]
        g_tmp7 = [ -0.27964459, -4.980705E-05,  3.392395E-07, -1.003909E-07, -6.114530E-10 ]
        g_tmp8 = [ -0.75715963, -3.011020E-03,  3.068570E-06,  3.366969E-07,  1.366694E-09 ]
        # RWI+HF gain (dB) 
        g0 = g_tmp0[0] + g_tmp0[1] * T_RWI + g_tmp0[2] * T_RWI**2 + g_tmp0[3] * T_RWI**3 + g_tmp0[4] * T_RWI**4
        g1 = g_tmp1[0] + g_tmp1[1] * T_RWI + g_tmp1[2] * T_RWI**2 + g_tmp1[3] * T_RWI**3 + g_tmp1[4] * T_RWI**4
        g2 = g_tmp2[0] + g_tmp2[1] * T_RWI + g_tmp2[2] * T_RWI**2 + g_tmp2[3] * T_RWI**3 + g_tmp2[4] * T_RWI**4
        g3 = g_tmp3[0] + g_tmp3[1] * T_RWI + g_tmp3[2] * T_RWI**2 + g_tmp3[3] * T_RWI**3 + g_tmp3[4] * T_RWI**4
        g4 = g_tmp4[0] + g_tmp4[1] * T_RWI + g_tmp4[2] * T_RWI**2 + g_tmp4[3] * T_RWI**3 + g_tmp4[4] * T_RWI**4
        g5 = g_tmp5[0] + g_tmp5[1] * T_RWI + g_tmp5[2] * T_RWI**2 + g_tmp5[3] * T_RWI**3 + g_tmp5[4] * T_RWI**4
        g6 = g_tmp6[0] + g_tmp6[1] * T_RWI + g_tmp6[2] * T_RWI**2 + g_tmp6[3] * T_RWI**3 + g_tmp6[4] * T_RWI**4
        g7 = g_tmp7[0] + g_tmp7[1] * T_RWI + g_tmp7[2] * T_RWI**2 + g_tmp7[3] * T_RWI**3 + g_tmp7[4] * T_RWI**4
        g8 = g_tmp8[0] + g_tmp8[1] * T_RWI + g_tmp8[2] * T_RWI**2 + g_tmp8[3] * T_RWI**3 + g_tmp8[4] * T_RWI**4

        # RWI temperature (degC) 
        p_tmp0 = [ 0., 0., 0., 0., 0. ]
        p_tmp1 = [ 0., 0., 0., 0., 0. ]
        p_tmp2 = [ 0., 0., 0., 0., 0. ]
        p_tmp3 = [ 0., 0., 0., 0., 0. ]
        p_tmp4 = [ 0., 0., 0., 0., 0. ]
        p_tmp5 = [ 0., 0., 0., 0., 0. ]
        p_tmp6 = [ 0., 0., 0., 0., 0. ]
        p_tmp7 = [ 0., 0., 0., 0., 0. ]
        p_tmp8 = [ 0., 0., 0., 0., 0. ]
        # RWI+HF phase (dB) 
        p0 = p_tmp0[0] + p_tmp0[1] * T_RWI + p_tmp0[2] * T_RWI**2 + p_tmp0[3] * T_RWI**3 + p_tmp0[4] * T_RWI**4
        p1 = p_tmp1[0] + p_tmp1[1] * T_RWI + p_tmp1[2] * T_RWI**2 + p_tmp1[3] * T_RWI**3 + p_tmp1[4] * T_RWI**4
        p2 = p_tmp2[0] + p_tmp2[1] * T_RWI + p_tmp2[2] * T_RWI**2 + p_tmp2[3] * T_RWI**3 + p_tmp2[4] * T_RWI**4
        p3 = p_tmp3[0] + p_tmp3[1] * T_RWI + p_tmp3[2] * T_RWI**2 + p_tmp3[3] * T_RWI**3 + p_tmp3[4] * T_RWI**4
        p4 = p_tmp4[0] + p_tmp4[1] * T_RWI + p_tmp4[2] * T_RWI**2 + p_tmp4[3] * T_RWI**3 + p_tmp4[4] * T_RWI**4
        p5 = p_tmp5[0] + p_tmp5[1] * T_RWI + p_tmp5[2] * T_RWI**2 + p_tmp5[3] * T_RWI**3 + p_tmp5[4] * T_RWI**4
        p6 = p_tmp6[0] + p_tmp6[1] * T_RWI + p_tmp6[2] * T_RWI**2 + p_tmp6[3] * T_RWI**3 + p_tmp6[4] * T_RWI**4
        p7 = p_tmp7[0] + p_tmp7[1] * T_RWI + p_tmp7[2] * T_RWI**2 + p_tmp7[3] * T_RWI**3 + p_tmp7[4] * T_RWI**4
        p8 = p_tmp8[0] + p_tmp8[1] * T_RWI + p_tmp8[2] * T_RWI**2 + p_tmp8[3] * T_RWI**3 + p_tmp8[4] * T_RWI**4

        f = np.log10(freq/1000.)
        for i in range(3):
            CAL_gain [i] = g0 + g1 * f + g2 * f**2 + g3 * f**3 + g4 * f**4 + g5 * f**5 + g6 * f**6 + g7 * f**7 + g8 * f**8
            CAL_phase[i] = p0 + p1 * f + p2 * f**2 + p3 * f**3 + p4 * f**4 + p5 * f**5 + p6 * f**6 + p7 * f**7 + p8 * f**8

    return CAL_gain, CAL_phase
"""
