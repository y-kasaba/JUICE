import glob
import spacepy.pycdf
import numpy as np
import statistics

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
def juice_gethk_hf(data):

    hk = struct()
    hk.epoch = data['Epoch'][...]
    
    hk.heater_ena = data['LWT03314']
    hk.calsig_ena = data['LWT0332C']

    hk.deploy_pri_x=data['LWT0332E']
    hk.deploy_red_x=data['LWT0332F']
    hk.deploy_pri_y=data['LWT03330']
    hk.deploy_red_y=data['LWT03331']
    hk.deploy_pri_z=data['LWT03332']
    hk.deploy_red_z=data['LWT03333']
    hk.deploy_lock_stat=data['LWT03334']

    hk.temp_rwi_u = data['LWT03337_CALIBRATED'][...]
    hk.temp_rwi_w = data['LWT03339_CALIBRATED'][...]
    hk.temp_hf_fpga = data['LWT0333B_CALIBRATED'][...]

    return hk

#---------------------------------------------------------------------
def juice_gethk_dpu(data):

    hk = struct()
    hk.epoch = data['Epoch'][...]
    hk.dpu_temp = data['LWT03437_CALIBRATED'][...]
    hk.lvps_temp = data['LWT03438_CALIBRATED'][...]
    hk.lp_temp = data['LWT03439_CALIBRATED'][...]
    hk.lf_temp = data['LWT0343A_CALIBRATED'][...]
    hk.hf_temp = data['LWT0343B_CALIBRATED'][...]
    hk.scm_temp = data['LWT0343C_CALIBRATED'][...]

    return hk

#---------------------------------------------------------------------
def juice_gethk_lvps(data):

    hk = struct()
    hk.epoch = data['Epoch'][...]
    hk.vol_hf_33 = data['LWT03358_CALIBRATED'][...]
    hk.vol_hf_85 = data['LWT03359_CALIBRATED'][...]
    hk.cur_hf_33 = data['LWT03362_CALIBRATED'][...]
    hk.cur_hf_85 = data['LWT03363_CALIBRATED'][...]
    hk.hf_on_off = data['LWT03372'][...]

    return hk

#---------------------------------------------------------------------
def clean_rfi(power, kernel_size=5):
    from scipy.signal import medfilt
    clean_power = medfilt(power, kernel_size)
    # clean_power = minfilt(power, kernel_size)
    return clean_power

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
def power_label(cal_mode, hz_mode):
    if hz_mode == 0:
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

#---------------------------------------------------------------------
def juice_getdata_hf_sid02(cdf):

    data = struct()

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

    data.time = cdf['time'][...]
    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]

    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]

    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]

    # shaping
    n_num = data.N_samp[0] * data.N_step[0]
    #
    data.Eu_i = data.Eu_i[:, 0:n_num]
    data.Eu_q = data.Eu_q[:, 0:n_num]
    data.Ev_i = data.Ev_i[:, 0:n_num]
    data.Ev_q = data.Ev_q[:, 0:n_num]
    data.Ew_i = data.Ew_i[:, 0:n_num]
    data.Ew_q = data.Ew_q[:, 0:n_num]
    data.pps_count = data.pps_count[:, 0:n_num] 
    data.sweep_start = data.sweep_start[:, 0:n_num] 
    data.reduction = data.reduction[:, 0:n_num]
    data.overflow = data.overflow[:, 0:n_num] 
    data.time = data.time[:, 0:n_num] 
    data.frequency = data.frequency[:, 0:n_num] 
    data.freq_step = data.freq_step[:, 0:n_num] 
    data.freq_width = data.freq_width[:, 0:n_num] 
    
    return data

