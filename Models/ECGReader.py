import wfdb
import numpy as np
import padasip as pa
from scipy.signal import iirnotch, lfilter, iirdesign,savgol_filter,filtfilt
from scipy import ndimage
import pywt
class ECGReader:

    def read(self, path, ):
        record = wfdb.rdrecord(path)
        ann = wfdb.rdann(path, "atr", sampto=100)

        return record, ann

    def bandStopFilter(self, signal, lowcut, highcut, fs,  type="notch"):
        '''
        :param signal: input signal
        :param lowcut: low freq for the cutoff
        :param highcut: high freq for the cutoff
        :param fs: frequency of sampling
        :param type: notch or low
        :return: the filtered signal
        filtfilt is used to compensate the delay that is introduced when applying filter to the input signal
        '''
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq

        #b = numerator
        #a = denominator
        if type=="notch":
            b, a = iirnotch(low, 30, fs)
            y = lfilter(b, a, signal)
        else:
            b, a = iirdesign(wp=low, ws=high, analog=False, ftype='butter', gpass=0.1, gstop=30)
            y = filtfilt(b, a, signal)


            # b, a = iirfilter(order, low, btype=type, analog=False, ftype='butter')

        return y

    def smoothing(self, signal, n =5, order=4):
        y = savgol_filter(signal, n, order)
        return y

    def waveDriftFilter(self, signal, n=9):
        '''
        :param signal: signal input
        :param n: level of decomposition
        :return: signal - baseline
        The signal is decomposed into 9 level and only the last coeffictient [1] is used to reconstruct the baseline
        To remove baseline wondering the baseline is substracted from the input signal
        '''
        waveletName = "bior1.5"
        coeffs = pywt.wavedecn(signal, waveletName, level=n)
        for i in range(2, len(coeffs), 1):
            coeffs[i] = self.ignoreCoefficient(coeffs[i])
        baseline = pywt.waverecn(coeffs, waveletName)
        filtered = signal - baseline
        return filtered

    def ignoreCoefficient(self, coeff):
        coeff = {k: np.zeros_like(v) for k, v in coeff.items()}
        return coeff

    def morphologyCoefficient(self, coeff):
        coeff = {k: (ndimage.grey_opening(v, size=(10,)) + ndimage.grey_closing(v, size=(10,))) / 2 for k, v in
                 coeff.items()}
        return coeff

    def adaptiveFilter(self, signal, n = 10):
        N = len(signal)
        d = signal + np.random.normal(0, 0.1, N)
        n = 10

        # filtering
        x = pa.input_from_history(signal, n)[:-1]
        d = d[n:]


        f = pa.filters.FilterRLS(n=n, mu=0.9, w="random")
        y, e, _ = f.run(d, x)

        return y, e
