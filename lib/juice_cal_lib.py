# JUICE RPWI HF CAL lib -- 2024/8/17

import csv
import math
import numpy as np

class struct:
    pass


# power label
def power_label(unit_mode, band_mode):
    """
    Input:  unit_mode       0: raw     1: V＠ADC     2: V@HF    3: V@RWI
            band_mode       0: sum     1: /Hz
    Outout: str
    """
    if band_mode == 0:
        if   unit_mode == 0:
            str = '[RAW2]'
        elif unit_mode == 1:
            str = '[V2 @ADC]'
        elif unit_mode == 2:
            str = '[V2 @HF]'
        elif unit_mode == 3:
            str = '[V2 @RWI]'
    else:
        if  unit_mode == 0:
            str = '[RAW2/Hz]'
        elif unit_mode == 1:
            str = '[V2/Hz @ADC]'
        elif unit_mode == 2:
            str = '[V2/Hz @HF]'
        elif unit_mode == 3:
            str = '[V2/Hz @RWI]'
    return str


def wave_cal(data, sid, unit_mode, T_HF, T_RWI):
    """
    Input:  data            Eu_i, Eu_q, Ev_i, Ev_q, Ew_i, Ew_q
            sid             (n/a at the moment)
            unit_mode       0: raw     1: V@ADC     2: V@HF     3: V@RWI
            T_HF & T_RWI    HF & RWI T (degC)
    Output: wave_cal        Eu_i, Eu_q, Ev_i, Ev_q, Ew_i, Ew_q, cf (dB), str
    """
    # ******************************************************
    # [EM2-0]
    # "1-bit" = -104.1 dBm = -114.1 dB V  = 1.97E-6 V    ==> "20-bit": 2.06 Vpp
    # "HF input"  +15dB(AMP) -3dB(50-ohm) = "+12dB"      ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    # [EM2-3 / FM / FS]
    # "1-bit" = -110.1 dBm = -110.1 dB V  = 9.9E-7 V "   ==> "20-bit": 1.03 Vpp
    # "HF input"  +9dB(AMP)  -3dB(50-ohm) = "+6dB"       ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    str     = '[RAW]';     cf = 0.0         # RAW
    if unit_mode == 1:                      # V @ ADC   gain: 120.4 dB          1.0 Vpp @ 20-bit    9.5E-7 V/bit = -120.4 dB V/bit
        str = '[V @ADC]';  cf = -120.4
    if unit_mode == 2:                      # V @ HF    gain: 128.3 dB @ RT      8.2dB (-25degC)     7.9dB (25degC)      7.6dB (+75degC)       
        str = '[V @HF]';   cf = -120.4 - 7.9 + 0.3*(T_HF-25.)/50.
    if unit_mode == 3:                      # V @ RWI   gain: 135.2 dB @ RT     18.7dB (-145degC)   14.8dB (25degC)     13.0dB (+75degC)
        str = '[V @RWI]';  cf = -120.4 - (1.55409E+01 + (-2.96308E-02) * T_RWI + (-5.05863E-05) * T_RWI**2)

    wave_cal = struct()
    wave_cal.Eu_i = data.Eu_i * 10**(cf/20.);   wave_cal.Eu_q = data.Eu_q * 10**(cf/20.)
    wave_cal.Ev_i = data.Ev_i * 10**(cf/20.);   wave_cal.Ev_q = data.Ev_q * 10**(cf/20.)
    wave_cal.Ew_i = data.Ew_i * 10**(cf/20.);   wave_cal.Ew_q = data.Ew_q * 10**(cf/20.)
    wave_cal.cf   = cf      # dB
    wave_cal.str  = str     # unit for wave
    return wave_cal


