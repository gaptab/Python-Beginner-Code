import pandas as pd
import numpy as np
student_dict={'Names':["Vena","Mura","Kamsa","Madhu"],'Age':[22,35,43,23],'Marks':[85.90,np.nan,np.nan,90]}
student_df=pd.DataFrame(student_dict)
print("Before dropping column NA:\n",student_df)

student_df=student_df.dropna(axis='columns')
print("After dropping column NA:\n",student_df)

# Drop column where all values are missing
student_dict={'Names':["Vena","Mura","Kamsa","Madhu"],'Age':[np.nan,np.nan,np.nan,np.nan],'Marks':[85.90,np.nan,np.nan,90]}
student_df=pd.DataFrame(student_dict)
print("Before dropping column NA:\n",student_df)

student_df=student_df.dropna(axis='columns',how='all')
print("After dropping column NA:\n",student_df)

student_dict={'Names':["Vena","Mura","Kamsa","Madhu"],'Age':[22,35,43,23],'Marks':[85.90,np.nan,np.nan,90]}
student_df=pd.DataFrame(student_dict)
print("Before dropping column NA:\n",student_df)
student_df=student_df.dropna(axis='columns',thresh=3)
print("After dropping column NA:\n",student_df)

student_dict={'Names':["Vena","Mura","Kamsa","Madhu"],'Age':[22,35,43,23],'Marks':[85.90,np.nan,77,90]}
student_df=pd.DataFrame(student_dict)
print("Before dropping column NA:\n",student_df)
student_df=student_df.dropna(axis='columns',subset=[0,2])
print("After dropping column NA:\n",student_df)