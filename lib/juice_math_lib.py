# import glob
# import spacepy.pycdf
import numpy as np
# import statistics

# frequency [kHz]
def _fft_freq(n_samp, freq_array, frequency, dt):
    freq = np.fft.fftfreq(n_samp, d=dt)/1000. + freq_array
    # frequency.extend( freq )
    # frequency.extend( freq[np.int16(n_samp/2):n_samp] )
    # frequency.extend( freq[0:np.int16(n_samp/2)] )
    # frequency.extend( freq[np.int16(n_samp/2+n_samp/8):n_samp] )
    # frequency.extend( freq[0:np.int16(n_samp/2-n_samp/8)] )
    frequency.extend( freq[np.int16(n_samp/2+n_samp/6):n_samp] )
    frequency.extend( freq[0:np.int16(n_samp/2-n_samp/6)] )

    # print(n_samp, len(freq), len(freq[np.int16(n_samp/2+n_samp/8):n_samp]), len(freq[0:np.int16(n_samp/2-n_samp/8)]))
    # print(freq[np.int16(n_samp/2)], freq[np.int16(n_samp/2+n_samp/8)], freq[np.int16(n_samp/2-n_samp/8)], freq[np.int16(n_samp/2-1)])
    return freq[1] - freq[0]

# power
# hz_mode:  0: sum   1: /Hz
def _fft_power(n_samp, E_i, E_q, E_power, dt, df, hz_mode):
    num = len ( E_i )
    window = np.hanning( num ) 
    E = (E_i - E_q * 1j) * window
    s = np.fft.fft(E)
    power = np.power(np.abs(s) / n_samp, 2.0) 
    acf = 1/(sum(window)/num)
    power = acf * acf * power
    
    # No Hunning
    s = np.fft.fft(E_i - E_q * 1j)
    power = np.power(np.abs(s) / n_samp, 2.0) 

    if hz_mode > 0:
        power = power / (df * 1000)
    # E_power.extend( power )
    # E_power.extend( power[np.int16(n_samp/2):n_samp] )
    # E_power.extend( power[0:np.int16(n_samp/2)] )
    # E_power.extend( power[np.int16(n_samp/2+n_samp/8):n_samp] )
    # E_power.extend( power[0:np.int16(n_samp/2-n_samp/8)] )
    E_power.extend( power[np.int16(n_samp/2+n_samp/6):n_samp] )
    E_power.extend( power[0:np.int16(n_samp/2-n_samp/6)] )
    
    return
