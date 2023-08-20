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
#--- HK --------------------------------------------------------------
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
#--- QL --------------------------------------------------------------
#---------------------------------------------------------------------
"""
def clean_rfi(power, kernel_size=5):
    from scipy.signal import medfilt
    clean_power = medfilt(power, kernel_size)
    # clean_power = minfilt(power, kernel_size)
    return clean_power
"""

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
#--- HID3 ------------------------------------------------------------
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