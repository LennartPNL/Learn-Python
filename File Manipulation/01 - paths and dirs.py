# Directrories and paths

import os # How paths are constructed, depends on your os

print(os.path.join('C', 'Users', 'Piraato')) # C\Users\Piraato on windows
# On MacOS or Linux this would be C/Users/Piraato
print()

myStuff = ['text.txt', 'pic.jpg', 'hacks.py']

for filename in myStuff:
    print(os.path.join('C:\\Users\\Piraato\\SecretFolder', filename))

print()

# Current dir

projectDir = os.getcwd()

print(projectDir) # cwd = current working directory (in my case D:\OneDrive\Dev\Python\File Manipulation)

os.chdir('C:\\Windows') # Change dir

print(os.getcwd()) # Current working directory is now changed to C:\Windows

os.chdir(projectDir) # Let's change that back


# Let's break the program

# os.chdir('D:\\FlopMyFlippersAndCallMeManfred') # Results in error: The system cannot find the file specified
# i assume you do not have a folder with that name on your computer...

print()

# Absolute and Relative paths

absolute = 'D:\\OneDrive\\Dev\\Python\\File Manipulation' # Includes the root folder

relative = 'Examples\\text' # Refers to a folder in the current working directory

# Creating folders


if 1 > 2: # Just so i won't have useless folders on my pc
    
    os.makedirs('C:\\Whoops') # creates the folder in this absolute path
    os.makedirs('Whoops') # creates the folder in the current working directory
    
else:
    print('I am not going to make these folders right now')

# Find the absolute path

print(os.path.abspath('.\\Example')) # D:\OneDrive\Dev\Python\File Manipulation\Example
print()

# base and dir

path = str('‪C:\\Windows\\System32\\Magnify.exe')

print(os.path.basename(path)) # Magnify.exe
print(os.path.dirname(path)) # ‪C:\Windows\System32
print(path.split(os.path.sep)) # ['\xxxxx:', 'Windows', 'System32', 'Magnify.exe']

# File sizes/ content of folders

print(os.path.getsize('C:\\Windows\\System32\\Magnify.exe')) # size is 809472 bytes

print(os.listdir(os.getcwd())) # lists all files in this dir: ['01 - paths and dirs.py', 'example.txt', 'README.md']

# print(os.listdir('C:\\Windows\\System32\\')) A LOT!
print()

# Size of all items in folder


total = 0

for file in os.listdir(os.getcwd()):
    total = total + os.path.getsize(os.path.join(os.getcwd(), file))

print(total) # total size of files in the current working directory
print()


# Checking path validity

somePath = 'C:\\Windows\\System32'
fakePath = 'D:\\FlopMyFlippersAndCallMeManfred'
someFile = 'C:\\Windows\\System32\\Magnify.exe'
print(os.path.exists(somePath)) # True
print(os.path.exists(fakePath)) # False
print(os.path.isdir(someFile))  # False, it is not a dir
print(os.path.isfile(someFile)) # True

print()

# Checking if device is attatched

print(os.path.exists('F:\\')) # My USB is F:






