#numpy 创建的数组都有一个shape属性，它是一个元组，返回各个维度的维数。
#shape[0]表示最外围的数组的维数，shape[1]表示次外围的数组的维数，数字不断增大，维数由外到内。
import numpy as np

arr=np.arange(9)
arr.shape = (3,3)
print(arr)
