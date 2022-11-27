import pathlib
print(pathlib.Path('waterlily.jpg').parent.absolute())
print(pathlib.Path().absolute())

# os module

import os
print(os.path.dirname(os.path.abspath('redrrose.jpg')))#file path
print(os.path.abspath(os.getcwd())) #cwd