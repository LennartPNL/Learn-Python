# Introduction to Machine Learning
 Define characteristics Machine Learning

##TensorFlow:

- Used in Deep Learning and Neural Networks
- Platform independent
- Library for numerical computations
- Becoming the default library

##Machine Learning:

- Finds relations in huge amounts of data
- Is used to find patterns and make intelligent decisions
- Change their behaviour based on the data that is presented to it
- So: they learn from the data

##Machine Learning algorithms:
- Is used in mail classification for example:
- To define if some e-mail is spam, a few years back a set of static rules would determine 
if it was spam or not.
- Spammers would adapt to static rules:
- Now the rules adapt to the data the spammers generate when they change their tactics

##An image is also a dataset:
- It is a set of pixels
- Based on identified shapes, colours, edges and lines, it might be able to classify a picture

##Usual problems that people are trying to solve with Machine Learning;
- Classification
- Regression
- Clustering
- Rule extraction

The biggest difference between rule based systems and Machine Learning
systems is that the latter changes it's inner workings based on the data that is processes.

###### End of introduction

# Representation Learning

### Traditional Machine Learning

For example, you are trying to classify animals.

We have a whale and we want to classify it as either a fish or a mammal.
You could do this without ML:
 - Pass an animal to a rule based classification system which is made by humans

With ML:
- Pass a set of attributes to a ML-system: it does not have human made rules, but a corpus of data
- It will refer to all examples in the corpus, and will, by comparing your given attributes to the attributes
in the corpus, conclude what kind of animal a whale is 
- If the ML system is loaded with a faulty dataset, it can only produce faulty conclusions  

- The corpus should be large and accurate
- It must have correct features, which are defined by human experts:
- You need to tell the system what the features are

##### Main difference between ML-based and rule-based

**These apply to traditional Machine Learning Systems, Deep Learning Systems are different*

| ML                    | Rule                      |
| -------------         |-------------              | 
| Dynamic               | Static                    |
| Experts are optional  | Experts are required      | 
| Corpus required       | Corpus optional           | 
| Must be trained       | Doesn't need training     |

- The set of attributes we tell our ML-algorithm to pay attention to is called a __Feature Vector__.
- The output a classifier generates is called a __Label__.

__Feature Vectors__
 
- *Features* are the attributes that the ML-Algorithm focuses on
- *Vectors*: each data point is a list of features


# Introduction to Neural Networks/ Deep Learning

__Traditional ML-Systems__ still need human experts to select certain features.
The more complex the system becomes, the more important the human experts become.

__Representation ML-Systems__ skips the humans: they figure out themselves what features are important.

__Neural Networks__ are the most common type of Deep Learning Algorithms.

__Neurons__ are the simple building blocks that actually learn.

__A Deep Learning Classifier would work like this__:

- The system will take in a corpus of images
- It will feed these into different layers:
- Layers with: 
    - Pixels
    - Edges
    - Colors 
    - Lines
    - Output Layer (Object Parts)
 - The programmer only deals with the input and output layers, known as the __Visible Layers__.
 The other layers are called the __Hidden Layers__.
 - The hidden layers are a black box, meaning that you will have to trust the model to do it's work right.
 
__Deep Learning__ refers to the fact that a Neural Network consists of neurons arranged in depth.
Each layer has connections with the following layer. When there are too many connections, it might be possible that you 
fit the training data too much to the network. This would mean it is only applicable to the given corpus 
of data and not to new data. This means you would have to drop some connections, which is known as __Drop Out__.

 
__Layers__ consist of individual interconnected __neurons__.

# Introduction to TensorFlow

- Is an open source library for numerical computations using data flow graphs.
 
__Advantages__:
- It is distributed: it runs on a cluster of machines or multiple GPU's/CPU's
- It is part of a suite of software

__Common Uses__:
- Research and development of new ML-Algorithms
- Take models from training to productions
- Large scale distributed models
- Models for mobile and embedded systems

__Strengths__:
- Easy and stable Python API
- Runs on both large as small systems
- Very efficient 
- Has additional tools

__Challenges__:
- Distributed support is not yet where it has to be
- Libraries are still in development
- Making custom Neural Networks is not simple

All computations are modelled in a graph.
Every node stands for a computation, all nodes are connected to each other by __Tensors__.


