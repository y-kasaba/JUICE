import numpy as np
import statistics

import juice_cdf_lib as juice_cdf
import juice_math_lib as juice_math

class struct:
    pass

#---------------------------------------------------------------------
#--- HID2 ------------------------------------------------------------
#---------------------------------------------------------------------
def hf_sid02_getdata(cdf):

    data = struct()

    # all data
    data.Eu_i = cdf['Eu_i'][...]
    data.Eu_q = cdf['Eu_q'][...]
    data.Ev_i = cdf['Ev_i'][...]
    data.Ev_q = cdf['Ev_q'][...]
    data.Ew_i = cdf['Ew_i'][...]
    data.Ew_q = cdf['Ew_q'][...]
    data.pps_count = cdf['pps_count'][...]
    data.sweep_start = cdf['sweep_start'][...]
    data.reduction = cdf['reduction'][...]
    data.overflow = cdf['overflow'][...]
    #
    data.time = cdf['time'][...]
    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]

    # once per data
    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]
    #
    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]
    #
    n_num = len(data.scet)
    data.n_data = np.arange(0, n_num, 1)

    return data

#---------------------------------------------------------------------
def hf_sid02_getspec(data, mode, hz_mode, ave_mode):

    # INPUT: convrsion to 1D
    Eu_i_1d = np.ravel(data.Eu_i)
    Eu_q_1d = np.ravel(data.Eu_q)
    Ev_i_1d = np.ravel(data.Ev_i)
    Ev_q_1d = np.ravel(data.Ev_q)
    Ew_i_1d = np.ravel(data.Ew_i)
    Ew_q_1d = np.ravel(data.Ew_q)
    sweep_start_1d = np.ravel(data.sweep_start)
    # frequency_1d = np.ravel(data.frequency)

    # OUTPUT
    epoch = []
    Eu_power = []
    Ev_power = []
    Ew_power = []
    frequency = []

    # Index
    index = np.where(data.sweep_start == 1)
    sweep_start_1d = np.append(sweep_start_1d, [1])     # to show "last packet"
    index_1d = np.where(sweep_start_1d)
    index_n = len(index_1d[0])
    """
    # Ver.1 -- longer packet case: N_samp detection + Error packet rejection
    index_n_tmp = 0
    for i in range(index_n):
        if i < index_n-1:
            if index[1][i] == 0:
                index_1d[0][index_n_tmp] = index_1d[0][i]
                index[0][index_n_tmp] = index[0][i]
                index_n_tmp = index_n_tmp + 1
        else:
            index_1d[0][index_n_tmp] = index_1d[0][i]
            index_n_tmp = index_n_tmp + 1            
    index_n = index_n_tmp
    n_len = index_1d[0][1] - index_1d[0][0]
    """
    
    # Spec formation
    spec = struct()
    index_n0 = 0
    for i in range(index_n-1):

        # number of sweep step (fixed for ver.1 SW SID2)
        n_step = data.N_step[index[0][i]]

        # number of sampling (fixed for ver.1 SW SID2)
        n_samp = data.N_samp[index[0][i]]
        #
        # Ver.1 -- longer packet case
        # n_samp = np.int16(n_len / n_step)

        # 1/bandwidth [sec]
        decimation = data.decimation[index[0][i]]
        sample_rate = juice_cdf._sample_rate(decimation)  # Hz
        dt = 1.0 / (296e+3 / 2**decimation)

        # get_frequency  (f_step_1d: 87.90607kHz -- not used yet   f_width_1d: 111.9768 kHz = Sample_rate(148kHz) * 0.7566)
        frequency_1d, f_step_1d, f_width_1d = juice_cdf._get_frequencies(n_step, n_samp, sample_rate)
        # n_samp_width = np.int16(n_samp * f_step_1d[0] / (sample_rate/1000.) / 2.)
        # print(n_samp, n_samp_width, sample_rate/1000, f_step_1d[0], sample_rate/1000, f_step_1d[0] / (sample_rate/1000.) / 2)
        # print(len(frequency_1d), frequency_1d)
        # print(n_samp_width, n_samp, len(f_step_1d), f_step_1d)
        # print(sample_rate, len(f_width_1d), f_width_1d)

        # data length
        index_len = index_1d[0][i+1] - index_1d[0][i]
        if index_len != n_step * n_samp:
            print("****ERROR**** [", i, index_n0, data.epoch[index[0][i]], "] length:", index_len, "!=", n_samp, "*", n_step)
            continue

        # epoch
        epoch.append(data.epoch[index[0][i]])
        index_n0 = index_n0 + 1

        # data cut
        Eu_i = np.array(Eu_i_1d[index_1d[0][i]:index_1d[0][i+1]])
        Eu_q = np.array(Eu_q_1d[index_1d[0][i]:index_1d[0][i+1]])
        Ev_i = np.array(Ev_i_1d[index_1d[0][i]:index_1d[0][i+1]])
        Ev_q = np.array(Ev_q_1d[index_1d[0][i]:index_1d[0][i+1]])
        Ew_i = np.array(Ew_i_1d[index_1d[0][i]:index_1d[0][i+1]])
        Ew_q = np.array(Ew_q_1d[index_1d[0][i]:index_1d[0][i+1]])
        # freq = np.array(frequency_1d[index_1d[0][i]:index_1d[0][i+1]])
        freq = np.array(frequency_1d)

        Eu_i_array = Eu_i.reshape(n_step, n_samp)
        Eu_q_array = Eu_q.reshape(n_step, n_samp)
        Ev_i_array = Ev_i.reshape(n_step, n_samp)
        Ev_q_array = Ev_q.reshape(n_step, n_samp)
        Ew_i_array = Ew_i.reshape(n_step, n_samp)
        Ew_q_array = Ew_q.reshape(n_step, n_samp)
        freq_array = freq.reshape(n_step, n_samp)

        # low resolution power spectra
        if mode == 0:
            if (ave_mode == 0):  # [ave_mode] 0: simple sum   1: FFT sum   2: median sum   3: min sum
                juice_math._mean_power(Eu_i_array, Eu_q_array, Eu_power, f_width_1d[0], hz_mode)
                juice_math._mean_power(Ev_i_array, Ev_q_array, Ev_power, f_width_1d[0], hz_mode)
                juice_math._mean_power(Ew_i_array, Ew_q_array, Ew_power, f_width_1d[0], hz_mode)
            else:               # [ave_mode] 0: simple sum   1: FFT sum   2: median sum   3: min sum
                for ii in range(n_step):
                    freq0 = np.fft.fftfreq(n_samp, d=dt)/1000. + freq_array[ii][:]
                    df = freq0[np.int16(n_samp/2-n_samp/8)]-freq0[np.int16(n_samp/2+n_samp/8)]
                    #
                    s = np.fft.fft(Eu_i_array[ii][:] - Eu_q_array[ii][:] * 1j)
                    power = np.power(np.abs(s) / n_samp, 2.0)
                    if hz_mode > 0:
                        power = power / (df * 1000)
                    if (ave_mode == 1):
                        power0 = np.sum(power[np.int16(n_samp/2+n_samp/8):n_samp])+np.sum(power[0:np.int16(n_samp/2-n_samp/8)])
                    elif (ave_mode == 2):
                        power0 = statistics.median(power[np.int16(n_samp/2+n_samp/8):n_samp])*(n_samp/8*3) + statistics.median(power[0:np.int16(n_samp/2-n_samp/8)])*(n_samp/8*3)
                    else:
                        power0 = min(power[np.int16(n_samp/2+n_samp/8):n_samp])*(n_samp/8*3) + min(power[0:np.int16(n_samp/2-n_samp/8)])*(n_samp/8*3)                            
                    Eu_power.append(power0)
                    #
                    s = np.fft.fft(Ev_i_array[ii][:] - Ev_q_array[ii][:] * 1j)
                    power = np.power(np.abs(s) / n_samp, 2.0)
                    if hz_mode > 0:
                        power = power / (df * 1000)
                    if (ave_mode == 1):
                        power0 = np.sum(power[np.int16(n_samp/2+n_samp/8):n_samp])+np.sum(power[0:np.int16(n_samp/2-n_samp/8)])
                    elif (ave_mode == 2):
                        power0 = statistics.median(power[np.int16(n_samp/2+n_samp/8):n_samp])*(n_samp/8*3) + statistics.median(power[0:np.int16(n_samp/2-n_samp/8)])*(n_samp/8*3)
                    else:
                        power0 = min(power[np.int16(n_samp/2+n_samp/8):n_samp])*(n_samp/8*3) + min(power[0:np.int16(n_samp/2-n_samp/8)])*(n_samp/8*3)                            
                    Ev_power.append(power0)
                    #
                    s = np.fft.fft(Ew_i_array[ii][:] - Ew_q_array[ii][:] * 1j)
                    power = np.power(np.abs(s) / n_samp, 2.0)
                    if hz_mode > 0:
                        power = power / (df * 1000)
                    if (ave_mode == 1):
                        power0 = np.sum(power[np.int16(n_samp/2+n_samp/8):n_samp])+np.sum(power[0:np.int16(n_samp/2-n_samp/8)])
                    elif (ave_mode == 2):
                        power0 = statistics.median(power[np.int16(n_samp/2+n_samp/8):n_samp])*(n_samp/8*3) + statistics.median(power[0:np.int16(n_samp/2-n_samp/8)])*(n_samp/8*3)
                    else:
                        power0 = min(power[np.int16(n_samp/2+n_samp/8):n_samp])*(n_samp/8*3) + min(power[0:np.int16(n_samp/2-n_samp/8)])*(n_samp/8*3)                            
                    Ew_power.append(power0)

            freq = freq.reshape(n_step, n_samp)
            freq = freq[:, 0]
            frequency.extend(freq)

        # high resolution power spectra
        else:
            for ii in range(n_step):
                df = juice_math._fft_freq(n_samp, freq_array[ii][:], frequency, dt)
                juice_math._fft_power(n_samp, Eu_i_array[ii][:], Eu_q_array[ii][:], Eu_power, dt, df, hz_mode)
                juice_math._fft_power(n_samp, Ev_i_array[ii][:], Ev_q_array[ii][:], Ev_power, dt, df, hz_mode)
                juice_math._fft_power(n_samp, Ew_i_array[ii][:], Ew_q_array[ii][:], Ew_power, dt, df, hz_mode)

    # return: "spec"
    frequency = np.array(frequency)
    Eu_power = np.array(Eu_power)
    Ev_power = np.array(Ev_power)
    Ew_power = np.array(Ew_power)
    index_n = index_n0
    n_set = int(Eu_power.size / index_n)
    spec.frequency = frequency.reshape(index_n, n_set).transpose()
    spec.Eu_power = Eu_power.reshape(index_n, n_set).transpose()
    spec.Ev_power = Ev_power.reshape(index_n, n_set).transpose()
    spec.Ew_power = Ew_power.reshape(index_n, n_set).transpose()
    spec.n_samp = n_samp
    spec.n_step = n_step
    spec.epoch = epoch

    return spec