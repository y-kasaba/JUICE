"""
    JUICE RPWI HF SID3 (Full): L1a QL -- 2026/3/11
"""
import glob
import numpy as np
import math
import juice_hf_hk_lib as hf_hk
# import juice_cdf_lib   as hk_cdf

class struct:
    pass

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
        base_dir = '/Users/D-Univ/data/data-JUICE/datasets/'
        data_dir = base_dir+yr_str+'/'+mn_str+'/'+dy_str + '/'
        data_name = '*HF*SID3_*'+ver_str+'.cdf'
        cdf_file = data_dir + data_name

        data_list = glob.glob(cdf_file)
        num_list = len(data_list)
        data_list.sort()
        for i in range(num_list):
            data_list[i] = os.path.split(data_list[i])[1]

    else:
        # *** Ground Test - Ver.3 ***
        # 202601-- ASW3 test
        data_dir = '/Users/user/0-python/JUICE_data/test-TMIDX/ASW3/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID3_20260109T162606-20260109T162606_V01___Sec03_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20260109T164153-20260109T165023_V01___Sec04_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20260109T181819-20260109T182649_V01___Sec10_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20260109T210405-20260109T211235_V01___Sec11_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20260109T211904-20260109T212734_V01___Sec12_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20260109T213707-20260109T213707_V01___Sec13_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20260109T214925-20260109T215755_V01___Sec14_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20260109T225315-20260109T230145_V01___Sec15_260118.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20260109T232303-20260109T233133_V01___Sec17_260118.bin.cdf',
                    ]
        # 202511 -- SAMPLE  sweep 0.02-2MHz 5s		Vin=10 mVpp
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID3_20000101T001750-20000101T003120_V01___SID3_C1_20251113-1557.ccs.cdf',
                            # (2d matix, RFI rejection OFF), new sweep table (Beff=62.5%)
	                        # int=40 [s]		f = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1 [MHz]
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000043-20000101T001343_V01___SID3_C2_20251113-1715.ccs.cdf',  
                            # (polariztion separation, RFI rejection OFF, noise floor subtraction OFF), new sweep table (Beff=62.5%)
	                        # int=40 [s]		f = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1 [MHz]
                     'JUICE_L1a_RPWI-HF-SID3_20000101T001555-20000101T002925_V01___SID3_C1_20251123-1021.ccs.cdf',
                            # (2d matix, RFI rejection OFF), new sweep table (Beff=62.5%)
                            # int=40 [s]		f = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1 [MHz]
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T003123-20000101T004453_V01___SID3_C2_20251123-1037.ccs.cdf',
                            # (polariztion separation, RFI rejection OFF, noise floor subtraction OFF), new sweep table (Beff=62.5%)
	                        # int=40 [s]		f = [0.02 0.05 0.1 0.2 0.5 1.1 1.8 2.1 3.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1] [MHz]
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000153-20000101T000323_V01___SID3_20251211-2231.ccs.cdf',
                    ]
        """
        """
        # 202509 -- SAMPLE
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW3/cdf/old2/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID3_20000101T000109-20000101T001049_V01___SID03-comp1_20250925-0949.ccs.cdf',
                     	    # Freq=1.5MHz       Vin=0.01-100mVpp Phase=0deg (X, Y & Z)
                     'JUICE_L1a_RPWI-HF-SID3_20000101T000151-20000101T000731_V01___SID03-comp1_20250925-1148_10mVpp.ccs.cdf',
                     	    # Freq=1.5MHz       Vin=10mVpp       Phase=[0 45 90 135 180 225 270 315 0] deg (for Y-ch)
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T002724-20000101T003604_V01___SID03-comp1_20250925-1015.ccs.cdf',
                            # Freq=0.02-44.1MHz Vin=10mVpp,      Phase=0deg (X, Y & Z)
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T021007-20000101T024127_V01___SID03-comp2_20250927-2008.ccs.cdf',
                            # (1) Freq=1.5MHz   Vin =[0.01 0.02 0.05 0.1 0.2 0.5 1 2 5 10 20 50 100 200 500] mVpp
                            # (2)               Vin =10mVpp      Freq = [0.02 0.05 0.1 0.2 0.5 1.1 2.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1] MHz
                            # (3) Freq=1.5MHz   Vin =10mVpp      Phase (x ch) = [0 45 90 135 180 225 270 315 0] deg
                            # (4) Freq=1.5MHz   Vin =10mVpp      Phase (y ch) = [0 45 90 135 180 225 270 315 0] deg
                            # (5) Freq=1.5MHz   Vin =10mVpp      Phase (z ch) = [0 45 90 135 180 225 270 315 0] deg
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T004825-20000101T011945_V01___SID03-comp3_20250927-1847.ccs.cdf',
                            # (1) Freq=1.5MHz   Vin =[0.01 0.02 0.05 0.1 0.2 0.5 1 2 5 10 20 50 100 200 500] mVpp
                            # (2)               Vin =10mVpp      Freq = [0.02 0.05 0.1 0.2 0.5 1.1 2.1 5.1 10.1 15.1 20.1 25.1 30.1 35.1 40.1 44.1] MHz
                            # (3) Freq=1.5MHz   Vin =10mVpp      Phase (x ch) = [0 45 90 135 180 225 270 315 0] deg
                            # (4) Freq=1.5MHz   Vin =10mVpp      Phase (y ch) = [0 45 90 135 180 225 270 315 0] deg
                            # (5) Freq=1.5MHz   Vin =10mVpp      Phase (z ch) = [0 45 90 135 180 225 270 315 0] deg
                    ]
        """
        # *** Ground Test - Ver.2 ***
        # 202510 -- PCW4 emulation
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID3_20251003T080527-20251003T080527_V01___PC4-1_00000.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20251003T080540-20251003T080540_V01___TMIDX_00000.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20251003T080550-20251003T080700_V01___PC4-1_00001.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20251003T080603-20251003T080713_V01___TMIDX_00001.bin.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20000101T000935-20000101T000935_V01___PC4-2_00000.bin.cdf',
                    ]
        """
        # 202410 -- SAMPLE    10/10/10mV, 90/0/0deg,  1.55MHz
        """
        data_dir = '/Users/user/0-python/JUICE_data/test-CCSDS/ASW2/cdf/'
        data_list = ['JUICE_L1a_RPWI-HF-SID3_20000101T000319-20000101T000621_V01___SID03_20241009-1915_RadioFull_comp1.ccs.cdf',          # saturated
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000055-20000101T001033_V01___SID03_20241010-1027_RadioFull_comp1.ccs.cdf',           # saturated 
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000147-20000101T001449_V01___SID03_20241010-1139_RadioFull_comp1_FFTmod.ccs.cdf',    # saturated
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000251-20000101T001411_V01___SID03_20241010-1428_RadioFull_comp1_levelbias1k.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000131-20000101T000529_V01___SID03_20241014-2138_RadioFull_complex1_bias0.ccs.cdf',  # CAL 1mVpp?
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000511-20000101T000855_V01___SID03_20241009-1806_RadioFull_comp2.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000051-20000101T000517_V01___SID03_20241009-1906_RadioFull_comp2_bg06dB.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000056-20000101T000412_V01___SID03_20241009-1922_RadioFull_comp2_bg10dB.ccs.cdf',    # saturated
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000042-20000101T002032_V01___SID03_20241010-2130_RadioFull_polsep_bias0.ccs.cdf',    # saturated
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000302-20000101T000552_V01___SID03_20241011-1823_RadioFull_polsep_bias0.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000055-20000101T000453_V01___SID03_20241014-1132_RadioFull_polsep_bias0.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000217-20000101T000831_V01___SID03_20241014-0323_RadioFull_polsep_bias0.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000043-20000101T000731_V01___SID03_20241022-1915_complex2_bias3.ccs.cdf',
                     ##'JUICE_L1a_RPWI-HF-SID3_20000101T000046-20000101T000518_V01___SID03_20241015-2313_3ch-comp3.ccs.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20000101T000226-20000101T000334_V01___SID03_20241023-1850-polsep.ccs.cdf',
                     #'old/JUICE_L1a_RPWI-HF-SID3_20000101T001351-20000101T001607_V01___SID03_20231024-0036.ccs.cdf',                       # saturated
                     #'old/JUICE_L1a_RPWI-HF-SID3_20000101T000049-20000101T000231_V01___SID03-3ch-comp0-20231117-1424.ccs.cdf',             # saturated
                     #'old/JUICE_L1a_RPWI-HF-SID3_20000101T000212-20000101T000428_V01___SID03-3ch-comp1-20231117-1418.ccs.cdf',             # saturated
                     #'old/JUICE_L1a_RPWI-HF-SID3_20000101T000100-20000101T000242_V01___SID03-3ch-comp2-20231117-1429.ccs.cdf',
                     ##'old/JUICE_L1a_RPWI-HF-SID3_20000101T000052-20000101T000200_V01___SID03-3ch-comp3-20231117-1432.ccs.cdf',             # saturated
                    ]
        """
        # *** Flight data: Ver.2 ***
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW2/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID3_20240126T083835-20240126T113101_V01___RPR1_52000013_2024.026.13.22.14.423.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20240701T011127-20240701T011309_V01___RPR1_52000001_2024.183.15.43.53.614.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20240706T121009-20240706T131448_V01___RPR1_52000002_2024.190.14.59.43.630.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20240706T175202-20240706T183012_V01___RPR1_52000003_2024.190.15.33.44.638.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20240819T202636-20240819T221323_V01___RPR1_52000003_2024.233.02.43.43.102.cdf',    # LGA
                     #'JUICE_L1a_RPWI-HF-SID3_20240820T180734-20240822T022254_V01___RPR1_52000003_2024.235.03.19.13.483.cdf',   # EGA
                     #'JUICE_L1a_RPWI-HF-SID3_20240822T095914-20240822T182844_V01___RPR1_52000004_2024.236.08.13.31.519.cdf',    # CAL
                     #'JUICE_L1a_RPWI-HF-SID3_20240823T035818-20240823T215457_V01___RPR1_52000005_2024.237.04.37.21.527.cdf',   # CAL-roll
                     #'JUICE_L1a_RPWI-HF-SID3_20240909T093241-20240909T101941_V01___RPR1_52000005_2024.254.16.53.07.436.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20250331T030012-20250331T201834_V01___RPR1_52000005_2025.091.16.38.56.448.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20260223T004250-20260223T004427_V01___RPR1_52000001_2026.062.08.07.27.435.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20260224T071223-20260224T202104_V01___RPR1_52000003_2026.062.10.00.23.546.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20260225T032214-20260225T035144_V01___RPR1_52000004_2026.062.10.36.22.491.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20260225T073900-20260227T054301_V01___RPR1_52000005_2026.062.11.30.25.518.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20260227T091840-20260228T222000_V01___RPR1_52000006_2026.062.11.56.35.462.cdf',
        ]
        """
        # *** Flight - Ver.1 ***
        """
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/ASW1/'
        data_list = [#'JUICE_L1a_RPWI-HF-SID3_20230420T103604-20230420T103806_V01___RPR1_52000002_2023.110.10.48.51.475.cdf',   # before MAG-BOOM deployment
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T090038-20230523T091026_V01___RPR1_52000000_2023.143.09.24.44.467.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T092634-20230523T093622_V01___RPR1_52000000_2023.143.09.50.39.471.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T095231-20230523T100219_V01___RPR1_52000000_2023.143.10.05.03.469.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T102041-20230523T102252_V01___RPR1_52000000_2023.143.10.24.52.503.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T102436-20230523T102652_V01___RPR1_52000001_2023.143.10.29.16.491.cdf',   # after X deployment
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T104541-20230523T104752_V01___RPR1_52000001_2023.143.10.49.52.471.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T104936-20230523T105153_V01___RPR1_52000002_2023.143.10.54.17.487.cdf',   # after Z deployment
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T110542-20230523T110754_V01___RPR1_52000002_2023.143.11.09.54.471.cdf',
                     'JUICE_L1a_RPWI-HF-SID3_20230523T110938-20230523T111154_V01___RPR1_52000003_2023.143.11.14.17.500.cdf',   # after Y deployment: with CAL
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T121543-20230523T122531_V01___RPR1_52000003_2023.143.12.39.49.467.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T124139-20230523T125127_V01___RPR1_52000003_2023.143.12.55.52.507.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20230523T125743-20230523T130731_V01___RPR1_52000003_2023.143.13.11.36.466.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20230525T130154-20230525T131142_V01___RPR1_52000006_2023.145.13.51.50.508.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20230525T150440-20230525T151428_V01___RPR1_52000006_2023.145.15.46.34.503.cdf',
                     #'JUICE_L1a_RPWI-HF-SID3_20230525T165318-20230525T170306_V01___RPR1_52000006_2023.145.17.20.46.547.cdf',
                    ]
        """

    print(data_dir)
    print(data_list)
    return data_dir, data_list


# ---------------------------------------------------------------------
# --- HID3 ------------------------------------------------------------
# ---------------------------------------------------------------------
def hf_sid3_read(cdf):
    """
    input:  CDF
    return: data
    """
    data = struct()

    # Data
    data.EuEu       = np.float64(cdf['EuEu'][...]);       data.EvEv       = np.float64(cdf['EvEv'][...]);       data.EwEw = np.float64(cdf['EwEw'][...])
    data.EuEv_re    = np.float64(cdf['EuEv_re'][...]);    data.EvEw_re    = np.float64(cdf['EvEw_re'][...]);    data.EwEu_re    = np.float64(cdf['EwEu_re'][...])   
    data.EuEv_im    = np.float64(cdf['EuEv_im'][...]);    data.EvEw_im    = np.float64(cdf['EvEw_im'][...]);    data.EwEu_im    = np.float64(cdf['EwEu_im'][...])
    # complex == 2:    # Matrix - N/R/L-separated
    data.EuEu_NC    = np.float64(cdf['EuEu_NC'][...]);    data.EvEv_NC    = np.float64(cdf['EvEv_NC'][...]);    data.EwEw_NC    = np.float64(cdf['EwEw_NC'][...])
    data.EuEv_re_NC = np.float64(cdf['EuEv_re_NC'][...]); data.EvEw_re_NC = np.float64(cdf['EvEw_re_NC'][...]); data.EwEu_re_NC = np.float64(cdf['EwEu_re_NC'][...])
    data.EuEv_im_NC = np.float64(cdf['EuEv_im_NC'][...]); data.EvEw_im_NC = np.float64(cdf['EvEw_im_NC'][...]); data.EwEu_im_NC = np.float64(cdf['EwEu_im_NC'][...])
    data.EuEu_RC    = np.float64(cdf['EuEu_RC'][...]);    data.EvEv_RC    = np.float64(cdf['EvEv_RC'][...]);    data.EwEw_RC    = np.float64(cdf['EwEw_RC'][...])
    data.EuEv_re_RC = np.float64(cdf['EuEv_re_RC'][...]); data.EvEw_re_RC = np.float64(cdf['EvEw_re_RC'][...]); data.EwEu_re_RC = np.float64(cdf['EwEu_re_RC'][...])
    data.EuEv_im_RC = np.float64(cdf['EuEv_im_RC'][...]); data.EvEw_im_RC = np.float64(cdf['EvEw_im_RC'][...]); data.EwEu_im_RC = np.float64(cdf['EwEu_im_RC'][...])
    data.EuEu_LC    = np.float64(cdf['EuEu_LC'][...]);    data.EvEv_LC    = np.float64(cdf['EvEv_LC'][...]);    data.EwEw_LC    = np.float64(cdf['EwEw_LC'][...])
    data.EuEv_re_LC = np.float64(cdf['EuEv_re_LC'][...]); data.EvEw_re_LC = np.float64(cdf['EvEw_re_LC'][...]); data.EwEu_re_LC = np.float64(cdf['EwEu_re_LC'][...])
    data.EuEv_im_LC = np.float64(cdf['EuEv_im_LC'][...]); data.EvEw_im_LC = np.float64(cdf['EvEw_im_LC'][...]); data.EwEu_im_LC = np.float64(cdf['EwEu_im_LC'][...])
    data.num_NC     = cdf['num_NC'][...];                 data.num_RC     = cdf['num_RC'][...];                 data.num_LC     = cdf['num_LC'][...]
    #
    data.EuEu_amp = np.float64(cdf['EuEu_amp'][...]);   data.EuEu_raw = np.float64(cdf['EuEu_raw'][...])
    data.EvEv_amp = np.float64(cdf['EvEv_amp'][...]);   data.EvEv_raw = np.float64(cdf['EvEv_raw'][...])
    data.EwEw_amp = np.float64(cdf['EwEw_amp'][...]);   data.EwEw_raw = np.float64(cdf['EwEw_raw'][...])
    data.gain_raw = cdf['gain_raw'][...];               data.df_raw   = cdf['df_raw'][...]
    #
    data.BG_Eu      = np.float64(cdf['BG_Eu'][...]);      data.BG_Ev      = np.float64(cdf['BG_Ev'][...]);     data.BG_Ew      = np.float64(cdf['BG_Ew'][...])
    #
    data.frequency  = cdf['frequency'][...];  data.freq_step = cdf['freq_step'][...];  data.freq_width  = cdf['freq_width'][...]

    hf_hk.status_read(cdf, data)
    return data


def hf_sid3_add(data, data1):
    """
    input:  data, data1
    return: data
    """
    # Data
    data.EuEu       = np.r_["0", data.EuEu, data1.EuEu]
    data.EvEv       = np.r_["0", data.EvEv, data1.EvEv]
    data.EwEw       = np.r_["0", data.EwEw, data1.EwEw]
    data.EuEv_re    = np.r_["0", data.EuEv_re, data1.EuEv_re];       data.EvEw_re = np.r_["0", data.EvEw_re, data1.EvEw_re]
    data.EwEu_re    = np.r_["0", data.EwEu_re, data1.EwEu_re];       data.EuEv_im = np.r_["0", data.EuEv_im, data1.EuEv_im]
    data.EvEw_im    = np.r_["0", data.EvEw_im, data1.EvEw_im];       data.EwEu_im = np.r_["0", data.EwEu_im, data1.EwEu_im]
    # complex == 2:    # Matrix - N/R/L-separated
    data.EuEu_NC    = np.r_["0", data.EuEu_NC, data1.EuEu_NC]
    data.EvEv_NC    = np.r_["0", data.EvEv_NC, data1.EvEv_NC]
    data.EwEw_NC    = np.r_["0", data.EwEw_NC, data1.EwEw_NC]
    data.EuEv_re_NC = np.r_["0", data.EuEv_re_NC, data1.EuEv_re_NC]; data.EvEw_re_NC = np.r_["0", data.EvEw_re_NC, data1.EvEw_re_NC]
    data.EwEu_re_NC = np.r_["0", data.EwEu_re_NC, data1.EwEu_re_NC]; data.EuEv_im_NC = np.r_["0", data.EuEv_im_NC, data1.EuEv_im_NC]
    data.EvEw_im_NC = np.r_["0", data.EvEw_im_NC, data1.EvEw_im_NC]; data.EwEu_im_NC = np.r_["0", data.EwEu_im_NC, data1.EwEu_im_NC]
    data.EuEu_RC    = np.r_["0", data.EuEu_RC, data1.EuEu_RC]
    data.EvEv_RC    = np.r_["0", data.EvEv_RC, data1.EvEv_RC]
    data.EwEw_RC    = np.r_["0", data.EwEw_RC, data1.EwEw_RC]
    data.EuEv_re_RC = np.r_["0", data.EuEv_re_RC, data1.EuEv_re_RC]; data.EvEw_re_RC = np.r_["0", data.EvEw_re_RC, data1.EvEw_re_RC]
    data.EwEu_re_RC = np.r_["0", data.EwEu_re_RC, data1.EwEu_re_RC]; data.EuEv_im_RC = np.r_["0", data.EuEv_im_RC, data1.EuEv_im_RC]
    data.EvEw_im_RC = np.r_["0", data.EvEw_im_RC, data1.EvEw_im_RC]; data.EwEu_im_RC = np.r_["0", data.EwEu_im_RC, data1.EwEu_im_RC]
    data.EuEu_LC    = np.r_["0", data.EuEu_LC, data1.EuEu_LC]
    data.EvEv_LC    = np.r_["0", data.EvEv_LC, data1.EvEv_LC]
    data.EwEw_LC    = np.r_["0", data.EwEw_LC, data1.EwEw_LC]
    data.EuEv_re_LC = np.r_["0", data.EuEv_re_LC, data1.EuEv_re_LC]; data.EvEw_re_LC = np.r_["0", data.EvEw_re_LC, data1.EvEw_re_LC]
    data.EwEu_re_LC = np.r_["0", data.EwEu_re_LC, data1.EwEu_re_LC]; data.EuEv_im_LC = np.r_["0", data.EuEv_im_LC, data1.EuEv_im_LC]
    data.EvEw_im_LC = np.r_["0", data.EvEw_im_LC, data1.EvEw_im_LC]; data.EwEu_im_LC = np.r_["0", data.EwEu_im_LC, data1.EwEu_im_LC]
    data.num_NC     = np.r_["0", data.num_NC, data1.num_NC]
    data.num_RC     = np.r_["0", data.num_RC, data1.num_RC]
    data.num_LC     = np.r_["0", data.num_LC, data1.num_LC]
    #
    data.EuEu_raw   = np.r_["0", data.EuEu_raw, data1.EuEu_raw]
    data.EvEv_raw   = np.r_["0", data.EvEv_raw, data1.EvEv_raw]
    data.EwEw_raw   = np.r_["0", data.EwEw_raw, data1.EwEw_raw]
    data.EuEu_amp   = np.r_["0", data.EuEu_amp, data1.EuEu_amp]
    data.EvEv_amp   = np.r_["0", data.EvEv_amp, data1.EvEv_amp]
    data.EwEw_amp   = np.r_["0", data.EwEw_amp, data1.EwEw_amp]
    data.gain_raw   = np.r_["0", data.gain_raw, data1.gain_raw]
    data.df_raw     = np.r_["0", data.df_raw,   data1.df_raw]
    #
    data.BG_Eu      = np.r_["0", data.BG_Eu, data1.BG_Eu]
    data.BG_Ev      = np.r_["0", data.BG_Ev, data1.BG_Ev]
    data.BG_Ew      = np.r_["0", data.BG_Ew, data1.BG_Ew]
    #
    data.frequency  = np.r_["0", data.frequency, data1.frequency]
    data.freq_step  = np.r_["0", data.freq_step, data1.freq_step]
    data.freq_width = np.r_["0", data.freq_width, data1.freq_width]

    hf_hk.status_add(data, data1)
    return data


def hf_sid3_shaping(data, cal_mode, N_ch, comp_mode):
    """
    input:  data
            cal_mode    [Power]     0: background          1: CAL           2: all
            N_ch0       [channel]   2: 2-ch    3: 3-ch                   0,>3: any
            comp_mode   [Complex]   0: Poweer  1: Matrix   3: Matrix-2D    >3: any   
    return: data
    """

    # Selection: CAL, N_ch, comp_mode
    data.n_time  = data.EuEu.shape[0]
    data.n_freq  = data.EuEu.shape[1]
    data.U_selected = (data.ch_selected & 0b1   ) 
    data.V_selected = (data.ch_selected & 0b10  ) >> 1
    data.W_selected = (data.ch_selected & 0b100 ) >> 2
    N_ch0 = data.U_selected + data.V_selected + data.W_selected
    print("  org:", data.EuEu.shape, data.n_time, "x", data.n_freq, "[", data.n_time * data.n_freq, "]")
    if cal_mode < 2 or N_ch < 4 or comp_mode < 4:
        if cal_mode < 2:
            if N_ch < 4:
                if comp_mode < 4:
                    index = np.where( (data.cal_signal == cal_mode) & (N_ch0 == N_ch) & (comp_mode == data.complex) )
                    print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch, " comp_mode:", comp_mode)
                else:
                    index = np.where( (data.cal_signal == cal_mode) & (N_ch0 == N_ch)                               )
                    print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch)
            else:
                if comp_mode < 4:
                    index = np.where( (data.cal_signal == cal_mode) &                   (comp_mode == data.complex) )
                    print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> cal-mode:", cal_mode, " comp_mode:", comp_mode)
                else:
                    index = np.where( (data.cal_signal == cal_mode)                                                 )
                    print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> cal-mode:", cal_mode)
        else:
            if N_ch < 4:
                if comp_mode < 4:
                    index = np.where(                                 (N_ch0 == N_ch) & (comp_mode == data.complex) )
                    print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> N_ch:", N_ch, " comp_mode:", comp_mode)
                else:
                    index = np.where(                                 (N_ch0 == N_ch)                               )
                    print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> N_ch:", N_ch)
            else:
                index     = np.where(                                                   (comp_mode == data.complex) )
                print(    "  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> comp_mode:", comp_mode)

        # Data
        data.EuEu        = data.EuEu       [index[0]]; data.EvEv       = data.EvEv      [index[0]]; data.EwEw       = data.EwEw      [index[0]]
        data.EuEv_re     = data.EuEv_re    [index[0]]; data.EvEw_re    = data.EvEw_re   [index[0]]; data.EwEu_re    = data.EwEu_re   [index[0]]
        data.EuEv_im     = data.EuEv_im    [index[0]]; data.EvEw_im    = data.EvEw_im   [index[0]]; data.EwEu_im    = data.EwEu_im   [index[0]]
        # complex == 2:    # Matrix - N/R/L-separated
        data.EuEu_NC     = data.EuEu_NC    [index[0]]; data.EvEv_NC    = data.EvEv_NC   [index[0]]; data.EwEw_NC    = data.EwEw_NC   [index[0]]
        data.EuEv_re_NC  = data.EuEv_re_NC [index[0]]; data.EvEw_re_NC = data.EvEw_re_NC[index[0]]; data.EwEu_re_NC = data.EwEu_re_NC[index[0]]
        data.EuEv_im_NC  = data.EuEv_im_NC [index[0]]; data.EvEw_im_NC = data.EvEw_im_NC[index[0]]; data.EwEu_im_NC = data.EwEu_im_NC[index[0]]
        data.EuEu_RC     = data.EuEu_RC    [index[0]]; data.EvEv_RC    = data.EvEv_RC   [index[0]]; data.EwEw_RC    = data.EwEw_RC   [index[0]]
        data.EuEv_re_RC  = data.EuEv_re_RC [index[0]]; data.EvEw_re_RC = data.EvEw_re_RC[index[0]]; data.EwEu_re_RC = data.EwEu_re_RC[index[0]]
        data.EuEv_im_RC  = data.EuEv_im_RC [index[0]]; data.EvEw_im_RC = data.EvEw_im_RC[index[0]]; data.EwEu_im_RC = data.EwEu_im_RC[index[0]]
        data.EuEu_LC     = data.EuEu_LC    [index[0]]; data.EvEv_LC    = data.EvEv_LC   [index[0]]; data.EwEw_LC    = data.EwEw_LC   [index[0]]
        data.EuEv_re_LC  = data.EuEv_re_LC [index[0]]; data.EvEw_re_LC = data.EvEw_re_LC[index[0]]; data.EwEu_re_LC = data.EwEu_re_LC[index[0]]
        data.EuEv_im_LC  = data.EuEv_im_LC [index[0]]; data.EvEw_im_LC = data.EvEw_im_LC[index[0]]; data.EwEu_im_LC = data.EwEu_im_LC[index[0]]
        data.num_NC      = data.num_NC     [index[0]]; data.num_RC     = data.num_RC    [index[0]]; data.num_LC     = data.num_LC    [index[0]]
        #
        data.EuEu_raw    = data.EuEu_raw   [index[0]]; data.EvEv_raw   = data.EvEv_raw  [index[0]]; data.EwEw_raw   = data.EwEw_raw  [index[0]]
        data.EuEu_amp    = data.EuEu_amp   [index[0]]; data.EvEv_amp   = data.EvEv_amp  [index[0]]; data.EwEw_amp   = data.EwEw_amp  [index[0]]
        data.gain_raw    = data.gain_raw   [index[0]]; data.df_raw     = data.df_raw    [index[0]]
        #
        data.BG_Eu       = data.BG_Eu      [index[0]]; data.BG_Ev      = data.BG_Ev     [index[0]]; data.BG_Ew      = data.BG_Ew     [index[0]]
        #
        data.frequency   = data.frequency  [index[0]]; data.freq_step  = data.freq_step [index[0]]; data.freq_width = data.freq_width[index[0]]

        hf_hk.status_shaping(data, index[0])
        
        data.n_time = data.EuEu.shape[0]
        if cal_mode < 2:
            if N_ch < 4:
                if comp_mode < 4: print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch, " comp_mode:", comp_mode)
                else:             print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> cal-mode:", cal_mode, " N_ch:", N_ch)
            else:
                if comp_mode < 4: print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> cal-mode:", cal_mode, " comp_mode:", comp_mode)
                else:             print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> cal-mode:", cal_mode)
            if   cal_mode == 0:   print("<only BG>")
            else:                 print("<only CAL>")
        else:
            if N_ch < 4:
                if comp_mode < 4: print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> N_ch:", N_ch, " comp_mode:", comp_mode)
                else:             print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> N_ch:", N_ch)
            else:                 print("  cut:", data.EuEu.shape, data.n_time, "x", data.n_freq, "===> comp_mode:", comp_mode)

    # Size
    data.n_time  = data.EuEu.shape[0]
    data.n_freq  = data.EuEu.shape[1]
    data.U_selected = (data.ch_selected & 0b1   ) 
    data.V_selected = (data.ch_selected & 0b10  ) >> 1
    data.W_selected = (data.ch_selected & 0b100 ) >> 2

    # *** frequncy & width for spec cal
    data.freq   = data.frequency
    data.freq_w = data.freq_width

    # NAN
    index = np.where(data.complex == 0)
    data.EuEv_re   [index[0]] = math.nan; data.EvEw_re   [index[0]] = math.nan; data.EwEu_re   [index[0]] = math.nan
    data.EuEv_im   [index[0]] = math.nan; data.EvEw_im   [index[0]] = math.nan; data.EwEu_im   [index[0]] = math.nan
    index = np.where(data.complex != 2)
    data.EuEu_NC   [index[0]] = math.nan; data.EvEv_NC   [index[0]] = math.nan; data.EwEw_NC   [index[0]] = math.nan
    data.EuEv_re_NC[index[0]] = math.nan; data.EvEw_re_NC[index[0]] = math.nan; data.EwEu_re_NC[index[0]] = math.nan
    data.EuEv_im_NC[index[0]] = math.nan; data.EvEw_im_NC[index[0]] = math.nan; data.EwEu_im_NC[index[0]] = math.nan
    data.EuEu_RC   [index[0]] = math.nan; data.EvEv_RC   [index[0]] = math.nan; data.EwEw_RC   [index[0]] = math.nan
    data.EuEv_re_RC[index[0]] = math.nan; data.EvEw_re_RC[index[0]] = math.nan; data.EwEu_re_RC[index[0]] = math.nan
    data.EuEv_im_RC[index[0]] = math.nan; data.EvEw_im_RC[index[0]] = math.nan; data.EwEu_im_RC[index[0]] = math.nan
    data.EuEu_LC   [index[0]] = math.nan; data.EvEv_LC   [index[0]] = math.nan; data.EwEw_LC   [index[0]] = math.nan
    data.EuEv_re_LC[index[0]] = math.nan; data.EvEw_re_LC[index[0]] = math.nan; data.EwEu_re_LC[index[0]] = math.nan
    data.EuEv_im_LC[index[0]] = math.nan; data.EvEw_im_LC[index[0]] = math.nan; data.EwEu_im_LC[index[0]] = math.nan
    #
    index = np.where(data.U_selected == 0) 
    data.EuEu      [index[0]] = math.nan; data.EuEu_NC   [index[0]] = math.nan; data.EuEu_RC   [index[0]] = math.nan; data.EuEu_LC   [index[0]] = math.nan
    data.EuEv_re   [index[0]] = math.nan; data.EwEu_re   [index[0]] = math.nan; data.EuEv_im   [index[0]] = math.nan; data.EwEu_im   [index[0]] = math.nan
    data.EuEv_re_NC[index[0]] = math.nan; data.EwEu_re_NC[index[0]] = math.nan; data.EuEv_im_NC[index[0]] = math.nan; data.EwEu_im_NC[index[0]] = math.nan
    data.EuEv_re_RC[index[0]] = math.nan; data.EwEu_re_RC[index[0]] = math.nan; data.EuEv_im_RC[index[0]] = math.nan; data.EwEu_im_RC[index[0]] = math.nan
    data.EuEv_re_LC[index[0]] = math.nan; data.EwEu_re_LC[index[0]] = math.nan; data.EuEv_im_LC[index[0]] = math.nan; data.EwEu_im_LC[index[0]] = math.nan
    data.EuEu_raw  [index[0]] = math.nan; data.EuEu_amp  [index[0]] = math.nan; 
    index = np.where(data.V_selected == 0)
    data.EvEv      [index[0]] = math.nan; data.EvEv_NC   [index[0]] = math.nan; data.EvEv_RC   [index[0]] = math.nan; data.EvEv_LC   [index[0]] = math.nan 
    data.EvEw_re   [index[0]] = math.nan; data.EwEu_re   [index[0]] = math.nan; data.EvEw_im   [index[0]] = math.nan; data.EwEu_im   [index[0]] = math.nan
    data.EuEv_re_NC[index[0]] = math.nan; data.EvEw_re_NC[index[0]] = math.nan; data.EuEv_im_NC[index[0]] = math.nan; data.EvEw_im_NC[index[0]] = math.nan
    data.EuEv_re_RC[index[0]] = math.nan; data.EvEw_re_RC[index[0]] = math.nan; data.EuEv_im_RC[index[0]] = math.nan; data.EvEw_im_RC[index[0]] = math.nan
    data.EuEv_re_LC[index[0]] = math.nan; data.EvEw_re_LC[index[0]] = math.nan; data.EuEv_im_LC[index[0]] = math.nan; data.EvEw_im_LC[index[0]] = math.nan
    data.EvEv_raw  [index[0]] = math.nan; data.EvEv_amp  [index[0]] = math.nan; 
    index = np.where(data.W_selected == 0)
    data.EwEw      [index[0]] = math.nan; data.EwEw_NC   [index[0]] = math.nan; data.EwEw_RC   [index[0]] = math.nan; data.EwEw_LC   [index[0]] = math.nan
    data.EvEw_re   [index[0]] = math.nan; data.EwEu_re   [index[0]] = math.nan; data.EvEw_im   [index[0]] = math.nan; data.EwEu_im   [index[0]] = math.nan
    data.EvEw_re_NC[index[0]] = math.nan; data.EwEu_re_NC[index[0]] = math.nan; data.EvEw_im_NC[index[0]] = math.nan; data.EwEu_im_NC[index[0]] = math.nan    
    data.EvEw_re_RC[index[0]] = math.nan; data.EwEu_re_RC[index[0]] = math.nan; data.EvEw_im_RC[index[0]] = math.nan; data.EwEu_im_RC[index[0]] = math.nan
    data.EvEw_re_LC[index[0]] = math.nan; data.EwEu_re_LC[index[0]] = math.nan; data.EvEw_im_LC[index[0]] = math.nan; data.EwEu_im_LC[index[0]] = math.nan
    data.EwEw_raw  [index[0]] = math.nan; data.EwEw_amp  [index[0]] = math.nan; 
    
    # MIN: cut
    data.EuEu = np.ravel(data.EuEu);  data.EvEv = np.ravel(data.EvEv);  data.EwEw = np.ravel(data.EwEw)
    index = np.where(data.EuEu < 1e-9);  data.EuEu[index[0]] = math.nan
    index = np.where(data.EvEv < 1e-9);  data.EvEv[index[0]] = math.nan
    index = np.where(data.EwEw < 1e-9);  data.EwEw[index[0]] = math.nan
    data.EuEu = data.EuEu.reshape(data.n_time, data.n_freq)
    data.EvEv = data.EvEv.reshape(data.n_time, data.n_freq)
    data.EwEw = data.EwEw.reshape(data.n_time, data.n_freq)

    return data


def spec_nan(data, i):
    data.EuEu      [i] = math.nan; data.EvEv      [i] = math.nan; data.EwEw      [i] = math.nan
    data.EuEv_re   [i] = math.nan; data.EvEw_re   [i] = math.nan; data.EwEu_re   [i] = math.nan
    data.EuEv_im   [i] = math.nan; data.EvEw_im   [i] = math.nan; data.EwEu_im   [i] = math.nan
    data.EuEu_NC   [i] = math.nan; data.EvEv_NC   [i] = math.nan; data.EwEw_NC   [i] = math.nan
    data.EuEv_re_NC[i] = math.nan; data.EvEw_re_NC[i] = math.nan; data.EwEu_re_NC[i] = math.nan
    data.EuEv_im_NC[i] = math.nan; data.EvEw_im_NC[i] = math.nan; data.EwEu_im_NC[i] = math.nan
    data.EuEu_RC   [i] = math.nan; data.EvEv_RC   [i] = math.nan; data.EwEw_RC   [i] = math.nan
    data.EuEv_re_RC[i] = math.nan; data.EvEw_re_RC[i] = math.nan; data.EwEu_re_RC[i] = math.nan
    data.EuEv_im_RC[i] = math.nan; data.EvEw_im_RC[i] = math.nan; data.EwEu_im_RC[i] = math.nan
    data.EuEu_LC   [i] = math.nan; data.EvEv_LC   [i] = math.nan; data.EwEw_LC   [i] = math.nan
    data.EuEv_re_LC[i] = math.nan; data.EvEw_re_LC[i] = math.nan; data.EwEu_re_LC[i] = math.nan
    data.EuEv_im_LC[i] = math.nan; data.EvEw_im_LC[i] = math.nan; data.EwEu_im_LC[i] = math.nan
    #
    data.EuEu_raw  [i] = math.nan; data.EvEv_raw  [i] = math.nan; data.EwEw_raw  [i] = math.nan
    data.EuEu_amp  [i] = math.nan; data.EvEv_amp  [i] = math.nan; data.EwEw_amp  [i] = math.nan

    hf_hk.status_nan(data, i, 3)
