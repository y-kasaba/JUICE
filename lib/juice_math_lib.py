#---------------------------------------------------------------------
#--- Y Kasaba   2023/10/11 -------------------------------------------
#---------------------------------------------------------------------
import numpy as np
# import statistics

#---------------------------------------------------------------------
#--- HID-2 RAW data --------------------------------------------------
#---------------------------------------------------------------------
# FFT frequency [kHz] --- retun "df"
def _fft_freq(n_samp, freq_array, frequency, dt):
    freq = np.fft.fftfreq(n_samp, d=dt)/1000. + freq_array
    frequency.extend( freq[np.int16(n_samp*2/3+1):n_samp] )
    frequency.extend( freq[0:np.int16(n_samp/3-1)] )
    return freq[1] - freq[0]

#---------------------------------------------------------------------
# FFT power
def _fft_power(n_samp, E_i, E_q, E_power, df, unit_mode, ave_mode):
    # Hunning
    window = np.hanning( n_samp ) 
    acf = 1/(sum(window)/n_samp)
    s = np.fft.fft((E_i - E_q * 1j) * window)
    power = np.power(np.abs(s) / n_samp, 2.0) * acf * acf

    if unit_mode > 0:
        power = power / (df * 1000)

    if (ave_mode == 0):
        E_power.extend(power[np.int16(n_samp*2/3+1):n_samp])
        E_power.extend(power[0:np.int16(n_samp/3-1)])
        return

    if (ave_mode == 1):
        power0 = np.sum(power[np.int16(n_samp*2/3+1):n_samp])+np.sum(power[0:np.int16(n_samp/3-1)])
    elif (ave_mode == 2):
        power0 = np.median(power[np.int16(n_samp*2/3+1):n_samp])*(n_samp/3) + np.median(power[0:np.int16(n_samp/3-1)])*(n_samp/3-1)
    else:
        power0 = min(power[np.int16(n_samp*2/3+1):n_samp])*(n_samp/3) + min(power[0:np.int16(n_samp/3-1)])*(n_samp/3-1)                            
    E_power.append(power0)
    return

#---------------------------------------------------------------------
# mean power
def _mean_power(E_i_array, E_q_array, E_power, df, unit_mode):
    power = np.mean(E_i_array**2 + E_q_array**2, axis=1)

    if unit_mode > 0:
        power = power / (df * 1000)

    E_power.extend( power )
    return

#---------------------------------------------------------------------
#--- HID-3 RAW data --------------------------------------------------
#---------------------------------------------------------------------
def clean_rfi(power, kernel_size=5):
    from scipy.signal import medfilt
    clean_power = medfilt(power, kernel_size)
    # clean_power = minfilt(power, kernel_size)
    return clean_power


#---------------------------------------------------------------------
#--- HID-3 RAW data --------------------------------------------------
#---------------------------------------------------------------------
def hf_proc_get_stokes(p1, p2, re, im):
    I = p1 + p2;
    Q = p1 - p2;
    U = re * 2.0;
    V = im * 2.0;
    return I, Q, U, V 