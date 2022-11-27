import pandas as pd
student_dict={'Name':['Dushasan','Ashvathama','Vikarna','Dushasan','Ashvathama'],'Age':[20,21,19,20,21],'Marks':[85.10,77.80,91.54,85.10,77.80]}
student_df=pd.DataFrame(student_dict)
student_df=student_df.drop_duplicates()
print(student_df)

# drop duplicates from defined columns
student_dict={'Name':['Dushasan','Ashvathama','Vikarna','Dushasan','Ashvathama'],'Age':[20,21,19,20,21],'Marks':[85.10,77.80,91.54,85.10,77.80]}
student_df=pd.DataFrame(student_dict)
student_df=student_df.drop_duplicates(subset=['Age','Marks'])
print(student_df)

#drop duplicates but keep last
student_dict={'Name':['Dushasan','Ashvathama','Vikarna','Dushasan','Ashvathama'],'Age':[20,21,19,20,21],'Marks':[85.10,77.80,91.54,85.10,77.80]}
student_df=pd.DataFrame(student_dict)
student_df=student_df.drop_duplicates(keep='last')
print(student_df)

# drop all duplicates
student_dict={'Name':['Dushasan','Ashvathama','Vikarna','Dushasan','Ashvathama'],'Age':[20,21,19,20,21],'Marks':[85.10,77.80,91.54,85.10,77.80]}
student_df=pd.DataFrame(student_dict)
student_df=student_df.drop_duplicates(keep=False)
print(student_df)

#drop duplicates and reset index

student_dict={'Name':['Dushasan','Ashvathama','Vikarna','Dushasan','Ashvathama'],'Age':[20,21,19,20,21],'Marks':[85.10,77.80,91.54,85.10,77.80]}
student_df=pd.DataFrame(student_dict,index=['a','b','c','d','e'])
print(student_df)
student_df=student_df.drop_duplicates(keep=False,ignore_index=True)
print(student_df)