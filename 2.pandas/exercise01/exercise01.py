import pandas as pd 
import numpy as np 

path = "chipotle.tsv"
csv = pd.read_csv(path,sep='\t')
pd.set_option('display.max_rows', 100)
csv.head(10)   #显示前十行信息
csv.shape[0]   #显示总共的行数