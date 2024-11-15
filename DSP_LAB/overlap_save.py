import numpy as np

def dft(x, N=None):
    if N is None:
        N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        sum_ = 0
        for n in range(len(x)):
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
    N = len(x)  # Length of x should be the same as the FFT length
    M = len(h)
    X = dft(x, N)
    H = dft(h, N)
    Y = X * H
    y = idft(Y)
    return np.real(y)

def overlap_save(x, h):
    M = len(h)  # Length of the filter
    L = M       # Length of each block for overlap-save
    N = L + M - 1  # Length for FFT
    
    # Zero-pad input x to the appropriate length for FFT
    x_padded = np.pad(x, (0, N - len(x) % N), 'constant')
    
    # Number of blocks
    num_blocks = len(x_padded) // N
    
    # Prepare output array
    y = np.zeros(len(x_padded) + M - 1)
    
    # Process each block
    for i in range(num_blocks):
        start = i * N
        end = start + N
        x_block = x_padded[start:end]
        conv_block = circular_convolution(x_block, h)
        
        # Save only the non-overlapping part of the block
        y[start:start+N-M+1] += conv_block[M-1:]
    
    return y[:len(x) + len(h) - 1]

# Example usage
x = np.random.rand(100)  # Example long sequence
h = np.array([1, 2, 3, 4, 5, 6])  # Filter of length 6

# Perform overlap-save convolution
y = overlap_save(x, h)
print("overlap and save:",y)