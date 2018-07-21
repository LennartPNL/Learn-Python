## Learning algorithm

#### Neurons as Learning Units
 - The base classifier is learning a functiion
 - It tells us how the input links to the output label
 - That is learned using layers in the neural network
 - One layer learns what the pixels represent, other layers learn what other features represent,
 such as lines etc.
 - All layers are used to reverse engineer the relation of the input to the output
 
 #### Learning algorithms
 
 - It learns and improves with experience
 - A program learns from experience E, with respect to class of 
 task T amd measures performance in P. P in T should improve with E.
 - A __Task__ might be classification or regression and clustering
 - __Performance__ measures are specific to a task: the accuracy for example
 - __Experience__ in terms of the training process
 
 
 #### Deep learning
 
 - __Deep learning algorithms__ learn by tweaking the weight of their neurons
 - Layers in a computation graph represent groups of neurons that perform similar functions
 - Each layer contains multiple neurons that are interconnected with neurons in other layers
 - Deep learning means that there are many layers arranged in depth
 - Neural networks quickly become black boxes
 - Learning a ML-A linear regression only takes one single neuron:
 - A set of datapoints is fed into a simple neural network that consists of one neuron..;
 - The neuron will go through a training process that tweaks it's own parameters
 - A single neuron performs two operations, one of them is already like linear regression
 
 ## Example 
 
 #### Learning XOR
 
 - The function should look like:
 
```python
def XOR(X1,X2):
    if(X1==X2):
        return 0
    return 1
```
- This is a non-linear function, so you would need three neurons
- It has 2 inputs and will be automagically able to reverse engineer the XOR function
 
 __More__
 - Neural networks are capable of learning much more complex functions
 - Adding enough layers can learn a network any code possible
 

## The individual neuron

- The nodes in a computation graph are called neurons
- Each neuron performs a very simple operation
- These neurons are connected in complex ways
- The interconnection between neurons vary based on your application
- In a convolutional neural network, the neurons are wired in such a way it is optimal for image recognition
- A recurrent neural network is wired so it is better at text processing
- In practice, the architecture of the neural network and the way the neurons are connected to each other is very important
- Individual neurons only apply two simple functions to their inputs
- The first is an affine transformation (linear), which is like linear regression
- The second is an activation function, which is used to model non-linear functions

#### operation of one single neuron

- Inputs from X1 to Xn are fed into the neuron;
- The inputs will be multiplied by weights W1 to Wn;
- They are added to the bias b;
- This is known as an affine transformation - > Wx + b
- Wx + b gets passed to the activation function;
- The activation function might be something like max(Wx+b, 0);
- The transformation applied in the transformation function might change,
as well as the weights and the values of the biases

#### Example

- X1 to Xn might be a feature vector;
- The output of the activation function is the output of the neuron as a whole;
- The affine transformation and activation function define the neuron;
- Training a neural network means tweaking the parameters of these functions;
- The affine transformation is a weighted sum with an added bias (parameters W and b)

- __W and b__ are variables: not constants or placeholders!
- The values are determined by tensorFlow during the training process;
- The objective of the training process is finding the best values of W and b for each neuron
- The optimal values are found by using the cost function, an optimizer and a corpus:
these are defined by the programmer
- This will result in the best possible values
- The configurations can be very complex: so the training process can take very long
- The output of deeper layers of the network need to be fed back into the earlier layers in need to find the best values of W and b in these earlier layers
- That process is called __Back Propagation__ and is the standard way of training neural networks
- The affine transformation, thus, can learn a linear function;
- In order for the neuron to learn a non-linear function, 
the output of the affine function needs to be generalized using the activation function;
- A common activation function is the __ReLU__ (Rectified Linear Unit), which is the max of zero and the input;
- The output of the affine transformation is chained to the activation function;


## Simple regression

- If linear regression needs to be learned by our NN (Y = Wx + b),
we pass X inputs into the affine transformation function of a neuron.
- The output of that affine function exactly mirrors the regression equation
- The affine transformation is just a weighted sum of the inputs with a bias added 
- If we want to determine the value of Y based on the constants A and B: Y = A + Bx1
- Perfect equality is impossible, so we would need to calculate in some error rate: Y = A + Bx1 + E1
- The best values of A and B are the values that will minimize the sums of the squares of the residuals:
minimizing the least square error;
- E1 = Y1 - Y'1
- The line with the lowest sum of the squares of the errors, is the optimal line


## Learning the XOR function

- *To teach a neural network a specific function, it is wise to first research if it has been done before,
if not, you should experiment with different architectures of layers to determine which works best*;
- The outputs of the XOR functions can be seen in a truth table;
- Y depends on X1 and X2;
- XOR is not linearly separable;
- If you put all possible outcomes of the XOR function onto a graph, you will end up with 4 points in a square;
- (0,0), (0,1), (1,0), (1,1);
- No straight line can be drawn through these points;
- This is why XOR is not linear
- For XOR, you would need two neurons in the first layer and one neuron in the second;
- Inputs X1 and X2 will flow into both neurons of the first layer;
- Both of these neurons will have both an affine and transformation function;
- They will both have their own weights and biases;
- The outputs of these two neurons will be passed into a third neuron;
- That neuron will also have an affine and activation function;
- And the output of the last activation function will represent the output of the neural network as a whole;

#### More detailed

- X1 and X2 are put into neuron #1 as the inputs to the affine transformation;
- There will be weights and a bias;
- In neuron #2, the same happens;
- In the first two neurons, the activation function will be called, because the XOR function is not linearly separable;
- Wx + b is passed to the activation function;
- The activation function in this case will be the ReLU;
- ReLU will return the maximum of zero and some value (ReLU = max(X,0))
- The ReLU will pass their outputs to the third neuron, in the second layer;
- This amount of non-linearity is enough for this NN to learn XOR;
- The activation function of the third neuron does not need to add any more non-linearity;
- So the Identity activation function is used: sends the input as output, nothing changes here;
- In this NN, info only feeds forward;
- This network is called a 2-layer feed-forward neural network;


#### Even more detailed

- The weights and biases are determined by the training process;
- neuron #1 the weights of the values are 1 and the bias is 0;
- neuron #2 the weights of the values are 1 and the bias is -1;
- neuron #3 the weights of the values are 1 and -2  and the bias is 0;
- Now the network is capable of executing the XOR function:
- Say our inputs are X1= 0 and X2 =0;
- So Wx1 + b = 0 & Wx3 + b = 0 -> this 0 goes into the ReLU, which also outputs 0
- Wx2 + b = -1 & Wx4 + b = -1 this -1 gets rectified by the ReLu to be 0
- Both of the inputs to neuron #3 are 0 -> so the output is 0;
- The Identity activation function just passes through the 0;
- You can try the same with all kinds of inputs;
- This has successfully reverse engineered the XOR function

#### Other activation functions

- __Softmax__: the output will be presented as a number between 0 and 1;
- This represents a probability





 

