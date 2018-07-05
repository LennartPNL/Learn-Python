# Launching other programs

import subprocess, os

i = 0


# opens 4 instances of paint

while i < 5:
    p = subprocess.Popen("C:\\Windows\\system32\\mspaint.exe")
    i += 1

# poll() returns None if the process is still running
print(p.poll() == None)

# Arguments with Popen

# Opening text files
pro = subprocess.Popen(["C:\\Windows\\system32\\notepad.exe", "test.txt"])

# Running python code

process = subprocess.Popen(["C:\\Python36\\python.exe", "openme.py"])

# Opening with default application #

openPic = subprocess.Popen(["start", "piraato.png"], shell=True)
openMD = subprocess.Popen(["start", "README.md"], shell=True)