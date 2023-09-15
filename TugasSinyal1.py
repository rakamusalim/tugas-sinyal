import numpy as np
import matplotlib.pyplot as plt

# Generate a sine wave signal
Fs = 1500  # Sampling rate
T = 1 / Fs  # Time interval between samples
t = np.arange(0, 1, T)  # Time vector
f = 30  # Frequency of the sine wave
x = np.sin(2 * np.pi * f * t)  # Sine wave signal

## ID
print("Nama: Rakan Akmal Musalim")
print("NRP: 5009201016")

# Compute the FFT
N = len(x) 
X = np.fft.fft(x)  

# Generate the frequency axis
freqs = np.fft.fftfreq(N, T)  

# Plot the signal in the time domain
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sine Wave Signal')

# Plot the signal in the frequency domain
plt.subplot(2, 1, 2)
plt.plot(freqs[1:N//2], np.abs(X[1:N//2]))  # Only plot positive frequencies
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')

# Show the plots
plt.tight_layout()
plt.show()






