import pandas as pd
student_dict={'Name':['Panchali','Subhadra','Uttara'], 'Age':[20,21,18],'Marks':[90,91.70,89.06]}
student_df=pd.DataFrame(student_dict)
print(student_df)
student_df.info()
print(student_df.describe())

print("DataFrame Index:",student_df.index)
print("DataFrame Columns:",student_df.columns)
print("DataFrame Column types:",student_df.dtypes)
print("DataFrame is empty?",student_df.empty)
print("DataFrame Shape:",student_df.shape)
print("DataFrame Size:",student_df.size)
print("DataFrame Values:",student_df.values)

print(student_df.head(2))
print(student_df.tail(2))
print(student_df.at[0,'Name'])
print(student_df.iat[0,0])
print(student_df.get('Name'))
print(student_df.loc[0:2,['Name']])
print(student_df.iloc[0:2,0:2])

student_df.insert(loc=2,column="Class", value='A')
print(student_df)

student_df=student_df.drop(columns='Class')
print(student_df)
filter=student_df['Marks']>90
student_df['Marks'].where(filter,other=0,inplace=True)
print(student_df)

student_df=student_df.filter(like='N', axis='columns')
print(student_df)

student_df=student_df.rename(columns={'Marks':'Percentage'})
print(student_df)