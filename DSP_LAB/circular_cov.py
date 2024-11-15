import numpy as np
def dft(sequence):
    N = len(sequence)
    result = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            result[k] += sequence[n] * np.exp(-2j * np.pi * k * n / N)
    return result
def idft(sequence):
    N = len(sequence)
    result = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            result[n] += sequence[k] * np.exp(2j * np.pi * k * n / N)
    return result / N
def circular_convolution_dft(x, h):
    N = max(len(x), len(h))
    x = np.pad(x, (0, N - len(x)), mode='constant')
    h = np.pad(h, (0, N - len(h)), mode='constant')
    X = dft(x)
    H = dft(h)
    Y = X * H   
    y = idft(Y)
    return np.real(y)  
x = np.array([4,3,2,1])   
h = np.array([1,-2,0,4]) 
output_dft = circular_convolution_dft(x, h)
print("Circular Convolution Result (DFT without FFT):", output_dft)
def circular_convolution_direct(x, h):
    N = max(len(x), len(h))
    x = np.pad(x, (0, N - len(x)), mode='constant')
    h = np.pad(h, (0, N - len(h)), mode='constant')
    result = np.zeros(N)
    for n in range(N):
        for m in range(N):
            result[n] += x[m] * h[(n - m) % N]
    return result
output_direct = circular_convolution_direct(x, h)
print("Circular Convolution Result (Direct):", output_direct)
if any(output_dft==output_direct):
	print("circular convolotion is verified")
else:
	print("circular convolotion is not verified")

