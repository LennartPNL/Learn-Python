# Json and APIs

import json

# JSON to Python #

jsonData = open("ex.json")

# Load the json file and make it Python friendly
jsonToPy = json.load(jsonData)

print(jsonToPy)

# Python to JSON #

pyVal = {"name": "Old mcDonald", "hasAFarm": True, "likesCheese": False, "likesPython": False, "chickens": 12}

jsVal = json.dumps(pyVal)

print(jsVal)

