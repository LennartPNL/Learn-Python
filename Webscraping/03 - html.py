# Parse HTML with Beatiful Soup
# You will have to install the module: pip install bs4

import bs4
import requests

website = 'https://www.piraato.nl'

res = requests.get(website)

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

# This prints out all the HTML on the given website

print(soup)

# Finding elements with select()

print('----------')

# Selects all the elements with the name div
print(soup.select('div'))

# Selects all the elements with the id attribute contact-button
print(soup.select('#contact-button'))

# Selects all the li elements that are in a ul that is in a div
print(soup.select('div ul li'))

# Selects all elements img that have a attribute named src that has any value
print(soup.select('img[src]'))

# Selects all elements img that have a attribute named alt that has the value of 'python'
print('Python: ' + str(soup.select('img[alt="python"]')))


