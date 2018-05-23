# Traceback as a string

import traceback

try:
    raise Exception('Error!')
except:
    errLog = open('log.txt', 'w')
    errLog.write(traceback.format_exc()) # Write the traceback error to your new file
    errLog.close()
    print('errors logged in your file')