# Directory Trees

import os

# You should also try this with other folders
# using os.walk()
for folder, subfolders, filenames in os.walk('C:\\Program Files\\windows nt'):
    print('Current folder: ' + folder)

    for subfolder in subfolders:
        print('Contains folder: ' + folder + ' \ ' + subfolder)

    for filename in filenames:
        print('File in ' + folder + ': ' + filename)

    print()
    print('==========NEXT==========')


# This will rape your PC, if you remove the # form line 24
for file in os.walk('C:\\'):
    # WARNING:
    # This will permanently delete all files on your C drive
    # os.unlink(file)
    print(file)

