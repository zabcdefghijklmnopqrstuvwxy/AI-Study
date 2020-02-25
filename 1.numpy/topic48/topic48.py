#numpy.iinfo(type)[source]
#Machine limits for integer types.

#Parameters:	
#int_type : integer type, dtype, or instance

#The kind of integer data type to get information about.

#See also
#finfo
#The equivalent for floating point data types.

import numpy as np 
for dtype in [np.int8, np.int32, np.int64]:
   print(np.iinfo(dtype).min)
   print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
   print(np.finfo(dtype).min)
   print(np.finfo(dtype).max)
   print(np.finfo(dtype).eps)