
import pandas as pd
df=pd.DataFrame({'A':[1,2,3],'B':[True,True,False],
                 'C':[0.23424,-0.546567,0.46597]},
                index=['a','b','c'])
print(df)
print(df['A'])

cols=['A','C']
print(df[cols])

print(df.loc[['a','b']])

print(df.iloc[:2])

print(df.loc['a','B'])

print(df.loc['a':'b',['A','C']])

print(df['A'])

print(df.loc[:,'A'])

print(df.A)

df['mean']=['a','b','c']
print(df)
