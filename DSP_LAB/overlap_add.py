import numpy as np

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

def idft(X):
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        sum_ = 0
        for k in range(N):
            angle = 2 * np.pi * k * n / N
            sum_ += X[k] * np.exp(1j * angle)
        x[n] = sum_ / N
    return np.real(x)

def circular_convolution(x, h):
    N = len(x)
    M = len(h)
    # Zero-pad x and h to length N
    x_padded = np.pad(x, (0, N - len(x)), 'constant')
    h_padded = np.pad(h, (0, N - len(h)), 'constant')
    X = dft(x_padded)
    H = dft(h_padded)
    Y = X * H
    y = idft(Y)
    return np.real(y)

def overlap_add(x, h):
    M = len(h)
    L = M  # Length of each block for overlap-add method
    
    # Zero-padding to make block length equal to M
    x_padded = np.pad(x, (0, L - len(x) % L), 'constant')
    
    # Number of blocks
    num_blocks = len(x_padded) // L
    
    # Result placeholder
    y = np.zeros(len(x_padded) + M - 1)
    
    for i in range(num_blocks):
        start = i * L
        end = start + L
        x_block = x_padded[start:end]
        conv_block = circular_convolution(x_block, h)
        y[start:start+len(conv_block)] += conv_block
    
    return y[:len(x) + len(h) - 1]

# Define long input signal and filter
x = np.random.rand(100)  # Example long sequence
h = np.array([1, 2, 3, 4, 5, 6])  # Filter of length 6

# Perform overlap-add convolution
y = overlap_add(x, h)
print("overlap and add:",y)