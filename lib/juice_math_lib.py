import numpy as np

#---------------------------------------------------------------------
#--- HID-2 RAW data --------------------------------------------------
#---------------------------------------------------------------------
# FFT frequency [kHz]
def _fft_freq(n_samp, freq_array, frequency, dt):
    freq = np.fft.fftfreq(n_samp, d=dt)/1000. + freq_array

    frequency.extend( freq[np.int16(n_samp/2+n_samp/6):n_samp] )
    frequency.extend( freq[0:np.int16(n_samp/2-n_samp/6)] )
    return freq[1] - freq[0]

#---------------------------------------------------------------------
# FFT power
def _fft_power(n_samp, E_i, E_q, E_power, dt, df, hz_mode):
    # Hunning
    window = np.hanning( n_samp ) 
    acf = 1/(sum(window)/n_samp)
    s = np.fft.fft((E_i - E_q * 1j) * window)
    power = np.power(np.abs(s) / n_samp, 2.0) * acf * acf
    
    # hz_mode:  0: sum   1: /Hz
    if hz_mode > 0:
        power = power / (df * 1000)

    E_power.extend( power[np.int16(n_samp/2+n_samp/6):n_samp] )
    E_power.extend( power[0:np.int16(n_samp/2-n_samp/6)] )   
    return

#---------------------------------------------------------------------
# mean power
def _mean_power(E_i_array, E_q_array, E_power, df, hz_mode):
    power = np.mean(E_i_array**2 + E_q_array**2, axis=1)

    # hz_mode:  0: sum   1: /Hz
    if hz_mode > 0:
        power = power / (df * 1000)

    E_power.extend( power )
    return