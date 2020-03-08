import numpy as np 

N=3
S=10

Z=np.zeros(shape=(3,3))
arr=np.random.randint(0,100,size=(S,S))
print(arr)

for j in range(S):
    if(j < S - (N -1)):
        for i in range(S):
            if(i < S - (N - 1)):
                Z=arr[j:j+N,i:i+N]
                print(Z)



