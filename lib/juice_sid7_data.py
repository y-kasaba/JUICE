"""
    JUICE RPWI HF SID7 (PSSR3 Surv): L1a data list -- 2025/7/5
"""
import glob
import os
os.environ["CDF_LIB"] = "/Applications/cdf/cdf39_1-dist/lib"

def datalist(date_str, ver_str):
    """
    input:  date_str        yyyymmdd: group read    others: file list
    return: data_dir
            data_name_list
    """
    yr_format = date_str[0:2]
    yr_str    = date_str[0:4]
    mn_str    = date_str[4:6]
    dy_str    = date_str[6:8]
    
    # *** Group read
    if yr_format=='20':
        base_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/'         # ASW2
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        data_name = '*HF*SID07_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_name_list = glob.glob(cdf_file)
        num_list = len(data_name_list)
        data_name_list.sort()
        for i in range(num_list):
            data_name_list[i] = os.path.split(data_name_list[i])[1]

    else:
        # *** Ground Test - Ver.3 ***
        # 202411 -- SAMPLE -- SG: 1.75MHz 100mVpp 90/0/0deg
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID7_20000101T000512-20000101T000512_V01___SID07-23_20241125-1321_PSSR3_asw3.ccs.cdf']    

    print(data_dir)
    print(data_name_list)
    return data_dir, data_name_list