#---------------------------------------------------------------------
# JUICE RPWI HF HK -- 2024/6/27
#---------------------------------------------------------------------
import glob
import spacepy.pycdf
import numpy as np

class struct:
    pass

#---------------------------------------------------------------------
# Read: HK data in IRFU server
def juice_readhk(date_str, label, ver_str="01", base_dir="/db/JUICE/juice/datasets/"):

    yr_format = date_str[0:2]
    yr_str = date_str[0:4]
    mn_str = date_str[4:6]
    dy_str = date_str[6:8]

    if yr_format=='20':
        search_path = base_dir+yr_str+'/'+mn_str+'/'+dy_str + \
            '/JUICE_LU_RPWI-PPTD-'+label+'_'+date_str+'T??????_V'+ver_str+'.cdf'
    else:
        search_path = base_dir + date_str + \
            '/JUICE_LU_RPWI-*'+label+'_V'+ver_str+'*.cdf'

    fname = glob.glob(search_path)
    if len(fname) > 0:
        print("[[read data]] ", search_path)
        err = 0
        ret = spacepy.pycdf.concatCDF([
            spacepy.pycdf.CDF(f) for f in glob.glob(search_path)])
    else:
        print("!! no data !! ", search_path)
        err = 1
        ret = 0

    return ret, err

#---------------------------------------------------------------------
# HF-HK
def juice_gethk_hf(data, mode):

    hk = struct()
    hk.epoch = data['Epoch'][...]
    
    if mode == 0:
        # LWYHK00032
        hk.pol = data['LWT03313']
        hk.heater_ena = data['LWT03314']
        hk.calsig_ena = data['LWT0332C']

        hk.temp_rwi_ch1_raw = np.float32(data['LWT03337'][...])
        hk.temp_rwi_ch2_raw = np.float32(data['LWT03339'][...])
        hk.temp_hf_fpga_raw = np.float32(data['LWT0333B'][...])

        hk.temp_rwi_ch1 = data['LWT03337_CALIBRATED'][...]
        hk.temp_rwi_ch2 = data['LWT03339_CALIBRATED'][...]
        hk.temp_hf_fpga = data['LWT0333B_CALIBRATED'][...]
    else:
        # LWYHK10033
        hk.pol = data['LWT04331']
        hk.heater_ena = data['LWT04332']
        # hk.calsig_ena = none?

        hk.temp_rwi_ch1_raw = np.float32(data['LWT04333'][...])
        hk.temp_rwi_ch2_raw = np.float32(data['LWT04334'][...])
        hk.temp_hf_fpga_raw = np.float32(data['LWT04335'][...])

        hk.temp_rwi_ch1 = -2.322450E+02 + 1.337700E-03 * hk.temp_rwi_ch1_raw + 1.050860E-04 * (hk.temp_rwi_ch1_raw)**2 -5.410590E-08 * (hk.temp_rwi_ch1_raw)**3 + 1.580980E-11* (hk.temp_rwi_ch1_raw)**4
        hk.temp_rwi_ch2 = -2.322450E+02 + 1.337700E-03 * hk.temp_rwi_ch2_raw + 1.050860E-04 * (hk.temp_rwi_ch2_raw)**2 -5.410590E-08 * (hk.temp_rwi_ch2_raw)**3 + 1.580980E-11* (hk.temp_rwi_ch2_raw)**4
        hk.temp_hf_fpga = -2.302250E+02 + 1.343320E-03 * hk.temp_hf_fpga_raw + 1.053010E-04 * (hk.temp_hf_fpga_raw)**2 -5.422890E-08 * (hk.temp_hf_fpga_raw)**3 + 1.583520E-11* (hk.temp_hf_fpga_raw)**4  

    # ICD - modified
    hk.temp_rwi_ch1_rev = -2.28245E+02 + 1.33770E-03 * hk.temp_rwi_ch1_raw + 1.05086E-04 * (hk.temp_rwi_ch1_raw)**2 -5.41059E-08 * (hk.temp_rwi_ch1_raw)**3 + 1.58098E-11* (hk.temp_rwi_ch1_raw)**4
    hk.temp_rwi_ch2_rev = -2.28245E+02 + 1.33770E-03 * hk.temp_rwi_ch1_raw + 1.05086E-04 * (hk.temp_rwi_ch1_raw)**2 -5.41059E-08 * (hk.temp_rwi_ch1_raw)**3 + 1.58098E-11* (hk.temp_rwi_ch1_raw)**4
    hk.temp_hf_fpga_rev = -2.49225E+02 + 1.04332E-02 * hk.temp_hf_fpga_raw + 1.05301E-04 * (hk.temp_hf_fpga_raw)**2 -5.42289E-08 * (hk.temp_hf_fpga_raw)**3 + 1.58352E-11* (hk.temp_hf_fpga_raw)**4
    # ICD
    # hk.temp_rwi_ch1_rev = -2.322450E+02 + 1.337700E-03 * hk.temp_rwi_ch1_raw + 1.050860E-04 * (hk.temp_rwi_ch1_raw)**2 -5.410590E-08 * (hk.temp_rwi_ch1_raw)**3 + 1.580980E-11* (hk.temp_rwi_ch1_raw)**4
    # hk.temp_rwi_ch2_rev = -2.322450E+02 + 1.337700E-03 * hk.temp_rwi_ch2_raw + 1.050860E-04 * (hk.temp_rwi_ch2_raw)**2 -5.410590E-08 * (hk.temp_rwi_ch2_raw)**3 + 1.580980E-11* (hk.temp_rwi_ch2_raw)**4
    # hk.temp_hf_fpga_rev = -2.302250E+02 + 1.343320E-03 * hk.temp_hf_fpga_raw + 1.053010E-04 * (hk.temp_hf_fpga_raw)**2 -5.422890E-08 * (hk.temp_hf_fpga_raw)**3 + 1.583520E-11* (hk.temp_hf_fpga_raw)**4
    # Current code
    hk.temp_rwi_ch1_rev2 = -2.754000E+02 + 6.979000E-02 * hk.temp_rwi_ch1_raw + 7.553000E-05 * (hk.temp_rwi_ch1_raw)**2 -5.196000E-08 * (hk.temp_rwi_ch1_raw)**3 + 1.643000E-11* (hk.temp_rwi_ch1_raw)**4
    hk.temp_rwi_ch2_rev2 = -2.743000E+02 + 6.838000E-02 * hk.temp_rwi_ch2_raw + 7.865000E-05 * (hk.temp_rwi_ch2_raw)**2 -5.466000E-08 * (hk.temp_rwi_ch2_raw)**3 + 1.707000E-11* (hk.temp_rwi_ch2_raw)**4
    hk.temp_hf_fpga_rev2 = -2.288629E+02 - 4.686928E-02 * hk.temp_hf_fpga_raw + 1.584843E-04 * (hk.temp_hf_fpga_raw)**2 -8.207110E-08 * (hk.temp_hf_fpga_raw)**3 + 2.189507E-11* (hk.temp_hf_fpga_raw)**4

    return hk

