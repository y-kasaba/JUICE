"""
    JUICE RPWI HF SID23 (PSSR3 rich): L1a QL -- 2023/11/19
"""
import numpy as np
import juice_cdf_lib as juice_cdf
import scipy.stats as stats


class struct:
    pass


# ---------------------------------------------------------------------
# --- SID23 ------------------------------------------------------------
# ---------------------------------------------------------------------
def juice_getdata_hf_sid23(cdf, cf):
    """
    input:  CDF, cf:conversion factor
    return: data
    """
    data = struct()

    # AUX
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    data.cal_signal = cdf['cal_signal'][...]
    data.pol_AUX = cdf['pol_AUX'][...]
    data.decimation_AUX = cdf['decimation_AUX'][...]
    data.N_block = cdf['N_block'][...]
    data.freq_center = cdf['freq_center'][...]
    data.N_feed = cdf['N_feed'][...]
    data.N_skip = cdf['N_skip'][...]

    # Header
    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]
    data.pol = cdf['pol'][...]

    # Data
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]
    #
    data.Eu_i = cdf['Eu_i'][...] * 10**(cf/20)
    data.Eu_q = cdf['Eu_q'][...] * 10**(cf/20)
    data.Ev_i = cdf['Ev_i'][...] * 10**(cf/20)
    data.Ev_q = cdf['Ev_q'][...] * 10**(cf/20)
    data.Ew_i = cdf['Ew_i'][...] * 10**(cf/20)
    data.Ew_q = cdf['Ew_q'][...] * 10**(cf/20)
    data.pps_count = cdf['pps_count'][...]
    data.sweep_start = cdf['sweep_start'][...]
    data.reduction = cdf['reduction'][...]
    data.overflow = cdf['overflow'][...]

    # CUT & Reshape
    data.n_time = data.Eu_i.shape[0]
    n_num0 = data.N_feed[0] * 128
    n_num1 = (data.N_feed[0] + data.N_skip[0]) * 128
    n_num = n_num0 * data.N_block[0]
    if n_num < data.Eu_i.shape[1]:
        print(" org:", data.Eu_i.shape, data.N_block[0], data.N_feed[0])
        data.Eu_i = data.Eu_i[:, 0:n_num]
        data.Eu_q = data.Eu_q[:, 0:n_num]
        data.Ev_i = data.Ev_i[:, 0:n_num]
        data.Ev_q = data.Ev_q[:, 0:n_num]
        data.Ew_i = data.Ew_i[:, 0:n_num]
        data.Ew_q = data.Ew_q[:, 0:n_num]
        print(" cut:", data.Eu_i.shape, data.N_block[0], data.N_feed[0])
    data.Eu_i = np.array(data.Eu_i).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Eu_q = np.array(data.Eu_q).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ev_i = np.array(data.Ev_i).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ev_q = np.array(data.Ev_q).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ew_i = np.array(data.Ew_i).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ew_q = np.array(data.Ew_q).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)

    # Time   
    time = np.arange(0, n_num0, 1) / juice_cdf._sample_rate(data.decimation_AUX[0])
    time0 = np.float32(np.arange(0, n_num, 1))
    for i in range(data.N_block[0]):
        time0[n_num0*i:n_num0*(i+1)] = time + i * n_num1 / juice_cdf._sample_rate(data.decimation_AUX[0])
    time0 = np.array(time0).reshape(data.N_block[0], data.N_feed[0]*128)
    #
    data.time = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    data.time = data.time.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    for i in range(data.n_time):
        data.time[i][:][:] = time0

    return data


# ---------------------------------------------------------------------
def hf_sid23_getspec(data, unit_mode):
    """
    input:  data, unit_mode
    return: spec
    """
    # Spec formation
    spec = struct()
    n_data = data.N_feed[0]*128

    # Frequency
    dt = 1.0 / juice_cdf._sample_rate(data.decimation_AUX[0])
    spec.freq = np.fft.fftshift(np.fft.fftfreq(data.N_feed[0]*128, d=dt)) / 1000.
    spec.freq = spec.freq + data.freq_center[0]

    # FFT
    window = np.hanning(n_data) 
    acf = 1/(sum(window)/n_data)
    #
    s = np.fft.fft((data.Eu_i - data.Eu_q * 1j) * window)
    s = np.power(np.abs(s) / n_data, 2.0) * acf * acf
    spec.EuEu = np.fft.fftshift(s, axes=(2,))
    s = np.fft.fft((data.Ev_i - data.Ev_q * 1j) * window)
    s = np.power(np.abs(s) / n_data, 2.0) * acf * acf
    spec.EvEv = np.fft.fftshift(s, axes=(2,))
    s = np.fft.fft((data.Ew_i - data.Ew_q * 1j) * window)
    s = np.power(np.abs(s) / n_data, 2.0) * acf * acf
    spec.EwEw = np.fft.fftshift(s, axes=(2,))

    spec.EE = spec.EuEu + spec.EvEv + spec.EwEw

    return spec


# ---------------------------------------------------------------------
def hf_sid23_getauto(data):
    """
    input:  data
    return: auto
    """
    # Spec formation
    auto = struct()
    auto.EuEu = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    auto.EvEv = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    auto.EwEw = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    auto.EE   = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    auto.EuEu = auto.EuEu.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    auto.EvEv = auto.EvEv.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    auto.EwEw = auto.EwEw.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    auto.EE   = auto.EE.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)

    for i in range(data.n_time):
        for j in range(data.N_block[0]):
            EuEu = data.Eu_i[i][j]**2 + data.Eu_q[i][j]**2  
            EvEv = data.Ev_i[i][j]**2 + data.Ev_q[i][j]**2  
            EwEw = data.Ew_i[i][j]**2 + data.Ew_q[i][j]**2  
            EE = EuEu + EvEv + EwEw
            EuEu = stats.zscore(EuEu); EvEv = stats.zscore(EvEv); EwEw = stats.zscore(EwEw); EE = stats.zscore(EE)

            EuEu_auto = np.correlate(EuEu, EuEu, mode='full')
            EuEu_auto = EuEu_auto[EuEu_auto.shape[0]//2:]
            EuEu_auto /= len(EuEu_auto)
            auto.EuEu[i][j] = EuEu_auto

            EvEv_auto = np.correlate(EvEv, EvEv, mode='full')
            EvEv_auto = EvEv_auto[EvEv_auto.shape[0]//2:]
            EvEv_auto /= len(EvEv_auto)
            auto.EvEv[i][j] = EvEv_auto

            EwEw_auto = np.correlate(EwEw, EwEw, mode='full')
            EwEw_auto = EwEw_auto[EwEw_auto.shape[0]//2:]
            EwEw_auto /= len(EwEw_auto)
            auto.EwEw[i][j] = EwEw_auto

            EE_auto   = np.correlate(EE, EE, mode='full')
            EE_auto   = EE_auto[EE_auto.shape[0]//2:]
            EE_auto   /= len(EE_auto)
            auto.EE[i][j] = EE_auto

            auto.EuEu[i][j][0] = auto.EvEv[i][j][0] = auto.EwEw[i][j][0] = auto.EE[i][j][0] = 0
            auto.EuEu[i][j][1] = auto.EvEv[i][j][1] = auto.EwEw[i][j][1] = auto.EE[i][j][1] = 0
    return auto
