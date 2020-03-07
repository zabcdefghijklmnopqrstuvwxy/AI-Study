import numpy as np 

N=4
arr=np.arange(1,15)

Z=np.zeros((len(arr) - (N - 1),N),dtype=int)

for i in range(len(arr)):
    if(i < len(arr) - (N - 1)):
        Z[i,0:N] = arr[i:i+N]

print(Z)
