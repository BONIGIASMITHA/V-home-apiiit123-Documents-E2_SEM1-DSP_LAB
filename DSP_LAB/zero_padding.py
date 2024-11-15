import numpy as np
import matplotlib.pyplot as plt

# Define the DFT function
def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        sum_ = 0
        for n in range(N):
            angle = 2 * np.pi * k * n / N
            sum_ += x[n] * np.exp(-1j * angle)
        X[k] = sum_
    return X

# Define the original signal x[n] with length=4
x = np.array([1, 2, 3, 4])

# Perform DFT for the original length
X = dft(x)

# Zero-padding lengths
N_pad1 = 6
N_pad2 = 9

# Zero-pad the signal to length 6 and 9
x_pad1 = np.pad(x, (0, N_pad1 - len(x)), 'constant')
x_pad2 = np.pad(x, (0, N_pad2 - len(x)), 'constant')

# Perform DFT for the zero-padded lengths
X_1 = dft(x_pad1)
X_2 = dft(x_pad2)

# Define frequency axis
freq_orig = np.fft.fftfreq(len(x))
freq_pad1 = np.fft.fftfreq(N_pad1)
freq_pad2 = np.fft.fftfreq(N_pad2)

# Plotting
plt.figure(figsize=(12, 8))

# Plot magnitude of DFT for original signal
plt.subplot(3, 1, 1)
plt.stem(freq_orig, np.abs(X))
plt.title('Magnitude of DFT (Original Length=4)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()

# Plot magnitude of DFT for zero-padded length 6
plt.subplot(3, 1, 2)
plt.stem(freq_pad1, np.abs(X_1))
plt.title('Magnitude of DFT (Zero-padded Length=6)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()

# Plot magnitude of DFT for zero-padded length 9
plt.subplot(3, 1, 3)
plt.stem(freq_pad2, np.abs(X_2))
plt.title('Magnitude of DFT (Zero-padded Length=9)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()

plt.tight_layout()
plt.show()