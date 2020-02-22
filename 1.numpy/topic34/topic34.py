#设定numpy.arange()函数中的dtype参数，可以调整时间的间隔，比如以年、月、周，甚至小时、分钟、毫秒程度的间隔生成时间数组
# Code             Menaing
# Y                 year
# M                 month
# W                 week
# D                 day
# h                 hour
# m                 minute
# s                 second
# ms                millisecond
# us                microsecond
# ns                nanosecond
# ps                picosecond
# fs                femtosecond
# as                attosecond

import numpy as np 
Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(Z)
