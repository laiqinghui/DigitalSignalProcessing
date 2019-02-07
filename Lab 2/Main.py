import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile  as wavfile
import scipy
import winsound
from scipy import signal
from Helper import Helper

helper = Helper()

def q1():

    nx = np.arange(0, 102)
    x = np.cos(0.1*np.pi*nx)

    nh = np.arange(0, 3)
    nnh = np.negative(nh)
    h = np.array([0.2, 0.3, -0.5])

    y = np.convolve(x, h)
    ny = np.arange(0, len(y))

    fig, ax = plt.subplots(3,1)
    ax[0].stem(nx, x)
    ax[0].grid()
    ax[1].stem(nh, h)
    ax[1].grid()
    ax[1].stem(nnh, h)
    ax[1].grid()
    ax[2].stem(ny, y)
    ax[2].grid()
    plt.show()

def q3():

    impulseH = np.zeros(8000)
    impulseH[1] = 1
    impulseH[4000] = 0.5
    impulseH[7900] = 0.3

    ipcleanfilename = 'helloworld_16bit.wav'
    print "Playing original wav file..."
    winsound.PlaySound(ipcleanfilename, winsound.SND_FILENAME)
    Fs, sampleX_16bit = wavfile.read(ipcleanfilename)
    sampleX_float = helper.fnNormalize16BitToFloat(sampleX_16bit)
    print "Convolving..."
    y = np.convolve(sampleX_float, impulseH)
    y_self = helper.convolve(sampleX_float, impulseH)
    print y
    print y_self
    y_16bit = helper.fnNormalizeFloatTo16Bit(y)
    wavfile.write('t1_16bit.wav', Fs, y_16bit)
    print "Playing convolved wav file..."
    winsound.PlaySound('t1_16bit.wav', winsound.SND_FILENAME)
    fig, ax = plt.subplots(2,1)
    print "Plotting..."
    ax[0].plot(sampleX_float)
    ax[0].grid()
    ax[1].plot(np.arange(0, len(sampleX_float)), y[:len(sampleX_float)])
    ax[1].grid()
    plt.show()

def q3_self():

    x = np.array([1,2,3])
    h = np.array([1,2])

    y1 = helper.convolve(x, h)
    y2 = np.convolve(x,h)
    print y1
    print y2

q3()
