"""
    JUICE RPWI HF math -- 2024/9/19
"""
import copy
import numpy as np
from scipy.signal import medfilt


# ---------------------------------------------------------------------
# RFI rejection:  Mode -- 0:median   1:max reject   2:min
# ---------------------------------------------------------------------
def clean_rfi(power, kernel_size=5, mode=0):
    """
    Input:  power, kernel_size
    Output: clean_power
    """
    if    mode == 0:
        clean_power = medfilt(power, kernel_size)
    elif  mode == 1:
        num = power.shape[0]
        d = int(kernel_size/2)
        clean_power = copy.copy(power)
        for i in range (num-d):
            if i-d>0:
                s = power[i-d:i+d+1]
                #s = [power[i-1], power[i], power[i+1]]
                clean_power[i] = (sum(s) - max(s)) / (d*2)
    else:
        num = power.shape[0]
        d = int(kernel_size/2)
        clean_power = copy.copy(power)
        for i in range (num-d):
            if i-d>0:
                s = power[i-d:i+d+1]
                #s = [power[i-1], power[i], power[i+1]]
                clean_power[i] = min(s) 
    return clean_power
