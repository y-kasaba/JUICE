"""
    JUICE RPWI HF SID3 (Full): L1a data list -- 2025/3/31
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
        # *** Flight data: Ver.2 ***
        """
        # 202401
        data_dir = '/Users/user/0-python/JUICE_data/Data-CDF/2024/01/26/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240126T083835_V01.cdf',
                        ]
        # 202407
        data_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/2024/07/01/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240701T011127_V01.cdf',
                        ]
        data_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/2024/07/06/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240706T121009_V01.cdf',
                        'JUICE_L1a_RPWI-HF-SID3_20240706T175202_V01.cdf',
                        ]
        # 202408-09  LEGA
        data_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/2024/08/19/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240819T202636_V01.cdf']
        data_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/2024/08/20/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240820T180734_V01.cdf']
        data_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/2024/08/22/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240822T095914_V01.cdf']         # all CAL
        data_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/2024/08/23/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240823T035818_V01.cdf']
        """
        data_dir = '/Users/user/D-Univ/data/data-JUICE/datasets/2024/09/09/'
        data_name_list = ['JUICE_L1a_RPWI-HF-SID3_20240909T093241_V01.cdf']

    print(data_dir)
    print(data_name_list)
    return data_dir, data_name_list