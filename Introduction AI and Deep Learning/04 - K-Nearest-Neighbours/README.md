## K-Nearest Neighbours for digit recognition

- Making use of the MNIST handwritten digit dataset.
- __MNIST__ = Modified National Institute of Standards and Technology

The DB can be downloaded from: http://yann.lecun.com/exdb/mnist/ - there is a TensorFlow library that can do this


## K-Nearest Neighbour for Unsupervised Learning

- ___Unsupervised__ ML-A's the model has to be set up, but is also responsible for learning the structure of the data
- If X is the input and Y is the output: the unsupervised ML-A 
is responsible for finding the mapping function -> Y = f(X)
- The mapping function needs to be estimated so well, that it is able to predict Y based on the input of a previously unknown X
- An existing dataset is used to correct the mapping function approximation
- The model learns about the underlying structure 
- Algorithms discover patterns and structure in the data by themselves

- The __K-nearest Neighbour Algorithm__, for images for example, returns an estimation of what known Y the previously unknown X looks like the most.
- The neighbours of a sample are calculated by __distance measures__: they indicate how far one datapoint is from another.

  
#### One-hot notation and L-1 distance

The Euclidean distance is the most common way of calculating the distance between two points.
Euclideandistance(X,Xi) = SquareRoot(sum((Xj-Xij)^2))
Goes in a straight line.


L1 distance is the preferred metric when dealing with points in a discrete space.
Also known as the snake distance/city block distance/ Manhattan distance.
It corresponds to the number of grid blocks that have to be travelled to reach the destination.
Going from point (1,0) to (5,4) ->  5 - 1 = 4 -> 4-0 = 4 -> 4 + 4 = 8 blocks are travelled.

The __One Hot Notation__ for labels of images for example:
in the handwritten number dataset you have numbers form 0 to 9.
The label of a written number 2 should be [0,0,1,0,0,0,0,0,0,0,0].
Only one of the numbers between 0 and 9 is a 2.
only categorical variables can be represented in the one-hot form.

The one hot notation of the feature vectors of images:
- An image of 28x28 (784 pixels)
- Grey scale (single channel of a number between 0.0 and 1.0)
- Every singe pixel will be added to one single long vector (of 784 elements)
- So a tensor of the shape of 784
- Not the best representation
- A grid is a better representation: finding groups of pixels
- In a flat representation you lose the data of having a stacked image
- for more accuracy you would have to use a more dimensional representation of an image

Using the 784 element vector as a training digit: 
- Calculating the L-1 distance would mean you compare it to another 784 element vector
- First you would calculate the negative (tf.negative()) of the other vector
- Then you would add up the two vectors: you subtract the other vector from the training vector
- These steps are repeated for every image in the training data
- You will need the absolute values (negative to positive -> tf.abs() to calculate te distance between every of the elements
- Each vector will element-wise be reduced to just one number (tf.reduce sum())
- When you use 5000 training digit you will have 5000 distances
- Now all the distances need to be sorted and an average of the k-neighbours nearest to our test-digit needs to be calculated
- So you would need to find the digit that is the closest to the digit in the training data
