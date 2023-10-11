class struct:
    pass

#---------------------------------------------------------------------
#--- SID21 ------------------------------------------------------------
#---------------------------------------------------------------------
def juice_getdata_hf_sid21(cdf):

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

    data.frequency = cdf['frequency'][...]
    data.freq_step = cdf['freq_step'][...]
    data.freq_width = cdf['freq_width'][...]

    data.epoch = cdf['Epoch'][...]
    data.scet = cdf['SCET'][...]

    # AUX
    data.U_selected = cdf['U_selected'][...]
    data.V_selected = cdf['V_selected'][...]
    data.W_selected = cdf['W_selected'][...]
    data.N_component = cdf['N_component'][...]      # [b2:U  b1:V  b0:W]
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
    data.freq_start = cdf['freq_start'][...]        # [same with ‘B0_startf’]

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

    # CUT
    n_num = data.B0_step[0] * data.B0_subdiv[0]
    if n_num < data.EuEu.shape[1]:
        print("Cut: ", data.EuEu.shape[1], " ->", n_num)
        data.EuEu = data.EuEu[:, 0:n_num]
        data.EvEv = data.EvEv[:, 0:n_num]
        data.EwEw = data.EwEw[:, 0:n_num]
        data.EuEv_re = data.EuEv_re[:, 0:n_num]
        data.EuEv_im = data.EuEv_im[:, 0:n_num]
        data.EvEw_re = data.EvEw_re[:, 0:n_num]
        data.EvEw_im = data.EvEw_im[:, 0:n_num]
        data.EwEu_re = data.EwEu_re[:, 0:n_num]
        data.EwEu_im = data.EwEu_im[:, 0:n_num]
        data.frequency = data.frequency[:, 0:n_num]
        data.freq_step = data.freq_step[:, 0:n_num]
        data.freq_width = data.freq_width[:, 0:n_num]

    return data