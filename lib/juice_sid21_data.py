"""
    JUICE RPWI HF SID21 (PSSR1 rich): L1a data list -- 2025/7/21
"""
import glob
import os
os.environ["CDF_LIB"] = "/Applications/cdf/cdf39_1-dist/lib"

def datalist(date_str, ver_str):
    """
    input:  date_str        yyyymmdd: group read    others: file list
    return: data_dir
            data_list
    """
    yr_format = date_str[0:2]
    yr_str    = date_str[0:4]
    mn_str    = date_str[4:6]
    dy_str    = date_str[6:8]
    
    # *** Group read
    if yr_format=='20':
        base_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/'         # ASW2
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        data_name = '*HF*SID21_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    else:
        # *** Ground Test - Ver.3 ***
        # 202411 -- SAMPLE -- SG 1.75MHz, 100mVpp  --- comp0 & comp1
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = [# 'JUICE_L1a_RPWI-HF-SID21_20000101T000149-20000101T000219_V01___SID05-21_20241125-1341_PSSR1_comp0_asw3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID21_20000101T000100-20000101T000200_V01___SID05-21_20241125-1335_PSSR1_comp1_asw3.ccs.cdf',
                          ] 
        
        # *** Ground Test - Ver.2 ***
        # 202311 -- SAMPLE -- SG 1.55MHz, 10mVpp, [90.0, 0.0, 0.0]    20231117-1611: with RFI-mitigation
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/old/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID21_20000101T002245-20000101T002330_V01___SID05-21_20231024-0046.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID21_20000101T000044-20000101T000144_V01___SID05-21_20231117-1611.ccs.cdf',
                          #'JUICE_L1a_RPWI-HF-SID21_20000101T000128-20000101T000213_V01___SID05-21_20231117-1603.ccs.cdf',
                        ]
        """

        # 202503 -- Flight
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = ['JUICE_L1a_RPWI-HF-SID21_20250331T033821-20250331T034222_V01___RPR2_62000007_2025.091.16.40.05.450.cdf',
                        ]
        """

    print(data_dir)
    print(data_list)
    return data_dir, data_list