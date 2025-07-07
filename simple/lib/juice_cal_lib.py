# JUICE RPWI HF CAL lib -- 2025/6/5

import copy
import csv
import numpy as np

class struct_hf:
    pass


# -----------------------------------------------------------------------------
# power label
# -----------------------------------------------------------------------------
def power_label(unit_mode, band_mode):
    """
    Input:  unit_mode       0: raw     1: V＠ADC     2: V@HF    3: V@RWI    4: V/m@RWI
            band_mode       0: sum     1: /Hz
    Outout: str_unit
    """
    if band_mode == 0:
        if   unit_mode == 0:  str_unit = '[RAW2]'
        elif unit_mode == 1:  str_unit = '[V2 @ADC]'
        elif unit_mode == 2:  str_unit = '[V2 @HF]'
        elif unit_mode == 3:  str_unit = '[V2 @RWI]'
        elif unit_mode == 4:  str_unit = '[V2/m2]'
    else:
        if   unit_mode == 0:  str_unit = '[RAW2/Hz]'
        elif unit_mode == 1:  str_unit = '[V2/Hz @ADC]'
        elif unit_mode == 2:  str_unit = '[V2/Hz @HF]'
        elif unit_mode == 3:  str_unit = '[V2/Hz @RWI]'
        elif unit_mode == 4:  str_unit = '[V2/m2/Hz]'
    return str_unit


# -----------------------------------------------------------------------------
# Setting Wave CAL (non FFT/IFFT)
# [SID-2 evaluation @ 1.5MHz for ASW2]
#      0.0 dB  [RAW]
#   -120.4 dB  [V @ADC]
#   -128.3 dB  [V @HF]
#   -143.1 dB  [V @RWI]
#   -132.7 dB  [V/m]
# -----------------------------------------------------------------------------
def wave_cal(data, sid, unit_mode, T_HF, T_RWI):
    """
    Input:  data            Eu_i, Eu_q, Ev_i, Ev_q, Ew_i, Ew_q
            sid             (n/a at the moment)
            unit_mode       0: raw     1: V@ADC     2: V@HF     3: V@RWI
            T_HF & T_RWI    HF & RWI T (degC)
    Output: wave_cal        Eu_i, Eu_q, Ev_i, Ev_q, Ew_i, Ew_q, cf (dB), str
    """
    # ******************************************************************************************
    # ***** SID-3 cal: different in ASW-1&3 - ASW-2 (wrong) --- TBC
    # ******************************************************************************************
    print("  ASW:", data.RPWI_FSW_version)
    # ***************************************
    # ***** Date will be used in future *****
    # ***************************************
    print("Epoch:", data.epoch[0], "-", data.epoch[-1])

    # ******************************************************
    # [EM2-0]
    # "1-bit" = -104.1 dBm = -114.1 dB V  = 1.97E-6 V    ==> "20-bit": 2.06 Vpp
    # "HF input"  +15dB(AMP) -3dB(50-ohm) = "+12dB"      ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    # [EM2-3 / FM / FS]
    # "1-bit" = -110.1 dBm = -110.1 dB V  = 9.9E-7 V "   ==> "20-bit": 1.03 Vpp
    # "HF input"  +9dB(AMP)  -3dB(50-ohm) = "+6dB"       ==> "1-bit": 5E-7 V,  Full: 0.5 Vpp
    # ******************************************************
    str_unit     = '[RAW]';    cf = 0.0         # RAW
    if unit_mode >= 1:          # V @ ADC   gain: 120.4 dB          1.0 Vpp @ 20-bit    9.5E-7 V/bit = -120.4 dB V/bit
        str_unit = '[V @ADC]'; cf = -120.4
    if unit_mode >= 2:          # V @ HF    gain: 128.3 dB @ RT      8.2dB (-25degC)     7.9dB (25degC)      7.6dB (+75degC)       
        str_unit = '[V @HF]';  cf = cf - ( 8.05 + (-6.00E-03) * T_HF )
    if unit_mode >= 3:          # V @ RWI   gain: 143.1 dB @ RT     18.7dB (-145degC)   14.8dB (25degC)     13.0dB (+75degC)
        str_unit = '[V @RWI]'; cf = cf - (15.60 + (-2.96E-02) * T_RWI + (-5.06E-05) * T_RWI**2)
    if unit_mode == 4:
        str_unit = '[V/m]'

    wave_cal = struct_hf()
    wave_cal.Eu_i = data.Eu_i * 10**(cf/20.);   wave_cal.Eu_q = data.Eu_q * 10**(cf/20.)
    wave_cal.Ev_i = data.Ev_i * 10**(cf/20.);   wave_cal.Ev_q = data.Ev_q * 10**(cf/20.)
    wave_cal.Ew_i = data.Ew_i * 10**(cf/20.);   wave_cal.Ew_q = data.Ew_q * 10**(cf/20.)

    if unit_mode == 4:          # V @ RWI   gain: 135.2 dB @ RT     18.7dB (-145degC)   14.8dB (25degC)     13.0dB (+75degC)
        """
        # In LGA
        wave_cal.Eu_i = wave_cal.Eu_i / 0.20;   wave_cal.Eu_q = wave_cal.Eu_q / 0.20    # U-ANT     TMP: ~0.20m   [-14 dB down]    in 100s KHz (AKR)
        wave_cal.Ev_i = wave_cal.Ev_i / 0.47;   wave_cal.Ev_q = wave_cal.Ev_q / 0.47    # V-ANT     TMP: ~0.47m   [-6.5dB down]    in 100s KHz (AKR)
        wave_cal.Ew_i = wave_cal.Ew_i / 0.25;   wave_cal.Ew_q = wave_cal.Ew_q / 0.25    # W-ANT     TMP: ~0.25m   [-12 dB down]    in 100s KHz (AKR)
        """
        # Fischer+ 2021
        wave_cal.Eu_i = wave_cal.Eu_i / 0.26;   wave_cal.Eu_q = wave_cal.Eu_q / 0.26    # U-ANT     TMP: ~0.20m   [-14 dB down]    in 100s KHz (AKR)
        wave_cal.Ev_i = wave_cal.Ev_i / 0.43;   wave_cal.Ev_q = wave_cal.Ev_q / 0.43    # V-ANT     TMP: ~0.47m   [-6.5dB down]    in 100s KHz (AKR)
        wave_cal.Ew_i = wave_cal.Ew_i / 0.23;   wave_cal.Ew_q = wave_cal.Ew_q / 0.23    # W-ANT     TMP: ~0.25m   [-12 dB down]    in 100s KHz (AKR)
        cf = cf - 20*np.log10(0.30)

    wave_cal.cf       = cf          # dB
    wave_cal.str_unit = str_unit    # unit for wave
    print("Wave-CAL (dB):", cf, str_unit)
    return wave_cal


