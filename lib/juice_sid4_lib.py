# JUICE RPWI HF SID4 (Burst surv): L1a QL -- 2023/10/25
class struct:
    pass

#---------------------------------------------------------------------
#--- SID20 ------------------------------------------------------------
#---------------------------------------------------------------------
def juice_getdata_hf_sid4(cdf):

    data = struct()

    # Data
    data.EuEu = cdf['EuEu'][...]
    data.EvEv = cdf['EvEv'][...]
    data.EwEw = cdf['EwEw'][...]
    data.EuEv_re = cdf['EuEv_re'][...]
    data.EuEv_im = cdf['EuEv_im'][...]
    data.EvEw_re = cdf['EvEw_re'][...]
    data.EvEw_im = cdf['EvEw_im'][...]
    data.EwEu_re = cdf['EwEu_re'][...]
    data.EwEu_im = cdf['EwEu_im'][...]

    data.EuiEui = cdf['EuiEui'][...]
    data.EuqEuq = cdf['EuqEuq'][...]
    data.EviEvi = cdf['EviEvi'][...]
    data.EvqEvq = cdf['EvqEvq'][...]
    data.EwiEwi = cdf['EwiEwi'][...]
    data.EwqEwq = cdf['EwqEwq'][...]

    data.EuiEvi = cdf['EuiEvi'][...]
    data.EviEwi = cdf['EviEwi'][...]
    data.EwiEui = cdf['EwiEui'][...]
    data.EuqEvq = cdf['EuiEvq'][...]
    data.EvqEwq = cdf['EviEwq'][...]
    data.EwqEuq = cdf['EwiEuq'][...]

    data.EuiEuq = cdf['EuiEuq'][...]
    data.EviEvq = cdf['EviEvq'][...]
    data.EwiEwq = cdf['EwiEwq'][...]

    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]

    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]

    data.EuiEvq = cdf['EuiEvq'][...]
    data.EuqEvi = cdf['EuqEvi'][...]
    data.EviEwq = cdf['EviEwq'][...]
    data.EvqEwi = cdf['EvqEwi'][...]
    data.EwiEuq = cdf['EwiEuq'][...]
    data.EwqEui = cdf['EwqEui'][...]


    # AUX
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    data.complex = cdf['complex'][...]
    #
    data.cal_signal = cdf['cal_signal'][...]
    data.sweep_table = cdf['sweep_table'][...]      # (fixed: not defined in V.2)
    data.onboard_cal = cdf['onboard_cal'][...]      # (not used)
    data.BG_subtract = cdf['BG_subtract'][...]
    data.BG_select = cdf['BG_select'][...]
    data.FFT_window = cdf['FFT_window'][...]
    data.RFI_rejection = cdf['RFI_rejection'][...]
    data.Pol_sep_thres = cdf['Pol_sep_thres'][...]
    data.Pol_sep_SW = cdf['Pol_sep_SW'][...]
    data.overflow_U = cdf['overflow_U'][...]        # (fixed: not defined in V.2)
    data.overflow_V = cdf['overflow_V'][...]        # (fixed: not defined in V.2)
    data.overflow_W = cdf['overflow_W'][...]        # (fixed: not defined in V.2)
    data.proc_param0 = cdf['proc_param0'][...]
    data.proc_param1 = cdf['proc_param1'][...]
    data.proc_param2 = cdf['proc_param2'][...]
    data.proc_param3 = cdf['proc_param3'][...]
    data.BG_downlink = cdf['BG_downlink'][...]

    data.N_block = cdf['N_block'][...]
    data.T_RWI_CH1 = cdf['T_RWI_CH1'][...]
    data.T_RWI_CH2 = cdf['T_RWI_CH2'][...]
    data.T_HF_FPGA = cdf['T_HF_FPGA'][...]

    # Header
    data.N_samp = cdf['N_samp'][...]
    data.N_step = cdf['N_step'][...]
    data.decimation = cdf['decimation'][...]
    data.pol = cdf['pol'][...]
    data.B0_startf = cdf['B0_startf'][...]
    data.B0_stopf = cdf['B0_stopf'][...]
    data.B0_step = cdf['B0_step'][...]
    data.B0_repeat = cdf['B0_repeat'][...]
    data.B0_subdiv = cdf['B0_subdiv'][...]

    return data