#数据异常处理：
#· ignore'忽略'： 发生异常时不采取任何行动。
#· warn' 警告 ' ： 打印一个 RuntimeWarning（通过Python warnings模块）。
#· 'raise'： 引发FloatingPointError。
#· 'call'： 调用使用seterrcall函数指定的函数。
#· 'log'： 直接打印警告stdout。
#· 'log'： 在由seterrcall指定的Log对象中记录错误。
 
#针对各种错误或特定的错误进行设置：
#· all全部： 适用于所有数字例外
#· invalid无效： 生成NaN时
#· divide除以零（对于整数也是！）
#· overflow溢出： 浮点溢出
#· underflow下溢：浮点下溢 

import numpy as np 
defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0

# Back to sanity
_ = np.seterr(**defaults)

# An equivalent way, with a context manager:

with np.errstate(divide='ignore'):
    Z = np.ones(1) / 0