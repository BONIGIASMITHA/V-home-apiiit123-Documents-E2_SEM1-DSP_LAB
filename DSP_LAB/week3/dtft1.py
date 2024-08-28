import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4])
l= 4
n = np.arange(l)
omega = np.linspace(-np.pi, np.pi)  
X = np.array([sum(x[n]* np.exp(-1j * w * n)
for n in range(l)) for w in omega])
plt.subplot(2, 1, 1)
plt.plot(omega, np.abs(X))
plt.title('Magnitude of DTFT')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.subplot(2, 1, 2)
plt.plot(omega, np.angle(X))
plt.title('Phase of DTFT')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (radians)')
plt.show()