#---------------------------------------------------------------------
# DPU HK
def juice_gethk_dpu(data, mode):
    hk = struct()
    hk.epoch = data['Epoch'][...]

    if mode == 0:
        # V1: LWYHK00064
        hk.dpu_temp = data['LWT03437_CALIBRATED'][...]
        hk.lvps_temp = data['LWT03438_CALIBRATED'][...]
        hk.lp_temp = data['LWT03439_CALIBRATED'][...]
        hk.lf_temp = data['LWT0343A_CALIBRATED'][...]
        hk.hf_temp = data['LWT0343B_CALIBRATED'][...]
        hk.scm_temp = data['LWT0343C_CALIBRATED'][...]
    else:
        # V2: LWYHK10064
        hk.dpu_temp = data['LWT04565_CALIBRATED'][...]
        hk.lvps_temp = data['LWT04566_CALIBRATED'][...]
        hk.lp_temp = data['LWT04567_CALIBRATED'][...]
        hk.lf_temp = data['LWT04568_CALIBRATED'][...]
        hk.hf_temp = data['LWT04569_CALIBRATED'][...]
        hk.scm_temp = data['LWT0456A_CALIBRATED'][...]

    return hk

#---------------------------------------------------------------------
# LVPS HK
def juice_gethk_lvps(data):

    hk = struct()
    hk.epoch = data['Epoch'][...]

    # LWYHK00080
    hk.vol_hf_33 = data['LWT03358_CALIBRATED'][...]
    hk.vol_hf_85 = data['LWT03359_CALIBRATED'][...]
    hk.cur_hf_33 = data['LWT03362_CALIBRATED'][...]
    hk.cur_hf_85 = data['LWT03363_CALIBRATED'][...]
    hk.hf_on_off = data['LWT03372'][...]
    return hk