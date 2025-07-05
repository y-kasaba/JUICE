"""
    JUICE RPWI HF SID2 (RAW): L1a read -- 2025/7/4
"""
import numpy as np
import math

class struct:
    pass


# ---------------------------------------------------------------------
# --- SID2 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid2_read(cdf, RPWI_FSW_version):
    """
    input:  CDF, FSW version
    return: data
    """
    data = struct()
    data.RPWI_FSW_version = RPWI_FSW_version

    # AUX
    data.ch_selected = cdf['ch_selected'][...]
    data.cal_signal  = cdf['cal_signal'][...]
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    # Header
    data.N_samp      = np.int64(cdf['N_samp'][...])
    data.N_step      = np.int64(cdf['N_step'][...])
    data.decimation  = cdf['decimation'][...]
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...] 
    data.ISW_ver     = cdf['ISW_ver'][...]
    # Data
    data.Eu_i        = np.float64(cdf['Eu_i'][...]);  data.Eu_q = np.float64(cdf['Eu_q'][...])
    data.Ev_i        = np.float64(cdf['Ev_i'][...]);  data.Ev_q = np.float64(cdf['Ev_q'][...])
    data.Ew_i        = np.float64(cdf['Ew_i'][...]);  data.Ew_q = np.float64(cdf['Ew_q'][...])
    data.frequency   = cdf['frequency'][...];  data.freq_step = cdf['freq_step'][...]; data.freq_width = cdf['freq_width'][...]
    data.time       = cdf['time'][...]
    #
    data.epoch       = cdf['Epoch'][...]
    data.scet        = cdf['SCET'][...]

    # ### ASW1: SPECIAL: data shift -16
    date = data.epoch[0];  month = date.strftime('%Y%m')
    if month == "202304" or month == "202305" or month == "202307":
        data.Eu_i = np.roll(data.Eu_i, -16);  data.Eu_q = np.roll(data.Eu_q, -16)
        data.Ev_i = np.roll(data.Ev_i, -16);  data.Ev_q = np.roll(data.Ev_q, -16)
        data.Ew_i = np.roll(data.Ew_i, -16);  data.Ew_q = np.roll(data.Ew_q, -16)
        print("-16 shift in ASW1 data")
    return data


def hf_sid2_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # AUX
    data.ch_selected = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    # Header
    data.N_samp      = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step      = np.r_["0", data.N_step, data1.N_step]
    data.decimation  = np.r_["0", data.decimation, data1.decimation]
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.ISW_ver     = np.r_["0", data.ISW_ver, data1.ISW_ver]
    # Data
    data.Eu_i        = np.r_["0", data.Eu_i, data1.Eu_i]
    data.Eu_q        = np.r_["0", data.Eu_q, data1.Eu_q]
    data.Ev_i        = np.r_["0", data.Ev_i, data1.Ev_i]
    data.Ev_q        = np.r_["0", data.Ev_q, data1.Ev_q]
    data.Ew_i        = np.r_["0", data.Ew_i, data1.Ew_i]
    data.Ew_q        = np.r_["0", data.Ew_q, data1.Ew_q]
    #
    data.frequency   = np.r_["0", data.frequency, data1.frequency]
    data.freq_step   = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width  = np.r_["0", data.freq_width, data1.freq_width]
    data.time        = np.r_["0", data.time, data1.time]
    #
    data.epoch       = np.r_["0", data.epoch, data1.epoch]
    data.scet        = np.r_["0", data.scet,  data1.scet]
    return data


