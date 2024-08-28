import numpy as np 
from matplotlib import pyplot as plt

signal=[1,2,3,4,5]
kernel=[0.2,0.5,0.2]


convolved_length=len(signal)+len(kernel)-1
convolved_signal=np.zeros(convolved_length)


for i in range(convolved_length):
	for j in range(len(kernel)):
		if i-j>=0 and i-j<len(signal):
			convolved_signal[i]+=signal[i-j]*kernel[j]
print(convolved_signal)

plt.subplot(3,1,1)
plt.stem(signal)

plt.subplot(3,1,2)
plt.stem(kernel)

plt.subplot(3,1,3)
plt.stem(convolved_signal)

plt.show()
convolution