# -----------------------------------------------------------------------------
# Setting Spectrum CAL
# -----------------------------------------------------------------------------
# complex version
def spec_cal(spec, sid, unit_mode, band_mode, T_HF, T_RWI):
    """
    Input:  spec            EuEu, EuEv, EwEw, EuEv_re, EuEv_im, EvEw_re, EvEw_im, EwEu_re, EwEu_im, freq, freq_w
            sid             (n/a at the moment)
            unit_mode       0: raw     1: V@ADC     2: V@HF     3: V@RWI    4: V/m@RWI
            band_mode       0: sum     1: /Hz
            T_HF & T_RWI    HF & RWI T (degC)
    Output: spec            EuEu, EuEv, EwEw, EuEv_re, EuEv_im, EvEw_re, EvEw_im, EwEu_re, EwEu_im, cf (dB)
    """

    # ******************************************************************************************
    # ***** SID-3 cal: different in ASW-1&3 - ASW-2 (wrong) --- TBC
    # ******************************************************************************************
    print("  ASW:", spec.RPWI_FSW_version)
    if sid==5:
        n_time = spec.EE.shape[0]
    else:
        n_time = spec.EuEu.shape[0]
    # ***************************************
    # ***** Date will be used in future *****
    # ***************************************
    print("Epoch:", spec.epoch[0], "-", spec.epoch[-1])

    freq = spec.freq[n_time//2];  n_freq = freq.shape[0];  freq_w = spec.freq_w[n_time//2]

    # BUG correction in ASW2 SID-3
    cal_factor = 1.0
    if unit_mode > 0:
        if sid==3 and spec.RPWI_FSW_version == '2.0':
            cal_factor = 0.1                            # ASW2 --- bug
    
    # Spectral CAL parameters from Ground + Onboard Test
    CAL_f_gain, CAL_f_phase = spec_gain_phase(freq, unit_mode, T_HF, T_RWI)
    if band_mode > 0:
        # BUG correction in ASW2 SID-3
        if sid==3 and spec.RPWI_FSW_version == '2.0':
            CAL_f_gain = CAL_f_gain / 289.              # ASW2 --- bug
        else:
            CAL_f_gain = CAL_f_gain / (freq_w*1000)**0.5

    # Complex CAL parameters
    CAL_f_gainC  = CAL_f_gain  * np.cos(np.pi * CAL_f_phase/180) + CAL_f_gain * np.sin(np.pi * CAL_f_phase/180) * 1j
    CAL_f_gainC  = CAL_f_gainC * cal_factor
    CAL_f_gainC2 = np.conjugate(CAL_f_gainC)
    CAL_f_gain0  = CAL_f_gain  * cal_factor

    if sid==5:
        spec.EE   = spec.EE   * CAL_f_gain0[0]**2
    else:
        spec.EuEu = spec.EuEu * CAL_f_gain0[0]**2;  spec.EvEv = spec.EvEv * CAL_f_gain0[1]**2;      spec.EwEw = spec.EwEw * CAL_f_gain0[2]**2
        EuEv = spec.EuEv_re + spec.EuEv_im * 1j;    EuEv = EuEv * CAL_f_gainC[0] * CAL_f_gainC[1];  spec.EuEv_re = EuEv.real; spec.EuEv_im = EuEv.imag
        EvEw = spec.EvEw_re + spec.EvEw_im * 1j;    EvEw = EvEw * CAL_f_gainC[1] * CAL_f_gainC[2];  spec.EvEw_re = EvEw.real; spec.EvEw_im = EvEw.imag
        EwEu = spec.EwEu_re + spec.EwEu_im * 1j;    EwEu = EwEu * CAL_f_gainC[2] * CAL_f_gainC[0];  spec.EwEu_re = EwEu.real; spec.EwEu_im = EwEu.imag
        #
        if sid == 3:
            spec.EuEu_NC = spec.EuEu_NC * CAL_f_gain0[0]**2;  spec.EvEv_NC = spec.EvEv_NC * CAL_f_gain0[1]**2;  spec.EwEw_NC = spec.EwEw_NC * CAL_f_gain0[2]**2
            spec.EuEu_RC = spec.EuEu_RC * CAL_f_gain0[0]**2;  spec.EvEv_RC = spec.EvEv_RC * CAL_f_gain0[1]**2;  spec.EwEw_RC = spec.EwEw_RC * CAL_f_gain0[2]**2
            spec.EuEu_LC = spec.EuEu_LC * CAL_f_gain0[0]**2;  spec.EvEv_LC = spec.EvEv_LC * CAL_f_gain0[1]**2;  spec.EwEw_LC = spec.EwEw_LC * CAL_f_gain0[2]**2
            spec.BG_Eu   = spec.BG_Eu   * CAL_f_gain0[0]**2;  spec.BG_Ev   = spec.BG_Ev   * CAL_f_gain0[1]**2;  spec.BG_Ew   = spec.BG_Ew   * CAL_f_gain0[2]**2
            #
            EuEv = spec.EuEv_re_NC + spec.EuEv_im_NC * 1j;  EuEv = EuEv * CAL_f_gainC[0] * CAL_f_gainC2[1];  spec.EuEv_re_NC = EuEv.real; spec.EuEv_im_NC = EuEv.imag
            EvEw = spec.EvEw_re_NC + spec.EvEw_im_NC * 1j;  EvEw = EvEw * CAL_f_gainC[1] * CAL_f_gainC2[2];  spec.EvEw_re_NC = EvEw.real; spec.EvEw_im_NC = EvEw.imag
            EwEu = spec.EwEu_re_NC + spec.EwEu_im_NC * 1j;  EwEu = EwEu * CAL_f_gainC[2] * CAL_f_gainC2[0];  spec.EwEu_re_NC = EwEu.real; spec.EwEu_im_NC = EwEu.imag
            #
            EuEv = spec.EuEv_re_RC + spec.EuEv_im_NC * 1j;  EuEv = EuEv * CAL_f_gainC[0] * CAL_f_gainC2[1];  spec.EuEv_re_RC = EuEv.real; spec.EuEv_im_RC = EuEv.imag
            EvEw = spec.EvEw_re_RC + spec.EvEw_im_NC * 1j;  EvEw = EvEw * CAL_f_gainC[1] * CAL_f_gainC2[2];  spec.EvEw_re_RC = EvEw.real; spec.EvEw_im_RC = EvEw.imag
            EwEu = spec.EwEu_re_RC + spec.EwEu_im_NC * 1j;  EwEu = EwEu * CAL_f_gainC[2] * CAL_f_gainC2[0];  spec.EwEu_re_RC = EwEu.real; spec.EwEu_im_RC = EwEu.imag
            #
            EuEv = spec.EuEv_re_LC + spec.EuEv_im_NC * 1j;  EuEv = EuEv * CAL_f_gainC[0] * CAL_f_gainC2[1];  spec.EuEv_re_LC = EuEv.real; spec.EuEv_im_LC = EuEv.imag
            EvEw = spec.EvEw_re_LC + spec.EvEw_im_NC * 1j;  EvEw = EvEw * CAL_f_gainC[1] * CAL_f_gainC2[2];  spec.EvEw_re_LC = EvEw.real; spec.EvEw_im_LC = EvEw.imag
            EwEu = spec.EwEu_re_LC + spec.EwEu_im_NC * 1j;  EwEu = EwEu * CAL_f_gainC[2] * CAL_f_gainC2[0];  spec.EwEu_re_LC = EwEu.real; spec.EwEu_im_LC = EwEu.imag
            """
            spec.EuiEui = spec.EuiEui
            spec.EuqEuq = spec.EuqEuq
            spec.EviEvi = spec.EviEvi
            spec.EvqEvq = spec.EvqEvq
            spec.EwiEwi = spec.EwiEwi
            spec.EwqEwq = spec.EwqEwq
            #
            spec.EuiEvi = spec.EuiEvi
            spec.EuqEvq = spec.EuqEvq
            spec.EviEwi = spec.EviEwi
            spec.EvqEwq = spec.EvqEwq
            spec.EwiEui = spec.EwiEui
            spec.EwqEuq = spec.EwqEuq
            #
            spec.EuiEvq = spec.EuiEvq
            spec.EuqEvi = spec.EuqEvi
            spec.EviEwq = spec.EviEwq
            spec.EvqEwi = spec.EvqEwi
            spec.EwiEuq = spec.EwiEuq
            spec.EwqEui = spec.EwqEui
            #
            spec.EuiEuq = spec.EuiEuq
            spec.EviEvq = spec.EviEvq
            spec.EwiEwq = spec.EwiEwq
            """

    for j in range(n_freq):
        if 1000 < freq[j]:
            break
    spec.cf  = 20*np.log10(CAL_f_gain[0][j])
    spec.str_unit = power_label(unit_mode, band_mode)

    n_freq0 = freq.shape[0]
    print("CAL-U (Hz) (gain) (dB) :", freq[n_freq0//8], 1/CAL_f_gain0[0][n_freq0//8]**2, -20*np.log10(CAL_f_gain0[0][n_freq0//8]))
    print("CAL-V (Hz) (gain) (dB) :", freq[n_freq0//8], 1/CAL_f_gain0[1][n_freq0//8]**2, -20*np.log10(CAL_f_gain0[1][n_freq0//8]))
    print("CAL-W (Hz) (gain) (dB) :", freq[n_freq0//8], 1/CAL_f_gain0[2][n_freq0//8]**2, -20*np.log10(CAL_f_gain0[2][n_freq0//8]))
    return spec


# -----------------------------------------------------------------------------
# Setting Spectrum CAL prameters
# [SID-2 evaluation @ 1.5MHz for ASW2]
#      0.0 dB [RAW]
#   -120.4 dB  [V @ADC]
#   -128.3 dB  [V @HF]
#   -143.1 dB  [V @RWI]
#   -132.7 dB  [V/m]
# -----------------------------------------------------------------------------
def spec_gain_phase(freq, unit_mode, T_HF, T_RWI):
    """
    [Spectral CAL parameters from Ground + Onboard Test]
    Input:  freq            frequency (kHz)
            unit_mode       0: raw     1: V@ADC     2: V@HF     3: V@RWI
            T_HF & T_RWI    HF & RWI T (degC)
    Output: CAL_gain[3]     Gain cal parameters
            CAL_phase[3]    Phase cal parameters    ("0.0" at the moment)
            str_unit                     
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
        # -----------------------
        # 20kHz - 35.5MHz
        # -----------------------
        g0_l = +7.87438532E+0;  g1_l = +9.72891774E-3;  g2_l = -5.01061375E-3;  g3_l = +1.08353478E-3;  g4_l = -1.19769590E-4
        g5_l = +7.30311031E-6;  g6_l = -2.47328435E-7;  g7_l = +4.33831673E-9;  g8_l = -3.06837976E-11
        # p0_l = +1.45012955E-02;  p1_l = -6.79809370E+00;  p2_l = +1.32583659E-02;  p3_l = -2.94140368E-03;  p4_l = +2.38078227E-04
        # p5_l = -1.15806368E-05;  p6_l = +2.73703677E-07;  p7_l = -2.60940286E-09;  p8_l = +1.18266537E-12
        # -----------------------
        # 35.5 - 45 MHz
        # -----------------------
        g0_h = -7.48554687E+2;  g1_h = +0.00000000E+0;  g2_h = +0.00000000E+0;  g3_h = +5.93627500E-1;  g4_h = -5.30852619E-2
        g5_h = +2.01301317E-3;  g6_h = -3.94992379E-5;  g7_h = +3.95918790E-7;  g8_h = -1.60963119E-9
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
        #
        # CAL_gain with HF-T
        CAL_gain = 10**( (cf - CAL_gain + 0.3*(T_HF-25.)/50.)/20 )

    if unit_mode >= 3:                      # V @ RWI   gain: 135.2 dB @ RT     18.7dB (-145degC)   14.8dB (25degC)     13.0dB (+75degC)
        # HF + Harness + RWI + Dummy-ANT: gain (dB) with RWI-T (degC) during RWI TVAC
        #   p.2 of https://share.obspm.fr/apps/files/files/29962540?dir=/JUICE-RPWI/JENRAGE/CAL&openfile=true
        # Dummy-ANT correction: gain (dB)
        #   p.3 of https://share.obspm.fr/apps/files/files/29962540?dir=/JUICE-RPWI/JENRAGE/CAL&openfile=true
        b0 = [ 15.70226060, -2.044197E-02, -7.640780E-05, -1.562152E-06, -6.620953E-09 ]
        b1 = [ -1.22544328, -2.428311E-04,  3.869358E-05,  5.149496E-07,  1.726930E-09 ]
        b2 = [ -0.81571010,  1.503548E-02, -1.999807E-06, -1.812614E-06, -7.821654E-09 ]
        b3 = [ -0.71374875,	-8.299497E-04,  1.493876E-05, -3.903649E-07, -2.818792E-09 ]
        b4 = [ -3.02304099,	-3.070438E-02, -3.540418E-05,  2.903294E-06,  1.255253E-08 ]
        b5 = [  0.92912903,  4.171481E-04,  1.964224E-05,  6.550603E-07,  3.354454E-09 ]
        b6 = [  2.33609583,  1.730226E-02, -1.294253E-05, -1.922596E-06, -7.870634E-09 ]
        b7 = [ -0.27964459, -4.980705E-05,  3.392395E-07, -1.003909E-07, -6.114530E-10 ]
        b8 = [ -0.75715963, -3.011020E-03,  3.068570E-06,  3.366969E-07,  1.366694E-09 ]
        a0 = b0[0] + b0[1] * T_RWI + b0[2] * T_RWI**2 + b0[3] * T_RWI**3 + b0[4] * T_RWI**4
        a1 = b1[0] + b1[1] * T_RWI + b1[2] * T_RWI**2 + b1[3] * T_RWI**3 + b1[4] * T_RWI**4
        a2 = b2[0] + b2[1] * T_RWI + b2[2] * T_RWI**2 + b2[3] * T_RWI**3 + b2[4] * T_RWI**4
        a3 = b3[0] + b3[1] * T_RWI + b3[2] * T_RWI**2 + b3[3] * T_RWI**3 + b3[4] * T_RWI**4
        a4 = b4[0] + b4[1] * T_RWI + b4[2] * T_RWI**2 + b4[3] * T_RWI**3 + b4[4] * T_RWI**4
        a5 = b5[0] + b5[1] * T_RWI + b5[2] * T_RWI**2 + b5[3] * T_RWI**3 + b5[4] * T_RWI**4
        a6 = b6[0] + b6[1] * T_RWI + b6[2] * T_RWI**2 + b6[3] * T_RWI**3 + b6[4] * T_RWI**4
        a7 = b7[0] + b7[1] * T_RWI + b7[2] * T_RWI**2 + b7[3] * T_RWI**3 + b7[4] * T_RWI**4
        a8 = b8[0] + b8[1] * T_RWI + b8[2] * T_RWI**2 + b8[3] * T_RWI**3 + b8[4] * T_RWI**4
        f = np.log10(freq/1000.)
        for i in range(3):
            CAL_gain [i] = a0 + a1 * f + a2 * f**2 + a3 * f**3 + a4 * f**4 + a5 * f**5 + a6 * f**6 + a7 * f**7 + a8 * f**8
        # print("0:", T_RWI, a0, a1, a2, a3, a4, a5, a6, a7, a8)
        # for j in range(0, n_freq, 1000):
        #    print(n_freq, j, freq[j], CAL_gain[0][j])
        CAL_gain = 10**( (cf - CAL_gain + 0.3*(T_HF-25.)/50.)/20 )

        b0 = [ 15.70226060 + 7.38949866,    -2.044197E-02, -7.640780E-05, -1.562152E-06, -6.620953E-09 ]
        b1 = [ -1.22544328 - 1.48435771E-1, -2.428311E-04,  3.869358E-05,  5.149496E-07,  1.726930E-09 ]
        b2 = [ -0.81571010 + 1.09242767E-1,  1.503548E-02, -1.999807E-06, -1.812614E-06, -7.821654E-09 ]
        b3 = [ -0.71374875 - 1.87627444E-1,	-8.299497E-04,  1.493876E-05, -3.903649E-07, -2.818792E-09 ]
        b4 = [ -3.02304099 + 7.7013971E-2,	-3.070438E-02, -3.540418E-05,  2.903294E-06,  1.255253E-08 ]
        b5 = [  0.92912903,                  4.171481E-04,  1.964224E-05,  6.550603E-07,  3.354454E-09 ]
        b6 = [  2.33609583,                  1.730226E-02, -1.294253E-05, -1.922596E-06, -7.870634E-09 ]
        b7 = [ -0.27964459,                 -4.980705E-05,  3.392395E-07, -1.003909E-07, -6.114530E-10 ]
        b8 = [ -0.75715963,                 -3.011020E-03,  3.068570E-06,  3.366969E-07,  1.366694E-09 ]
        a0 = b0[0] + b0[1] * T_RWI + b0[2] * T_RWI**2 + b0[3] * T_RWI**3 + b0[4] * T_RWI**4
        a1 = b1[0] + b1[1] * T_RWI + b1[2] * T_RWI**2 + b1[3] * T_RWI**3 + b1[4] * T_RWI**4
        a2 = b2[0] + b2[1] * T_RWI + b2[2] * T_RWI**2 + b2[3] * T_RWI**3 + b2[4] * T_RWI**4
        a3 = b3[0] + b3[1] * T_RWI + b3[2] * T_RWI**2 + b3[3] * T_RWI**3 + b3[4] * T_RWI**4
        a4 = b4[0] + b4[1] * T_RWI + b4[2] * T_RWI**2 + b4[3] * T_RWI**3 + b4[4] * T_RWI**4
        a5 = b5[0] + b5[1] * T_RWI + b5[2] * T_RWI**2 + b5[3] * T_RWI**3 + b5[4] * T_RWI**4
        a6 = b6[0] + b6[1] * T_RWI + b6[2] * T_RWI**2 + b6[3] * T_RWI**3 + b6[4] * T_RWI**4
        a7 = b7[0] + b7[1] * T_RWI + b7[2] * T_RWI**2 + b7[3] * T_RWI**3 + b7[4] * T_RWI**4
        a8 = b8[0] + b8[1] * T_RWI + b8[2] * T_RWI**2 + b8[3] * T_RWI**3 + b8[4] * T_RWI**4
        f = np.log10(freq/1000.)
        for i in range(3):
            CAL_gain [i] = a0 + a1 * f + a2 * f**2 + a3 * f**3 + a4 * f**4 + a5 * f**5 + a6 * f**6 + a7 * f**7 + a8 * f**8
        CAL_gain = 10**( (cf - CAL_gain + 0.3*(T_HF-25.)/50.)/20 )
        

        b0 = [ 15.70226060 + 7.38949866,    -2.044197E-02, -7.640780E-05, -1.562152E-06, -6.620953E-09 ]
        b1 = [ -1.22544328 - 1.48435771E-1, -2.428311E-04,  3.869358E-05,  5.149496E-07,  1.726930E-09 ]
        b2 = [ -0.81571010 + 1.09242767E-1,  1.503548E-02, -1.999807E-06, -1.812614E-06, -7.821654E-09 ]
        b3 = [ -0.71374875 - 1.87627444E-1,	-8.299497E-04,  1.493876E-05, -3.903649E-07, -2.818792E-09 ]
        b4 = [ -3.02304099 + 7.7013971E-2,	-3.070438E-02, -3.540418E-05,  2.903294E-06,  1.255253E-08 ]
        b5 = [  0.92912903,                  4.171481E-04,  1.964224E-05,  6.550603E-07,  3.354454E-09 ]
        b6 = [  2.33609583,                  1.730226E-02, -1.294253E-05, -1.922596E-06, -7.870634E-09 ]
        b7 = [ -0.27964459,                 -4.980705E-05,  3.392395E-07, -1.003909E-07, -6.114530E-10 ]
        b8 = [ -0.75715963,                 -3.011020E-03,  3.068570E-06,  3.366969E-07,  1.366694E-09 ]
        a0 = b0[0] + b0[1] * T_RWI + b0[2] * T_RWI**2 + b0[3] * T_RWI**3 + b0[4] * T_RWI**4
        a1 = b1[0] + b1[1] * T_RWI + b1[2] * T_RWI**2 + b1[3] * T_RWI**3 + b1[4] * T_RWI**4
        a2 = b2[0] + b2[1] * T_RWI + b2[2] * T_RWI**2 + b2[3] * T_RWI**3 + b2[4] * T_RWI**4
        a3 = b3[0] + b3[1] * T_RWI + b3[2] * T_RWI**2 + b3[3] * T_RWI**3 + b3[4] * T_RWI**4
        a4 = b4[0] + b4[1] * T_RWI + b4[2] * T_RWI**2 + b4[3] * T_RWI**3 + b4[4] * T_RWI**4
        a5 = b5[0] + b5[1] * T_RWI + b5[2] * T_RWI**2 + b5[3] * T_RWI**3 + b5[4] * T_RWI**4
        a6 = b6[0] + b6[1] * T_RWI + b6[2] * T_RWI**2 + b6[3] * T_RWI**3 + b6[4] * T_RWI**4
        a7 = b7[0] + b7[1] * T_RWI + b7[2] * T_RWI**2 + b7[3] * T_RWI**3 + b7[4] * T_RWI**4
        a8 = b8[0] + b8[1] * T_RWI + b8[2] * T_RWI**2 + b8[3] * T_RWI**3 + b8[4] * T_RWI**4
        f = np.log10(freq/1000.)
        for i in range(3):
            CAL_gain [i] = a0 + a1 * f + a2 * f**2 + a3 * f**3 + a4 * f**4 + a5 * f**5 + a6 * f**6 + a7 * f**7 + a8 * f**8
        """    
        print("0:", T_RWI, a0, a1, a2, a3_l, a4, a5, a6, a7, a8)
        for j in range(0, n_freq, 1000):
            print(n_freq, j, freq[j], CAL_gain[0][j])
        """
        CAL_gain = 10**( (cf - CAL_gain + 0.3*(T_HF-25.)/50.)/20 )

        # HF + Harness + RWI + Dummy-ANT: gain (dB) with RWI-T (degC) during RWI TVAC
        #   p.2 of https://share.obspm.fr/apps/files/files/31417192?dir=/JUICE-RPWI/JENRAGE/CAL&openfile=true
        # Dummy-ANT correction: gain (dB)
        #   p.3 of https://share.obspm.fr/apps/files/files/31417192?dir=/JUICE-RPWI/JENRAGE/CAL&openfile=true
        #
        # 0.5 MHz - 45 MHz
        b0 = [ 15.70226060 + 7.40316107,    -2.044197E-02, -7.640780E-05, -1.562152E-06, -6.620953E-09 ]
        b1 = [ -1.22544328 - 1.82506569E-1, -2.428311E-04,  3.869358E-05,  5.149496E-07,  1.726930E-09 ]
        b2 = [ -0.81571010 - 7.73616930E-3,  1.503548E-02, -1.999807E-06, -1.812614E-06, -7.821654E-09 ]
        b3 = [ -0.71374875 + 2.06190481E-2,	-8.299497E-04,  1.493876E-05, -3.903649E-07, -2.818792E-09 ]
        b4 = [ -3.02304099,	                -3.070438E-02, -3.540418E-05,  2.903294E-06,  1.255253E-08 ]
        b5 = [  0.92912903,                  4.171481E-04,  1.964224E-05,  6.550603E-07,  3.354454E-09 ]
        b6 = [  2.33609583,                  1.730226E-02, -1.294253E-05, -1.922596E-06, -7.870634E-09 ]
        b7 = [ -0.27964459,                 -4.980705E-05,  3.392395E-07, -1.003909E-07, -6.114530E-10 ]
        b8 = [ -0.75715963,                 -3.011020E-03,  3.068570E-06,  3.366969E-07,  1.366694E-09 ]
        a0_h = b0[0] + b0[1] * T_RWI + b0[2] * T_RWI**2 + b0[3] * T_RWI**3 + b0[4] * T_RWI**4
        a1_h = b1[0] + b1[1] * T_RWI + b1[2] * T_RWI**2 + b1[3] * T_RWI**3 + b1[4] * T_RWI**4
        a2_h = b2[0] + b2[1] * T_RWI + b2[2] * T_RWI**2 + b2[3] * T_RWI**3 + b2[4] * T_RWI**4
        a3_h = b3[0] + b3[1] * T_RWI + b3[2] * T_RWI**2 + b3[3] * T_RWI**3 + b3[4] * T_RWI**4
        a4_h = b4[0] + b4[1] * T_RWI + b4[2] * T_RWI**2 + b4[3] * T_RWI**3 + b4[4] * T_RWI**4
        a5_h = b5[0] + b5[1] * T_RWI + b5[2] * T_RWI**2 + b5[3] * T_RWI**3 + b5[4] * T_RWI**4
        a6_h = b6[0] + b6[1] * T_RWI + b6[2] * T_RWI**2 + b6[3] * T_RWI**3 + b6[4] * T_RWI**4
        a7_h = b7[0] + b7[1] * T_RWI + b7[2] * T_RWI**2 + b7[3] * T_RWI**3 + b7[4] * T_RWI**4
        a8_h = b8[0] + b8[1] * T_RWI + b8[2] * T_RWI**2 + b8[3] * T_RWI**3 + b8[4] * T_RWI**4

        # 0.01MHz - 0.5 MHz
        b0 = [ 15.70226060 + 7.41749899,    -2.044197E-02, -7.640780E-05, -1.562152E-06, -6.620953E-09 ]
        b1 = [ -1.22544328 - 7.42895532E-1, -2.428311E-04,  3.869358E-05,  5.149496E-07,  1.726930E-09 ]
        b2 = [ -0.81571010 - 4.10439739,    1.503548E-02, -1.999807E-06, -1.812614E-06, -7.821654E-09 ]
        b3 = [ -0.71374875 - 8.81978306,	-8.299497E-04,  1.493876E-05, -3.903649E-07, -2.818792E-09 ]
        b4 = [ -3.02304099 - 6.29731174,	-3.070438E-02, -3.540418E-05,  2.903294E-06,  1.255253E-08 ]
        b5 = [  0.92912903 - 1.46407881,     4.171481E-04,  1.964224E-05,  6.550603E-07,  3.354454E-09 ]
        b6 = [  2.33609583,                  1.730226E-02, -1.294253E-05, -1.922596E-06, -7.870634E-09 ]
        b7 = [ -0.27964459,                 -4.980705E-05,  3.392395E-07, -1.003909E-07, -6.114530E-10 ]
        b8 = [ -0.75715963,                 -3.011020E-03,  3.068570E-06,  3.366969E-07,  1.366694E-09 ]
        a0_l = b0[0] + b0[1] * T_RWI + b0[2] * T_RWI**2 + b0[3] * T_RWI**3 + b0[4] * T_RWI**4
        a1_l = b1[0] + b1[1] * T_RWI + b1[2] * T_RWI**2 + b1[3] * T_RWI**3 + b1[4] * T_RWI**4
        a2_l = b2[0] + b2[1] * T_RWI + b2[2] * T_RWI**2 + b2[3] * T_RWI**3 + b2[4] * T_RWI**4
        a3_l = b3[0] + b3[1] * T_RWI + b3[2] * T_RWI**2 + b3[3] * T_RWI**3 + b3[4] * T_RWI**4
        a4_l = b4[0] + b4[1] * T_RWI + b4[2] * T_RWI**2 + b4[3] * T_RWI**3 + b4[4] * T_RWI**4
        a5_l = b5[0] + b5[1] * T_RWI + b5[2] * T_RWI**2 + b5[3] * T_RWI**3 + b5[4] * T_RWI**4
        a6_l = b6[0] + b6[1] * T_RWI + b6[2] * T_RWI**2 + b6[3] * T_RWI**3 + b6[4] * T_RWI**4
        a7_l = b7[0] + b7[1] * T_RWI + b7[2] * T_RWI**2 + b7[3] * T_RWI**3 + b7[4] * T_RWI**4
        a8_l = b8[0] + b8[1] * T_RWI + b8[2] * T_RWI**2 + b8[3] * T_RWI**3 + b8[4] * T_RWI**4

        for i in range(3):
            for j in range(n_freq):
                f = np.log10(freq[j]/1000.)
                #print(freq[j], f)
                if f < np.log10(0.5):
                    CAL_gain [i][j] = a0_l + a1_l * f + a2_l * f**2 + a3_l * f**3 + a4_l * f**4 + a5_l * f**5 + a6_l * f**6 + a7_l * f**7 + a8_l * f**8
                    # CAL_phase[i][j] = p0_l + p1_l * f + p2_l * f**2 + p3_l * f**3 + p4_l * f**4 + p5_l * f**5 + p6_l * f**6 + p7_l * f**7 + p8_l * f**8
                else:
                    CAL_gain [i][j] = a0_h + a1_h * f + a2_h * f**2 + a3_h * f**3 + a4_h * f**4 + a5_h * f**5 + a6_h * f**6 + a7_h * f**7 + a8_h * f**8
                    # CAL_phase[i][j] = p0_h + p1_h * f + p2_h * f**2 + p3_h * f**3 + p4_h * f**4 + p5_h * f**5 + p6_h * f**6 + p7_h * f**7 + p8_h * f**8
        # print("2:", T_RWI, a0_h, a1_h, a2_h, a3_h, a4_h, a5_h, a6_h, a7_h, a8_h)
        # print("3:", T_RWI, a0_l, a1_l, a2_l, a3_l, a4_l, a5_l, a6_l, a7_l, a8_l)
        # for j in range(0, n_freq, 1000):
        #    print(n_freq, j, freq[j], CAL_gain[0][j])

        # CAL_gain with HF-T
        CAL_gain = 10**( (cf - CAL_gain + 0.3*(T_HF-25.)/50.)/20. )
        # for j in range(n_freq):
        #    print(freq[j], CAL_gain[0][j])

    if unit_mode == 4:                      # V/m   with Effective length
        # LGA
        CAL_gain[0] = CAL_gain[0] / 0.22    # U-ANT ~0.20m [-14 dB] in 100s KHz (AKR)
        CAL_gain[1] = CAL_gain[1] / 0.50    # V-ANT ~0.47m [-6.5dB] in 100s KHz (AKR)
        CAL_gain[2] = CAL_gain[2] / 0.20    # W-ANT ~0.25m [-12 dB] in 100s KHz (AKR)
        """
        # LGA
        CAL_gain[0] = CAL_gain[0] / 0.20    # U-ANT ~0.20m [-14 dB] in 100s KHz (AKR)
        CAL_gain[1] = CAL_gain[1] / 0.47    # V-ANT ~0.47m [-6.5dB] in 100s KHz (AKR)
        CAL_gain[2] = CAL_gain[2] / 0.25    # W-ANT ~0.25m [-12 dB] in 100s KHz (AKR)
        # EGA
        CAL_gain[0] = CAL_gain[0] / 0.20    # U-ANT ~0.20m [-14 dB] in 100s KHz (AKR)
        CAL_gain[1] = CAL_gain[1] / 0.20    # V-ANT ~0.47m [-6.5dB] in 100s KHz (AKR)
        CAL_gain[2] = CAL_gain[2] / 0.20    # W-ANT ~0.25m [-12 dB] in 100s KHz (AKR)
        """

    """
    # TMP -- onboard CAL harness loss
    if unit_mode >= 3:
        CAL_gain_harness = spec_gain_onboard_cal(freq)
        CAL_gain = CAL_gain * CAL_gain_harness
        print("CAL_gain_harness (0.1Vpp = 1E-2 V2 @ RWI for EuEu,EvEv,EwEw, 3E-2 V2 @ RWI for EE):", CAL_gain_harness)
    # TMP -- onboard CAL harness loss
    """

    n_freq0 = freq.shape[0]
    """
    import csv
    with open("gain.csv", 'w') as f:
        writer = csv.writer(f)
        for i in range(n_freq0):
            writer.writerow([ i, freq[i], 20*np.log10(CAL_gain[0][i]), 20*np.log10(CAL_gain[1][i]), 20*np.log10(CAL_gain[2][i]) ])
    """
    if unit_mode > 0:   # U/V/W diff from Onboard CAL
        CAL_gain2, CAL_phase2 = spec_gain_phase2(freq)
        CAL_gain  = CAL_gain  * CAL_gain2
        CAL_phase = CAL_phase + CAL_phase2
    print("CAL-U (Hz) (dB) (phase):", freq[n_freq0//8], 20*np.log10(CAL_gain[0][n_freq0//8]), CAL_phase[0][n_freq0//8])
    print("CAL-V (Hz) (dB) (phase):", freq[n_freq0//8], 20*np.log10(CAL_gain[1][n_freq0//8]), CAL_phase[1][n_freq0//8])
    print("CAL-W (Hz) (dB) (phase):", freq[n_freq0//8], 20*np.log10(CAL_gain[2][n_freq0//8]), CAL_phase[2][n_freq0//8])
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
    g0 = -2.88554859E+01;  g1 = -9.80334986E-01;  g2 = +2.04468516E-01;  g3 = -2.61079083E-02;  g4 = +1.66536526E-03
    g5 = -5.71588394E-05;  g6 = +1.05658805E-06;  g7 = -9.43569895E-09;  g8 = 2.80310935E-11
    f = freq/1000.
    CAL_gain = g0 + g1 * f + g2 * f**2 + g3 * f**3 + g4 * f**4 + g5 * f**5 + g6 * f**6 + g7 * f**7 + g8 * f**8
    CAL_gain = 10**(-CAL_gain/20)
    return CAL_gain


