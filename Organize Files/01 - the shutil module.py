# Using the shutil module

import os, shutil


# This will copy the file into the textfiles folder
shutil.copy('CopyThisFile.txt', 'textfiles/')

#This will also copy the file into that folder, but it has a different name
shutil.copy('CopyThisFile.txt', 'textfiles/CopyOfCopyThisFile.txt')

# This will copy the folder's contents (and subfolders) to your destination
shutil.copytree('C:\Program Files\Windows Photo Viewer', 'somefiles/')

# This moves the file into the specified folder
shutil.move('FileToMove.txt', 'textfiles/')

# To ensure you don't overwrite certain files, you can move and rename
shutil.move('FileToMove2.txt', 'textfiles/FileToMove2.txt')

