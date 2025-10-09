"""
    JUICE RPWI HF Status -- 2025/10/9
"""
import numpy as np
import math
import juice_cdf_lib   as hk_cdf

class struct:
    pass

# ---------------------------------------------------------------------
# --- AUX and Header --------------------------------------------------
# ---------------------------------------------------------------------
def status_read(cdf, data, sid):
    # Common
    data.epoch       = cdf['Epoch'][...]                        # all
    data.scet        = cdf['SCET'][...]                         # all

    # AUX ###
    data.ch_selected = cdf['ch_selected'][...]                  # SID-2
    data.cal_signal  = cdf['cal_signal'][...]                   # SID-2
    data.T_RWI_CH1   = np.float32(cdf['T_RWI_CH1'][...])        # SID-2
    data.T_RWI_CH2   = np.float32(cdf['T_RWI_CH2'][...])        # SID-2
    data.T_HF_FPGA   = np.float32(cdf['T_HF_FPGA'][...])        # SID-2
    #    cdf['Unique_ID']
    #    cdf['header_size']
    if sid in [2, 3, 4, 20, 5, 21]:     # SID-2/3/4/20/5/21
        data.RFI_rejection = cdf['RFI_rejection'][...]
        #    cdf['sweep_table']
        #    cdf['FFT_window']
        data.complex     = cdf['complex'][...]
        data.BG_subtract = cdf['BG_subtract'][...]
        data.BG_select   = cdf['BG_select'][...]
        data.BG_downlink = cdf['BG_downlink'][...]
        data.Pol_sep_thres = cdf['Pol_sep_thres'][...]
        data.Pol_sep_SW  = cdf['Pol_sep_SW'][...]
        data.N_block     = np.int64(cdf['N_block'][...])
        #    cdf['onboard_cal']
        #    cdf['proc_param0']
        #    cdf['proc_param1']
        #    cdf['proc_param2']
        #    cdf['proc_param3']
        #    cdf['Rich_data_flag']
    elif sid in [6, 22]:                # SID-6/22
        data.RFI_rejection = cdf['RFI_rejection'][...]
        #    cdf['sweep_table']
        #    cdf['FFT_window']
        data.N_lag       = np.int64(cdf['N_lag'][...])
    else:                               # SID-7/23
        data.N_block     = np.int16(cdf['N_block'][...])
        data.N_feed      = np.int16(cdf['N_feed'][...])
        data.N_lag       = np.int16(cdf['N_lag'][...])
        data.freq_center = cdf['freq_center'][...]
        #    cdf['N_skip']

    # Header
    data.RPWI_FSW_version = cdf['ISW_ver'][...]                 # all
    data.RPWI_FSW_version = data.RPWI_FSW_version[0]
    data.N_samp      = np.int64(cdf['N_samp'][...])             # SID-2
    data.N_step      = np.int64(cdf['N_step'][...])             # SID-2
    data.decimation  = cdf['decimation'][...]                   # SID-2
    data.ADC_ovrflw  = cdf['ADC_ovrflw'][...]                   # SID-2
    data.HF_QF       = cdf['HF_QF'][...]                        # SID-2
    #       cdf['pol']

    return data


def status_add(data, data1, sid):
    # Common
    data.epoch      = np.r_["0", data.epoch, data1.epoch]
    data.scet       = np.r_["0", data.scet, data1.scet]

    # AUX
    data.ch_selected = np.r_["0", data.ch_selected, data1.ch_selected]
    data.cal_signal  = np.r_["0", data.cal_signal, data1.cal_signal]
    data.T_RWI_CH1   = np.r_["0", data.T_RWI_CH1, data1.T_RWI_CH1]
    data.T_RWI_CH2   = np.r_["0", data.T_RWI_CH2, data1.T_RWI_CH2]
    data.T_HF_FPGA   = np.r_["0", data.T_HF_FPGA, data1.T_HF_FPGA]
    #    cdf['Unique_ID']
    #    cdf['header_size']
    if sid in [2, 3, 4, 20, 5, 21]:     # SID-2/3/4/20/5/21
        data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
        #    cdf['sweep_table']
        #    cdf['FFT_window']
        data.complex     = np.r_["0", data.complex, data1.complex]
        data.BG_downlink = np.r_["0", data.BG_downlink, data1.BG_downlink]
        data.BG_subtract = np.r_["0", data.BG_subtract, data1.BG_subtract]
        data.BG_select   = np.r_["0", data.BG_select, data1.BG_select]
        data.Pol_sep_thres = np.r_["0", data.Pol_sep_thres, data1.Pol_sep_thres]
        data.Pol_sep_SW  = np.r_["0", data.Pol_sep_SW, data1.Pol_sep_SW]
        data.N_block     = np.r_["0", data.N_block, data1.N_block]
        #    cdf['onboard_cal']
        #    cdf['proc_param0']
        #    cdf['proc_param1']
        #    cdf['proc_param2']
        #    cdf['proc_param3']
        #    cdf['Rich_data_flag']
    elif sid in [6, 22]:                # SID-6/22
        data.RFI_rejection = np.r_["0", data.RFI_rejection, data1.RFI_rejection]
        #    cdf['sweep_table']
        #    cdf['FFT_window']
        data.N_lag       = np.r_["0", data.N_lag, data1.N_lag]
    else:                               # SID-7/23
        data.N_block     = np.r_["0", data.N_block, data1.N_block]
        data.N_feed      = np.r_["0", data.N_feed, data1.N_feed]
        data.N_lag       = np.r_["0", data.N_lag, data1.N_lag]
        data.freq_center = np.r_["0", data.freq_center, data1.freq_center]
        #    cdf['N_skip']

    # Header
    data.N_samp      = np.r_["0", data.N_samp, data1.N_samp]
    data.N_step      = np.r_["0", data.N_step, data1.N_step]
    data.decimation  = np.r_["0", data.decimation, data1.decimation]
    data.ADC_ovrflw  = np.r_["0", data.ADC_ovrflw, data1.ADC_ovrflw]
    data.HF_QF       = np.r_["0", data.HF_QF, data1.HF_QF]
    #       cdf['pol']

    return data


