"""
    JUICE RPWI HF SID2 (RAW): L1a data list -- 2025/7/21
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
        data_name = '*HF*SID2_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    else:
        # *** Ground Test - Ver.3 ***
        # 202411 -- SAMPLE -- SG - 1.75MHz 100mVpp 90/0/0deg
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID2_20000101T000129-20000101T000229_V01___SID02_20241125-1316_asw3.ccs.cdf']
        """

        # *** Ground Test - Ver.2 ***
        """
        # 202410 -- SAMPLE -- SG - 1.0MHz 10mVpp 90/0/0deg
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID2_20000101T000154-20000101T000454_V01___SID02_20241021-1026.ccs.cdf',                     
                          'old/JUICE_L1a_RPWI-HF-SID2_20000101T000413-20000101T000513_V01___SID02_20231117-1607.ccs.cdf',
                          'old/JUICE_L1a_RPWI-HF-SID2_20000101T001617-20000101T001647_V01___SID02_20231007-0349.ccs.cdf',
                         ]
        """

        # *** Flight - Ver.2 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID2_20240125T112327-20240125T113141_V01___RPR1_52000011_2024.025.15.57.21.441.cdf',    # f_max: 44888.625
                     #'JUICE_L1a_RPWI-HF-SID2_20240125T152238-20240125T152330_V01___RPR1_52000012_2024.025.16.07.08.425.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20240822T023129-20240822T023713_V01___RPR1_52000003_2024.235.03.19.13.483.cdf',    # f_max: 44813.
                     #'JUICE_L1a_RPWI-HF-SID2_20240822T023715-20240822T023953_V01___RPR1_52000004_2024.236.08.13.31.519.cdf',
                     'JUICE_L1a_RPWI-HF-SID2_20250331T005104-20250331T233757_V01___RPR1_52000005_2025.091.16.38.56.448.cdf',    # CAL
        ]
        """
        """

        # [MEMO: ASW1 data]  *** Flight - Ver.1
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW1/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID2_20230419T135855-20230419T141235_V01___RPR1_52000000_2023.109.16.17.21.607.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230419T141237-20230419T141408_V01___RPR1_52000001_2023.109.17.51.54.600.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230530T100330-20230530T100930_V01___RPR1_52000010_2023.150.10.40.53.663.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230530T100932-20230530T100942_V01___RPR1_52000011_2023.150.10.41.53.508.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230601T120804-20230601T120902_V01___RPR1_52000015_2023.152.12.32.12.471.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230601T121440-20230601T121538_V01___RPR1_52000016_2023.152.13.14.38.473.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230601T122143-20230601T122241_V01___RPR1_52000017_2023.152.13.55.02.539.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230601T122712-20230601T122810_V01___RPR1_52000018_2023.152.14.35.37.467.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230601T123421-20230601T123519_V01___RPR1_52000019_2023.152.15.15.55.483.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T090437-20230712T093851_V01___RPR1_52000001_2023.193.10.24.57.479.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T093945-20230712T101359_V01___RPR1_52000002_2023.194.08.38.36.474.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T101453-20230712T104151_V01___RPR1_52000003_2023.194.10.18.44.478.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T104153-20230712T232410_V01___RPR1_52000004_2023.194.11.15.35.498.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T232412-20230712T235200_V01___RPR1_52000005_2023.195.09.10.17.486.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230712T235202-20230713T001858_V01___RPR1_52000006_2023.195.10.28.57.506.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T001900-20230713T004648_V01___RPR1_52000007_2023.195.11.42.37.540.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T004652-20230713T011346_V01___RPR1_52000008_2023.195.12.39.02.479.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T011440-20230713T014138_V01___RPR1_52000009_2023.195.13.03.08.470.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T014140-20230713T020928_V01___RPR1_5200000A_2023.195.13.25.22.477.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T020932-20230713T023721_V01___RPR1_5200000B_2023.195.13.47.46.500.cdf',
                     # 'JUICE_L1a_RPWI-HF-SID2_20230713T023723-20230713T030419_V01___RPR1_5200000C_2023.195.14.10.35.574.cdf',
                     'JUICE_L1a_RPWI-HF-SID2_20230713T030513-20230713T033211_V01___RPR1_5200000D_2023.195.14.33.20.470.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T033213-20230713T040003_V01___RPR1_5200000E_2023.195.14.55.41.474.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T040005-20230713T042755_V01___RPR1_5200000F_2023.195.15.18.00.472.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T042757-20230713T045453_V01___RPR1_52000010_2023.195.15.40.11.470.cdf',
                     #'JUICE_L1a_RPWI-HF-SID2_20230713T045547-20230713T050921_V01___RPR1_52000011_2023.195.16.14.20.468.cdf',
                    ]
        """

    print(data_dir)
    print(data_list)
    return data_dir, data_list