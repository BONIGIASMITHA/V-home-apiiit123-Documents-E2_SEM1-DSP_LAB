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
    
k=3
x=np.array([1,2,3,4,5,6])
X=dtft(x)
w=np.arange(-np.pi,np.pi,0.00001*np.pi)
x2=np.array(np.append(np.zeros(k),x))
X1=np.exp(-1j*w*k)*X
X2=dtft(x2)
print(X1)
print(X2)
if any(X1==X2):
    print("time shifting property is proved")
else:
    print("time shifting property is not proved")

