#numpy的linespace功能
#在指定的间隔内返回均匀间隔的数字。
#返回num均匀分布的样本，在[start, stop]。
#这个区间的端点可以任意的被排除在外。

#numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#start：开始数值
#stop：结束数值
#num：默认是50个样本点（数据），为正整数。
#endpoint：默认为True，如果改为Fasle取不到右端点。
#restep：步长，如第一个数据和第第二个数据之间的距离。
#dtype：可以设置数值类型


import numpy as np 
arr=np.linspace(0,1,num=11,endpoint=False,dtype=float)[1:]
print(arr)