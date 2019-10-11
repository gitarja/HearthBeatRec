from Models.ECGReader import ECGReader
import os
import matplotlib.pyplot as plt
import numpy as np

basePath = "D:\\usr\\pras\\data\\Ecg\\ecg-id-database-1.0.0\\"
filePath = "Person_01\\rec_2"

reader = ECGReader()

data, ann = reader.read(os.path.join(basePath, filePath))
raw = data.p_signal[:, 0]
filtered = data.p_signal[:, 1]
driftFiltered = reader.waveDriftFilter(signal=raw, n=9)
bandStopFiltered = reader.bandStopFilter(driftFiltered, 50, 0, data.fs, type="notch")
lowPassFiltered = reader.smoothing(reader.bandStopFilter(bandStopFiltered, 40, 60, data.fs, type="lowpass"), n=5, order=2)
# adaptiveFiltered, error = reader.ada(raw)
# bandStopFiltered = reader.butter_bandstop_filter(raw, lowcut=59.9, highcut=60.1, fs=data.fs, order=2)

# plt.subplot(211)
plt.plot(raw, label="raw")
# plt.plot(bandStopFiltered, label="bandStop")
plt.plot(lowPassFiltered, label="lowPass")
# plt.plot(filtered, label="filtered")
plt.axhline(linewidth=1, color='b')
# plt.plot(adaptiveFiltered, label="adaptiveFiltered")
# plt.legend()
# plt.subplot(212)
# plt.plot(10*np.log10(error**2),"r", label="e - error [dB]")
plt.legend()
plt.show()
print(data)