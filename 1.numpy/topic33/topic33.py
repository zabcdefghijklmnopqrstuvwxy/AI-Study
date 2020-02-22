import numpy as np 
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today     = np.datetime64('today', 'D')
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print(f"yesterday is {yesterday}")
print(f"today is {today}")
print(f"tomorrow is {tomorrow}")