## Intro to computation graphs

- Everything is a graph in a neural network
- Each neuron is a pair of operators
- The lines are the data items, or Tensors (in TensorFlow)
- Tensors flow through the computation graph
- Individual neurons perform (simple) calculations

__Directed acyclic graphs__ have lines that point forward towards the result.
They have dependencies: nodes depend on other nodes. A node can send and receive output from and to multiple nodes.
The node immediately before the output are called the __Direct Dependency__. All other nodes __Indirect Dependencies__.
Data only flows from the input towards the output. So there are no cycles..

__ML Process__:
- Is cyclical
- The corpus of data is fed to the ML-Algorithm and it produces a result
- The ML-A changes itself based on the input data:
- The loss is calculated and then put back into the ML-A
- This creates a cycle
- The ML-A has a state: it needs to change based on the performance, which is done by TensorFlow
- The outputs of the network are fed back into a new iteration of the graph, which is known as the __Feedback Mechanism__.

Two steps are taken in a TensorFlow Program
- Building a graph
- Running the graph

Both are done separately.

__Tensorboard__ can be used to view how data flows and what computations operate on it.
Tensorflow calculates only the required portion of a graph.


## Tensors

- Are data-items: the central unit of data in TensorFlow.
- A tensor consists of a set of primitive values (integers, floats, etc.) 
shaped into an array of any number of dimensions.

- __Scalars__ can be seen as 0-dimensional tensors: 12, 4.2, "p" are scalars for example
- __Vectors__ are 1-dimensional tensors: [1,4,8,2,78] is a vector for example
- __Matrices__ are 2-dimensional tensors [[1,2,3],[4,2,1],[5,3,8]] is a matrix for example
- __More than 2-dimensional__: are called N-dimensional

__Characteristics of a tensor__:

- __Rank__: the number of dimensions in a tensor
- __Shape__: the number of elements in each dimension
- __Data Type__: the data type of each element in the tensor

__Shape__

| Tensor Example                   | Shape                      |
| -------------         |-------------              | 
| 4               | []                    |
| [4,2,1]  | [3]     | 
| [[1,2,4],[2,5,1]]       | [3,2]           | 
| [[[1],[2]],[[3],[4]]]     | [2,2,1]   |

## Linear Regression Introduction

#### Linear:

- Simplest example of a machine learning problem
- Used to measure causal relationships (X causes Y, 
X is the independent variable and Y is the dependant variable)
- This results in a straight line on a graph
- It finds the best straight line to pass through all (X,Y) points
- Line: Y = A + Bx

#### Simple Regression:

- In a case of perfect linear regression, the same A and B 
constant should be enough to predict the value of Y, using any X value.
This finds the best fitting line.

- Minimizing Least Square Errors: minimize the sum of the Y-value between a 
data point on the graph and the best fitting line: the residuals need to be as small a possible.

## Placeholders and variables

- The 'best' regression line: Y = Astart + BstartX could yield a very bad line
- The least square error needs to be calculated: the values of A and B have to change 
to get a better fitting line: Y = A1 + B1X.
- This could result in a better line, but still needs optimization:
the next step is Y = A2 + B2X
- This continues until the best line (lowest Square errors) is found
- This is an example of a supervised algorithm: any ML-A we train where we already know the correct answer
is known as a supervised approach.
- Unsupervised ML is used when you do not know the correct datapoints of a dataset


#### Placeholders

- Mechanism in TensorFlow that specify inputs into a graph:
you will specify these inputs 
- These are your X and Y value on a graph, which of course can always vary 
- These are our input-nodes
- The hold the place for a tensor that will be fed into the ML-A at runtime

## Variables

- Are a tensorFlow construct which are required for the training process,
because the algorithm is going to approach the solution iteratively
- The ML-A must be able to hold constantly changing values of it's model's parameters

TensorFlow has __three types of constructs__: 
- Constants: Do never change
- Placeholders: Are assigned once for one run of a model, and do not change after that. They are the inputs into the computation graph.
- Variables: These are constantly recomputed, at each iteration during training the model

variables will hold their value across running the session 
(Session.run()). 



### Notes:
- I do not use Google Cloud Computing, you could if you want.
 