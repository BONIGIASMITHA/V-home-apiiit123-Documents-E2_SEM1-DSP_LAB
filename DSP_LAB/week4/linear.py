import numpy as np
import matplotlib.pyplot as plt
def dtft(x):
    X=[]
    omega=np.arange(-np.pi,np.pi,0.00001*np.pi)
    for f in omega:
        s=0
        for n in range(len(x)):
            s+=x[n]*np.exp(-1j*f*n)
        X.append(s)
    return np.array(X)

x1=np.array([2,3,4,5])
x2=np.array([3,6,7,8])
X1=dtft(x1)
X2=dtft(x2)
X3=dtft(x1+x2)
X4=X1+X2
if any(X4==X3):
	print("linearity is proved")
else:
	print("linearity is not proved")
print(X1)
print(X2)
print(X3)
print(X4)

