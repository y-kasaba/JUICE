"""
    JUICE RPWI HF SID3 (Full): L1a data list -- 2024/10/19
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
        base_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/'
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        data_name = '*HF*SID3_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_name_list = glob.glob(cdf_file)
        num_list = len(data_name_list)
        data_name_list.sort()
        for i in range(num_list):
            data_name_list[i] = os.path.split(data_name_list[i])[1]

    else:
        # *** Flight data: Ver.2 ***
        """
        # 202401
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/2024/01/26/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240126T083835_V01.cdf',
                        ]
        # 202407
        data_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/2024/07/01/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240701T011127_V01.cdf',
                        ]
        data_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/2024/07/06/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240706T121009_V01.cdf',
                        'JUICE_L1a_RPWI-HF-SID3_20240706T175202_V01.cdf',
                        ]
        # 202408-09  LEGA
        data_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/2024/08/19/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240819T202636_V01.cdf']
        data_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/2024/08/20/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240820T180734_V01.cdf']
        data_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/2024/08/22/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240822T095914_V01.cdf']         # all CAL
        data_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/2024/08/23/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240823T035818_V01.cdf']
        data_dir = '/Users/user/Dropbox-Univ/data/data-JUICE/datasets/2024/09/09/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240909T093241_V01.cdf']
        """

        # *** Ground Test - Ver.3 ***
        """
        # 202410 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/sample/cdf/'
        data_name_list = [# 'SID03-3ch-comp1-20241014-2138.cdf',      # 10/10/10mV, 90/0/0deg,  1.55MHz
                          # 'SID03-3ch-comp2-20241014-1132.cdf',      # 10/10/10mV, 90/0/0deg,  1.55MHz
                         ]
        """

        # *** Ground Test - Ver.2 ***
        # 202310 -- SAMPLE
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/sample/cdf/'
        data_name_list = [#'SID03_20231024-0036.cdf',                # 10/10/10mV, 0/90/0deg,  1.55MHz
                          #'SID03-2ch-comp0-20231117-1438.cdf',      # 10/10/10mV, 90/0/0deg,  1.55MHz
                          #'SID03-2ch-comp1-20231117-1448.cdf',      # 10/10/10mV, 90/0/0deg,  1.55MHz
                          #'SID03-2ch-comp2-20231117-1500.cdf',      # 10/10/10mV, 90/0/0deg,  1.55MHz
                          # 'SID03-3ch-comp0-20231117-1424.cdf',      # 10/10/10mV, 90/0/0deg,  1.55MHz
                          # 'SID03-3ch-comp1-20231117-1418.cdf',      # 10/10/10mV, 90/0/0deg,  1.55MHz
                          'SID03-3ch-comp2-20231117-1429.cdf',      # 10/10/10mV, 90/0/0deg,  1.55MHz
                          #'SID03-3ch-comp3-20231117-1432.cdf',      # 10/10/10mV, 90/0/0deg,  1.55MHz
                         ]
        """
        # 202310 -- FS
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/202311_FS/cdf/'
        data_name_list = ['SID03_Seq03.cdf',
                        'SID03_Seq04.cdf',
                        'SID03_Seq10.cdf',
                        'SID03_Seq11.cdf',
                        'SID03_Seq12.cdf',
                        'SID03_Seq13.cdf',
                        'SID03_Seq15.cdf',
                        'SID03_Seq17.cdf',
                        'SID03_Seq14.cdf',
                        ]
        # 202401 -- ErrorCheck
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/202401_FS/cdf/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_comp2.cdf',
                        ]
        # 202405 -- dryrun check
        # TEST
        data_dir = '/Users/user/0-python/JUICE_data/CCSDS_test_v2/test_TMIDX/2405_dryrun_test/1_first_parts/'
        # COMP1->2, 2->1
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000108T040602-20000108T041954_V01___TMIDX_00000.bin.cdf',  # pc2_rpwi_hf_SID3_without_masking_2024_05_15_14_02_53
                        ]
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000108T042923-20000108T044315_V01___TMIDX_00000.bin.cdf',  # pc2_rpwi_hf_SID3_with_masking_2024_05_15_14_26_24
                        ]
        # COMP2
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000108T050103-20000108T051303_V01___TMIDX_00000.bin.cdf',  # pc2_SC_roll_RPW-SEQ-12i-1-Stack_RPWI_2_2024_05_15_14_57_41/TM00
                        'JUICE_L1a_RPWI-HF-SID3_20000108T051318-20000108T051533_V01___TMIDX_00001.bin.cdf',  # pc2_SC_roll_RPW-SEQ-12i-1-Stack_RPWI_2_2024_05_15_14_57_41/TM01
                        ]
        # COMP
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000108T051649-20000108T052219_V01___TMIDX_00000.bin.cdf',  # pc2_RPWI_combined-Stack_RPWI_3_2024_05_15_15_13_36
                        ]
        #
        # LGA: COMP-1
        data_dir = '/Users/user/0-python/JUICE_data/CCSDS_test_v2/test_TMIDX/2405_dryrun_test/2_LGA-dryrun/'   
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000108T052829-20000108T053159_V01___TMIDX_00000.bin.cdf',  # pc2_LGA-dryrun_RPW-SEQ-13a-1_2024_05_15_15_25_20
                        'JUICE_L1a_RPWI-HF-SID3_20000108T054433-20000108T055503_V01___TMIDX_00000.bin.cdf',  # pc2_LGA-dryrun_RPW-SEQ-13a-2_2024_05_15_15_41_26/TM00
                        'JUICE_L1a_RPWI-HF-SID3_20000108T055533-20000108T060533_V01___TMIDX_00001.bin.cdf',  # pc2_LGA-dryrun_RPW-SEQ-13a-2_2024_05_15_15_41_26/TM01
                        'JUICE_L1a_RPWI-HF-SID3_20000108T060603-20000108T060703_V01___TMIDX_00002.bin.cdf',  # pc2_LGA-dryrun_RPW-SEQ-13a-2_2024_05_15_15_41_26/TM02
                        'JUICE_L1a_RPWI-HF-SID3_20000108T064409-20000108T064839_V01___TMIDX_00000.bin.cdf',  # pc2_LGA-dryrun_RPW-SEQ-13b_2024_05_15_16_40_53
                        ]
        # EGA: COMP-1 & -2
        data_dir = '/Users/user/0-python/JUICE_data/CCSDS_test_v2/test_TMIDX/2405_dryrun_test/3_EGA-dryrun/'   
        # COMP-2
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000108T065600-20000108T065800_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-04a_2024_05_15_16_52_23
                        'JUICE_L1a_RPWI-HF-SID3_20000108T065858-20000108T070058_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-04b-1_2024_05_15_16_55_43
                        'JUICE_L1a_RPWI-HF-SID3_20000108T070151-20000108T070351_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-04c_2024_05_15_16_58_39
                        'JUICE_L1a_RPWI-HF-SID3_20000108T070445-20000108T070645_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-04b-2_2024_05_15_17_01_40
                        'JUICE_L1a_RPWI-HF-SID3_20000108T070750-20000108T070950_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-04d_2024_05_15_17_04_35
                        ]
        # COMP-1
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000108T071058-20000108T071258_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-12a-1_2024_05_15_17_07_46
                        'JUICE_L1a_RPWI-HF-SID3_20000108T071707-20000108T071907_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-12b_2024_05_15_17_13_55
                        'JUICE_L1a_RPWI-HF-SID3_20000108T071951-20000108T072151_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-12a-2_2024_05_15_17_16_42
                        'JUICE_L1a_RPWI-HF-SID3_20000108T072241-20000108T072441_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-12c_2024_05_15_17_19_28
                        'JUICE_L1a_RPWI-HF-SID3_20000108T072530-20000108T072730_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-12d_2024_05_15_17_22_18
                        'JUICE_L1a_RPWI-HF-SID3_20000108T073057-20000108T073257_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-12e_2024_05_15_17_27_45
                        'JUICE_L1a_RPWI-HF-SID3_20000108T073349-20000108T073549_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-12f_2024_05_15_17_30_37
                        'JUICE_L1a_RPWI-HF-SID3_20000108T073635-20000108T073835_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-12g_2024_05_15_17_33_23
                        'JUICE_L1a_RPWI-HF-SID3_20000108T073920-20000108T074120_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-12h_2024_05_15_17_36_08
                        ]
        # COMP-2
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000108T074210-20000108T074410_V01___TMIDX_00000.bin.cdf',  # pc2_SC_roll_RPW-SEQ-12i-2_2024_05_15_17_38_55
                        ]
        # COMP-1
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000108T074511-20000108T074711_V01___TMIDX_00000.bin.cdf',  # pc2_EGA-dryrun_RPW-SEQ-12j_2024_05_15_17_41_59
                         ]
        #
        # 202406-7 -- dryrun check
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/202406_EM3/cdf/'
        # COMP1->2, 2->1
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240614T161148-20240614T162539_V01___TMIDX_00000.bin.cdf',  
                         ]
        # 202407 -- LEGA check
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/202407_FS/cdf_20240716/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240716T152808-20240716T153933_V01.cdf',
                         ]
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/202407_FS/cdf_20240718/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000101T011258-20000101T013701_V01___TMIDX_00000.bin.cdf',
                         ]
        """

        # [MEMO: ASW1 data]  *** Flight - Ver.1 ***
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/2023/'
        # *** 2023/4/20 before deployment of MAG-BOOM
        data_name_list = ['04/20/JUICE_L1a_RPWI-HF-SID3_20230420T103604.cdf']
        # *** 2023/5/23 before deployment of RWI
        data_name_list = ['05/23/JUICE_L1a_RPWI-HF-SID3_20230523T090038.cdf',
                          '05/23/JUICE_L1a_RPWI-HF-SID3_20230523T092634.cdf',
                          '05/23/JUICE_L1a_RPWI-HF-SID3_20230523T095231.cdf',
                          '05/23/JUICE_L1a_RPWI-HF-SID3_20230523T102041.cdf',
                         ]
        data_name_list = ['05/23/JUICE_L1a_RPWI-HF-SID3_20230523T102436.cdf',        # *** 2023/5/23 after X deployment of RWI
                          '05/23/JUICE_L1a_RPWI-HF-SID3_20230523T104541.cdf',
                         ]
        data_name_list = ['05/23/JUICE_L1a_RPWI-HF-SID3_20230523T104936.cdf',        # *** 2023/5/23 after Z deployment of RWI
                          '05/23/JUICE_L1a_RPWI-HF-SID3_20230523T110542.cdf',
                         ]
        data_name_list = ['05/23/JUICE_L1a_RPWI-HF-SID3_20230523T110938.cdf']        # *** 2023/5/23 after Y deployment of RWI
        # *** 2023/5/23 background
        data_name_list = ['05/23/JUICE_L1a_RPWI-HF-SID3_20230523T121543.cdf',
                          '05/23/JUICE_L1a_RPWI-HF-SID3_20230523T124139.cdf',
                          '05/23/JUICE_L1a_RPWI-HF-SID3_20230523T125743.cdf',
                         ]
        # *** 20230525 
        data_name_list = ['05/25/JUICE_L1a_RPWI-HF-SID3_20230525T130154.cdf',
                          '05/25/JUICE_L1a_RPWI-HF-SID3_20230525T150440.cdf',
                          '05/25/JUICE_L1a_RPWI-HF-SID3_20230525T165318.cdf',
                         ]
        """

        # [MEMO: ASW1 data]  *** Ground Test - Ver.1 ***
        """
        # *** 202105
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202105/'
        data_name_list = ['SID3_20210531_SCPFM_PTR_RPWI_2_day4_xid32813.cdf']
        data_name_list = ['SID3_20210531_SCPFM_PTR_RPWI_2_day5_xid32814.cdf']
        # *** 202106 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202106/'
        data_name_list = ['SID3_SCTBTV_Phase3_xid32776.cdf']
        data_name_list = ['SID3_SCTBTV_Phase5_xid32794.cdf']
        data_name_list = ['SID3_SCTBTV_Phase11_xid32836.cdf']
        data_name_list = ['SID3_SCTBTV_Phase13_xid32848.cdf']
        # *** 202111 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202111/'        # CDF data folder
        data_name_list = ['SID3_SCPFM_PTR_RPWI_delta.RPWI_SCM_TEST_xid32816.cdf',
                          'SID3_SCPFM_PTR_RPWI_delta.RPWI_SCM_TEST_xid32817.cdf',
                          'SID3_SCPFM_PTR_RPWI_delta.RPWI_SCM_TEST_xid32818.cdf',
                         ]
        # *** 202204 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202204/'        # CDF data folder
        data_name_list = ['SID3_20220400_SCPFM_EMCR.Phase4_xid32994.cdf',
                          'SID3_20220400_SCPFM_EMCR.Phase4_xid32995.cdf',
                          'SID3_20220400_SCPFM_EMCR.Phase4_xid32996.cdf',
                          'SID3_20220400_SCPFM_EMCR.Phase4_xid32997.cdf',
                          'SID3_20220400_SCPFM_EMCR.Phase4_xid32998.cdf',
                          'SID3_20220400_SCPFM_EMCR.Phase4_xid32999.cdf',
                          'SID3_20220400_SCPFM_EMCR.Phase4_xid33000.cdf',
                          'SID3_20220400_SCPFM_EMCR.Phase4_xid33001.cdf',
                          'SID3_20220400_SCPFM_EMCR.Phase4_xid33002.cdf',
                          'SID3_20220400_SCPFM_EMCR.Phase4_xid33003.cdf',
                          'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32798.cdf',
                          'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32799.cdf',
                          'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32800.cdf',
                          'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32801.cdf',
                          'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32802.cdf',
                          'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32803.cdf',
                          'SID3_20220400_SCPFM_EMCR.RPWI_NCR_xid32804.cdf',
                         ] 
        # *** 202211 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202211/'        # CDF data folder
        data_name_list = ['SID3_20221115_Mission_Test_GCO500_1RPR_4.cdf',
                          'SID3_20221115_Mission_Test_GCO500_1RPR_6.cdf',
                         ]
        # *** 202301 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/prelaunch/202301/'        # CDF data folder
        data_name_list = ['SID3_20230113_Mission_Test_CSW3.2.1_SCOP020_1RPR_4.cdf',
                          'SID3_20230113_Mission_Test_CSW3.2.1_SCOP020_1RPR_6.cdf',
                         ]
        """

    print(data_dir)
    print(data_name_list)
    return data_dir, data_name_list