import numpy as np 
target=35
arr=np.random.randint(0,100,10)
print(f"target value is {target}")
print(f"random value is {arr}")

z=np.subtract(arr,target)
z=np.abs(z)
print(f"close value is {arr[z.argmin()]}")
    