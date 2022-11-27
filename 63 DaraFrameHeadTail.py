import pandas as pd
student_dict={'Name':['Kumbhakaran','Indrajeet','Meghnath','Sugreev','Bali','Jatayu','Jambvaan'],
              'Age':[20,21,19,17,18,19,17],
              'Marks':[85.10,77.80,91,87,90,94,91]}
student_df=pd.DataFrame(student_dict)
topRows=student_df.head()
print(topRows)
topRows=student_df.head(-2)
print(topRows)

index=pd.MultiIndex.from_tuples([('Standard 1','Class A'),('Standard 1','Class B'),
                                 ('Standard 2','Class A'),('Standard 2','Class B'),
                                 ('Standard 3','Class A'),('Standard 3','Class B')],
                                name=['Standard','Class'])

columns=pd.MultiIndex.from_tuples([('Name','Surname'), ('Marks','Percentage')])

student_df=pd.DataFrame([('Kumbhakaran',67),('Indrajeet',80),('Meghnath',75),
                         ('Sugreev',87),('Bali',90),('Jatayu',94)],
                        index=index,columns=columns)
topRows=student_df.head()
print(topRows)

# DataFrame Tail

student_dict={'Name':['Kumbhakaran','Indrajeet','Meghnath','Sugreev','Bali','Jatayu','Jambvaan'],
              'Age':[20,21,19,17,18,19,17],
              'Marks':[85.10,77.80,91,87,90,94,91]}
student_df=pd.DataFrame(student_dict)
bottomRows=student_df.tail()
print(bottomRows)

bottomRows=student_df.tail(-2)
print(bottomRows)

# select bottom rows from the multi index dataframe

index=pd.MultiIndex.from_tuples([('Standard 1','Class A'),('Standard 1','Class B'),
                                 ('Standard 2','Class A'),('Standard 2','Class B'),
                                 ('Standard 3','Class A'),('Standard 3','Class B')],
                                name=['Standard','Class'])

columns=pd.MultiIndex.from_tuples([('Name','Surname'), ('Marks','Percentage')])

student_df=pd.DataFrame([('Kumbhakaran',67),('Indrajeet',80),('Meghnath',75),
                         ('Sugreev',87),('Bali',90),('Jatayu',94)],
                        index=index,columns=columns)
bottomRows=student_df.tail()
print(bottomRows)

# at function
student_dict={'Name':['Kumbhakaran','Indrajeet','Meghnath','Sugreev','Bali','Jatayu','Jambvaan'],
              'Age':[20,21,19,17,18,19,17],
              'Marks':[85.10,77.80,91,87,90,94,91]}
student_df=pd.DataFrame(student_dict)

value=student_df.at[2,'Age']
print(value)

student_df.at[2,'Age']=50
print(student_df.at[2,'Age'])

#iat function
student_dict={'Name':['Kumbhakaran','Indrajeet','Meghnath','Sugreev','Bali','Jatayu','Jambvaan'],
              'Age':[20,21,19,17,18,19,17],
              'Marks':[85.10,77.80,91,87,90,94,91]}
student_df=pd.DataFrame(student_dict)
value=student_df.iat[1,2]

student_df.iat[1,2]=90
print(student_df.iat[1,2])