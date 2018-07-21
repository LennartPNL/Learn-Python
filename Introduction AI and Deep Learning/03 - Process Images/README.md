## Working with images

- __Image Recognition__ is the 'hello world' of tensorFlow

In images, pixels are the features in a feature vector. 
Convolutional Neural Networks are useful for image recognition.


#### Images as tensors

- Pixels are little rectangles that together make an image
- Each pixel holds some value, for example an RBA value (255,0,0 is red for example)
- In greyscale images, each pixel represents only one value between 0.0 and 1.0 (intensity of a shade of black
0.0 is white, 1.0 is black)
- Both greyscale and color images can be represented as 3-dimensional tensors:
two dimensions will refer to the X,Y location of the pixel. The third will refer to the shape of the element.
So a greyscale image of 100 by 100 pixels is (100,100,1) and a RGB image of the same size is (100,100,3).

#### Lists of images in 4-d tensors

A list of ten images that are RGB and 100x100 is represented like (10, 100,100,3) - the shape vector of the 4-dimensional tensor that you would use.
This is only possible if all images are of the same size.




