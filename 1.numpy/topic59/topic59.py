#argsort(a, axis=-1, kind='quicksort', order=None)
#    Returns the indices that would sort an array.
#    
#    Perform an indirect sort along the given axis using the algorithm specified
#    by the `kind` keyword. It returns an array of indices of the same shape as
#    `a` that index data along the given axis in sorted order.
    
#    Parameters
#    ----------
#    a : array_like
#        Array to sort.
#    axis : int or None, optional
#        Axis along which to sort.  The default is -1 (the last axis). If None,
#        the flattened array is used.
#    kind : {'quicksort', 'mergesort', 'heapsort'}, optional
#        Sorting algorithm.
#    order : str or list of str, optional
#        When `a` is an array with fields defined, this argument specifies
#        which fields to compare first, second, etc.  A single field can
#        be specified as a string, and not all fields need be specified,
#        but unspecified fields will still be used, in the order in which
#        they come up in the dtype, to break ties.
    
#    Returns
#    -------
#    index_array : ndarray, int
#        Array of indices that sort `a` along the specified axis.
#        If `a` is one-dimensional, ``a[index_array]`` yields a sorted `a`.

#argsort()函数返回的是数组值从小到大的索引值。
#排序后会产生一个新的数组，不改变原有的数组。


import numpy as np 

arr=np.random.randint(0,100,size=(5,5))
print(f"random arr is \n{arr}")
Z=arr[arr[:,1].argsort()]
#Z=np.argsort(arr,axis=1)
print(f"sort arr is \n{Z}")


