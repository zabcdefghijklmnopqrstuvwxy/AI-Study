#numpy.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, suppress=None, nanstr=None, infstr=None)
#Set printing options.

#These options determine the way floating point numbers, arrays and other NumPy objects are displayed.

#Parameters :	
#precision : int, optional
#Number of digits of precision for floating point output (default 8).

#threshold : int, optional
#Total number of array elements which trigger summarization rather than full repr (default 1000).

#edgeitems : int, optional
#Number of array items in summary at beginning and end of each dimension (default 3).

#linewidth : int, optional
#The number of characters per line for the purpose of inserting line breaks (default 75).

#suppress : bool, optional
#Whether or not suppress printing of small floating point values using scientific notation (default False).

#nanstr : str, optional
#String representation of floating point not-a-number (default nan).

#infstr : str, optional
#String representation of floating point infinity (default inf).


import numpy as np 
np.set_printoptions(threshold=1000)
Z = np.zeros((16,16))
print(Z)