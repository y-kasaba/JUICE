"""
    JUICE RPWI HF math -- 2024/7/23
"""
import numpy as np
import math
from scipy.signal import medfilt


# ---------------------------------------------------------------------
# --- HID-2 RAW data --------------------------------------------------
# ---------------------------------------------------------------------
# FFT frequency [kHz] --- retun "df"
def _fft_freq(n_samp, freq_array, frequency, dt):
    freq = np.fft.fftfreq(n_samp, d=dt)/1000. + freq_array
    # frequency.extend( freq[np.int16(n_samp*2/3+1):n_samp] )
    # frequency.extend( freq[0:np.int16(n_samp/3-1)] )

    frequency.extend(freq[np.int16(n_samp/2):n_samp])
    frequency.extend(freq[0:np.int16(n_samp/2)])
    return freq[1] - freq[0]


# ---------------------------------------------------------------------
# FFT power
def _fft_power(n_samp, E_i, E_q, E_power, df, unit_mode, ave_mode):
    # Hunning
    window = np.hanning(n_samp)
    acf = 1/(sum(window)/n_samp)
    s = np.fft.fft((E_i - E_q * 1j) * window)
    power = np.power(np.abs(s) / n_samp, 2.0) * acf * acf

    if unit_mode > 0:
        power = power / (df * 1000)

    if ave_mode == 0:
        # E_power.extend(power[np.int16(n_samp*2/3+1):n_samp])
        # E_power.extend(power[0:np.int16(n_samp/3-1)])
        E_power.extend(power[np.int16(n_samp/2):n_samp])
        E_power.extend(power[0:np.int16(n_samp/2)])
        return

    if ave_mode == 1:
        power0 = np.sum(power[np.int16(n_samp*2/3+1):n_samp]) \
            + np.sum(power[0:np.int16(n_samp/3-1)])
    elif ave_mode == 2:
        power0 = np.median(power[np.int16(n_samp*2/3+1):n_samp])*(n_samp/3) \
            + np.median(power[0:np.int16(n_samp/3-1)])*(n_samp/3-1)
    else:
        power0 = min(power[np.int16(n_samp*2/3+1):n_samp])*(n_samp/3) \
            + min(power[0:np.int16(n_samp/3-1)])*(n_samp/3-1)
    E_power.append(power0)
    return


# ---------------------------------------------------------------------
# mean power
# ---------------------------------------------------------------------
def _mean_power(E_i_array, E_q_array, E_power, df, unit_mode):
    """
    Input:  E_i_array, E_q_array, "E_power", df, unit_mode
    Output: E_power
    """
    power = np.mean(E_i_array**2 + E_q_array**2, axis=1)
    if unit_mode > 0:
        power = power / (df * 1000)
    E_power.extend(power)


# ---------------------------------------------------------------------
# RFI rejection
# ---------------------------------------------------------------------
def clean_rfi(power, kernel_size=5):
    """
    Input:  power, kernel_size
    Output: clean_power
    """
    clean_power = medfilt(power, kernel_size)
    # clean_power = minfilt(power, kernel_size)
    return clean_power


# ---------------------------------------------------------------------
# --- Stokes parameters --------------------------------------------------
# ---------------------------------------------------------------------
def get_stokes(p1, p2, re, im):
    """
    Input:  EuEu, EvEv, EuEv_re, EuEv_im
    Output: I, Q, U, V: Stokes parameters [Any]
    """
    m = p1.shape[0]
    n = p1.shape[1]
    I = np.zeros((m, n))
    Q = np.zeros((m, n))
    U = np.zeros((m, n))
    V = np.zeros((m, n))
    if p1[0][0] > 0:
        I = p1 + p2     # total
        Q = p1 - p2     # 0deg -  90deg
        U = re * 2.0    # 45deg - 135deg
        V = im * 2.0    # Right -  Left  (minus?)
    return I, Q, U, V


# ---------------------------------------------------------------------
def get_pol(I, Q, U, V):
    """
    Input:  I, Q, U, V: Stokes parameters [Any]
    Output: DoP, DoL, DoC, Ang
    """
    m = I.shape[0];  n = I.shape[1]
    dop = np.zeros((m, n))
    dol = ang = np.zeros((m, n))
    doc = np.zeros((m, n))
    ang = np.zeros((m, n))
    for j in range(m):
        if I[j][0] > 0 and Q[j][0] > -1e30 and U[j][0] > -1e30 and V[j][0] > -1e30:
            dop[j] = (Q[j]*Q[j] + U[j]*U[j] + V[j]*V[j])**0.5 / I[j]   # Degree of Total Polarization
            dol[j] = (Q[j]*Q[j] + U[j]*U[j])**0.5 / I[j]               # Degree of Linear Polarization
            doc[j] = V[j] / I[j]                                       # Degree of Circular Polarization

            for i in range(n):
                if U[j][i] >= 0.0 and Q[j][i] > 0.0:    # 0-90
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi
                elif U[j][i] <= 0.0 and Q[j][i] > 0.0:  # 270-360
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi + 180.
                elif Q[j][i] < 0.0:                     # 90-270
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi + 90.
                else:
                    if U[j][i] >= 0.0:
                        ang[j][i] = 45.
                    else:
                        ang[j][i] = 135.
    return dop, dol, doc, ang


