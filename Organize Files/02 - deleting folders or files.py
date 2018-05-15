# Delete files and folders

import os


# Creating a dummy file
f= open("createsome.fake","w")
f.write('Something')
f.close()


# For all files in our current folder
for file in os.listdir():
    if file.endswith('.fake'):
        # And deleting the file again
        os.unlink(file)
        # This will permanently delete these files, which can be dangerous
        print(file)

# Send2Trash module

import send2trash

# You will have to install the send2trash module by:
# open terminal --> cd C:\Python36 (or wherever your python is installed) -- > python -m pip install send2trash

f= open("mess.txt","w")
f.write('i will be trash')
f.close()

# This moves the file to your recycle bin
send2trash.send2trash('mess.txt')

