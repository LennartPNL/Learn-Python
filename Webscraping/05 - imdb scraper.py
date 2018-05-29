# Scrape Movies and some of their details from imdb
# Write them to your database
# Made because I am too lazy to write dummy data for my database homework

###ENTER YOUR CREDENTIALS FIRST###

usr='root'
psswd='password'
db_host='127.0.0.1'
db='mydb'

import requests
import bs4
from random import randint
from datetime import date, datetime
import datetime
import mysql.connector


def addMovies(amount):
    website = 'https://www.imdb.com/search/title?count='+str(amount)+'&title_type=feature,tv_series&ref_=nv_wl_img_2'

    res = requests.get(website)

    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')


    # All Movie Titles
    movieTitles = soup.select('h3[class="lister-item-header"] a')

    i = 1
    titles = []
    for text in movieTitles:
        try:
            # Add all titles to the list
            titles.append(text.get_text())
            i = i + 1
        except Exception as e:
            print('Error parsing titles: ' + str(e))



    # All Movie Descriptions
    descriptions = soup.select('div[class="lister-item mode-advanced"] div[class="lister-item-content"] p[class="text-muted"]')

    i = 1
    mDiscriptions = []
    for text in descriptions:
        try:
            # Add all descriptions to the list
            mDiscriptions.append(text.get_text().strip())
            i = i + 1
        except Exception as e:
            print('Error parsing Descriptions: ' + str(e))



    # All Movie Years
    years = soup.select('div[class="lister-item mode-advanced"] div[class="lister-item-content"] span[class="lister-item-year text-muted unbold"]')

    i = 1
    mYears = []
    for text in years:
        try:
            # We need to remove all special characters used in the years
            removeSpecialChars = text.get_text().translate({ord(c): " " for c in "()–II"})
            # These are the first 4 digits of the string, since we only want the release year
            # Add all years to the list
            mYears.append(removeSpecialChars.strip()[:4])
            i = i + 1
        except Exception as e:
            print('Error parsing years: ' + str(e))



    i = 0
    month = int(datetime.datetime.now().strftime("%m"))
    day = int(datetime.datetime.now().strftime("%d"))


    while i < amount:
        print('\nItem ' + str(i))

        # SQL Query with placeholders
        addVideo = ("INSERT INTO videos "
                    "(title, description, video_types_id, release_date, duration, credits_time) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")

        # Try to add all values of the list to the queries
        try:
            year = int(mYears[i])
            dat = date(year, month, day)
            dur = randint(0, 320)
            cred = randint(0, dur)
            # The values to replace the placeholders in the query
            videoValues =  (titles[i],  mDiscriptions[i], 1, dat, dur, cred)
            cursor.execute(addVideo, videoValues)
            cnx.commit()
            print('-Sucessfully executed the query\n')
        except Exception as e:
            print('Something went wrong with the query:\n ' + str(e))

        i = i + 1
    # End of Function addMovies()


# Connecting to the database

try:
    cnx = mysql.connector.connect(user=usr, password=psswd,
                                  host=db_host,
                                  database=db)
    if cnx:
        print('-Connection To DB Established ')

    cursor = cnx.cursor()

except Exception as e:
    print('-Something went wrong while connecting to DB:\n ' + str(e))


addMovies(500)

# Close the connection to the database

cnx.close()

print('Code has been executed, press any key to close')
input()

'''
This code will crash when you try to run it without an internet connection
Also, if movies don't have a title, description or year, the whole order of the lists will be messed up.
But I have not encountered such a case yet. 
'''

