"""
    JUICE RPWI HF SID23 (PSSR3 rich): L1a data list -- 2025/6/28
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
        data_name = '*HF*SID23_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_name_list = glob.glob(cdf_file)
        num_list = len(data_name_list)
        data_name_list.sort()
        for i in range(num_list):
            data_name_list[i] = os.path.split(data_name_list[i])[1]

        """
        # *** Flight data: Ver.2 ***
        # 202401
        data_name_list = ['2024/01/26/JUICE_L1a_RPWI-HF-SID23_20240126T092930_V01.cdf',    # 1.5MHz
                          '2024/01/26/JUICE_L1a_RPWI-HF-SID23_20240126T094802_V01.cdf',    # 1.5MHz
                        ]
        # 202407 -- CO2
        data_name_list = ['2024/07/06/JUICE_L1a_RPWI-HF-SID23_20240706T023200_V01.cdf',
                        '2024/07/06/JUICE_L1a_RPWI-HF-SID23_20240706T124753_V01.cdf',
                        '2024/07/06/JUICE_L1a_RPWI-HF-SID23_20240706T130407_V01.cdf',
                        ]
        # 202408 -- LEGA
        data_name_list = ['2024/08/19/JUICE_L1a_RPWI-HF-SID23_20240819T210319_V01.cdf',
                          '2024/08/19/JUICE_L1a_RPWI-HF-SID23_20240819T211916_V01.cdf',
                        ]
        data_name_list = ['2024/08/22/JUICE_L1a_RPWI-HF-SID23_20240822T024109_V01.cdf',
                        ]
        """

    else:
        # *** Ground Test - Ver.3 ***
        # 202411 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/sample-ASW3/cdf/'
        data_name_list = ['SID23_20241125-1321_PSSR3_asw3.ccs.cdf']                     # SG - 1.5MHz 10mVpp 90/0/0deg

        # *** Ground Test - Ver.2 ***
        """
        # 202310 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/sample-ASW2/cdf/old/'
        data_name_list = ['SID23_20231024-0011.ccs.cdf',
                          'SID23_20231024-0024.ccs.cdf',    # 0/0/10mVpp 
                          'SID23_20231024-0034.ccs.cdf',    # 0/0/10mVpp
                        ]
        # 202311 -- FS
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/202311_FS/cdf/'          # CDF data folder
        data_name_list = ['SID23_Seq07.cdf',
                        'SID23_Seq08.cdf',
                        'SID23_Seq09.cdf',
                        ]
        # 202405 -- dryrun check
        # TEST
        data_dir = '/Users/user/0-python/JUICE_data/CCSDS_test_v2/test_TMIDX/2405_dryrun_test/1_first_parts/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID23_20000108T045452-20000108T045711_V01___TMIDX_00000.bin.cdf',    # 400kHz  pc2_rpwi_pssr3_test_2024_05_15_14_51_46
                        'JUICE_L1a_RPWI-HF-SID23_20000108T045849-20000108T045916_V01___TMIDX_00000.bin.cdf',    # 9MHz    pc2_rpwi_pssr3_9MHz_2024_05_15_14_55_51
                        ]
        # LGA
        data_dir = '/Users/user/0-python/JUICE_data/CCSDS_test_v2/test_TMIDX/2405_dryrun_test/2_LGA-dryrun/'   
        data_name_list = ['JUICE_L1a_RPWI-HF-SID23_20000108T060822-20000108T061002_V01___TMIDX_00000.bin.cdf',    # 9MHz    pc2_LGA-dryrun_RPW-SEQ-08b-1_2024_05_15_16_05_11
                        'JUICE_L1a_RPWI-HF-SID23_20000108T061805-20000108T062005_V01___TMIDX_00000.bin.cdf',    # 9MHz    pc2_LGA-dryrun_RPW-SEQ-08b-2_2024_05_15_16_14_58/TM00
                        'JUICE_L1a_RPWI-HF-SID23_20000108T062025-20000108T062245_V01___TMIDX_00001.bin.cdf',    # 9MHz    pc2_LGA-dryrun_RPW-SEQ-08b-2_2024_05_15_16_14_58/TM01
                        'JUICE_L1a_RPWI-HF-SID23_20000108T062305-20000108T062525_V01___TMIDX_00002.bin.cdf',    # 9MHz    pc2_LGA-dryrun_RPW-SEQ-08b-2_2024_05_15_16_14_58/TM02
                        'JUICE_L1a_RPWI-HF-SID23_20000108T062605-20000108T062725_V01___TMIDX_00003.bin.cdf',    # 9MHz    pc2_LGA-dryrun_RPW-SEQ-08b-2_2024_05_15_16_14_58/TM03
                        'JUICE_L1a_RPWI-HF-SID23_20000108T063854-20000108T064114_V01___TMIDX_00000.bin.cdf',    # 400kHz  pc2_LGA-dryrun_RPW-SEQ-08a-2_2024_05_15_16_35_43/TM00
                        'JUICE_L1a_RPWI-HF-SID23_20000108T064154-20000108T064314_V01___TMIDX_00001.bin.cdf',    # 400kHz  pc2_LGA-dryrun_RPW-SEQ-08a-2_2024_05_15_16_35_43/TM01
                        ]
        """

    print(data_dir)
    print(data_name_list)
    return data_dir, data_name_list