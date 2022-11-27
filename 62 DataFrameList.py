import pandas as pd
fruits_list=['Apple',10,'Orange',77.77]
print(fruits_list)
fruits_df=pd.DataFrame(fruits_list)
print(fruits_df)

# Custom column name

fruits_list=['Apple','Banana','Orange','Mango']
fruits_df=pd.DataFrame(fruits_list,columns=['Fruits'])
print(fruits_df)

#Custom index

fruits_df=pd.DataFrame(fruits_list,index=['Fruit1','Fruit2','Fruit3','Fruit4'])
print(fruits_df)

# Changing the datatype

price_list=['50','100','60','120']
price_df=pd.DataFrame(price_list)
print("Data type before:", price_df.dtypes)

price_df=pd.DataFrame(price_list,dtype='float64')
print("Data type after:",price_df.dtypes)
print(price_df)

# DF from hierarchial lists as row

fruits_list=[['Apple','Banana','Orange','Mango'],[120,40,100,50]]
print(fruits_list)
fruits_df=pd.DataFrame(fruits_list)
print(fruits_df)

# DF from hierarchial lists as columns
fruits_list=[['Apple','Banana','Orange','Mango'],[120,40,100,50]]
print(fruits_list)
fruits_df=pd.DataFrame(fruits_list).transpose()
print(fruits_df)

#Df from multiple list

fruits_list=['Apple','Banana','Orange','Mango']
price_list=[120,40,100,50]
fruits_df=pd.DataFrame(list(zip(fruits_list,price_list)),columns=['Names','Price'])
print(fruits_df)

fruits_dict={'Name':fruits_list,
             'Price':price_list}
print(fruits_dict)