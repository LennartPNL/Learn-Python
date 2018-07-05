# Images and their attributes
import random

from PIL import ImageColor

# COLOURS #

# Usually a computer works with RGBA values when representing colours

# This converts a color's name (e.g red) to a RGBA value

red = ImageColor.getcolor("red", 'RGBA')
green = ImageColor.getcolor("green", 'RGBA')
blue = ImageColor.getcolor("blue", 'RGBA')
yellow = ImageColor.getcolor("yellow", 'RGBA')

# Prints out all the RGBA values of the colors

print(red)
print(green)
print(blue)
print(yellow)

# The last value is the alpha, the opacity: 0 is invisible and 255 is fully visible

# COORDINATES #

# Pictures have coordinates: the origin (0,0 -> x,y) is in the top-left corner.

# X increases from left to right, Y increases from top to bottom

from PIL import Image

# THE IMG DATATYPE #

image = Image.open('ba.jpeg')

# Prints the max x and y of the image
print(image.size)

# Description of the image's format
print(image.format_description)

# You can also do .filename, .format

# Save the image
image.save('newimg.jpeg')

img = Image.new('RGBA', (50, 50), 'red')

# Creates an png image of 50 by 50 pixels which is fully red
img.save('redblock.png')

# CROPPING IMAGES #

# This crops the image as follows:
# Start cropping from X: 250 and form Y: 50
# End the crop region at X: 400 and Y: 200
cropped = image.crop((250, 50, 400, 200))

# You'll end up with Bassie's face
cropped.save('crop.jpeg')

# Copying and pasting

# Picture to edit
editThisPic = Image.open('newimg.jpeg')

# Picture to paste
pasteThisPic = Image.open('crop.jpeg')

# Pasting the image onto the original image, with coordinates
editThisPic.paste(pasteThisPic, (0, 0))
editThisPic.paste(pasteThisPic, (0, 180))
editThisPic.paste(pasteThisPic, (350, 0))
editThisPic.paste(pasteThisPic, (350, 180))

# Save the file
editThisPic.save('newimg.jpeg')

# Resizing pictures

width, height = editThisPic.size

# The dimensions of the picture *4
biggerImg = editThisPic.resize((int(width * 4), int(height * 4)))

biggerImg.save('bigbassie.jpeg')

# Rotating pictures

i = 0

x = 0

y = 0

deg = 0

mentalImg = Image.open('bigbassie.jpeg')

while i < 15:
    # .rotate() rotates the image a certain amount of degrees
    mentalImg.paste(pasteThisPic.rotate(deg), (x, y))
    mentalImg.paste(pasteThisPic.rotate(deg+10), (x+300, y-10))
    mentalImg.paste(pasteThisPic.rotate(deg+20), (x+600, y-20))
    mentalImg.paste(pasteThisPic.rotate(deg+30), (x+900, y-30))
    deg += 30
    x += 120
    y += 100
    i += 1

mentalImg.save('bigbassie.jpeg')

# CHANGING PIXELS #

# Create a new image
photo = Image.new('RGBA', (80,80))

# For every x and y value

colors = []

for x in range(80):
    for y in range(80):
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        a = random.randint(180,255)
        rgba = (r,g,b,a)
        # We only want unique colors in our piece of art
        if (x,y) not in colors:
            photo.putpixel((x,y), rgba)
            colors.append(photo.getpixel((x,y)))


photo.save('putpixels.png')

