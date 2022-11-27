import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

df=pd.read_csv('admission_predict.csv')

print(df.shape)

print(df.head())

print(df.tail())

print(df.columns)

print(df.info())

print(df.describe().T)

print(df.dtypes)


print(df.isnull().any())


df=df.rename(columns={'GRE Score':'GRE'})
print(df.head())

# Data Visualization

fig=plt.hist(df['GRE'],rwidth=0.7)
plt.title("Distribution of GRE Scores")
plt.xlabel("GRE SCORES")
plt.ylabel("COUNT")
print(plt.show())

fig=plt.hist(df['TOEFL Score'],rwidth=0.7)
plt.title("Distribution of TOEFL Scores")
plt.xlabel("TOEFL SCORES")
plt.ylabel("COUNT")
print(plt.show())

fig=plt.hist(df['SOP'],rwidth=0.7)
plt.title("Distribution of SOP")
plt.xlabel("SOP Rating")
plt.ylabel("COUNT")
print(plt.show())

fig=plt.hist(df['CGPA'],rwidth=0.7)
plt.title("Distribution of CGPA")
plt.xlabel("CGPA")
plt.ylabel("COUNT")
print(plt.show())

fig=plt.hist(df['Research'],rwidth=0.7)
plt.title("Distribution of Research Papers")
plt.xlabel("Research")
plt.ylabel("Count")
print(plt.show())
































