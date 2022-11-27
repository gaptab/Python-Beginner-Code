# os module
import os
file_stat=os.stat('waterlily.jpg')
print("The size of file is:",file_stat.st_size,'bytes.')

# pathlib module

from pathlib import Path
file=Path("waterlily.jpg")
print("The size of file is:",file.stat().st_size,'bytes.')