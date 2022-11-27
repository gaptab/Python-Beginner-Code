import pandas as pd
student_dict={'Name':['Sarmistha','Devyani'],'Age':[18,19],'Marks':[86,90]}
student_df=pd.DataFrame(student_dict)
print(student_df)
student_df=student_df.drop(columns='Age')
print(student_df)

student_dict={'Name':['Sarmistha','Devyani'],'Age':[18,19],'Marks':[86,90]}
student_df=pd.DataFrame(student_dict)
print(student_df)
student_df=student_df.drop(columns=["Age","Marks"])
print(student_df)

#axis
student_dict={'Name':['Sarmistha','Devyani'],'Age':[18,19],'Marks':[86,90]}
student_df=pd.DataFrame(student_dict)
print(student_df)

student_df=student_df.drop(['Age','Marks'],axis=1)
print(student_df)

#Suppressing errors

student_dict={'Name':['Sarmistha','Devyani'],'Age':[18,19],'Marks':[86,90]}
student_df=pd.DataFrame(student_dict)
print(student_df)

student_df=student_df.drop(columns='Salary',errors='ignore')
print(student_df)

#drop by index position

student_dict={'Name':['Sarmistha','Devyani'],'Age':[18,19],'Marks':[86,90]}
student_df=pd.DataFrame(student_dict)
print(student_df.columns.values)

pos=len(student_df.columns)-1
student_df=student_df.drop(columns=student_df.columns[pos])
print(student_df.columns.values)

#iloc
student_dict={'Name':['Sarmistha','Devyani'],'Age':[18,19],'Marks':[86,90]}
student_df=pd.DataFrame(student_dict)
print(student_df)

student_df=student_df.drop(columns=student_df.iloc[:,1:3])
print(student_df.columns.values)

# drop first n columns

student_dict={'Name':['Sarmistha','Devyani'],'Age':[18,19],'Marks':[86,90]}
student_df=pd.DataFrame(student_dict)
print(student_df)

student_df=student_df.drop(columns=student_df.iloc[:,range(2)])
print(student_df.columns.values)

