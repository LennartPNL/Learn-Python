## Unsupervised ML vs. Unsupervised ML

__Unsupervised Learning__ has no labeled data and no distinct training phase.
Regression and classification are __supervised__ learning problems.
Unsupervised algorithms look at the data and tries to find patterns.It only looks at the X data.
Clustering and Principal Components Analysis are some examples of unsupervised learning.


__Supervised__ Learning

- Refers to all ML algorithms where labels are associated with the training data;
- These labels are used to tweak the model's parameters;
- Has input X and output Y;
- Tries learning the function y = f(x);
- Approximates the mapping function.

__Unsupervised__ Learning

- Have no labels that are used to tweak parameters;
- Has to be set up exactly right so it can learn the structure of the data;
- Only data X without Y labels;
- It tries to model the underlying structure;
- Self discovering algorithms;
- Make unlabelled data self-sufficient;
- Only a small fraction of available data has labels;
- Latent factor analysis;
- Clustering: identify data with same characteristics;
- Anomaly detection: detect outliers;
- Quantization: converting a continuous range of values to a finite range of discrete values;
- Can be used to pre-train data for supervised learning problems.

__Unsupervised Learning use Cases__

- Identify photo's of an individual person;
- Find common factors that drive the value of a group of stocks;
- Find relevant documents in a corpus;
- Flag fraudulent credit card transactions;
- Compress 24 bit into 8 bit color;
- Or used as pre-training for all of these use-cases.

#### Expressing attributes as numbers

__Clustering__

- These algorithms look within the data to discover patterns that allows to divide the data into logical groups;
- K-means clustering;
- You could group the data based on common attributes: group files based on their types for example;
- ML-A is used in too complex data;
- Anything can be represented by a set of numbers;
- N-attributes are represented in a N-dimensional hypercube;
- You want to maximize intra-cluster similarity;
- You want to minimize inter-cluster similarity.

#### K-means clustering

- A clustering algorithm;
- Finds groups in a dataset;
- You start by initializing K-centroids (means for example);
- Initialized at random;
- Assign each point to a cluster;
- Once the clusters are set up, the means are calculated: which makes it the new centroid of the cluster;
- This is iterated until they are final clusters (points no longer move = convergence);
- When the algorithm is converged, the entire cluster can be represented with this single point (reference vector/ centroid);
- You iterate until convergence;

Initializing K-centroids:
- Hyperparameters:
    - Number of clusters;
    - Initial value of centroids

First design choice:
- Distance measure between point and cluster;
- Euclidean distance for example

Second design choice:
- Calculating the cluster center from all points in the cluster;
- Calculate the simple average of all points

__Total reconstruction error__:

- When you find all euclidean distances between all points of all cluster centers;
- Sum over all points and reference vectors: this sum is the total reconstruction error;

__Hyperparameters__

- Parameters that can be set before training;
- During training they do not change;
- Are design choices;
- Choice depends on:
    - Kind of data that is available;
    - The problem statement;
    - Efficiency
- K is the most important one;
- Initial values are usually random;
- Right initial values could be found using Principal Component Analysis;
- Principle Components are normalized into K;
- Takes the average of each of these ranges.
- Distance measures:
    - Usually Euclidean distance;
    - Mahalanobis distance;
    - Cosine distance;
 

#### Patterns in data

__Auto encoders__:

- Neural networks that are capable of learning efficient representation of input data;
- Low dimensionality;
- Great for feature analysis;
- Finds patterns in numbers so it can remember the numbers in a more compact representation;
- Instead of remembering an enormous sequence of numbers, it tries to find a function that 
can define a pattern (like Collatz's sequene for example);
- The compact representation is called an __encoding__.

#### Principal Components Analysis

- Choosing the right axis makes sure that you need less dimensions to represent a dataset;
- The quality of representation on a chosen axis can be determined by the distances between each point;
- The greater the distances, the better the line;
- (3,3), (3,4), (3,5), (3,6) -> this data is best represented on the Y axis, if it is represented on the X axis, it is only one datapoint;
- The direction along which this variance is maximized is the __First Principal Component__ of the original data;
- The __Second Principal Component__ is the next best direction: the second largest variance;
- The first and second are always represented at a right angle, this helps express the most variation with the least number of directions;
- The names (first, second, third) of the principal component are ordered descending, by the amount of information captured;
- The number of principal components required is the same as the number of dimensions in your data;
- You redraw principal components;
- You reorient the dataset so that it is expressed in terms of these new axis;
- If you find the variance of the second principal component to be small enough, it is insignificant and can be ignored;
- So it it used to reduce the dimensionality.

#### Auto Encoders  

- Neural Networks that need to be trained, but do not have labelled data;
- Seek to learn the most important features/hidden latent factors in the data;
- They reconstruct the input through the output;
- They use the input itself to train the model;
- Then the output is fed back into the ML-A through the cost function;
- X = f(X) = g(L);
- Auto encoders uncover latent factors L that drive the data;
- Unsupervised technique that serves as a preparation for a supervised ML-A.

#### Auto encoder NN architecture

__Trivial auto encoder__:

- One layer of neurons;
- These neurons accept input X1-Xn;
- They copy the input value to the output -> X1 == Y1;
- It does nothing;
- The same layer is the input and output layer;
 
__Constraining it__:

- Feed the input to a hidden layer;
- Feed that data to an output layer;
- A middle hidden layer with three neurons forces a three dimension representation of the data;
- The output can not be a perfect mach because of this;
- The Output layer must be of the same size of the amount of inputs;
- This would be an undercomplete auto encoder.

#### Stacked auto encoders

__Avoiding overfitting__:

- Stacking auto encoders;
- The smallest layer is in the center;
- More layers make it possible to learn more complex patterns;
- If it completely learns a dataset it is overfitted;
- You could tie the weights of symmetric hidden layers to avoid overfitting;
- You could also train the hidden layers independently.

#### Denoising Auto Encoders

- Add in some random noise to the input, so the auto encoder is forced to recover the signal from the noise;
- In this way it can not just copy the input;
- This also prevents overfitting;
- You can add white noise (Gaussian random numbers);
- Or dropout.



