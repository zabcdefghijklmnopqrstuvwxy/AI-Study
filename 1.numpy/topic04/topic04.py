import numpy as np

zero = np.zeros((10,10),dtype=np.int32)
print("total byte is %d" % (zero.size*zero.itemsize))

