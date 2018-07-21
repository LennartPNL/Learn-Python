#### Implementing Regression in TensorFlow

- Regular Python code;
- Define the computation graph;
- We only need one neuron with an affine computation;
- Specify the cost function (Mean Square Error);
- Specify an optimizer (Gradient descent Optimizer);
- Train the model (Invoking the optimizer in epochs, done by TensorFlow);
- After the training process, the value of the variables W and b are frozen
 this gives us a converged and fully trained model that is ready to use on new test data; 

#### Regression in Python without TensorFlow

- You would use the pandas module for dataframes;
- You would use NumPy for arrays;
- You would use Statsmodels for statistical techniques like regression;
- You would use Matplotlib for plotting your graphs
 
 __Negative indices in Python__:
 - Are backward indices;
 - They count from the end of a container;
 - Just like positive (forward) indices,
 they travel from a point to a point;
 - For every negative (backward) index there is a positive one;
 - The reversed negative index accesses the same data;
 
__Machine Learning based regression__:

- A corpus is fed to the algorithm;
- All x variables are features;
- The y values are the labels;
- The distinction between the features and labels is a characteristic of the machine learning approach to regression;


__Reshape__ in NumPy: 

- Will give you a list of lists when invoked on a single list;
- [1,2,3,4,5] -> reshape(-1,1) -> [[1],[2],[3],[4],[5]];
- This takes one list and gives us a list of lists;

__Simple regression__:

- Involves just one X variable and one Y variable;
- One cause and one effect;

__Multiple regression__:

- Multiple causes for one effect;
- Hard to visualize;
- Reasonably visualized when you use two causes for one effect: 
that will result in a three dimensional graph;
- More is almost impossible with more than 2 explanatory factors;

#### Gradient Descent

- Used to optimize the best fitting regression line;
- We have three axis: W, b and MSE (error term);
- You would only want to find the smallest value of the MSE;
- This will result in the best W and b for our neuron;
- This is also the training process;
- Starting is usually just a estimate or guess;
- Then you use the optimization algorithm;
- Each step towards the lowest MSE is called an __Epoch__;
- The rate at which we move towards the global minimum is called the __Learning Rate__;
 
 __Choosing the amount of training data__ we use in each step of the optimizer (epoch):
 
 - This is an iterative process;
 - You need to choose the total number of epochs;
 - In each iteration you can choose how much training data is used by the optimizer;
 - That is called the __batch size__;
 
 __Stochastic Gradient Descent__:
 
 - Only takes one point of the training data at a time
 
 __Mini-batch Gradient Descent__:
 
 - Most common;
 - Some subset of the trainingdata is passed in each epoch;
 
 
  __Batch Gradient Descent__:
 
 - Is an extreme;
 - All of the training data is fed in at each epoch;
 - This is not a problem, as all data you pass to the algorithm helps
 
 
 
 
 



