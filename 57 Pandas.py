import pandas as pd
student_dict={'Name':['Karna','Arjun','Bheem'],'Age':[30,25,34],'Marks':[85,90,87.65]}
print(student_dict)

student_df=pd.DataFrame(student_dict)
print(student_df)

df=pd.DataFrame({'X':[12,67,89,90,45],'Y':[65,76,87,43,65],'Z':[87,34,23,12,55]})
print(df)

df1=pd.DataFrame({'A':[1,2,3],'B':[True,True,False],
                  'C':[0.45678,-0.3425,0.98765]},
                 index=['a','b','c'])
print(df1)