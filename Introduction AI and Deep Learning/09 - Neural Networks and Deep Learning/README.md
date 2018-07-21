# Short summary

## Deep Learning

- Does not rely on experts to decide which features are important;
- Because there are enormous datasets, it is impossible for humans to determine which features are important;
- The feature selection is done by an algorithm;
- This is representation;
- These models are much smarter than traditional ML-systems;
- Neural Networks are the most common type of deep learning algorithm;
- Every layer of a NN has it's own objective;
- The output of a layer is the input for the next image;
- All layers together form the feature selection algorithm;
- A NN with many layers is a deep NN;

## A Single Neuron

- The output of one neuron is connected to the input of a neuron in a following layer;
- A neuron is a mathematical function that performs a calculation on any amount of inputs (X);
- It outputs a single value (Y), which can be sent to multiple neurons in a following layer;
- Then the neuron is called active: if the neuron outputs the same as it's input, it is called dead or inactive;
- The connection of a neuron to another neuron has a weight W;
- Cells that fire together, wire together;
 
__The operations inside one neuron__:

- There is an affine transformation: the inputs are fed into this transformation, which then passes it's output to an activation function;
- Both of these functions make the neuron;
- The ___Affine__ transformation can only learn linear relationships between the inputs and outputs;
- The combination of __Affine and Activation__ functions allow the neuron to learn any kind of relationship;
- The inputs of the affine transformation all have a weight;
- The affine transformation also takes an input b (bias), which allows you to shift the linear relationship;
- The output of the affine transformation is a relationship which can be represented as Wx + b;
- W and b come from the training process: these values need to be optimal to make the right predictions;
- Wx + b is fed into the activation function.

## The activation function

#### Linear regression

- The activation function is an Identity function, which does nothing but pass the given input to the next neuron;
- So Wx + b -> Identity function -> Wx + b (activation=None);
- The output of the Identity function is also the output of the neuron itself;
- These are linear neurons

#### Logistic regression

- The activation function can be the Softmax function;
- It outputs two probabilities: the probability oy Y being true and false;
- So: Wx + b -> Softmax -> p(Y=True) and p(Y=false)
- Logistic regression results in a S-shaped curve;
- Softmax can be used on N-category classification;
    - Outputs a number between 0 and 1;
    - The output is a probability;

__Other activation functions__:

- ReLU: Rectified Linear Unit;
    - The maximum value of the output of the affine transformation -> max(Wx+b, 0);
- Logit: is for S-curve activation;
- Tanh: a hyperbolic tan (S-curve from -1 to 1);
    - S-shaped, continuous and differentiable;
    - Normalizes each layer's output;
    - Centered around 0;
- Step: clamps the output to either -1 or 1

The choice of activation is crucial in determining the performance of the NN.

## Training and Back Propagation

- The training of a NN happens for example through gradient descent optimization;

__Minimizing the mean square error__:

- When plotted results in a curve: on three axis;
- You want to find the values of W and b that result in the smallest possible MSE;
- Finding the smallest MSE value starts off with the initial value of MSE: this is arbitrary;
- We descend down the slope of the MSE to find the smallest possible value;
- There are other optimizers available, some are built in to TensorFlow.


__Training via back propagation__:

- A corpus is fed to the NN;
- You compare the predicted label to the actual label;
- You will feed back this data to train your W and b;
- The output of your last layer is used to train this layer again;
- Then you pass the values to the previous layer in the sequences all the way to your input layer;
- Allows the W and b of all connections to converge to a final value.

## Hyperparameters 

- Are the design decisions for your NN;
- E.g:
    - Network topology (neuron connections);
    - Number of layers;
    - Number of neurons in every layer;
    - Activation function

__Model parameters__ vs. __Hyper parameters__:

__Model parameters__:

- The W and b determined __during the training__.
- The __result__ of training.
- Used to __make predictions__.
- Using validation datasets you find the best model.

__Hyper parameters__:

- The __design of the model__.
- The __input__ of the training process.
- Used to __generate the best model__.
- Hyperparameter tuning generates the best model.

## Vanishing and exploding gradients

- Back propagation fails when gradients do not change or change too fast;
- When the gradients do not change at all during training, you have encountered the vanishing gradient problem;
- In this way the other layers can not change as well;
- The algorithm never creates a good solution;
- Exploding gradient problem: your gradient moves up and down in an explosive fashion;
- The weight of your layers will not converge;
- The weights of the layers become too large and thus meaningless;
- These problems have been mostly solved:
    - Proper initialization of W and b
    - Gradient clipping
    - Batch normalization (scaling, center around 0)
    - Using correct activation functions


## Prevent over-fitting

- Regularisation;
    - Penalise complex models;
    - Simple gradient descent;
    - Add a penalty to the cost or loss function;
    - Increases the cost if the model gets more complex;
- Cross validation;
    - Split the dataset into training sets and validation sets;
    - Distinct training and validation phases;
    - You train different models with only training data;
    - You select the model that does the best on validation data;
    - Hyperparameter tuning;
- Ensemble learning;
    -  
- Dropout;
    - Intentionally turn off some neurons;
    - Specify a fraction of neurons that will stay off;
    - A different set of neurons are turned off at every step;
    - Your network configuration is turned on and of every step;
    