def hf_sid2_shaping(data, cal_mode):
    """
    input:  data, cal_mode
    return: data
    """
    ### filtered by N_step (n_freq)
    n_time = data.Eu_i.shape[0]
    n0 = 0
    while data.N_step[n0] < 110:
        n0 = n0 + 1
        if n0 >= n_time:
            n0 = n_time - 1
            break
    n_freq = data.N_step[n0];  n_samp = data.N_samp[n0];  n_num = n_freq * n_samp
    print("  org:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "[", n_num, "] at", n0)
    # N_step (n_freq) selection
    index  = np.where(data.N_step != n_freq);  print(" [error packets]", index[0], data.N_step[index[0]], data.epoch[index[0]])
    index  = np.where(data.N_step == n_freq)
    data   = hf_sid2_select_time(data, index)
    n_time = data.Eu_i.shape[0]
    print(" cut0:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "  <n_freq selection>")

    # CUT & Shaping: less packet length
    if n_num < data.Eu_i.shape[1]:
        data.Eu_i = data.Eu_i[:, 0:n_num];  data.Eu_q = data.Eu_q[:, 0:n_num]
        data.Ev_i = data.Ev_i[:, 0:n_num];  data.Ev_q = data.Ev_q[:, 0:n_num]
        data.Ew_i = data.Ew_i[:, 0:n_num];  data.Ew_q = data.Ew_q[:, 0:n_num]
        data.frequency   = data.frequency  [:, 0:n_num]
        data.freq_step   = data.freq_step  [:, 0:n_num]
        data.freq_width  = data.freq_width [:, 0:n_num]
        data.time        = data.time       [:, 0:n_num]
        print(" cut1:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "[", n_num, "]   <n_freq*n_samp selection>")

    # Reshape from "2D: n_time * (n_freq * n_samp)" to "3D: n_time * n_freq * n_samp"
    data.Eu_i        = np.array(data.Eu_i).reshape(n_time, n_freq, n_samp)
    data.Eu_q        = np.array(data.Eu_q).reshape(n_time, n_freq, n_samp)
    data.Ev_i        = np.array(data.Ev_i).reshape(n_time, n_freq, n_samp)
    data.Ev_q        = np.array(data.Ev_q).reshape(n_time, n_freq, n_samp)
    data.Ew_i        = np.array(data.Ew_i).reshape(n_time, n_freq, n_samp)
    data.Ew_q        = np.array(data.Ew_q).reshape(n_time, n_freq, n_samp)
    data.frequency   = np.array(data.frequency).reshape(n_time, n_freq, n_samp)
    data.freq_step   = np.array(data.freq_step).reshape(n_time, n_freq, n_samp)
    data.freq_width  = np.array(data.freq_width).reshape(n_time, n_freq, n_samp)
    data.time        = np.array(data.time).reshape(n_time, n_freq, n_samp)
    print(" sort:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp)

    # ### ASW1: data shift -16 for error packets in 2023
    date = data.epoch[0];  month = date.strftime('%Y%m')
    if month == "202304" or month == "202305" or month == "202307":
        data.Eu_i[:, -1, n_samp//2:n_samp] = 0.;  data.Eu_q[:, -1, n_samp//2:n_samp] = 0.
        data.Ev_i[:, -1, n_samp//2:n_samp] = 0.;  data.Ev_q[:, -1, n_samp//2:n_samp] = 0.
        data.Ew_i[:, -1, n_samp//2:n_samp] = 0.;  data.Ew_q[:, -1, n_samp//2:n_samp] = 0.

    # ### CAL
    # ASW1: CAL flag
    if data.cal_signal[0] == 255:
        power = data.Eu_i[:,-1]**2 + data.Eu_q[:,-1]**2 + data.Ev_i[:,-1]**2 + data.Ev_q[:,-1]**2 + data.Ew_i[:,-1]**2 + data.Ew_q[:,-1]**2
        power = np.mean(power, axis=1)
        index = np.where(power > 1e4)
        data.cal_signal[:] = 0
        data.cal_signal[index[0]] = 1
    # Selection: CAL
    if cal_mode < 2:
        index  = np.where(data.cal_signal == cal_mode)
        data   = hf_sid2_select_time(data, index)
        n_time = data.Eu_i.shape[0]
        if cal_mode == 0: print("  cut:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "  <only BG>")
        else:             print("  cut:", data.Eu_i.shape, n_time, "x", n_freq, "x", n_samp, "  <only CAL>")

    # NAN -- no data channels
    data.U_selected = (data.ch_selected & 0b1   ) 
    data.V_selected = (data.ch_selected & 0b10  ) >> 1
    data.W_selected = (data.ch_selected & 0b100 ) >> 2
    index = np.where(data.U_selected == 0);  data.Eu_i[index[0]] = math.nan;  data.Eu_q[index[0]] = math.nan
    index = np.where(data.V_selected == 0);  data.Ev_i[index[0]] = math.nan;  data.Ev_q[index[0]] = math.nan
    index = np.where(data.W_selected == 0);  data.Ew_i[index[0]] = math.nan;  data.Ew_q[index[0]] = math.nan

    print("data.Eu_i",      data.Eu_i.shape);      print("data.Eu_q",      data.Eu_q.shape)
    print("data.Ev_i",      data.Ev_i.shape);      print("data.Ev_q",      data.Ev_q.shape)
    print("data.Ew_i",      data.Ew_i.shape);      print("data.Ew_q",      data.Ew_q.shape)
    print("data.frequency", data.frequency.shape); print("data.freq_step", data.freq_step.shape); print("data.freq_width", data.freq_width.shape)
    print("data.time",      data.time.shape)
    print("data.T_RWI_CH1", data.T_RWI_CH1.shape, data.T_RWI_CH1)

    return data


def hf_sid2_select_time(data, index):
    # AUX

    data.ch_selected = data.ch_selected [index[0]]
    data.cal_signal  = data.cal_signal [index[0]]
    data.T_RWI_CH1   = data.T_RWI_CH1  [index[0]]
    data.T_RWI_CH2   = data.T_RWI_CH2  [index[0]]
    data.T_HF_FPGA   = data.T_HF_FPGA  [index[0]]
    # Header
    data.N_samp      = data.N_samp     [index[0]]
    data.N_step      = data.N_step     [index[0]]
    data.decimation  = data.decimation [index[0]]
    data.ADC_ovrflw  = data.ADC_ovrflw [index[0]]
    data.ISW_ver     = data.ISW_ver    [index[0]]
    # Data
    data.epoch       = data.epoch      [index[0]]
    data.scet        = data.scet       [index[0]]
    data.Eu_i        = data.Eu_i       [index[0]];  data.Eu_q = data.Eu_q[index[0]]
    data.Ev_i        = data.Ev_i       [index[0]];  data.Ev_q = data.Ev_q[index[0]]
    data.Ew_i        = data.Ew_i       [index[0]];  data.Ew_q = data.Ew_q[index[0]]
    data.time        = data.time       [index[0]]
    data.frequency   = data.frequency  [index[0]]
    data.freq_step   = data.freq_step  [index[0]]
    data.freq_width  = data.freq_width [index[0]]

    return data


def hf_sid2_spec_nan(data, i):
    data.EE        [i] = math.nan; 
    data.EuEu      [i] = math.nan; data.EvEv      [i] = math.nan; data.EwEw      [i] = math.nan
    data.EuEv_re   [i] = math.nan; data.EvEw_re   [i] = math.nan; data.EwEu_re   [i] = math.nan
    data.EuEv_im   [i] = math.nan; data.EvEw_im   [i] = math.nan; data.EwEu_im   [i] = math.nan


"""
import csv
with open("sid2-f.csv", 'w') as f:
    writer = csv.writer(f)
    for i in range(n_freq1):
        writer.writerow([ i, freq_1d[i], freq_w_1d[i]])
print(n_freq1, spec.freq.shape)
"""

"""
import csv
with open("sid2-f-org.csv", 'w') as f:
    writer = csv.writer(f)
    for i in range(n_freq0):
        writer.writerow([ i, data.frequency[1][i][0], data.freq_width[1][i][0], data.freq_step[1][i][0]])
print(n_freq0, data.frequency.shape)
"""