def status_shaping(data, index, sid):
    # Common
    data.epoch       = data.epoch      [index]
    data.scet        = data.scet       [index]

    # AUX
    data.ch_selected = data.ch_selected[index]
    data.cal_signal  = data.cal_signal [index]
    data.T_RWI_CH1   = data.T_RWI_CH1  [index]
    data.T_RWI_CH2   = data.T_RWI_CH2  [index]
    data.T_HF_FPGA   = data.T_HF_FPGA  [index]
    #    cdf['Unique_ID']
    #    cdf['header_size']
    if sid in [2, 3, 4, 20, 5, 21]:     # SID-2/3/4/20/5/21
        data.RFI_rejection = data.RFI_rejection[index]
        #    cdf['sweep_table']
        #    cdf['FFT_window']
        data.complex     = data.complex    [index]
        data.BG_downlink = data.BG_downlink[index]
        data.BG_subtract = data.BG_subtract[index]
        data.BG_select   = data.BG_select  [index]
        data.Pol_sep_thres = data.Pol_sep_thres[index]
        data.Pol_sep_SW  = data.Pol_sep_SW [index]
        data.N_block     = data.N_block    [index]
        #    cdf['onboard_cal']
        #    cdf['proc_param0']
        #    cdf['proc_param1']
        #    cdf['proc_param2']
        #    cdf['proc_param3']
        #    cdf['Rich_data_flag']
    elif sid in [6, 22]:                # SID-6/22
        data.RFI_rejection = data.RFI_rejection[index]
        #    cdf['sweep_table']
        #    cdf['FFT_window']
        data.N_lag       = data.N_lag  [index]
    else:                               # SID-7/23
        data.N_block     = data.N_block    [index]
        data.N_feed      = data.N_feed     [index]
        data.N_lag       = data.N_lag      [index]
        data.freq_center = data.freq_center[index]

    # Header
    data.N_samp      = data.N_samp     [index]
    data.N_step      = data.N_step     [index]
    data.ADC_ovrflw  = data.ADC_ovrflw [index]
    data.decimation  = data.decimation [index]
    data.HF_QF       = data.HF_QF      [index]
    #       cdf['pol']

    return data


def status_nan(data, i, sid):
    # AUX
    data.ch_selected  [i] = math.nan
    data.cal_signal   [i] = math.nan
    data.T_RWI_CH1    [i] = math.nan
    data.T_RWI_CH2    [i] = math.nan
    data.T_HF_FPGA    [i] = math.nan
    #    cdf['Unique_ID']
    #    cdf['header_size']
    if sid in [2, 3, 4, 20, 5, 21]:     # SID-2/3/4/20/5/21
        data.RFI_rejection[i] = math.nan
        #    cdf['sweep_table']
        #    cdf['FFT_window']
        data.complex      [i] = math.nan
        data.BG_downlink  [i] = math.nan
        data.BG_subtract  [i] = math.nan
        data.BG_select    [i] = math.nan
        data.Pol_sep_thres[i] = math.nan
        data.Pol_sep_SW   [i] = math.nan
        data.N_block      [i] = math.nan
        #    cdf['onboard_cal']
        #    cdf['proc_param0']
        #    cdf['proc_param1']
        #    cdf['proc_param2']
        #    cdf['proc_param3']
        #    cdf['Rich_data_flag']
    elif sid in [6, 22]:                # SID-6/22
        data.RFI_rejection[i] = math.nan
        #    cdf['sweep_table']
        #    cdf['FFT_window']
        data.N_lag        [i] = math.nan
    else:                               # SID-7/23
        data.N_block      [i] = math.nan
        data.N_feed       [i] = math.nan
        data.N_lag        [i] = math.nan
        data.freq_center  [i] = math.nan


    # Header
    data.N_samp       [i] = math.nan
    data.N_step       [i] = math.nan
    data.ADC_ovrflw   [i] = math.nan
    data.ISW_ver      [i] = math.nan
    data.HF_QF        [i] = math.nan
    #       cdf['pol']
    
    return data