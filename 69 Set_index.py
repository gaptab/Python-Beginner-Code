import pandas as pd
student_dict={'Name':['Shreedhama','Subala','Sudama'],'Age':[20,21,22],'Marks':[85.10,89,91.54]}
student_df=pd.DataFrame(student_dict)
print('Before set index:\n',student_df)
student_df=student_df.set_index('Name')
print("After set index:\n",student_df)

#set index using a list

student_dict={'Name':['Shreedhama','Subala','Sudama'],'Age':[20,21,22],'Marks':[85.10,89,91.54]}
student_df=pd.DataFrame(student_dict)
print('Before set index:\n',student_df)
index=pd.Index(['s1','s2','s3'])
student_df=student_df.set_index(index)
print("After set index:\n",student_df)

# Set index using multiple columns

student_dict={'Name':['Shreedhama','Subala','Sudama'],'Age':[20,21,22],'Marks':[85.10,89,91.54]}
student_df=pd.DataFrame(student_dict)
print('Before set index:\n',student_df)
student_df=student_df.set_index(['Name','Marks'])
print('After set index:\n',student_df)

#Set index using a list and a column
student_dict={'Name':['Shreedhama','Subala','Sudama'],'Age':[20,21,22],'Marks':[85.10,89,91.54]}
student_df=pd.DataFrame(student_dict)
print('Before set index:\n',student_df)
index=pd.Index(['s1','s2','s3'])
student_df=student_df.set_index([index,'Name'])
print('After set index:\n',student_df)

# set multiple-index using two python series
student_dict={'Name':['Shreedhama','Subala','Sudama'],'Age':[20,21,22],'Marks':[85.10,89,91.54]}
student_df=pd.DataFrame(student_dict)
print('Before set index:\n',student_df)
s=pd.Series([1,2,3])
student_df=student_df.set_index([s,s**2])
print("after set index:\n",student_df)

# set index using python range
student_dict={'Name':['Shreedhama','Subala','Sudama'],'Age':[20,21,22],'Marks':[85.10,89,91.54]}
student_df=pd.DataFrame(student_dict,index=['s1','s2','s3'])
print('Before set index:\n',student_df)
index=pd.Index(range(1,4,1))
student_df=student_df.set_index(index)
print("After set index:\n",student_df)
# set index but keep column

student_dict={'Name':['Shreedhama','Subala','Sudama'],'Age':[20,21,22],'Marks':[85.10,89,91.54]}
student_df=pd.DataFrame(student_dict)
print('Before set index:\n',student_df)
student_df=student_df.set_index('Name',drop=False)
print("After set index:\n",student_df)

# set index by keeping old index

student_dict={'Name':['Shreedhama','Subala','Sudama'],'Age':[20,21,22],'Marks':[85.10,89,91.54]}
student_df=pd.DataFrame(student_dict,index=['s1','s2','s3'])
print('Before set index:\n',student_df)
student_df=student_df.set_index('Name',append=True)
print("After set index:\n",student_df)