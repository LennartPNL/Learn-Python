# Removing unwanted files from a video collection
# Author: Piraato
# If you have a huge collection of (torrented) movies, you want the collection to be clean
# So all files except video files and subtitle files should be removed
# Also, empty folders should be removed
# Only video files and subtitles remain after running this program!

import os
import time
import datetime
import shutil

# First, let's get our current working directory
cwd = os.getcwd()

f = open('logTrashClear.txt', 'a')

# Writing the current time to the log file
f.write("==========Ran at: " + str(datetime.datetime.now()) + '==========')
f.write('\n\n')

i = 0
# If we have folders with empty subfolders, and they make the upper folder a empty folder (jesus)
# You want that folder to be removed too. That's why we loop the program.
while i < 10:
    for folder, subfolders, filenames in os.walk(cwd):

        for filename in filenames:
            # Telling the program which files to keep
            if not filename.lower().endswith(('.avi', '.mp4', '.mkv', '.srt', '.ini', 'wmv', 'flv')) and not 'clearTrash.py' in filename and not 'logTrashClear.txt' in filename:
                try:
                    os.unlink(folder + '/' + filename)
                    f.write('- ' + folder + ': ' + filename + ' is deleted! \n')
                except Exception as e:
                    f.write('FILE - ' + folder+ '\\' + filename + ' threw error %s. \n' % e)
                # Logging what files are being deleted


        for subfolder in subfolders:
            # If the list of items in a folder returns false, the folder is empty
            if not os.listdir(folder + '/' + subfolder):
                # So we remove the folder
                try:
                    shutil.rmtree(folder + '/' + subfolder)
                except Exception as e:
                    f.write('FOLDER - ' + folder+ '\\' + subfolder + ' threw error %s. \n' % e)

    i = i + 1

f.write('\n\n')
f.write('**********END at: ' + str(datetime.datetime.now()) + '**********')
f.write('\n\n')
#cont = input()
f.close()