import pandas as pd
import numpy as np
student_dict={'Name':['Vrushali','Supriya',np.nan,'Uruvi'],'Age':[20,21,np.nan,22],'Marks':[85.10,89.99,np.nan,90]}
student_df=pd.DataFrame(student_dict,index=['s1','s2','s3','s4'])
print("Original DataFrame:\n",student_df)
student_df=student_df.dropna()
print("DataFrame after dropping NA:\n",student_df)
student_df=student_df.reset_index()
print("DataFrame after resetting index:\n",student_df)
#reset index without new column

student_dict={'Name':['Vrushali','Supriya',np.nan,'Uruvi'],'Age':[20,21,np.nan,22],'Marks':[85.10,89.99,np.nan,90]}
student_df=pd.DataFrame(student_dict,index=['s1','s2','s3','s4'])
print("Original DataFrame:\n",student_df)
student_df=student_df.dropna()
print("DataFrame after dropping NA:\n",student_df)
student_df=student_df.reset_index(drop=True)
print("DataFrame after reset index:\n",student_df)

# reset index starts from 1
student_dict={'Name':['Vrushali','Supriya',np.nan,'Uruvi'],'Age':[20,21,np.nan,22],'Marks':[85.10,89.99,np.nan,90]}
student_df=pd.DataFrame(student_dict,index=['s1','s2','s3','s4'])
print("Original DataFrame:\n",student_df)
student_df=student_df.dropna()
print("DataFrame after dropping NA:\n",student_df)
student_df=student_df.reset_index()
student_df.index=student_df.index+1
print("After reset index:\n",student_df)

#reset index to the range of numbers
student_dict={'Name':['Vrushali','Supriya',np.nan,'Uruvi'],'Age':[20,21,np.nan,22],'Marks':[85.10,89.99,np.nan,90]}
student_df=pd.DataFrame(student_dict,index=['s1','s2','s3','s4'])
print("Original DataFrame:\n",student_df)
student_df=student_df.dropna()
print("DataFrame after dropping NA:\n",student_df)
student_df.index=pd.RangeIndex(start=101,stop=101+len(student_df),step=1)
print("After reset index:\n",student_df)

#reset index and change column name
student_dict={'Name':['Vrushali','Supriya',np.nan,'Uruvi'],'Age':[20,21,np.nan,22],'Marks':[85.10,89.99,np.nan,90]}
student_df=pd.DataFrame(student_dict,index=['s1','s2','s3','s4'])
print("Original DataFrame:\n",student_df)
student_df=student_df.dropna()
print("DataFrame after dropping NA:\n",student_df)
student_df=student_df.reset_index().rename(columns={'index':'ID'})
print("After reset index:\n",student_df)