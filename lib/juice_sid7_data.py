"""
    JUICE RPWI HF SID4/20 (Burst): L1a data list -- 2024/10/11
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
        base_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/'         # ASW2
        # if yr_str == '2023':
        #    base_dir = '/Users/user/0-python/JUICE_data/Data-CDF/'             # ASW1 -- DATA in IRFU's server has old format.
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        if sid == 4:  data_name = '*HF*SID4_*'+ver_str+'.cdf'
        else:         data_name = '*HF*SID20_*'+ver_str+'.cdf'    
        cdf_file = data_dir + data_name

        data_name_list = glob.glob(cdf_file)
        num_list = len(data_name_list)
        data_name_list.sort()
        for i in range(num_list):
            data_name_list[i] = os.path.split(data_name_list[i])[1]

    else:
        # *** Flight data: Ver.2 ***
        """
        # 20240126
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/'
        data_name_list = ['2024/01/26/JUICE_L1a_RPWI-HF-SID4_20240126T113727_V01.cdf' ]
        data_name_list = ['2024/01/26/JUICE_L1a_RPWI-HF-SID20_20240126T113714_V01.cdf',
                          '2024/01/26/JUICE_L1a_RPWI-HF-SID20_20240126T114800_V01.cdf',
                         ]
        # 202407 -- CO2
        data_name_list = ['2024/07/06/JUICE_L1a_RPWI-HF-SID4_20240706T121439_V01.cdf']
        data_name_list = ['2024/07/06/JUICE_L1a_RPWI-HF-SID20_20240706T121424_V01.cdf']
        # 202408 -- CO2
        data_name_list = ['2024/08/19/JUICE_L1a_RPWI-HF-SID4_20240819T203025_V01.cdf']
        data_name_list = ['2024/08/19/JUICE_L1a_RPWI-HF-SID20_20240819T203013_V01.cdf']
        """

        # *** Ground Test - Ver.2 ***
        """
        # 202310 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/sample/cdf/'
        data_name_list = [#'SID04_20231024-0042.cdf',
                          'SID04-comp0-20231117-1529.cdf',          # 10/10/0mVpp, 0/90/0deg
                          'SID04-comp1-20231117-1532.cdf',          # 10/10/0mVpp, 0/90/0deg
                         ]
        data_name_list = [#'SID20_20231024-0042.cdf',
                          #'SID20-comp0-20231117-1529.cdf',          # 10/10/0mVpp, 0/90/0deg
                          'SID20-comp1-20231117-1532.cdf',          # 10/10/0mVpp, 0/90/0deg
                         ]
        # 202310 -- FS
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/202311_FS/cdf/'
        data_name_list = ['SID04_Seq01.cdf',
                          'SID04_Seq02.cdf',
                          'SID04_Seq16.cdf',
                          'SID04_Seq18.cdf',
                          'SID04_Seq19.cdf',
                          'SID04_Seq20.cdf',
                         ]
        sid = 20
        data_name_list = ['SID20_Seq01.cdf',
                          'SID20_Seq02.cdf',
                          'SID20_Seq16.cdf',
                          'SID20_Seq18.cdf',
                          'SID20_Seq19.cdf',
                          'SID20_Seq20.cdf',
                         ]
        # 202312 -- Checkout
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/202312_C/cdf/'
        data_name_list = ['SID4_RPWI_NEWv2_SCI.cdf']
        data_name_list = ['SID20_RPWI_NEWv2_SCI.cdf']
        # 202402 -- Ver.3
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/IRFU/cdf/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID20_20240201.cdf']
        # 202405 -- dryrun check
        data_dir = '/Users/user/0-python/JUICE_data/CCSDS_test_v2/test_TMIDX/2405_dryrun_test/2_LGA-dryrun/'   
        data_name_list = ['JUICE_L1a_RPWI-HF-SID4_20000108T053334-20000108T054137_V01___TMIDX_00000.bin.cdf',   # pc2_LGA-dryrun_RPW-SEQ-01a-1_2024_05_15_15_30_16/TM00
                          'JUICE_L1a_RPWI-HF-SID4_20000108T054148-20000108T054316_V01___TMIDX_00001.bin.cdf',   # pc2_LGA-dryrun_RPW-SEQ-01a-1_2024_05_15_15_30_16/TM01
                          'JUICE_L1a_RPWI-HF-SID4_20000108T061111-20000108T061524_V01___TMIDX_00000.bin.cdf',   # pc2_LGA-dryrun_RPW-SEQ-01a-2_2024_05_15_16_07_58
                         ]
        data_name_list = ['JUICE_L1a_RPWI-HF-SID20_20000108T053322-20000108T054141_V01___TMIDX_00000.bin.cdf',  # pc2_LGA-dryrun_RPW-SEQ-01a-1_2024_05_15_15_30_16/TM00
                          'JUICE_L1a_RPWI-HF-SID20_20000108T054142-20000108T054318_V01___TMIDX_00001.bin.cdf',  # pc2_LGA-dryrun_RPW-SEQ-01a-1_2024_05_15_15_30_16/TM01
                          'JUICE_L1a_RPWI-HF-SID20_20000108T061058-20000108T061531_V01___TMIDX_00000.bin.cdf',  # pc2_LGA-dryrun_RPW-SEQ-01a-2_2024_05_15_16_07_58
                         ]
        """

    print(data_dir)
    print(data_name_list)
    return data_dir, data_name_list