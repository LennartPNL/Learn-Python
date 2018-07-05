# Multithreading

import threading, time

print("Starting")

def doNothing():
    time.sleep(5)
    print("Go work, damn it!")

def doNothingSpecial():
    time.sleep(2)
    print("Go work, you have too much to do!")

threadObject = threading.Thread(target=doNothing)
threadObject.start()

threadObject2 = threading.Thread(target=doNothingSpecial)
threadObject2.start()

# this line will appear right after "Starting":
# The doNothing and doNothingSpecial functions execute in a new thread so you do not have to wait for it to complete
print("End of script")


# Threading with arguments #

thrd = threading.Thread(target=print, args=['Hey', 'A', 'Function', 'With', 'Arguments'])
thrd.start()
