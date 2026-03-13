#---------------------------------------------------------------------
# JUICE RPWI HF HK -- 2026/3/13
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
    elif yr_format=='HK':
        search_path = base_dir + date_str + \
            '/JUICE_LU_RPWI-*'+label+'_*V'+ver_str+'*.cdf'
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
    
    if mode == 0:       # ASW1 / LWYHK00032
        hk.v1_8             =  data['LWT03316']
        hk.rwi_on           = (data['LWT0331D']<<2) + (data['LWT0331E']<<1) + data['LWT0331F']
        hk.heater_ena       =  data['LWT03314']
        hk.temp_rwi_ch1_raw =  np.float32(data['LWT03337'][...])
        hk.temp_rwi_ch2_raw =  np.float32(data['LWT03339'][...])
        hk.temp_hf_fpga_raw =  np.float32(data['LWT0333B'][...])
    elif mode == 1:     # ASW2 / LWYHK10033
        hk.v1_8             = data['LWT04320']
        hk.rwi_on           = (data['LWT04327']<<2) + (data['LWT04328']<<1) + data['LWT04329']
        hk.heater_ena       = data['LWT04332']
        hk.temp_rwi_ch1_raw = np.float32(data['LWT04333'][...])
        hk.temp_rwi_ch2_raw = np.float32(data['LWT04334'][...])
        hk.temp_hf_fpga_raw = np.float32(data['LWT04335'][...])
    elif mode == 2:     # ASW3 /LWYHK20033
        hk.v1_8             = data['LWT04300']
        hk.rwi_on           = (data['LWT04304']<<2) + (data['LWT04305']<<1) + data['LWT04306']
        hk.heater_ena       = data['LWT04313']
        hk.temp_rwi_ch1_raw = np.float32(data['LWT04314'][...])
        hk.temp_rwi_ch2_raw = np.float32(data['LWT04315'][...])
        hk.temp_hf_fpga_raw = np.float32(data['LWT04316'][...])

    # ASW3
    hk.temp_hf_fpga = -2.47787E+02 + 4.54293E-03 * hk.temp_hf_fpga_raw + 1.12892E-04 * (hk.temp_hf_fpga_raw)**2 -5.79267E-08 * (hk.temp_hf_fpga_raw)**3 + 1.64358E-11 * (hk.temp_hf_fpga_raw)**4
    hk.temp_rwi_ch1 = -2.29287E+02 - 4.54293E-03 * hk.temp_rwi_ch1_raw + 1.12892E-04 * (hk.temp_rwi_ch1_raw)**2 -5.79267E-08 * (hk.temp_rwi_ch1_raw)**3 + 1.64358E-11 * (hk.temp_rwi_ch1_raw)**4
    hk.temp_rwi_ch2 = -2.28787E+02 - 4.54293E-03 * hk.temp_rwi_ch2_raw + 1.12892E-04 * (hk.temp_rwi_ch2_raw)**2 -5.79267E-08 * (hk.temp_rwi_ch2_raw)**3 + 1.64358E-11 * (hk.temp_rwi_ch2_raw)**4

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