"""
    JUICE RPWI HF SID4/20 (Burst): L1a data list -- 2025/7/8
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
        if sid == 4:  data_name = '*HF*SID4_*'+ver_str+'.cdf'
        else:         data_name = '*HF*SID20_*'+ver_str+'.cdf'    
        cdf_file = data_dir + data_name

        data_name_list = glob.glob(cdf_file)
        num_list = len(data_name_list)
        data_name_list.sort()
        for i in range(num_list):
            data_name_list[i] = os.path.split(data_name_list[i])[1]

    elif sid == 20:     # <<< SID-20 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202411 -- SAMPLE  1.75MHz  (100mVpp, 10mVpp, 100mVpp, 10mVpp, 100mVpp)  (0,0,0),(90,0,0),(0,90,0),(0,0,90)
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_name_list = [#'JUICE_L1a_RPWI-HF-SID20_20000101T000057-20000101T000114_V01___SID04-20_20241125-1517_RadioBurst_comp0_asw3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID20_20000101T000214-20000101T000228_V01___SID04-20_20241125-1520_RadioBurst_comp1_asw3.ccs.cdf',
                          ]                   # SG - 1.5MHz 10mVpp 90/0/0deg
        # *** Ground Test - Ver.2 ***
        # 202310 -- SAMPLE
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID20_20000101T000102-20000101T000123_V01___SID04-20_20241016-1156-Radioburst.ccs.cdf',
                          'old/JUICE_L1a_RPWI-HF-SID20_20000101T001825-20000101T001852_V01___SID04-20_20231024-0042.ccs.cdf',
                          'old/JUICE_L1a_RPWI-HF-SID20_20000101T000046-20000101T000127_V01___SID04-20-comp0-20231117-1529.ccs.cdf',
                          'old/JUICE_L1a_RPWI-HF-SID20_20000101T000050-20000101T000147_V01___SID04-20-comp1-20231117-1532.ccs.cdf',
                         ]
        """
        # *** Flight data: Ver.2 ***
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID20_20240126T113714-20240126T114759_V01___RPR2_62000007_2024.026.12.58.18.441.cdf',
                          'JUICE_L1a_RPWI-HF-SID20_20240126T114800-20240126T123719_V01___RPR2_62000008_2024.026.13.54.26.469.cdf',
                          'JUICE_L1a_RPWI-HF-SID20_20240706T121424-20240706T125428_V01___RPR2_62000002_2024.190.19.50.21.637.cdf',
                          'JUICE_L1a_RPWI-HF-SID20_20240819T203013-20240819T210936_V01___RPR2_62000004_2024.235.10.15.04.518.cdf',
                         ]
        """

    else:     # <<< SID-4 test datas >>>
        # *** Ground Test - Ver.3 ***
        # 202411 -- SAMPLE  0.2-2MHz, 10mVpp, 0/90/0deg
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_name_list = [#'JUICE_L1a_RPWI-HF-SID4_20000101T000106-20000101T000106_V01___SID04-20_20241125-1517_RadioBurst_comp0_asw3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID4_20000101T000226-20000101T000226_V01___SID04-20_20241125-1520_RadioBurst_comp1_asw3.ccs.cdf',
                          ]
        # *** Ground Test - Ver.2 ***
        # 202310 -- SAMPLE
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID4_20000101T000112-20000101T000123_V01___SID04-20_20241016-1156-Radioburst.ccs.cdf',
                          'old/JUICE_L1a_RPWI-HF-SID4_20000101T000057-20000101T000119_V01___SID04-20-comp0-20231117-1529.ccs.cdf',
                          'old/JUICE_L1a_RPWI-HF-SID4_20000101T000100-20000101T000144_V01___SID04-20-comp1-20231117-1532.ccs.cdf',
                          'old/JUICE_L1a_RPWI-HF-SID4_20000101T001837-20000101T001848_V01___SID04-20_20231024-0042.ccs.cdf',
                         ]
        """
        # *** Flight data: Ver.2 ***
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID4_20240126T113727-20240126T123719_V01___RPR1_52000013_2024.026.13.22.14.423.cdf',
                          'JUICE_L1a_RPWI-HF-SID4_20240706T121439-20240706T125422_V01___RPR1_52000002_2024.190.14.59.43.630.cdf',
                          'JUICE_L1a_RPWI-HF-SID4_20240819T203025-20240819T210933_V01___RPR1_52000003_2024.233.02.43.43.102.cdf',
                         ]
        """

    print(data_dir)
    print(data_name_list)
    return data_dir, data_name_list