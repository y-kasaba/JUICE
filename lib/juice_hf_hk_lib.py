"""
    JUICE RPWI HF Status -- 2026/3/19
"""
import numpy as np
import math
import juice_cdf_lib   as hk_cdf

class struct:
    pass

# ---------------------------------------------------------------------
# --- AUX and Header --------------------------------------------------
# ---------------------------------------------------------------------
def status_read(cdf, data):
    # HF-ID 
    #   b15-8: SID
    #   b7-4:  ISW_version
    #   b3-0:  config       0: [SID-2]
    #                       1: [SID-20/4] (dt=2s)   2: (dt=1s)          3: (dt=0.5s)    4: (dt=0.2s)
    #                       5: [SID-3] comp=2       6 [SID-3] comp=1    8: [SID-21/5]   A: [SID-23/7]
    data.HF_ID = cdf['HF_ID'][...]
    data.sid              = (data.HF_ID[0] >> 8) & 0xFF
    data.RPWI_FSW_version = (data.HF_ID[0] >> 4) & 0xF
    data.HF_config        =  data.HF_ID[0]       & 0xF

    # HF-QF
    #   b0:RWI-OFF      0:ON    1:off 
    #   b1:cal_signal   0:non   1:CAL
    #   b2-3:overflow   0:n/a   1:few ovf   2: ovf>1%   3: ovf>10%
    #   b4: RIME        0:n/a   1:Activated
    #   b5: Eclipse     0:n/a   1:Eclipse
    #   b6-7:reserved   [b0-1:0x03 -- Error Data]
    data.HF_QF       = cdf['HF_QF'][...]
    
    # common
    data.epoch = cdf['Epoch'][...];                         data.scet = cdf['SCET'][...]
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...]);   data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...]);   data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])
    data.cal_signal  = cdf['cal_signal'][...];              data.ADC_ovrflw  = cdf['ADC_ovrflw'][...];              data.decimation  = cdf['decimation'][...]

    if data.sid in [3, 4, 20, 5, 21, 6, 9, 22, 7, 8]:       data.ch_selected = cdf['ch_selected'][...]
    if data.sid in [3]:
        data.RFI_rejection  = cdf['RFI_rejection'][...]
        data.BG_subtract    = cdf['BG_subtract'][...];      data.BG_select   = cdf['BG_select'][...];       data.BG_downlink  = cdf['BG_downlink'][...]
        data.Pol_sep_thres  = cdf['Pol_sep_thres'][...];    data.Pol_sep_SW  = cdf['Pol_sep_SW'][...]
        data.proc_param0    = cdf['proc_param0'][...];      data.proc_param1 = cdf['proc_param1'][...]
        data.proc_param2    = cdf['proc_param2'][...];      data.proc_param3 = cdf['proc_param3'][...]
        data.sweep_table    = cdf['sweep_table'][...];      data.Ver_tbl_freq   = cdf['Ver_tbl_freq'][...]; data.Ver_tbl_mask = cdf['Ver_tbl_mask'][...]
    if data.sid in [3, 4, 20, 21]:                          data.complex     = cdf['complex'][...]
    if data.sid in [7, 8, 23]:                              data.frequency   = cdf['frequency'][...]

    if data.sid in [2, 8, 23]:                      data.N_samp     = np.int64(cdf['N_samp'][...])
    if data.sid in [2, 3, 4, 20, 5, 21, 6, 9, 22]:  data.N_step     = np.int64(cdf['N_step'][...])         # SID-2,3,4/20,5/21,6/22
    if data.sid in [20, 7, 8, 23]:                  data.N_block    = np.int64(cdf['N_block'][...])
    if data.sid in [8]:                             data.N_block_ID = np.int64(cdf['N_block_ID'][...])
    if data.sid in [6, 9, 22, 7]:                   data.N_lag      = np.int64(cdf['N_lag'][...])
    if data.sid in [9]:                             data.freq_ID    = np.int64(cdf['freq_ID'][...])
    return data


