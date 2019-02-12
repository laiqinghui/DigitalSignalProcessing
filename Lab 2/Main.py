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
    print "len of sampleX_float: ", len(sampleX_float)
    print y
    print y_self
    y_16bit = helper.fnNormalizeFloatTo16Bit(y_self)
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

    x = np.array([1,2,3, 4, 5, 6, 7, 8, 9])
    h = np.array([1,2, 3, 4, 5, 6])

    y1 = helper.convolve(x, h)
    y2 = np.convolve(x,h)
    print y1
    print y2


def delta(n):

    if n == 0:
        return 1
    else: return 0

def q4():

    n = np.arange(0, 100)
    h1 = np.array([0.06523, 0.14936, 0.21529, 0.2402, 0.21529, 0.14936, 0.06523], dtype='float')
    h2 = np.array([-0.06523, -0.14936, -0.21529, 0.7598, -0.21529, -0.14936, -0.06523], dtype='float')

    x1 = np.zeros(len(n))
    for i in range(len(n)):
        x1[i] = delta(n[i]) - 2*delta(n[i]-15)
    y1 = helper.convolve(x1, h1)
    y2 = helper.convolve(x1, h2)

    x2n, x2 = helper.fnGenSampledSinusoid(0.1, 700, 0, 16000, 0, 0.05)
    x3 = np.zeros(len(n))
    x3n, x3 = helper.fnGenSampledSinusoid(0.1, 3333, 0, 16000, 0, 0.05)
    x4 = x2 + x3
    y3 = helper.convolve(x4, h1)
    y4 = helper.convolve(x4, h2)
    #print "x4: ", x4
    # x4float = helper.fnNormalize16BitToFloat(x4)
    # [f, t, Sxx] = signal.spectrogram(x4float, 16000, window=('blackmanharris'),nperseg=512,noverlap=int(0.9*512))
    # plt.pcolormesh(t, f, 10*np.log10(Sxx))
    # plt.ylabel('Frequency [Hz]')
    # plt.xlabel('Time [sec]')
    # plt.title('spectrogram of signal')
    # plt.show()

    fig , axes = plt.subplots(5,1)
    axes[0].plot(x2n, x2)
    axes[0].grid()
    axes[1].plot(x3n, x3)
    axes[1].grid()
    axes[2].plot(x3n, x4)
    axes[2].grid()
    axes[3].plot(y3)
    axes[3].grid()
    axes[4].plot(y4)
    axes[4].grid()
    plt.show()

    # x2_16bit = helper.fnNormalizeFloatTo16Bit(x2)
    # wavfile.write('t1_16bit.wav', 16000, x2_16bit)
    # print "Playing x2_16bit wav file..."
    # winsound.PlaySound('t1_16bit.wav', winsound.SND_FILENAME)
    # x3_16bit = helper.fnNormalizeFloatTo16Bit(x3)
    # wavfile.write('t1_16bit.wav', 16000, x3_16bit)
    # print "Playing x3_16bit wav file..."
    # winsound.PlaySound('t1_16bit.wav', winsound.SND_FILENAME)
    # x4_16bit = helper.fnNormalizeFloatTo16Bit(x4)
    # wavfile.write('t1_16bit.wav', 16000, x4_16bit)
    # print "Playing x4_16bit wav file..."
    # winsound.PlaySound('t1_16bit.wav', winsound.SND_FILENAME)
    # y3_16bit = helper.fnNormalizeFloatTo16Bit(y3)
    # wavfile.write('t1_16bit.wav', 16000, y3_16bit)
    # print "Playing y3_16bit wav file..."
    # winsound.PlaySound('t1_16bit.wav', winsound.SND_FILENAME)
    # y4_16bit = helper.fnNormalizeFloatTo16Bit(y4)
    # wavfile.write('t1_16bit.wav', 16000, y4_16bit)
    # print "Playing y4_16bit wav file..."
    # winsound.PlaySound('t1_16bit.wav', winsound.SND_FILENAME)

def q5():

    # B = [1, -0.7653668, 0.99999], A = [1, -0.722744, 0.888622]

    ipcleanfilename = 'helloworld_noisy_16bit.wav'
    print "Playing original noisy wav file..."
    winsound.PlaySound(ipcleanfilename, winsound.SND_FILENAME)
    Fs, sampleX_16bit = wavfile.read(ipcleanfilename)
    x = helper.fnNormalize16BitToFloat(sampleX_16bit)
    y = np.zeros(len(x), dtype=float)

    for n in range(len(x)):
        if n == 0:
            y[n] = 1*x[n]
        elif n == 1:
            y[n] = 1*x[n] + (-0.7653668)*x[n-1] - (-0.722744)*y[n-1]
        elif n == 2:
            y[n] = 1*x[n] + (-0.7653668)*x[n-1] + 0.99999*x[n-2] - (-0.722744)*y[n-1]
        else:
            #print "Current n: ", n
            y[n] = 1*x[n] + (-0.7653668)*x[n-1] + 0.99999*x[n-2] - (-0.722744)*y[n-1] - 0.888622*y[n-3]

    B = [1, -0.7653668, 0.99999]
    A = [1, -0.722744, 0.888622]
    y_ifil = signal.lfilter(B, A, x)

    for n in range(len(y[0:10])):

        print y[n]
        print y_ifil[n]

















q5()
