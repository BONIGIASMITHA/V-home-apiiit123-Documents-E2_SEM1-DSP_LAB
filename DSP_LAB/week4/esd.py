import numpy as np

# Parameters
Fs = 1000  # Sampling frequency in Hz
T = 1.0 / Fs  # Sampling interval
L = 1000  # Length of the signal
t = np.arange(0, L) * T  # Time vector

# Generate a sample signal, for example, a sine wave
f = 50  # Frequency of the sine wave
A = 1  # Amplitude
signal = A * np.sin(2 * np.pi * f * t)

# Calculate the energy in the time domain
time_domain_energy = np.sum(np.abs(signal) ** 2) / L

# Compute the DTFT (Discrete-Time Fourier Transform) approximation
def dtft(x):
    N = len(x)
    omega = np.linspace(-np.pi, np.pi, N, endpoint=False)  # Frequency vector
    X = np.array([np.sum(x * np.exp(-1j * w * np.arange(N))) for w in omega])
    return omega, X

omega, signal_dtft = dtft(signal)

# Compute the energy in the DTFT domain
# Integrate the squared magnitude of the DTFT
# Normalize by the length of the signal to match the time-domain energy
dtft_energy = np.trapz(np.abs(signal_dtft) ** 2, omega) / (2* np.pi*L)

print(f"Energy in time-domain: {time_domain_energy}")
print(f"Energy in DTFT-domain: {dtft_energy}")

# Check if the energy is approximately the same
tolerance = 1e-10
if np.abs(time_domain_energy - dtft_energy) < tolerance:
    print("Energy in both domains is consistent.")
else:
    print("Energy in both domains is not consistent.")

