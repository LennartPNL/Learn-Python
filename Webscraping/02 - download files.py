# Downloading with the request module

import requests

# you probably have to install this one: py -m pip install requests

res = requests.get('http://piraato.nl/goatSuckingNipple.jpg')
type(res)

# This should evaluate to true
print(res.status_code == requests.codes.ok)

# Error checking

res2 = requests.get('http://google.nl/oh_damn/skittles/6235986328')

try:
    res2.raise_for_status()
except Exception as e:
    # Page nod found
    print('Whoops: %s' % (e))
    
# downloading text

res3 = requests.get('http://www.piraato.nl/index.php')

res3.raise_for_status()
file = open('indexPiraato.txt', 'wb')

for part in res3.iter_content(1000000):
    file.write(part)

file.close()



