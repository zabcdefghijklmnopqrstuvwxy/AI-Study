#numpy.genfromtxt(fname, dtype=<class  'float'>, comments='#', delimiter=None, skip_header=0, skip_footer=0, converters=None, missing_values=None, filling_values=None, usecols=None, names=None, excludelist=None, deletechars=None, replace_space='_', autostrip=False, case_sensitive=True, defaultfmt='f%i', unpack=None, usemask=False, loose=True, invalid_raise=True, max_rows=None, encoding='bytes')
#从文本文件加载数据，并按指定处理缺失值。

#参数fname：file, str, pathlib.Path, list of str, generator
#要读取的文件，文件名，列表或生成器。 如果文件扩展名为gz或bz2，则首先解压缩文件。 
#请注意，生成器必  须在Python 3k中返回字节字符串。 列表中的字符串或生成器生成的字符串被视为行。                                 须在Python 3k中返回字节字符串。 列表中的字符串或生成器生成的字符串被视为行。

#dtype : dtype, optional
#结果数组的数据类型。 如果为None，则dtypes将由每列的内容单独确定。

#comments : str, optional
#用于表示评论开始的字符。 注释后出现在行上的所有字符都将被丢弃

#delimiter : str, int, or sequence, optional
#用于分隔值的字符串。 默认情况下，任何连续的空格都用作分隔符。 也可以提供整数或整数序列作为每个字段的宽度。

#skiprows : int, optional
#skiprows was removed in numpy 1.10. Please use skip_header instead.

#skip_header : int, optional
#要在文件开头跳过的行数。

#skip_footer : int, optional
#要在文件末尾跳过的行数。

#converters : variable, optional
#将列数据转换为值的函数集。 转换器还可用于为丢失的数据提供默认值：converters = {3：lambda s：float（s或0）}。

#missing_values : variable, optional
#与缺失数据相对应的字符串集。

#usecols : sequence, optional
#要读取哪些列，其中0为第一列。 例如，usecols =（1,4,5）将提取第2列，第5列和第6列。


import numpy as np 
from io import StringIO

# Fake file
s = StringIO("""1, 2, 3, 4, 5\n
                6,  ,  , 7, 8\n
                 ,  , 9,10,11\n""")
#Z = np.genfromtxt(s, delimiter=",", dtype=np.int)
Z = np.genfromtxt(fname="test.txt", delimiter=",", dtype=np.int)

print(Z)