def status_add(data, data1):
    data.HF_ID = np.r_["0", data.HF_ID, data1.HF_ID];   data.HF_QF = np.r_["0", data.HF_QF, data1.HF_QF]
    
    # common
    data.epoch = np.r_["0", data.epoch, data1.epoch];   data.scet  = np.r_["0", data.scet, data1.scet]
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.decimation  = np.r_["0", data.decimation, data1.decimation]

    if data.sid in [3, 4, 20, 5, 21, 6, 9, 22, 7, 8]:       data.ch_selected = np.r_["0", data.ch_selected, data1.ch_selected]
    if data.sid in [3]:
        data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
        data.BG_subtract   = np.r_["0", data.BG_subtract, data1.BG_subtract]
        data.BG_select     = np.r_["0", data.BG_select, data1.BG_select]
        data.BG_downlink   = np.r_["0", data.BG_downlink, data1.BG_downlink]
        data.Pol_sep_thres = np.r_["0", data.Pol_sep_thres, data1.Pol_sep_thres]
        data.Pol_sep_SW    = np.r_["0", data.Pol_sep_SW, data1.Pol_sep_SW]
        data.proc_param0   = np.r_["0", data.proc_param0, data1.proc_param0]
        data.proc_param1   = np.r_["0", data.proc_param1, data1.proc_param1]
        data.proc_param2   = np.r_["0", data.proc_param2, data1.proc_param2]
        data.proc_param3   = np.r_["0", data.proc_param3, data1.proc_param3]
        data.sweep_table   = np.r_["0", data.sweep_table, data1.sweep_table]
        data.Ver_tbl_freq  = np.r_["0", data.Ver_tbl_freq, data1.Ver_tbl_freq]
        data.Ver_tbl_mask  = np.r_["0", data.Ver_tbl_mask, data1.Ver_tbl_mask]
    if data.sid in [3, 4, 20, 21]:                  data.complex    = np.r_["0", data.complex, data1.complex]
    if data.sid in [7, 8, 23]:                      data.frequency  = np.r_["0", data.frequency, data1.frequency]

    if data.sid in [2, 8, 23]:                      data.N_samp     = np.r_["0", data.N_samp, data1.N_samp]
    if data.sid in [2, 3, 4, 20, 5, 21, 6, 9, 22]:  data.N_step     = np.r_["0", data.N_step, data1.N_step]
    if data.sid in [20, 7, 8, 23]:                  data.N_block    = np.r_["0", data.N_block, data1.N_block]
    if data.sid in [8]:                             data.N_block_ID = np.r_["0", data.N_block_ID, data1.N_block_ID]
    if data.sid in [6, 9, 22, 7]:                   data.N_lag      = np.r_["0", data.N_lag, data1.N_lag]
    if data.sid in [9]:                             data.freq_ID    = np.r_["0", data.freq_ID, data1.freq_ID]
    return data


def status_shaping(data, index):
    data.HF_ID = data.HF_ID[index];             data.HF_QF      = data.HF_QF[index]

    # common
    data.epoch      = data.epoch      [index];  data.scet       = data.scet       [index]
    data.T_RWI_CH1  = data.T_RWI_CH1  [index];  data.T_RWI_CH2  = data.T_RWI_CH2  [index];  data.T_HF_FPGA  = data.T_HF_FPGA  [index]
    data.cal_signal = data.cal_signal [index];  data.ADC_ovrflw = data.ADC_ovrflw [index];  data.decimation = data.decimation [index]
    
    if data.sid in [3, 4, 20, 5, 21, 6, 9, 22, 7, 8]:   data.ch_selected = data.ch_selected[index]
    if data.sid in [3]:
        data.RFI_rejection = data.RFI_rejection[index]
        data.BG_subtract   = data.BG_subtract[index];   data.BG_select    = data.BG_select[index];    data.BG_downlink  = data.BG_downlink[index]
        data.Pol_sep_thres = data.Pol_sep_thres[index]; data.Pol_sep_SW   = data.Pol_sep_SW [index]
        data.proc_param0   = data.proc_param0[index];   data.proc_param1  = data.proc_param1[index]
        data.proc_param2   = data.proc_param2[index];   data.proc_param3  = data.proc_param3[index]
        data.sweep_table   = data.sweep_table[index];   data.Ver_tbl_freq = data.Ver_tbl_freq[index]; data.Ver_tbl_mask = data.Ver_tbl_mask[index]
    if data.sid in [3, 4, 20, 21]:              data.complex    = data.complex   [index]
    if data.sid in [7, 8, 23]:                  data.frequency  = data.frequency [index]

    if data.sid in [2, 8, 23]:                  data.N_samp     = data.N_samp    [index]
    if data.sid in [2, 3, 4, 20, 5, 21, 6, 22]: data.N_step     = data.N_step    [index]
    if data.sid in [20, 7, 8, 23]:              data.N_block    = data.N_block   [index]
    if data.sid in [8]:                         data.N_block_ID = data.N_block_ID[index]
    if data.sid in [6, 9, 22, 7]:               data.N_lag      = data.N_lag     [index]
    if data.sid in [9]:                         data.freq_ID    = data.freq_ID   [index]
    return data


def status_nan(data, i):
    data.T_RWI_CH1[i] = math.nan;  data.T_RWI_CH2[i] = math.nan;  data.T_HF_FPGA[i] = math.nan
    return data