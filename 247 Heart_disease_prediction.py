import numpy as np
import pandas as pd

df=pd.read_csv('heart.csv')

print(df.shape)

print(df.columns)
print(df.dtypes)
print(df.head())
print(df.tail())

print(df.isnull().any())

print(df.info())

print(df.describe().T)
#  Data Visualization

import matplotlib.pyplot as plt
import seaborn as sns

fig=plt.figure(figsize=(15,15))
ax=fig.gca()
g=df.hist(ax=ax)











