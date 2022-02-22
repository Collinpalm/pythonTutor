import numpy as np
from pandas import read_csv

df = read_csv('data.csv')

data = df.values
print(data)
