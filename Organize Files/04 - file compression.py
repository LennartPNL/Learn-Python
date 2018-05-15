# Compressed Files

import os, zipfile

# READING ZIPFILES

# Using the zipfile module to read zip files
zipped = zipfile.ZipFile('zipsample.zip')

# Prints the contents of the zip file
print(zipped.namelist())

about = zipped.getinfo('fileSize.txt')

# Prints the size of a particular file in the zip folder
print(about.file_size)

print(about.compress_size)

print('The compressed file is actually %s times smaller than the original!' % (round(about.file_size / about.compress_size, 1)))

# EXTRACTING ZIPFILES

# This extracts all files from zipsample.zip into a (newly created) folder called extracted
zipped.extractall('extracted')

# This extracts the specified file into the specified folder
zipped.extract('CopyThisFile.txt', 'extracted/specific')

zipped.close()
print()

# CREATING ZIPFILES AND ADDING FILES

# Creates the new zip file
createZip = zipfile.ZipFile('created.zip', 'w')

# This moves all the .txt files in your current working dir into the created.zip
for file in os.listdir():
    if file.endswith('.txt'):
        print(file)
        createZip.write(file, compress_type=zipfile.ZIP_DEFLATED)
        print()

createZip.close()




