import numpy as np  

arr=np.random.randint(0,10,size=(2,2,2,2))
print(f"sum is {arr.sum(axis=(-2,-1))}")