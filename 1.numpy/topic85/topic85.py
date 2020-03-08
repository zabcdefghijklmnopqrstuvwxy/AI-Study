import numpy as np 

def symetric(Z):
    for i in range(len(Z[0,...])):
        for j in range(len(Z[...,0])):
            Z[i][j] = Z[j][i]
    return Z

arr=np.random.randint(0,10,size=(5,5))
print(arr)
Z=symetric(arr)
print(Z)
