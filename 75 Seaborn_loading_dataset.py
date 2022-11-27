import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
iris=sns.load_dataset("iris")
print(iris.head(10))
print(iris.describe())
sns.set()
%matplotlib inline
sns.stripplot(x="species",y="petal_length",data=iris)

df=pd.read_csv("tesla.csv",encoding='windows-1252')
print(df.head(10))
print(df.describe())
%matplotlib inline
sns.stripplot(x='high',y='low',data=df)