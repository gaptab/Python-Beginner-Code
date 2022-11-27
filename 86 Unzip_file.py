import zipfile as zip
target='chatapp.zip'
print("Starting to Unzip the file\n")
root=zip.ZipFile(target)
root.extractall('unzipped chatapp')
root.close()
print("\n File is Successfully Unzipped!")
