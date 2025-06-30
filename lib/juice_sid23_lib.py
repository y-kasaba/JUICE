"""
    JUICE RPWI HF SID23 (PSSR3 rich): L1a QL -- 2025/6/30
"""
import numpy          as np
import scipy.stats    as stats
import juice_cdf_lib  as juice_cdf
import juice_spec_lib as juice_spec

class struct:
    pass


# ---------------------------------------------------------------------
# --- SID23 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid23_read(cdf, RPWI_FSW_version):
    """
    input:  CDF
    return: data
    """
    data = struct()
    data.RPWI_FSW_version = RPWI_FSW_version

    # AUX
    data.ch_selected = cdf['ch_selected'][...]
    data.cal_signal  = cdf['cal_signal'][...]
    data.N_block     = np.int16(cdf['N_block'][...])
    data.N_lag       = np.int16(cdf['N_lag'][...])
    data.N_feed      = np.int16(cdf['N_feed'][...])
    data.N_skip      = np.int16(cdf['N_skip'][...])
    data.freq_center = cdf['freq_center'][...]
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
    data.Eu_i        = np.float64(cdf['Eu_i'][...])
    data.Eu_q        = np.float64(cdf['Eu_q'][...])
    data.Ev_i        = np.float64(cdf['Ev_i'][...])
    data.Ev_q        = np.float64(cdf['Ev_q'][...])
    data.Ew_i        = np.float64(cdf['Ew_i'][...])
    data.Ew_q        = np.float64(cdf['Ew_q'][...])
    #
    data.epoch       = cdf['Epoch'][...]

    return data


def hf_sid23_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # AUX
    data.ch_selected = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.N_block     = np.r_["0", data.N_block, data1.N_block]
    data.N_lag       = np.r_["0", data.N_lag, data1.N_lag]
    data.N_skip      = np.r_["0", data.N_skip, data1.N_skip]
    data.N_feed      = np.r_["0", data.N_feed, data1.N_feed]
    data.freq_center = np.r_["0", data.freq_center, data1.freq_center]
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
    data.Eu_i           = np.r_["0", data.Eu_i, data1.Eu_i]
    data.Eu_q           = np.r_["0", data.Eu_q, data1.Eu_q]
    data.Ev_i           = np.r_["0", data.Ev_i, data1.Ev_i]
    data.Ev_q           = np.r_["0", data.Ev_q, data1.Ev_q]
    data.Ew_i           = np.r_["0", data.Ew_i, data1.Ew_i]
    data.Ew_q           = np.r_["0", data.Ew_q, data1.Ew_q]
    #
    data.epoch          = np.r_["0", data.epoch, data1.epoch]
    return data


