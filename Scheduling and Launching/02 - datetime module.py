# The datetime module

import datetime
import time

now = datetime.datetime.now()

# Prints the current date and time
print(now)

# Prints the year
print(now.year)

# Prints the day
print(now.day)

# This can also be done for .month, .hour, .second, .minute

# Comparing dates

mahBirthday = datetime.datetime(2019, 1, 18, 0, 0, 0)
mahDogsBirthday = datetime.datetime(2019, 6, 11, 0, 0, 0)

print(mahBirthday > mahDogsBirthday) # False: mah B-day is before mah dog's b-day

print(mahDogsBirthday > mahBirthday) # So this is true

# Time Delta #

delta = datetime.timedelta(days=25, hours=16, minutes=22, seconds=21)

# Checking the days and microseconds in the delta
print(str(delta.days) + " " + str(delta.microseconds))

print(str(delta))

# Checking what exact date and time it is in 1000 hours
print("Thousand hours from now, it is: " + str(now + datetime.timedelta(hours=1000)))

someTimeAgo = datetime.timedelta(days=500 * 25)

# Adding and detracting days
print(str(now - someTimeAgo))
print(str(now + someTimeAgo))

# pausing until a certain time:

certainTime = datetime.timedelta(seconds=4)
justNow = datetime.datetime.now()
inABit = justNow + certainTime

while datetime.datetime.now() < inABit:
    time.sleep(1)
    print("sleeping..")

print("I slept great")

# Stringify time #

strTime = justNow.strftime("%Y/%B/%d")

print(strTime)

# Strings to time Object #

timeString = "June 28, 2022"
timeObject = datetime.datetime.strptime(timeString, "%B %d, %Y")
print(timeObject)

