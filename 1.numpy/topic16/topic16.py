#numpy中的pad()函数用法(填充函数)
#1）语法结构
#pad(array, pad_width, mode, **kwargs)
#返回值：数组
#2）参数解释
#array——表示需要填充的数组；

#pad_width——表示每个轴（axis）边缘需要填充的数值数目。 
#参数输入方式为：（(before_1, after_1), … (before_N, after_N)），其中(before_1, after_1)表示第1轴两边缘分别填充before_1个和after_1个数值。取值为：{sequence, array_like, int}

#mode——表示填充的方式（取值：str字符串或用户提供的函数）,总共有11种填充模式；

#3) 填充方式
#‘constant’——表示连续填充相同的值，每个轴可以分别指定填充值，constant_values=（x, y）时前面用x填充，后面用y填充，缺省值填充0
#‘edge’——表示用边缘值填充
#‘linear_ramp’——表示用边缘递减的方式填充
#‘maximum’——表示最大值填充
#‘mean’——表示均值填充
#‘median’——表示中位数填充
#‘minimum’——表示最小值填充
#‘reflect’——表示对称填充
#‘symmetric’——表示对称填充
#‘wrap’——表示用原数组后面的值填充前面，前面的值填充后面

import numpy as np

arr=np.ones([5,5],dtype=int)
arr=np.pad(arr,pad_width=1,mode='constant',constant_values=0)
print(arr)