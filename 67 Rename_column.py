import pandas as pd
student_dict={'name':['Menaka','Rambha','Urvashi'],'age':[20,21,22],'marks':[93,91,89]}
student_df=pd.DataFrame(student_dict)
print(student_df)
student_df=student_df.rename(columns={'name':'a','age':'b','marks':'c'})
print(student_df)

#Using a function to rename column
student_dict={'name':['Menaka','Rambha','Urvashi'],'age':[20,21,22],'marks':[93,91,89]}
student_df=pd.DataFrame(student_dict)
print(student_df)
student_df.rename(columns=str.upper,inplace=True)
print(student_df)

#lambda function to rename column

student_dict={'#name':['Menaka','Rambha','Urvashi'],'#age':[20,21,22],'#marks':[93,91,89]}
student_df=pd.DataFrame(student_dict)
print(student_df)
student_df.rename(columns=lambda x:x[1:],inplace=True)
print(student_df)

#Rename all columns with a list

student_dict={'name':['Menaka','Rambha','Urvashi'],'age':[20,21,22],'marks':[93,91,89]}
student_df=pd.DataFrame(student_dict)
print(student_df)
student_df.columns=['stud_name','stud_age','stud_marks']
print(student_df.columns.values)