"""
    JUICE RPWI HF SID6/22 (PSSR2): L1a data list -- 2025/6/24
"""
import glob
import os
os.environ["CDF_LIB"] = "/Applications/cdf/cdf39_1-dist/lib"

def datalist(date_str, ver_str, sid):
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
        if sid == 6:  data_name = '*HF*SID6_*'+ver_str+'.cdf'
        else:         data_name = '*HF*SID22_*'+ver_str+'.cdf'    
        cdf_file = data_dir + data_name

        data_name_list = glob.glob(cdf_file)
        num_list = len(data_name_list)
        data_name_list.sort()
        for i in range(num_list):
            data_name_list[i] = os.path.split(data_name_list[i])[1]

    elif sid == 22:
		# <<< SID-22 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202411 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/sample-ASW3/cdf/'
        data_name_list = ['SID22_20241125-1325_PSSR2_asw3.ccs.cdf']     # SG - 1.5MHz 10mVpp 90/0/0deg

        # *** Flight data: Ver.2 ***
        """
        # 20240126
        data_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/'
        data_name_list = ['2024/01/26/JUICE_L1a_RPWI-HF-SID22_20240126T091728_V01.cdf',
                         ]
        """

    else:
		# <<< SID-06 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202411 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/sample-ASW3/cdf/'
        data_name_list = ['SID06_20241125-1325_PSSR2_asw3.ccs.cdf']                   # SG - 1.5MHz 10mVpp 90/0/0deg

        # *** Flight data: Ver.2 ***
        # 20240126
        """
        data_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/'
        data_name_list = ['2024/01/26/JUICE_L1a_RPWI-HF-SID6_20240126T091728_V01.cdf']"
        """

    print(data_dir)
    print(data_name_list)
    return data_dir, data_name_list