import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 256  # Number of samples
fs = 1000  # Sampling frequency in Hz
T = 1/fs  # Sample interval
t = np.arange(N) * T  # Discrete time vector

# Create a discrete time signal (e.g., a sine wave)
f_signal = 50  # Frequency of the sine wave
signal = np.sin(2 * np.pi * f_signal * t)

# Create an exponential envelope
alpha = -5  # Decay rate of the exponential
exponential_envelope = np.exp(alpha * t)

# Multiply the signal by the exponential
modulated_signal = signal * exponential_envelope

# Perform FFT
fft_result = np.fft.fft(modulated_signal)  # Compute the FFT
fft_freq = np.fft.fftfreq(N, T)  # Frequency bins

# Plotting the results
plt.figure(figsize=(12, 8))

# Time domain signal
plt.subplot(3, 1, 1)
plt.plot(t, signal, label='Original Signal', color='b')
plt.plot(t, modulated_signal, label='Modulated Signal', color='r')
plt.title('Time Domain Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Exponential Envelope
plt.subplot(3, 1, 2)
plt.plot(t, exponential_envelope, color='g')
plt.title('Exponential Envelope')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

# Frequency domain representation
plt.subplot(3, 1, 3)
plt.plot(fft_freq[:N//2], np.abs(fft_result[:N//2]))  # Plot only the positive frequencies
plt.title('Frequency Domain Spectrum (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()

plt.tight_layout()
plt.show()
