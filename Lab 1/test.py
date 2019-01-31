import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile  as wavfile
import winsound
import time
# plotting 3D complex plane
from mpl_toolkits.mplot3d import Axes3D

from Helper import Helper

helper = Helper()


#=======================================#3.1a===================================

def threedot1a():

    A = 0.5;
    #F = 500;
    Phi = 0; Fs = 16000; sTime = 0; eTime = 0.4;
    Freq = np.arange(2000, 34000, 2000)

    for F in Freq:
        sinusoid = helper.fnGenSampledSinusoid(A, F, Phi, Fs, sTime, eTime)
        y_16bit = helper.fnNormalizeFloatTo16Bit(sinusoid[1])
        wavfile.write('t1_16bit.wav', Fs, y_16bit)
        print ("Current Freq: ", F, "Hz")
        print ("")
        winsound.PlaySound('t1_16bit.wav', winsound.SND_FILENAME)
        time.sleep(1)


#=======================================#3.1a===================================

def threedot1b():

    A = 0.5; Phi = 0; Fs = 16000; sTime = 0; eTime = 0.006
    F1 = 1000
    F2 = 1000
    sinusoid1 = helper.fnGenSampledSinusoid(A, F1, Phi, 1000000, sTime, eTime)
    sinusoid2 = helper.fnGenSampledSinusoid(A, F2, Phi, 2000, sTime, eTime)

    fig, axs = plt.subplots(2,1)
    axs[0].plot(sinusoid1[0], sinusoid1[1])
    axs[0].grid()
    axs[1].plot(sinusoid2[0], sinusoid2[1])
    axs[1].grid()
    plt.show()

#=======================================#3.2===================================

def threedot2(seq = "0123456789*#", fs = 10000, durTone = 1):


    freq = {'0': [1336, 941],
            '1': [1209, 697],
            '2': [1336, 697],
            '3': [1477, 697],
            '4': [1209, 770],
            '5': [1336, 770],
            '6': [1477, 770],
            '7': [1209, 852],
            '8': [1336, 852],
            '9': [1477, 852],
            '*': [1209, 941],
            '#': [1477, 941]
             }

    sTime = 0
    eTime = sTime + durTone
    y = []

    for s in seq:

        n = np.arange(sTime,eTime,1.0/fs)
        y1 = 0.5*np.sin(2 * np.pi * freq[s][0] * n)
        y2 = 0.5*np.sin(2 * np.pi * freq[s][1] * n)
        y3 = y1 + y2
        # print("Current seq: ", len(y3))
        y = np.concatenate((y, y3))
        # print("Concated seq: ", len(y))
        # y_16bit = helper.fnNormalizeFloatTo16Bit(y3)
        # wavfile.write('t1_16bit.wav', fs, y_16bit)
        # winsound.PlaySound('t1_16bit.wav', winsound.SND_FILENAME)

        #time.sleep(0.5)

    y_16bit = helper.fnNormalizeFloatTo16Bit(y)
    wavfile.write('t1_16bit.wav', fs, y_16bit)
    winsound.PlaySound('t1_16bit.wav', winsound.SND_FILENAME)


#=======================================#3.4===================================

def threedot4():

    numSamples = 36
    A=0.95;
    w1=(2*np.pi)/18;
    #w1=0.1*np.pi;
    n = np.arange(0, numSamples, 1)
    y1 = np.multiply(np.power(A, n), np.exp(1j * w1 * n))
    print (y1)

    # plotting in 2-D, the real and imag in the same figure
    plt.figure(1)
    plt.plot(n, y1[0:numSamples].real,'r--o')
    plt.plot(n, y1[0:numSamples].imag,'g--o')
    plt.xlabel('sample index n'); plt.ylabel('y[n]')
    plt.title('Complex exponential (red=real) (green=imag)')
    plt.grid()
    plt.show()

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


#=======================================#3.5===================================

def threedot5():

    numSamples = 16

    fig, axs = plt.subplots(4,1)
    for k in range (4):
        print (k)
        w1=(2*np.pi*k)/16;
        n = np.arange(0, numSamples, 1)
        y1 = np.exp(1j * w1 * n)
        axs[k].plot(n, y1[0:numSamples].real,'r--o')
        axs[k].plot(n, y1[0:numSamples].imag,'g--o')
        axs[k].set_xlabel('sample index n')
        axs[k].set_ylabel('y[n]')
        axs[k].set_title('(red=real) (green=imag) k = ' + str(k)  )
        axs[k].grid()

    plt.show()






#===============================================================================

#threedot1a()
#threedot1b()
#threedot2(seq="98285937", durTone = 0.3)
threedot4()
#threedot5()
