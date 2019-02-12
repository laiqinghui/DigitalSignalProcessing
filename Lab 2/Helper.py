import numpy as np

class Helper():

    def __init__(self):

        return

    # The following function generates a continuous time sinusoid
    # given the amplitude A, F (cycles/seconds), Fs=sampling rate, start and endtime
    def fnGenSampledSinusoid(self, A, Freq, Phi, Fs, sTime, eTime):
        # Showing off how to use numerical python library to create arange
        n = np.arange(sTime,eTime,1.0/Fs)
        y = A*np.cos(2 * np.pi * Freq * n + Phi)
        return [n,y]


    # The input is a float array (should have dynamic value from -1.00 to +1.00
    def fnNormalizeFloatTo16Bit(self, yFloat):
        y_16bit = [int(s*32767) for s in yFloat]
        return(np.array(y_16bit, dtype='int16'))

    # The input is a float array (should have dynamic value from -1.00 to +1.00
    def fnNormalize16BitToFloat(self, y_16bit):
        yFloat = [float(s/32767.0) for s in y_16bit]
        return(np.array(yFloat, dtype='float'))

    def convolve(self, x, h):

        # xxxxxxx
        # 0xxxxxxxxx0
        #
        #          xxxxxxx
        # 0xxxxxxxxx000000
        lenXOrig = len(x)

        y = []
        #1) flip h
        h = h[::-1]
        #print "Flipped h:", h
        #2) append 0 to front of x and end of x
        for i in range(len(h)-1):
            x = np.concatenate(([0], x, [0]))

        for i in range(lenXOrig + len(h) - 1):
            limit = i + len(h)
            sum = np.sum(np.multiply(h, x[i:limit]))
            y.append(sum)

        return np.array(y)
