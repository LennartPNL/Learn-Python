# Drawing images

# Here, I try to make Python draw completely random images

from PIL import Image, ImageDraw, ImageFont
import random

# New canvas with random color
canvasC = (random.randint(0,255),random.randint(0,255),random.randint(0,255),255)

im = Image.new('RGBA', (200,200), canvasC)

draw = ImageDraw.Draw(im)

a = random.randint(0, 200)
b = random.randint(0, 200)
c = random.randint(0, 200)
d = random.randint(0, 200)
e = random.randint(0, 200)
f = random.randint(0, 200)
g = random.randint(0, 200)
h = random.randint(0, 200)
i = random.randint(0, 200)

points = [a,b,c,d,e,f,g,h,i]

randomList = []
i = 0

while i < 25:
    if (points[random.randint(0, len(points)-1)], points[random.randint(0, len(points)-1)]) not in randomList:
        randomList.append((points[random.randint(0, len(points)-1)], points[random.randint(0, len(points)-1)]))
        i += 1


c1 = random.randint(0, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

# Drawing some crazy shapes

draw.line(randomList, fill=(c1,c2,c3,255))
draw.rectangle((h, a, i, b), fill=(a,b,c,255))
draw.ellipse((i, e, f, d), fill=(d,e,f,255))
draw.polygon(randomList[2:6], fill=(a,e,g,255))

# Writing text
wordFile = open('dictionary.txt', 'r')

words = []

for w in wordFile:
    words.append(w)


ranWord = words[random.randint(0, len(words)-1)]

draw.text((i,a), ranWord, fill=(c2,b,c1,255))

im.save('drawing.png')