def juice_getspec_hf_sid02(data, mode, hz_mode, ave_mode):

    # INPUT
    Eu_i_1d = np.ravel(data.Eu_i)
    Eu_q_1d = np.ravel(data.Eu_q)
    Ev_i_1d = np.ravel(data.Ev_i)
    Ev_q_1d = np.ravel(data.Ev_q)
    Ew_i_1d = np.ravel(data.Ew_i)
    Ew_q_1d = np.ravel(data.Ew_q)
    sweep_start_1d = np.ravel(data.sweep_start)
    # frequency_1d = np.ravel(data.frequency)           # TMP

    # OUTPUT
    epoch = []
    Eu_power = []
    Ev_power = []
    Ew_power = []
    frequency = []

    # Num
    sweep_start_1d = np.append(sweep_start_1d, [1])     # to show "last packet"
    index_1d = np.where(sweep_start_1d)
    index = np.where(data.sweep_start == 1)
    index_n = len(index_1d[0])

    # N_samp detection + Error packet rejection
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
    n_len = index_1d[0][1]-index_1d[0][0]

    # Spec formation
    spec = struct()
    index_n0 = 0
    for i in range(index_n-1):

        # 1/bandwidth [sec]
        decimation = data.decimation[index[0][i]]
        sample_rate = _sample_rate(decimation)  # Hz
        dt = 1.0 / (296e+3 / 2**decimation)

        # number of sweep step (fixed for ver.1 SW SID2)
        n_step = data.N_step[index[0][i]]

        # number of sampling (fixed for ver.1 SW SID2)
        # n_samp = data.N_samp[index[0][i]]
        n_samp = np.int16(n_len / n_step)

        # get_frequency
        frequency_1d, f_step_1d, f_width_1d = _get_frequencies(n_step, n_samp, sample_rate)

        # data length
        index_len = index_1d[0][i+1]-index_1d[0][i]
        if index_len == n_step * n_samp:
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

            if mode == 0:
                # low resolution power spectra
                if (ave_mode == 0):
                    power = np.mean(Eu_i_array**2 + Eu_q_array**2, axis=1)
                    df = f_width_1d[0]
                    if hz_mode > 0:
                        power = power / (df * 1000)
                    Eu_power.extend(power)
                    #
                    power = np.mean(Ev_i_array**2 + Ev_q_array**2, axis=1)
                    df = f_width_1d[0]
                    if hz_mode > 0:
                        power = power / (df * 1000)
                    Ev_power.extend(power)
                    #
                    power = np.mean(Ew_i_array**2 + Ew_q_array**2, axis=1)
                    df = f_width_1d[0]
                    if hz_mode > 0:
                        power = power / (df * 1000)
                    Ew_power.extend(power)
                else:
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

                # freq = np.array(frequency_1d[index_1d[0][i]:index_1d[0][i+1]])
                freq = freq.reshape(n_step, n_samp)
                freq = freq[:, 0]
                frequency.extend(freq)

            else:
                # high resolution power spectra
                for ii in range(n_step):
                    freq = np.fft.fftfreq(n_samp, d=dt)/1000. + freq_array[ii][:]
                    frequency.extend(freq[np.int16(n_samp/2+n_samp/8):n_samp])
                    frequency.extend(freq[0:np.int16(n_samp/2-n_samp/8)])
                    df = freq[1]-freq[0]
                    #
                    s = np.fft.fft(Eu_i_array[ii][:] - Eu_q_array[ii][:] * 1j)
                    power = np.power(np.abs(s) / n_samp, 2.0) 
                    if hz_mode > 0:
                        power = power / (df * 1000)
                    Eu_power.extend(power[np.int16(n_samp/2+n_samp/8):n_samp])
                    Eu_power.extend(power[0:np.int16(n_samp/2-n_samp/8)])
                    #
                    s = np.fft.fft(Ev_i_array[ii][:] - Ev_q_array[ii][:] * 1j)
                    power = np.power(np.abs(s) / n_samp, 2.0) 
                    if hz_mode > 0:
                        power = power / (df * 1000)
                    Ev_power.extend(power[np.int16(n_samp/2+n_samp/8):n_samp])
                    Ev_power.extend(power[0:np.int16(n_samp/2-n_samp/8)])
                    #
                    s = np.fft.fft(Ew_i_array[ii][:] - Ew_q_array[ii][:] * 1j)
                    power = np.power(np.abs(s) / n_samp, 2.0)
                    if hz_mode > 0:
                        power = power / (df * 1000)
                    Ew_power.extend(power[np.int16(n_samp/2+n_samp/8):n_samp])
                    Ew_power.extend(power[0:np.int16(n_samp/2-n_samp/8)])

        else:
            print("****ERROR**** [", i, index_n0, data.epoch[index[0][i]], "] length:", index_len, "!=", n_samp, "*", n_step)

    Eu_power = np.array(Eu_power)
    Ev_power = np.array(Ev_power)
    Ew_power = np.array(Ew_power)
    frequency = np.array(frequency)

    spec.n_samp = n_samp
    spec.n_step = n_step
    spec.epoch = epoch

    index_n = index_n0
    n_set = int(Eu_power.size / index_n)

    spec.frequency = frequency.reshape(index_n, n_set).transpose()
    spec.Eu_power = Eu_power.reshape(index_n, n_set).transpose()
    spec.Ev_power = Ev_power.reshape(index_n, n_set).transpose()
    spec.Ew_power = Ew_power.reshape(index_n, n_set).transpose()

    return spec

#---------------------------------------------------------------------
def juice_getdata_hf_sid03(cdf):

    data = struct()

    data.EuEu = cdf['EuEu'][...]
    data.EvEv = cdf['EvEv'][...]
    data.EwEw = cdf['EwEw'][...]
    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]

    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]
    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]
    data.B0_step = cdf['B0_step'][...]

    # shaping
    n_num = data.B0_step[0]
    if n_num == 255:
        data.EuEu = data.EuEu[:, 0:n_num] 
        data.EvEv = data.EvEv[:, 0:n_num] 
        data.EwEw = data.EwEw[:, 0:n_num] 
        data.frequency = data.frequency[:, 0:n_num] 
        data.freq_step = data.freq_step[:, 0:n_num] 
        data.freq_width = data.freq_width[:, 0:n_num]     

    return data