# JUICE RPWI HF HK -- 2024/2/７

import glob
import spacepy.pycdf
import numpy as np

class struct:
    pass

def juice_readhk(date_str, label, ver_str="01", base_dir="/db/JUICE/juice/datasets/"):

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

def juice_gethk_hf(data):

    hk = struct()
    hk.epoch = data['Epoch'][...]
    
    hk.pol = data['LWT03313']
    hk.heater_ena = data['LWT03314']
    hk.calsig_ena = data['LWT0332C']
    hk.temp_rwi_ch1 = data['LWT03337_CALIBRATED'][...]
    hk.temp_rwi_ch2 = data['LWT03339_CALIBRATED'][...]
    hk.temp_hf_fpga = data['LWT0333B_CALIBRATED'][...]

    hk.temp_rwi_ch1_raw = np.float32(data['LWT03337'][...])
    hk.temp_rwi_ch2_raw = np.float32(data['LWT03339'][...])
    hk.temp_hf_fpga_raw = np.float32(data['LWT0333B'][...])
    # ICD
    hk.temp_rwi_ch1_rev = -2.322450E+02 + 1.337700E-03 * hk.temp_rwi_ch1_raw + 1.050860E-04 * (hk.temp_rwi_ch1_raw)**2 -5.410590E-08 * (hk.temp_rwi_ch1_raw)**3 + 1.580980E-11* (hk.temp_rwi_ch1_raw)**4
    hk.temp_rwi_ch2_rev = -2.322450E+02 + 1.337700E-03 * hk.temp_rwi_ch2_raw + 1.050860E-04 * (hk.temp_rwi_ch2_raw)**2 -5.410590E-08 * (hk.temp_rwi_ch2_raw)**3 + 1.580980E-11* (hk.temp_rwi_ch2_raw)**4
    hk.temp_hf_fpga_rev = -2.302250E+02 + 1.343320E-03 * hk.temp_hf_fpga_raw + 1.053010E-04 * (hk.temp_hf_fpga_raw)**2 -5.422890E-08 * (hk.temp_hf_fpga_raw)**3 + 1.583520E-11* (hk.temp_hf_fpga_raw)**4
    # Current code
    hk.temp_rwi_ch1_rev2 = -2.754000E+02 + 6.979000E-02 * hk.temp_rwi_ch1_raw + 7.553000E-05 * (hk.temp_rwi_ch1_raw)**2 -5.196000E-08 * (hk.temp_rwi_ch1_raw)**3 + 1.643000E-11* (hk.temp_rwi_ch1_raw)**4
    hk.temp_rwi_ch2_rev2 = -2.743000E+02 + 6.838000E-02 * hk.temp_rwi_ch2_raw + 7.865000E-05 * (hk.temp_rwi_ch2_raw)**2 -5.466000E-08 * (hk.temp_rwi_ch2_raw)**3 + 1.707000E-11* (hk.temp_rwi_ch2_raw)**4
    hk.temp_hf_fpga_rev2 = -2.288629E+02 - 4.686928E-02 * hk.temp_hf_fpga_raw + 1.584843E-04 * (hk.temp_hf_fpga_raw)**2 -8.207110E-08 * (hk.temp_hf_fpga_raw)**3 + 2.189507E-11* (hk.temp_hf_fpga_raw)**4




    """
    hk.deploy_pri_x=data['LWT0332E']
    hk.deploy_red_x=data['LWT0332F']
    hk.deploy_pri_y=data['LWT03330']
    hk.deploy_red_y=data['LWT03331']
    hk.deploy_pri_z=data['LWT03332']
    hk.deploy_red_z=data['LWT03333']
    hk.deploy_lock_stat=data['LWT03334']
    """
    
    return hk

def juice_gethk_hf2(data):

    hk = struct()
    hk.epoch = data['Epoch'][...]
    
    hk.heater_ena = data['LWT04332']
    # hk.calsig_ena = data['LWT0332C']

    hk.temp_rwi_ch1 = data['LWT04333'][...]
    hk.temp_rwi_ch2 = data['LWT04334'][...]
    hk.temp_hf_fpga = data['LWT04335'][...]
    
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