import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile  as wavfile
import winsound
import time
# plotting 3D complex plane
from mpl_toolkits.mplot3d import Axes3D

# Lets generate and plot complex exponential in 2-d, polar and 3d plot
# how to include phase shift? Phi != 0?
numSamples = 36
A=0.98; w1=0.1*np.pi;
n = np.arange(0, numSamples, 1)
y1 = np.multiply(np.power(A, n), np.exp(1j * w1 * n))


# # plotting in 2-D, the real and imag in the same figure
# plt.figure(1)
# plt.plot(n, y1[0:numSamples].real,'r--o')
# plt.plot(n, y1[0:numSamples].imag,'g--o')
# plt.xlabel('sample index n'); plt.ylabel('y[n]')
# plt.title('Complex exponential (red=real) (green=imag)')
# plt.grid()
# plt.show()
#
# plotting in polar, understand what the spokes are
plt.figure(2)
for x in y1:
    plt.polar([0,np.angle(x)],[0,np.abs(x)],marker='o')
    #plt.polar([0,np.angle(x)],[0,np.abs(x)],marker='o')

plt.title('Polar plot showing phasors at n=0..N')
plt.show()

# plotting 3D complex plane
plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
reVal = y1[0:numSamples].real
imgVal = y1[0:numSamples].imag
#ax.plot(n,reVal, imgVal,  label='complex exponential phasor')
ax.scatter(n,reVal,imgVal, c='r', marker='o')
ax.set_xlabel('sample n')
ax.set_ylabel('real')
ax.set_zlabel('imag')
ax.legend()
plt.show()
