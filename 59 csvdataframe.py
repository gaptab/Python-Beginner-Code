import pandas as pd
data=pd.read_csv("tesla.csv")
print(data)

print(type(data))

data1=data.iloc[:,2]
print(data1)
print(type(data1))

states=pd.read_csv("states.csv")
print(states)

pd.options.display.max_rows=200
pd.set_option("display.min_rows",100)
print(data)