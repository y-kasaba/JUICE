"""
    JUICE RPWI HF SID3 (Full): L1a data list -- 2025/7/7
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
        data_name = '*HF*SID3_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_name_list = glob.glob(cdf_file)
        num_list = len(data_name_list)
        data_name_list.sort()
        for i in range(num_list):
            data_name_list[i] = os.path.split(data_name_list[i])[1]

    else:
        # *** Ground Test - Ver.3 ***
        # 202411 -- SAMPLE	    1.75MHz, 100mVpp    (0,0,0),(90,0,0),(0,90,0),(0,0,90) 
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000101T000103-20000101T000137_V01___SID03_20241125-1421_RadioFull_comp0_table1_asw3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000317-20000101T000857_V01___SID03_20241125-1405_RadioFull_comp1_table1_asw3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000150-20000101T000406_V01___SID03_20241125-1502_RadioFull_comp1_table1_bg0_asw3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000116-20000101T000258_V01___SID03_20241125-1457_RadioFull_comp1_table1_bg1_asw3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000457-20000101T001111_V01___SID03_20241125-1349_RadioFull_comp2_table1_asw3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000119-20000101T000153_V01___SID03_20241125-1506_RadioFull_comp2_table2_asw3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000108-20000101T000648_V01___SID03_20241125-1413_RadioFull_comp3_table1_asw3.ccs.cdf',
                          #'JUICE_L1a_RPWI-HF-SID3_20000101T000113-20000101T000147_V01___SID03_20241125-1433_RadioFull_ch2_comp0_table1_asw3.ccs.cdf',
                          #'JUICE_L1a_RPWI-HF-SID3_20000101T000100-20000101T000640_V01___SID03_20241125-1436_RadioFull_ch2_comp1_table1_asw3.ccs.cdf',
                          #'JUICE_L1a_RPWI-HF-SID3_20000101T000116-20000101T000656_V01___SID03_20241125-1444_RadioFull_ch2_comp2_table1_asw3.ccs.cdf',
                         ]

        # *** Ground Test - Ver.2 ***
        """
        # 202410 -- SAMPLE    10/10/10mV, 90/0/0deg,  1.55MHz
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000101T000319-20000101T000621_V01___SID03_20241009-1915_RadioFull_comp1.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000055-20000101T001033_V01___SID03_20241010-1027_RadioFull_comp1.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000147-20000101T001449_V01___SID03_20241010-1139_RadioFull_comp1_FFTmod.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000251-20000101T001411_V01___SID03_20241010-1428_RadioFull_comp1_levelbias1k.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000131-20000101T000529_V01___SID03_20241014-2138_RadioFull_complex1_bias0.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000511-20000101T000855_V01___SID03_20241009-1806_RadioFull_comp2.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000051-20000101T000517_V01___SID03_20241009-1906_RadioFull_comp2_bg06dB.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000056-20000101T000412_V01___SID03_20241009-1922_RadioFull_comp2_bg10dB.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000042-20000101T002032_V01___SID03_20241010-2130_RadioFull_polsep_bias0.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000302-20000101T000552_V01___SID03_20241011-1823_RadioFull_polsep_bias0.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000055-20000101T000453_V01___SID03_20241014-1132_RadioFull_polsep_bias0.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000217-20000101T000831_V01___SID03_20241014-0323_RadioFull_polsep_bias0.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000043-20000101T000731_V01___SID03_20241022-1915_complex2_bias3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000046-20000101T000518_V01___SID03_20241015-2313_3ch-comp3.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000226-20000101T000334_V01___SID03_20241023-1850-polsep.ccs.cdf',
                         ]
        """
        # *** Ground Test - Ver.2 ***
        """
        # 202310 -- SAMPLE  10/10/10mV, 90/0/0deg,  1.55MHz
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/old/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20000101T001351-20000101T001607_V01___SID03_20231024-0036.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000049-20000101T000231_V01___SID03-3ch-comp0-20231117-1424.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000212-20000101T000428_V01___SID03-3ch-comp1-20231117-1418.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000052-20000101T000200_V01___SID03-3ch-comp3-20231117-1432.ccs.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20000101T000100-20000101T000242_V01___SID03-3ch-comp2-20231117-1429.ccs.cdf',
                         ]
        """
        """
        # *** Flight data: Ver.2 ***
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240126T083835-20240126T113101_V01___RPR1_52000013_2024.026.13.22.14.423.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20240701T011127-20240701T011309_V01___RPR1_52000001_2024.183.15.43.53.614.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20240706T121009-20240706T131448_V01___RPR1_52000002_2024.190.14.59.43.630.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20240706T175202-20240706T183012_V01___RPR1_52000003_2024.190.15.33.44.638.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20240819T202636-20240819T221323_V01___RPR1_52000003_2024.233.02.43.43.102.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20240820T180734-20240822T022254_V01___RPR1_52000003_2024.235.03.19.13.483.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20240822T095914-20240822T182844_V01___RPR1_52000004_2024.236.08.13.31.519.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20240823T035818-20240823T215457_V01___RPR1_52000005_2024.237.04.37.21.527.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20240909T093241-20240909T101941_V01___RPR1_52000005_2024.254.16.53.07.436.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20250331T030012-20250331T201834_V01___RPR1_52000005_2025.091.16.38.56.448.cdf',
        ]
        """
        # *** Flight - Ver.1 ***
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW1/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20230420T103604-20230420T103806_V01___RPR1_52000002_2023.110.10.48.51.475.cdf',   # efore deployment of MAG-BOOM
                          'JUICE_L1a_RPWI-HF-SID3_20230523T090038-20230523T091026_V01___RPR1_52000000_2023.143.09.24.44.467.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230523T092634-20230523T093622_V01___RPR1_52000000_2023.143.09.50.39.471.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230523T095231-20230523T100219_V01___RPR1_52000000_2023.143.10.05.03.469.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230523T102041-20230523T102252_V01___RPR1_52000000_2023.143.10.24.52.503.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230523T102436-20230523T102652_V01___RPR1_52000001_2023.143.10.29.16.491.cdf',   # after X deployment of RWI
                          'JUICE_L1a_RPWI-HF-SID3_20230523T104541-20230523T104752_V01___RPR1_52000001_2023.143.10.49.52.471.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230523T104936-20230523T105153_V01___RPR1_52000002_2023.143.10.54.17.487.cdf',   # after Z deployment of RWI
                          'JUICE_L1a_RPWI-HF-SID3_20230523T110542-20230523T110754_V01___RPR1_52000002_2023.143.11.09.54.471.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230523T110938-20230523T111154_V01___RPR1_52000003_2023.143.11.14.17.500.cdf',   # after Y deployment of RWI
                          'JUICE_L1a_RPWI-HF-SID3_20230523T121543-20230523T122531_V01___RPR1_52000003_2023.143.12.39.49.467.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230523T124139-20230523T125127_V01___RPR1_52000003_2023.143.12.55.52.507.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230523T125743-20230523T130731_V01___RPR1_52000003_2023.143.13.11.36.466.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230525T130154-20230525T131142_V01___RPR1_52000006_2023.145.13.51.50.508.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230525T150440-20230525T151428_V01___RPR1_52000006_2023.145.15.46.34.503.cdf',
                          'JUICE_L1a_RPWI-HF-SID3_20230525T165318-20230525T170306_V01___RPR1_52000006_2023.145.17.20.46.547.cdf',
                         ]
        """

    print(data_dir)
    print(data_name_list)
    return data_dir, data_name_list