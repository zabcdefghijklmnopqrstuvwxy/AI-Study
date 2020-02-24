#极坐标系也有两个坐标轴：r（半径坐标）和θ（角坐标、极角或方位角，有时也表示为φ或t）。r坐标表示与极点的距离，
#θ坐标表示按逆时针方向坐标距离0°射线（有时也称作极轴）的角度，极轴就是在平面直角坐标系中的x轴正方向。

import numpy as np 
arr=np.random.randint(1,10,(10,2))

print(f"arr is \n{arr}\n")
X,Y = arr[::,0], arr[:,1]

print(f"Cartesian coordinates\n X is {X}\n Y is {Y}\n")
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print(f"R is {R}\n")
print(f"T is {T}\n")