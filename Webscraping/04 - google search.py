# Small Google Search Project

import requests, webbrowser, bs4

print('Searching Big G.....')
print()

print('Enter your search term')
res = requests.get('http://google.com/search?q=' + ' '.join(input()))
print(res.raise_for_status())

soup = bs4.BeautifulSoup(res.text, 'lxml')

links = soup.select('.r a')

numOpen = min(5, len(links))

for i in range(numOpen):
    # Opens the first five search results in a new tab
    webbrowser.open('http://google.com' + links[i].get('href'))