def hf_sid23_shaping(data, f_max, f_min):
    """
    input:  data, f_max, f_min
    return: data
    """
    # Size
    data.n_time = data.Eu_i.shape[0]
    n_num0 =  data.N_feed[0] * 128
    n_num1 = (data.N_feed[0] + data.N_skip[0]) * 128
    n_num  = n_num0 * data.N_block[0]
    print("  org:", data.Eu_i.shape, data.n_time, n_num, data.N_block[0], data.N_feed[0])

    # ---------------------------
    # --- frequency selection ---
    # ---------------------------
    index = np.where( (data.freq_center > f_min) & (data.freq_center < f_max) )
    # AUX
    data.ch_selected = data.ch_selected[index[0]]
    data.cal_signal  = data.cal_signal [index[0]]
    data.N_block     = data.N_block [index[0]]
    data.N_lag       = data.N_lag   [index[0]]
    data.N_feed      = data.N_feed  [index[0]]
    data.N_skip      = data.N_skip  [index[0]]
    data.freq_center = data.freq_center[index[0]]
    data.T_RWI_CH1   = data.T_RWI_CH1[index[0]]
    data.T_RWI_CH2   = data.T_RWI_CH2[index[0]]
    data.T_HF_FPGA   = data.T_HF_FPGA[index[0]]
    # Header
    data.N_samp      = data.N_samp    [index[0]]
    data.N_step      = data.N_step    [index[0]]
    data.decimation  = data.decimation[index[0]]
    data.ADC_ovrflw  = data.ADC_ovrflw[index[0]]
    data.ISW_ver     = data.ISW_ver   [index[0]]
    # Data
    data.Eu_i        = data.Eu_i [index[0]]
    data.Eu_q        = data.Eu_q [index[0]]
    data.Ev_i        = data.Ev_i [index[0]]
    data.Ev_q        = data.Ev_q [index[0]]
    data.Ew_i        = data.Ew_i [index[0]]
    data.Ew_q        = data.Ew_q [index[0]]
    data.epoch       = data.epoch[index[0]]
    #
    data.n_time = data.Eu_i.shape[0]
    n_num0 = data.N_feed[0] * 128
    n_num1 = (data.N_feed[0] + data.N_skip[0]) * 128
    n_num  = n_num0 * data.N_block[0]
    print("  cut:", data.Eu_i.shape, data.n_time, n_num, data.N_block[0], data.N_feed[0], "   frequency in", f_min, "-", f_max)

    # -------------------------------------
    # CUT & Shaping: less packet length
    # -------------------------------------
    if n_num < data.Eu_i.shape[1]:
        data.Eu_i = data.Eu_i[:, 0:n_num];  data.Eu_q = data.Eu_q[:, 0:n_num]
        data.Ev_i = data.Ev_i[:, 0:n_num];  data.Ev_q = data.Ev_q[:, 0:n_num]
        data.Ew_i = data.Ew_i[:, 0:n_num];  data.Ew_q = data.Ew_q[:, 0:n_num]
        print("  cut:", data.Eu_i.shape, data.n_time, n_num, data.N_block[0], data.N_feed[0])

    # -------------------------------------
    # Reshape from "2D: n_time * (n_freq * n_samp)" to "3D: n_time * n_block * n_feed"
    # -------------------------------------
    data.Eu_i = np.array(data.Eu_i).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Eu_q = np.array(data.Eu_q).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ev_i = np.array(data.Ev_i).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ev_q = np.array(data.Ev_q).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ew_i = np.array(data.Ew_i).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    data.Ew_q = np.array(data.Ew_q).reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    print(" sort:", data.Eu_i.shape, data.n_time, n_num, data.N_block[0], data.N_feed[0])

    # Time   
    time  = np.arange(0, n_num0, 1) / juice_cdf._sample_rate(data.decimation[0])
    time0 = np.float64(np.arange(0, n_num, 1))
    for i in range(data.N_block[0]):
        time0[n_num0*i:n_num0*(i+1)] = time + i * n_num1 / juice_cdf._sample_rate(data.decimation[0])
    time0 = np.array(time0).reshape(data.N_block[0], data.N_feed[0]*128)
    #
    data.time = np.zeros(data.n_time*data.N_block[0]*data.N_feed[0]*128)
    data.time = data.time.reshape(data.n_time, data.N_block[0], data.N_feed[0]*128)
    for i in range(data.n_time):
        data.time[i][:][:] = time0

    print("data.Eu_i",           data.Eu_i.shape)
    print("data.Eu_q",           data.Eu_q.shape)
    print("data.Ev_i",           data.Ev_i.shape)
    print("data.Ev_q",           data.Ev_q.shape)
    print("data.Ew_i",           data.Ew_i.shape)
    print("data.Ew_q",           data.Ew_q.shape)

    return data


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

            auto.EuEu[i][j][0] = 0
            auto.EvEv[i][j][0] = 0
            auto.EwEw[i][j][0] = 0
            auto.EE[i][j][0] = 0
            auto.EuEu[i][j][1] = 0
            auto.EvEv[i][j][1] = 0
            auto.EwEw[i][j][1] = 0
            auto.EE[i][j][1] = 0
    return auto


# ---------------------------------------------------------------------
def hf_sid23_rime_detect(data):
    data.EuEu = (data.Eu_i * data.Eu_i + data.Eu_q * data.Eu_q) ** .5
    data.EvEv = (data.Ev_i * data.Ev_i + data.Ev_q * data.Ev_q) ** .5
    data.EwEw = (data.Ew_i * data.Ew_i + data.Ew_q * data.Ew_q) ** .5
    # print(data.EuEu.shape, data.n_time, data.N_block[0], data.N_feed[0]*128)

    k0 = 0
    for i in range(data.n_time):
        for j in range(data.N_block[0]):
            for k in range(data.N_feed[0]*128):
                if data.EuEu[i][j][k] >= 1000:
                    if k-k0 > 80:
                        print(k0, k)
                        data.EuEu[i][j][k:k0-1] = 10000
                        k0 = k
    return data