def spec_cal(spec, sid, unit_mode, band_mode, T_HF, T_RWI):
    """
    Input:  spec            EuEu, EuEv, EwEw, EuEv_re, EuEv_im, EvEw_re, EvEw_im, EwEu_re, EwEu_im, freq, freq_w
            sid             (n/a at the moment)
            unit_mode       0: raw     1: V@ADC     2: V@HF(tmp)   3: V@RWI(tmp)
            band_mode       0: sum     1: /Hz
            T_HF & T_RWI    HF & RWI T (degC)
    Output: spec            EuEu, EuEv, EwEw, EuEv_re, EuEv_im, EvEw_re, EvEw_im, EwEu_re, EwEu_im, cf (dB)
    """
    n_time = spec.EuEu.shape[0];  freq = spec.freq[n_time//2];  n_freq = freq.shape[0];  freq_w = spec.freq_w[n_time//2]

    # Spectral CAL parameters from Ground + Onboard Test
    CAL_f_gain, CAL_f_phase = spec_gain_phase(freq, unit_mode, T_HF, T_RWI)
    if band_mode > 0:
        CAL_f_gain = CAL_f_gain / (freq_w*1000)**0.5
    CAL_gain_u   = CAL_f_gain[0] * 1;               CAL_gain_v   = CAL_f_gain[1] * 1;               CAL_gain_w   = CAL_f_gain[2] * 1
    CAL_phase_uv = CAL_f_phase[1] - CAL_f_phase[0]; CAL_phase_vw = CAL_f_phase[2] - CAL_f_phase[1]; CAL_phase_uw = CAL_f_phase[2] - CAL_f_phase[0]
    CAL_UV_re = np.zeros(n_freq); CAL_UV_im = np.zeros(n_freq)
    CAL_VW_re = np.zeros(n_freq); CAL_VW_im = np.zeros(n_freq)
    CAL_WU_re = np.zeros(n_freq); CAL_WU_im = np.zeros(n_freq)
    for j in range(n_freq):                # frequency
        CAL_UV_re[j] =  math.cos(math.pi * CAL_phase_uv[j]/180) * CAL_gain_u[j] * CAL_gain_v[j]
        CAL_UV_im[j] =  math.sin(math.pi * CAL_phase_uv[j]/180) * CAL_gain_u[j] * CAL_gain_v[j]
        CAL_VW_re[j] =  math.cos(math.pi * CAL_phase_vw[j]/180) * CAL_gain_v[j] * CAL_gain_w[j]
        CAL_VW_im[j] =  math.sin(math.pi * CAL_phase_vw[j]/180) * CAL_gain_v[j] * CAL_gain_w[j]
        CAL_WU_re[j] =  math.cos(math.pi * CAL_phase_uw[j]/180) * CAL_gain_u[j] * CAL_gain_w[j]
        CAL_WU_im[j] = -math.sin(math.pi * CAL_phase_uw[j]/180) * CAL_gain_u[j] * CAL_gain_w[j]

    spec_cal = struct()
    spec_cal.EuEu    = spec.EuEu    * CAL_gain_u**2
    spec_cal.EvEv    = spec.EvEv    * CAL_gain_v**2
    spec_cal.EwEw    = spec.EwEw    * CAL_gain_w**2
    spec_cal.EuEv_re = spec.EuEv_re * CAL_UV_re + spec.EuEv_im * CAL_UV_im
    spec_cal.EuEv_im = spec.EuEv_im * CAL_UV_re - spec.EuEv_re * CAL_UV_im
    spec_cal.EvEw_re = spec.EvEw_re * CAL_VW_re + spec.EvEw_im * CAL_VW_im
    spec_cal.EvEw_im = spec.EvEw_im * CAL_VW_re - spec.EvEw_re * CAL_VW_im
    spec_cal.EwEu_re = spec.EwEu_re * CAL_WU_re + spec.EwEu_im * CAL_WU_im
    spec_cal.EwEu_im = spec.EwEu_im * CAL_WU_re - spec.EwEu_re * CAL_WU_im
    spec.EuEu    = spec_cal.EuEu;     spec.EvEv    = spec_cal.EvEv;     spec.EwEw    = spec_cal.EwEw
    spec.EuEv_re = spec_cal.EuEv_re;  spec.EvEw_re = spec_cal.EvEw_re;  spec.EwEu_re = spec_cal.EwEu_re
    spec.EuEv_im = spec_cal.EuEv_im;  spec.EvEw_im = spec_cal.EvEw_im;  spec.EwEu_im = spec_cal.EwEu_im 

    for j in range(n_freq):
        if 1000 < freq[j]:
            break
    spec.cf  = 20*np.log10(CAL_gain_u[j])
    spec.str = power_label(unit_mode, band_mode)
    return spec


def spec_gain_phase(freq, unit_mode, T_HF, T_RWI):
    """
    [Spectral CAL parameters from Ground + Onboard Test]
    Input:  freq            frequency (kHz)
            unit_mode       0: raw     1: V@ADC     2: V@HF     3: V@RWI
            T_HF & T_RWI    HF & RWI T (degC)
    Output: CAL_gain[3]     Gain cal parameters
            CAL_phase[3]    Phase cal parameters    ("0.0" at the moment)
            str                     
    """
    n_freq = freq.shape[0];  CAL_gain = np.zeros((3, n_freq));  CAL_phase = np.zeros((3, n_freq))
    cf = -120.4     # dB V of 1-bit

    if unit_mode == 0:                      # RAW
        CAL_gain  = CAL_gain  + 1.0
        # CAL_phase = CAL_phase + 0.0

    if unit_mode == 1:                      # V @ ADC   gain: 120.4 dB          1.0 Vpp @ 20-bit    9.5E-7 V/bit = -120.4 dB V/bit
        for i in range(3):
            CAL_gain [i] = CAL_gain [i] + 10**(cf/20.)
            # CAL_phase[i] = CAL_phase[i] + 0.0

    if unit_mode == 2:                      # V @ HF    gain: 128.3 dB @ RT      8.2dB (-25degC)     7.9dB (25degC)      7.6dB (+75degC)  
        # 20kHz - 35.5MHz
        g0_l = +7.87438532E+00;  g1_l = +9.72891774E-03;  g2_l = -5.01061375E-03;  g3_l = +1.08353478E-03;  g4_l = -1.19769590E-04
        g5_l = +7.30311031E-06;  g6_l = -2.47328435E-07;  g7_l = +4.33831673E-09;  g8_l = -3.06837976E-11
        # p0_l = +1.45012955E-02;  p1_l = -6.79809370E+00;  p2_l = +1.32583659E-02;  p3_l = -2.94140368E-03;  p4_l = +2.38078227E-04
        # p5_l = -1.15806368E-05;  p6_l = +2.73703677E-07;  p7_l = -2.60940286E-09;  p8_l = +1.18266537E-12
        # 35.5 - 45 MHz
        g0_h = -7.48554687E+02;  g1_h = +0.00000000E+00;  g2_h = +0.00000000E+00;  g3_h = +5.93627500E-01;  g4_h = -5.30852619E-02
        g5_h = +2.01301317E-03;  g6_h = -3.94992379E-05;  g7_h = +3.95918790E-07;  g8_h = -1.60963119E-09
        # p0_h = -1.19845870E+02;  p1_h = +0.00000000E+00;  p2_h = +0.00000000E+00;  p3_h = +4.04944288E-01;  p4_h = -4.99624633E-02
        # p5_h = +2.42086346E-03;  p6_h = -5.81058707E-05;  p7_h = +6.91408153E-07;  p8_h = -3.26259135E-09
        for i in range(3):
            for j in range(n_freq):
                f = freq[j]/1000.
                if f < 35.5:
                    CAL_gain [i][j] = g0_l + g1_l * f + g2_l * f**2 + g3_l * f**3 + g4_l * f**4 + g5_l * f**5 + g6_l * f**6 + g7_l * f**7 + g8_l * f**8
                    # CAL_phase[i][j] = p0_l + p1_l * f + p2_l * f**2 + p3_l * f**3 + p4_l * f**4 + p5_l * f**5 + p6_l * f**6 + p7_l * f**7 + p8_l * f**8
                else:
                    CAL_gain [i][j] = g0_h + g1_h * f + g2_h * f**2 + g3_h * f**3 + g4_h * f**4 + g5_h * f**5 + g6_h * f**6 + g7_h * f**7 + g8_h * f**8
                    # CAL_phase[i][j] = p0_h + p1_h * f + p2_h * f**2 + p3_h * f**3 + p4_h * f**4 + p5_h * f**5 + p6_h * f**6 + p7_h * f**7 + p8_h * f**8
        CAL_gain = 10**( (cf - CAL_gain + 0.3*(T_HF-25.)/50.)/20 )

    if unit_mode == 3:                      # V @ RWI   gain: 135.2 dB @ RT     18.7dB (-145degC)   14.8dB (25degC)     13.0dB (+75degC)
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
        """
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
        """
        f = np.log10(freq/1000.)
        for i in range(3):
            CAL_gain [i] = g0 + g1 * f + g2 * f**2 + g3 * f**3 + g4 * f**4 + g5 * f**5 + g6 * f**6 + g7 * f**7 + g8 * f**8
            # CAL_phase[i] = p0 + p1 * f + p2 * f**2 + p3 * f**3 + p4 * f**4 + p5 * f**5 + p6 * f**6 + p7 * f**7 + p8 * f**8
        CAL_gain = 10**( (cf - CAL_gain + 0.3*(T_HF-25.)/50.)/20 )

    if unit_mode > 0:   # U/V/W diff from Onboard CAL
        CAL_gain2, CAL_phase2 = spec_gain_phase2(freq)
        CAL_gain  = CAL_gain  * CAL_gain2
        CAL_phase = CAL_phase + CAL_phase2
    return CAL_gain, CAL_phase


def spec_gain_phase2(freq):
    """
    [U/V/W diff from Onboard CAL]
    Input:  freq            frequency (kHz)
    Output: CAL_gain[3]     Gain cal parameters
            CAL_phase[3]    Phase cal parameters    ("0.0" at the moment)
    """
    n_freq    = freq.shape[0]
    CAL_gain  = np.zeros((3, n_freq));   CAL_phase = np.zeros((3, n_freq))

    # CAL Table read
    n_cal_table = 202
    CAL_ch     = np.zeros(n_cal_table);  CAL_freq    = np.zeros(n_cal_table)
    gain_u     = np.zeros(n_cal_table);  phase_u     = np.zeros(n_cal_table)
    gain_v     = np.zeros(n_cal_table);  phase_v     = np.zeros(n_cal_table)
    gain_w     = np.zeros(n_cal_table);  phase_w     = np.zeros(n_cal_table)
    CAL_gain_u = np.zeros(n_cal_table);  CAL_phase_u = np.zeros(n_cal_table);  CAL_UV_re = np.zeros(n_cal_table);  CAL_UV_im = np.zeros(n_cal_table)
    CAL_gain_v = np.zeros(n_cal_table);  CAL_phase_v = np.zeros(n_cal_table);  CAL_VW_re = np.zeros(n_cal_table);  CAL_VW_im = np.zeros(n_cal_table)
    CAL_gain_w = np.zeros(n_cal_table);  CAL_phase_w = np.zeros(n_cal_table);  CAL_WU_re = np.zeros(n_cal_table);  CAL_WU_im = np.zeros(n_cal_table)
    cal_dir  = './lib/';  cal_name = 'hf_OnboardCAL.csv';  cal_file = cal_dir + cal_name
    with open(cal_file, 'r') as f:
        reader = csv.reader(f);  i = 0
        for row in reader:
            CAL_ch[i]     = row[0];   CAL_freq[i]    = row[1]
            gain_u[i]     = row[2];   gain_v[i]      = row[3];   gain_w[i]   = row[4]
            phase_u[i]    = row[5];   phase_v[i]     = row[6];   phase_w[i]  = row[7]
            CAL_gain_u[i] = row[8];   CAL_phase_u[i] = row[9]       # 0-dB, 0-deg 
            CAL_gain_v[i] = row[10];  CAL_phase_v[i] = row[11]      # gain & phase of V from U
            CAL_gain_w[i] = row[12];  CAL_phase_w[i] = row[13]      # gain & phase of W from U
            i = i+1
    k = 0
    for j in range(n_freq):
        while CAL_freq[k] < freq[j]:
            k = k+1
            if k >= n_cal_table:
                k = n_cal_table - 1
                break
        if k>0:
            if freq[j]-CAL_freq[k-1] < CAL_freq[k-1]-freq[j]:
                k = k-1
        CAL_gain [0][j] = 10**(-CAL_gain_u[k]/20);  CAL_phase[0][j] = CAL_phase_u[k]
        CAL_gain [1][j] = 10**(-CAL_gain_v[k]/20);  CAL_phase[1][j] = CAL_phase_v[k]
        CAL_gain [2][j] = 10**(-CAL_gain_w[k]/20);  CAL_phase[2][j] = CAL_phase_w[k]

    return CAL_gain, CAL_phase



def spec_gain_onboard_cal(freq):
    """
    [Onboard CAL gain from source (0.1Vpp)]
    Input:  freq            frequency (kHz)
    Output: CAL_gain        Gain cal parameters
    """
    # g0 = -1.35852444E+01;  g1 = -1.27127173E+00;  g2 = +1.42269322E-01;  g3 = -1.57468571E-02;  g4 = +9.15531853E-04
    # g5 = -2.78149871E-05;  g6 = +3.99622245E-07;  g7 = -1.53121094E-09;  g8 = -1.16048217E-11
    g0 = -2.88554859E+01;  g1 = -9.80334986E-01;  g2 = +2.04468516E-01;  g3 = -2.61079083E-02;  g4 = +1.66536526E-03
    g5 = -5.71588394E-05;  g6 = +1.05658805E-06;  g7 = -9.43569895E-09;  g8 = 2.80310935E-11
    f = freq/1000.
    CAL_gain = g0 + g1 * f + g2 * f**2 + g3 * f**3 + g4 * f**4 + g5 * f**5 + g6 * f**6 + g7 * f**7 + g8 * f**8
    CAL_gain = 10**(-CAL_gain/20)
    return CAL_gain


