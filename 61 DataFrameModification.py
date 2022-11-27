
import pandas as pd
student_dict={'Name':['Saubari','Kandu','Vritasur'],'Age':[22,24,19],'Marks':[76,85,91.7]}
student_df=pd.DataFrame(student_dict)
filter=student_df['Marks']>80
student_df['Marks'].where(filter,other=0,inplace=True)
print(student_df)

student_df=student_df.filter(like='N',axis='columns')
print(student_df)

student_dict={'Name':['Saubari','Kandu','Vritasur'],'Age':[22,24,19],'Marks':[76,85,91.7]}
student_df=pd.DataFrame(student_dict)
student_df=student_df.rename(columns={'Marks':'Percentage'})
print(student_df)

#join
student_dict={'Name':['Saubari','Kandu','Vritasur'],'Age':[22,24,19]}
student_df=pd.DataFrame(student_dict)
marks_dict={'Marks':[77,92,85]}
marks_df=pd.DataFrame(marks_dict)
print(marks_dict)
joined_df=student_df.join(marks_df)
print(joined_df)

#group by
student_dict={'Name':['Saubari','Kandu','Vritasur'],'Class':['C','A','B'],'Marks':[76,85,91.7]}
student_df=pd.DataFrame(student_dict)
student_df=student_df.groupby('Class').mean()
print(student_df)

#DFIteration
student_dict={'Name':['Saubari','Kandu','Vritasur'],'Age':[22,24,19],'Marks':[76,85,91.7]}
student_df=pd.DataFrame(student_dict)
for index,row in student_df.iterrows():
    print(index,row)
    
#Sort
student_dict={'Name':['Saubari','Kandu','Vritasur'],'Age':[22,24,19],'Marks':[86,85,71.7]}
student_df=pd.DataFrame(student_dict)
student_df=student_df.sort_values(by=['Marks'])
print(student_df)

dict=student_df.to_dict()
print(dict)