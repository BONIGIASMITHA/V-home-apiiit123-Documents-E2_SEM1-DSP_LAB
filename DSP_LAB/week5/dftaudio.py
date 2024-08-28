import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def compute_dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        X[k] = np.sum(x * np.exp(-2j * np.pi * k * np.arange(N) / N))
    return X

def compute_frequencies(N, sample_rate):

    return np.arange(N) * (sample_rate / N)

def plot_dft(filename):
   
    sample_rate, audio_data = wavfile.read("/home/apiiit123/Documents/E2_SEM1/DSP_LAB/week5/sample.wav")

   
    if len(audio_data.shape) > 1:
        audio_data = audio_data[:, 0]
    
   
    N = len(audio_data)
    X = compute_dft(audio_data)
    
    
    frequencies = compute_frequencies(N, sample_rate)
    
   
    magnitude = np.abs(X)
    phase = np.angle(X)

   
    half_N = N // 2
    frequencies = frequencies[:half_N]
    magnitude = magnitude[:half_N]
    phase = phase[:half_N]

    # Plot magnitude spectrum
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(frequencies, magnitude)
    plt.title('Magnitude Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    
    # Plot phase spectrum
    plt.subplot(2, 1, 2)
    plt.plot(frequencies, phase)
    plt.title('Phase Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (radians)')
    
    plt.tight_layout()
    plt.show()

# Example usage
plot_dft('path/to/your/audiofile.wav')

