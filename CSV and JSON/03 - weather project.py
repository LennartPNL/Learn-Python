# Fetch the current weather and a forecast for a given location

import json, requests

print("Enter your location: ")

# Get the user's input
location = str(input())
print()

# using the Yahoo API
url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22" + location + "%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

resp = requests.get(url)

r = resp.raise_for_status()

# Load the json file
weatherData = json.loads(resp.text)

# if we actually receive a usable file from Yahoo
if weatherData['query']['count'] == 1:

    # We are only interested in the key/value pairs after 'channel'
    w = weatherData['query']['results']['channel']

    # celsius =  (fahrenheit-32) /1.8
    celsius = (int(w['item']['condition']['temp']) - 32) / 1.800

    # print the result title (Yahoo may find something else than what you have searched for)
    print(w['item']['title'])

    # Current weather conditions
    print("Now: " + w['item']['condition']['text'] + " and " + str(round(celsius, 1)) + " degrees Celsius")

    # Just guessing what the average temperature of tomorrow will be
    avgTempTomorrow = (((int(w['item']['forecast'][1]['high']) + (int(w['item']['forecast'][1]['high']) / 6) + int(w['item']['forecast'][1]['low'])) / 2) - 32) / 1.8

    # Tomorrow's forecast
    print("Tomorrow " + w['item']['forecast'][1]['day'] + ' ' + w['item']['forecast'][1]['date'] + ': ' + w['item']['forecast'][1]['text'] + " and about " + str(round(avgTempTomorrow, 1)) + " degrees celcius")
else:
    # If you enter a bunch of nonsense, the program will let you know
    print("No results found for " + location)

# This program is not perfect: Yahoo may return a json file that is incomplete.
# For some places, you will not get a temperature for example.