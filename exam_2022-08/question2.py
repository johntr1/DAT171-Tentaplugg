import math
import matplotlib.pyplot as plt
import numpy as np

from scipy.io import wavfile


def pitch(frequency):
    f_a4 = 440
    f_c0 = f_a4 * 2 ** -4.75
    h = 12 * math.log2(frequency / f_c0)
    h_r = round(h, ndigits=None)
    n = h_r % 12
    o = int(h_r / 12)
    li = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return li[n] + str(o)

    # Inspired by example from chapter 3 Scipy documentation

samplerate, data = wavfile.read("violin.wav")

length = data.shape[0] / samplerate

# Get the time for the wav sound
time = np.linspace(0., length, data.shape[0])
plt.figure(figsize=(8, 3))
plt.plot(time, data, label="Amplitude")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

power_spectra = np.abs(np.fft.fft(data))
frequency = np.fft.fftfreq(len(power_spectra), d=1./samplerate)

position = np.argmax(power_spectra)

v_max = np.max(frequency)
base_frequency = np.abs(frequency[position])

note = pitch(base_frequency)

print(f'Note is:{note} and frequency:{base_frequency}')

plt.figure(figsize=(8, 3))
plt.plot(frequency, power_spectra)
plt.xlim([0, 3000])
plt.show()

# LÄROMÅL:
# LÄS DOKUMENTATIONEN DET HJÄLPER VÄLDIGT MYCKET!!!