# ---------------------------------------------------------------------
def get_pol_3D(I, Q, U, Vu, Vv, Vw):
    """
    Input:  I, Q, U, V: Stokes parameters [Any]
    Output: DoP, DoL, DoC, Ang, k_lon, k_lat
    """
    m = I.shape[0]
    n = I.shape[1]
    dop = np.zeros((m, n))
    dol = np.zeros((m, n))
    doc = np.zeros((m, n))
    ang = np.zeros((m, n))
    k_lon = np.zeros((m, n))
    k_lat = np.zeros((m, n))
    if I[0][0] > 0:
        V_mag = (Vu*Vu + Vv*Vv + Vw*Vw)**0.5
        dop = (Q*Q + U*U + V_mag*V_mag)**0.5 / I  # Degree of Total Polari.
        dol = (Q*Q + U*U)**0.5 / I                # Degree of Linear Polari.
        doc = V_mag / I                           # Degree of Circular Polari.

        # Linear Polarization Angle (deg)
        for j in range(m):
            for i in range(n):
                if U[j][i] >= 0.0 and Q[j][i] > 0.0:    # 0-90
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi
                elif U[j][i] <= 0.0 and Q[j][i] > 0.0:  # 270-360
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi + 180.
                elif Q[j][i] < 0.0:                     # 90-270
                    ang[j][i] = 0.5*math.atan(U[j][i]/Q[j][i])*180./math.pi + 90.
                else:
                    if U[j][i] >= 0.0:
                        ang[j][i] = 45.
                    else:
                        ang[j][i] = 135.

                #k_lat[j][i] = math.asin(Vw[j][i]/(Vu[j][i]*Vu[j][i] + Vv[j][i]*Vv[j][i])**0.5) * 180./math.pi
                k_lat[j][i] = math.atan2(Vw[j][i], (Vu[j][i]*Vu[j][i] + Vv[j][i]*Vv[j][i])**0.5) * 180./math.pi
                k_lon[j][i] = math.atan2(Vv[j][i], Vu[j][i]) * 180.0/math.pi
    return dop, dol, doc, ang, k_lon, k_lat


"""
# ---------------------------------------------------------------------
# --- Stokes parameter tests ------------------------------------------
# ---------------------------------------------------------------------
def get_stokes2(p1, p2, re, im):
    # Input:  EuEu, EvEv, EuEv_re, EuEv_im
    # Output: I, Q, U, V: Stokes parameters [Any]

    m = p1.shape[0]
    I = np.zeros(m)
    Q = np.zeros(m)
    U = np.zeros(m)
    V = np.zeros(m)
    if p1[0] > 0:
        I = p1 + p2     # total
        Q = p1 - p2     # 0deg -  90deg
        U = re * 2.0    # 45deg - 135deg
        V = im * 2.0    # Right -  Left  (minus?)
    return I, Q, U, V


# ---------------------------------------------------------------------
def get_pol2(I, Q, U, V):
    # Input:  I, Q, U, V: Stokes parameters [Any]
    # Output: DoP, DoL, DoC, Ang

    m = I.shape[0]
    dop = np.zeros(m)
    dol = ang = np.zeros(m)
    doc = np.zeros(m)
    ang = np.zeros(m)
    if I[0] > 0:
        dop = (Q*Q + U*U + V*V)**0.5 / I   # Degree of Total Polarization
        dol = (Q*Q + U*U)**0.5 / I         # Degree of Linear Polarization
        doc = V / I                        # Degree of Circular Polarization

        # Linear Polarization Angle (deg)
        for j in range(m):
            if U[j] >= 0.0 and Q[j] > 0.0:    # 0-90
                ang[j] = 0.5*math.atan(U[j]/Q[j])*180./math.pi
            elif U[j] <= 0.0 and Q[j] > 0.0:  # 270-360
                ang[j] = 0.5*math.atan(U[j]/Q[j])*180./math.pi + 180.
            elif Q[j] < 0.0:                  # 90-270
                ang[j] = 0.5*math.atan(U[j]/Q[j])*180./math.pi + 90.
            else:
                if U[j] >= 0.0:
                    ang[j] = 45.
                else:
                    ang[j] = 135.
    return dop, dol, doc, ang
"""