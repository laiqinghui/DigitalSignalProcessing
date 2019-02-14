import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def genDTSingalOmega(A, w, Phi, numSamples):
    n=np.arange(0,numSamples,1)
    y=A*np.cos(w*n+Phi)
    return n,y

H_low =  [0.06523, 0.14936,0.21529,0.2402,0.21529,0.14936,0.06523]
H_high =  [-0.06523, -0.14936,-0.21529,0.7598,-0.21529,-0.14936,-0.06523]
H_combined = np.convolve(H_low,H_high)

A=1; small_omega=0.5*np.pi; Phi = 0; numSamples = 300
[n,x_high] =  genDTSingalOmega(A,small_omega,Phi, numSamples)

A=1; small_omega=0.05*np.pi; Phi = 0; numSamples = 300
[n,x_low] =  genDTSingalOmega(A,small_omega,Phi, numSamples)

# x_high = np.zeros((300))
# x_high[::2] = -1
# x_high[1::2] = 1
#
# x_low = np.zeros((300))
# x_low[::20] = -1
# x_low[1::20] = 1

y_l_l  = np.convolve(x_low,H_low)
y_h_l  = np.convolve(x_high,H_low)
y_l_h  = np.convolve(x_low,H_high)
y_h_h  = np.convolve(x_high,H_high)
y_l_lh  = np.convolve(x_low,H_combined)
y_h_lh  = np.convolve(x_high,H_combined)
# showing that convolution can be realised by np.convolve and scipy.signal.lfilter(BCooeff,[1],impulseX)
# Lets save the file, fname, sequence, and samplingrate needed
plt.subplot(2,3,1)
plt.plot(x_low,'b-+')
plt.plot(y_l_l,'g-+')
plt.xlabel('sample n'); plt.ylabel('Amplitude')
plt.title('LowFre_by_LowPass(h1)')

plt.subplot(2,3,4)
plt.plot(x_high,'b-+')
plt.plot(y_h_l,'g-+')
plt.xlabel('sample n'); plt.ylabel('Amplitude')
plt.title('HighFre_by_LowPass(h1)')

plt.subplot(2,3,2)
plt.plot(x_low,'b-+')
plt.plot(y_l_h,'g-+')
plt.xlabel('sample n'); plt.ylabel('Amplitude')
plt.title('LowFre_by_HighPass(h2)')

plt.subplot(2,3,5)
plt.plot(x_high,'b-+')
plt.plot(y_h_h,'g-+')
plt.xlabel('sample n'); plt.ylabel('Amplitude')
plt.title('HighFre_by_HighPass(h2)')

plt.subplot(2,3,3)
plt.plot(x_low,'b-+')
plt.plot(y_l_lh,'g-+')
plt.xlabel('sample n'); plt.ylabel('Amplitude')
plt.title('LowFre_by_All(h1*h2)')

plt.subplot(2,3,6)
plt.plot(x_high,'b-+')
plt.plot(y_h_lh,'g-+')
plt.xlabel('sample n'); plt.ylabel('Amplitude')
plt.title('HighFre_by_All(h1*h2)')

plt.show()