import numpy as np
import matplotlib.pyplot as plt

def linear_convolution(x, h):
    # Length of the output
    N = len(x) + len(h) - 1
    # Initialize the output array
    y = np.zeros(N)
    
    # Perform convolution
    for n in range(N):
        for k in range(len(h)):
            if 0 <= n - k < len(x):  # Ensure indices are within bounds
                y[n] += x[n - k] * h[k]
    
    return y

# Example sequences
x = [1, 2, 3]
h = [0, 1, 0.5]

# Perform convolution
y = linear_convolution(x, h)

# Plot the result (removed use_line_collection argument)
plt.stem(range(len(y)), y)
plt.title("Linear Convolution")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)
plt.show()

# Print the result
print("Convolved sequence y[n]:", y)

