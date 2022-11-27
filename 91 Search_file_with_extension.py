import glob,os
os.chdir('text_files')
for file in glob.glob('*.txt'):
    print(file)
    
#os module

for file in os.listdir('text_files'):
    if file.endswith('.txt'):
        print(file)
        
#os.walk

for root,dirs,files in os.walk('text_files'):
    for file in files:
        if file.endswith('.txt'):
            print(file)