import numpy as np 
N=5
arr=np.random.randint(0,10,size=(N,N))
print(f"random arr is \n{arr}")

Z=arr - arr.mean(axis=1)
print(f"subtract mean is \n{Z}")