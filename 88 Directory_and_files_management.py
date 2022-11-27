import os
print(os.getcwd())

#change directory

os.chdir(r'c:\Users\bhavatavi\Desktop\Docs')
print("Directory changed")
print(os.getcwd())
os.chdir(r'c:\Users\bhavatavi\Desktop\files')

#listdir
print(os.listdir())

# make directory
#os.mkdir('python_series')
print("Directory created")
print(os.listdir())

# rename

#os.rename('python_series','python_learning')
print("Directory renamed")
print(os.listdir())

#remove directory
#os.rmdir(r'c:\Users\bhavatavi\Desktop\files\python_learning')
print('Directory deleted')
print(os.listdir())

import shutil
shutil.rmtree('insta')
print(os.listdir())