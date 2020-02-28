import numpy as np 
target=25
arr=np.random.randint(0,100,10)
print(f"random arr is {arr}")

Z = np.abs(arr - target)
print(f"close target is {arr[Z.argmin()]}")