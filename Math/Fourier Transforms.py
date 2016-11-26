# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!/usr/bin/python

from scipy.fftpack import fft, ifft
import numpy as np

x = np.array([1.0,2.0,1.0,-1.0,1.5])
y = fft(x)
print y
yinv = ifft(y)
print yinv