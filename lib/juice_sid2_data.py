"""
    JUICE RPWI HF SID2 (RAW): L1a data list -- 2025/03/31
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
        base_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/'         # ASW2
        # if yr_str == '2023':
        #    base_dir = '/Users/user/0-python/JUICE_data/Data-CDF/'             # ASW1 -- DATA in IRFU's server has old format.
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        data_name = '*HF*SID2_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_name_list = glob.glob(cdf_file)
        num_list = len(data_name_list)
        data_name_list.sort()
        for i in range(num_list):
            data_name_list[i] = os.path.split(data_name_list[i])[1]

    else:
        # *** Ground Test - Ver.3 ***
        """
        # 202412 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/sample-ASW3/cdf/'
        data_name_list = ['SID02_20241021-1026-SID2.ccs.cdf']                 # SG - 1.5MHz 10mVpp 90/0/0deg
        """

        # *** Flight - Ver.2 ***
        """
        data_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/'
        # 202401
        data_name_list = ['2024/01/25/JUICE_L1a_RPWI-HF-SID2_20240125T112327_V01.cdf']     # 128   CAL
        # 202408
        data_name_list = [#'2024/08/22/JUICE_L1a_RPWI-HF-SID2_20240822T023129_V01.cdf',    # 128   1st packet -- error
                          '2024/08/22/JUICE_L1a_RPWI-HF-SID2_20240822T023715_V01.cdf',     # 128   CAL
                         ]
        """

        # *** Ground Test - Ver.2 ***
        # 202310 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/sample-ASW2/cdf/old2/'
        data_name_list = ['SID02_20231007-0349.ccs.cdf',                       # SG - 1.0MHz 10mVpp 90/0/0deg
                          'SID02_20231117-1607.ccs.cdf',                       # SG - 1.5MHz 10mVpp 90/0/0deg 
                         ]
        """
        # 202312 -- Checkout
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/202312_C/cdf/'
        data_name_list = ['SID02_RPWI_HF_FFT_00000.cdf',
                          'SID02_RPWI_HF_FFT_00001.cdf',
                          'SID02_RPWI_HF_FFT_00002.cdf',                        # CAL
                          'SID02_RPWI_HF_FFT_00003.cdf',                        # CAL
                          'SID02_RPWI_HF_FFT_00004.cdf',
                          'SID02_RPWI_S8_272.cdf',
                        ]
        # 202405 -- dryrun      [Num-Frequency: 202    Length: 128     Frequency, width, step (kHz): 191.0 - 44813.0 222.0 222.0]
        data_dir = '/Users/user/0-python/JUICE_data/CCSDS_test_v2/test_TMIDX/2405_dryrun_test/1_first_parts/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID2_20000108T044504-20000108T044719_V01___TMIDX_00000.bin.cdf',
                        ]
        """

        # [MEMO: ASW1 data]  *** Flight - Ver.1
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/2023/'
        # *** 20230419 ***
        data_name_list = ['04/19/JUICE_L1a_RPWI-HF-SID2_20230419T135855.cdf',
                          '04/19/JUICE_L1a_RPWI-HF-SID2_20230419T141237.cdf',
                        ]
        # *** 202305-06 ***
        data_name_list = ['05/30/JUICE_L1a_RPWI-HF-SID2_20230530T100330.cdf',     # CAL
                          #'05/30/JUICE_L1a_RPWI-HF-SID2_20230530T100932.cdf',
                          #'06/01/JUICE_L1a_RPWI-HF-SID2_20230601T120804.cdf',
                          #'06/01/JUICE_L1a_RPWI-HF-SID2_20230601T121440.cdf',
                          #'06/01/JUICE_L1a_RPWI-HF-SID2_20230601T122143.cdf',
                          #'06/01/JUICE_L1a_RPWI-HF-SID2_20230601T122712.cdf',
                          #'06/01/JUICE_L1a_RPWI-HF-SID2_20230601T123421.cdf',
                         ]
        # *** 20230712-13 ***
        data_name_list = ['07/12/JUICE_L1a_RPWI-HF-SID2_20230712T090437.cdf',
                          '07/12/JUICE_L1a_RPWI-HF-SID2_20230712T093945.cdf',
                          '07/12/JUICE_L1a_RPWI-HF-SID2_20230712T101453.cdf',
                          '07/12/JUICE_L1a_RPWI-HF-SID2_20230712T104153.cdf',
                          '07/12/JUICE_L1a_RPWI-HF-SID2_20230712T232412.cdf',
                          '07/12/JUICE_L1a_RPWI-HF-SID2_20230712T235202.cdf',     # type-III
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T001900.cdf',     # type-III
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T004652.cdf',
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T011440.cdf',
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T014140.cdf',
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T020932.cdf',
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T023723.cdf',
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T030513.cdf',
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T033213.cdf',
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T040005.cdf',
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T042757.cdf',
                          '07/13/JUICE_L1a_RPWI-HF-SID2_20230713T045547.cdf',
                         ]
        """

        # [MEMO: ASW1 data]  *** Ground Test - Ver.1 ***
        """
        # *** 202105 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202105/'
        data_name_list = ['SID2_20210531_SCPFM_PTR_RPWI_2_day3_xid32770.cdf',
                        'SID2_20210531_SCPFM_PTR_RPWI_2_day3_xid32774.cdf',
                        'SID2_20210531_SCPFM_PTR_RPWI_2_day3_xid32775.cdf',
                        'SID2_20210531_SCPFM_PTR_RPWI_2_day3_xid32776.cdf',
                        'SID2_20210531_SCPFM_PTR_RPWI_2_day3_xid32777.cdf',
                        'SID2_20210531_SCPFM_PTR_RPWI_2_day3_xid32778.cdf',
                        ]
        data_name_list = ['SID2_20210531_SCPFM_PTR_RPWI_2_day5_xid32772.cdf',
                        'SID2_20210531_SCPFM_PTR_RPWI_2_day5_xid32773.cdf',
                        'SID2_20210531_SCPFM_PTR_RPWI_2_day5_xid32774.cdf',
                        'SID2_20210531_SCPFM_PTR_RPWI_2_day5_xid32775.cdf',
                        'SID2_20210531_SCPFM_PTR_RPWI_2_day5_xid32776.cdf',
                        'SID2_20210531_SCPFM_PTR_RPWI_2_day5_xid32777.cdf',
                        ]
        # *** 202106 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202106/'
        data_name_list = ['SID2_SCTBTV_Phase11_xid32831.cdf',
                        'SID2_SCTBTV_Phase11_xid32832.cdf',
                        'SID2_SCTBTV_Phase11_xid32833.cdf',
                        'SID2_SCTBTV_Phase11_xid32834.cdf',
                        ]
        data_name_list = ['SID2_SCTBTV_Phase13_xid32844.cdf',
                        'SID2_SCTBTV_Phase13_xid32845.cdf',
                        'SID2_SCTBTV_Phase13_xid32846.cdf',
                        ]
        # *** 202111 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202111/'
        data_name_list = ['SID2_SCPFM_PTR_RPWI_delta.RPWI_SCM_TEST_xid32770.cdf',
                        'SID2_SCPFM_PTR_RPWI_delta.RPWI_SCM_TEST_xid32771.cdf',
                        'SID2_SCPFM_PTR_RPWI_delta.RPWI_SCM_TEST_xid32772.cdf',
                        ]
        data_name_list = ['SID2_SCPFM_RPWI_30c_xid32776.cdf',
                        'SID2_SCPFM_RPWI_30c_xid32777.cdf',
                        'SID2_SCPFM_RPWI_30c_xid32778.cdf',
                        'SID2_SCPFM_RPWI_30c_xid32779.cdf',
                        ]
        # *** 202207 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202207/'
        data_name_list = ['SID2_SCPFM_RPWI_30c_xid32776.cdf',
                        'SID2_SCPFM_RPWI_30c_xid32777.cdf',
                        'SID2_SCPFM_RPWI_30c_xid32778.cdf',
                        'SID2_SCPFM_RPWI_30c_xid32779.cdf',
                        ]
        # *** 202208 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202208/'
        data_name_list = ['SID2_20220824_HF-FFT-rerun_xid32791.cdf',
                        'SID2_20220824_HF-FFT-rerun_xid32792.cdf',
                        'SID2_20220824_HF-FFT-rerun_xid32793.cdf',
                        ]
        """

    print(data_dir)
    print(data_name_list)
    return data_dir, data_name_list