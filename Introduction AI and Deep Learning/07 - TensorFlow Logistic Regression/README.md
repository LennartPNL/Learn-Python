## Logistic Regression

- Logistic Regression predicts the probability of effects based on the given causes;
- Can be used only for categorical Y-variables;

Say: you have a deadline, two approaches might be
- Starting five minutes before the deadline: impossible to pass the test (hopefully)
- Starting a year before the deadline: might be overkill

Both approaches are not optimal:
- Starting a year in advance makes sure you meet the deadline, but
there is little room to do different things;
- Starting five minutes before the deadline gives you about 0% chance
to meet the deadline, but you will have enough time for other things;

We want a __Goldilocks Solution__: 
- Not working to fast and not working to hard;
- We want to work smart:
    - Starting as late as possible, while still being sure you make the deadline


How do we get to the point of making 95% sure you meet the deadline, and make 95% sure you can do other things in your time:
- Plotting this on a graph: search for a point/ sweet spot;
- Logistic regression is a s-curve;
- It helps to strike a balance;

__Logistic regression__ helps with finding how probabilities 
are influenced by actions.

- The curve flattens out on both sides of the S;
- LR involves finding the best fitting curve;
- p(Yi) = 1 / (1+e^-(A+Bx)i)
- A is the intercept;
- B is the regression coefficient;


#### Logistic classification

- Pass a corpus into the logistic algorithm, which outputs a S-curve;
- Now you could give it feature vectors;
- It then predicts a probability based on the input data based on the S-curve;


__Linear regression__ 

- Predicts effects based on causes: because of X, Y happens.
- X can be continuous or categorical;
- Straight line;

__Logistic regression__

- Predicts the probability of an effect based on causes;
- On the Y axis, you do not place Y itself, but the probability of Y being equal to 1;
- Y must be categorical
- X can be continuous or categorical;
- S-curve;
- Can be made linear by the log transformation like;

#### Logit
 
 ```
 p(Yi) = 1 / (1+e^-(A+Bx)i)
 Odds(p) = p / (1-p)
 
 p = 1 / (1+e^-(A+Bx)i) ->
 p = e^A+Bx / (1+e^A+Bx) ->
 1-p = 1 -(e^A+Bx / (1+e^A+Bx)) - >
 1-p = (1 + e^A+Bx - e^A+Bx / (1+e^A+Bx)) ->
 1-p = (1 / (1 + e^A+Bx)) ->
Odds(p) = (p / (1-p)) = e^A+Bx ->

logit(p) = A + Bx 
 ```

#### Softmax

- Is an activation function;
- Outputs a probability -> P(Y= True);
- If there are two possible outcomes, only one neuron is enough;
- Now we have a W2 and b2 variable that are the output of the activation function;
- It takes in W1 and b1;
- Returns a vector of numbers that will sum to 1

#### Argmax

- Is an activation function;
- Takes in a tensor and dimension;
- Returns the index of the largest element in that tensor and dimension;
- Final prediction is the highest probability

