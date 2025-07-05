"""
    JUICE RPWI HF SID23 (PSSR3 rich): L1a data list -- 2025/7/5
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
        base_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/'
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        data_name = '*HF*SID23_*'+ver_str+'.cdf'
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
        data_name_list = ['JUICE_L1a_RPWI-HF-SID23_20000101T000512-20000101T000512_V01___SID07-23_20241125-1321_PSSR3_asw3.ccs.cdf']    
        """
        """

        """
        # *** Ground Test - Ver.2 ***
        # 202310 -- SAMPLE -- SG: 0/0/10mVpp 
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/old/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID23_20000101T000322-20000101T000322_V01___SID07-23_20231024-0011.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20000101T000047-20000101T000047_V01___SID07-23_20231024-0024.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20000101T001030-20000101T001030_V01___SID07-23_20231024-0034.ccs.cdf',
                         ]
        """

        # *** Flight - Ver.2 ***
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID23_20240126T092930-20240126T094732_V01___RPR2_62000006_2024.026.11.53.48.449.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20240126T094802-20240126T100504_V01___RPR2_62000007_2024.026.12.58.18.441.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20240706T023200-20240706T023440_V01___RPR2_62000001_2024.190.16.56.50.659.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20240706T124753-20240706T130347_V01___RPR2_62000002_2024.190.19.50.21.637.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20240706T130407-20240706T130904_V01___RPR2_62000003_2024.190.22.47.44.640.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20240819T210319-20240819T211856_V01___RPR2_62000004_2024.235.10.15.04.518.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20240819T211916-20240819T212356_V01___RPR2_62000005_2024.235.12.58.11.564.cdf',
                          'JUICE_L1a_RPWI-HF-SID23_20240822T024109-20240822T024134_V01___RPR2_62000006_2024.236.10.07.45.514.cdf',
                        ]
        """


    print(data_dir)
    print(data_name_list)
    return data_dir, data_name_list