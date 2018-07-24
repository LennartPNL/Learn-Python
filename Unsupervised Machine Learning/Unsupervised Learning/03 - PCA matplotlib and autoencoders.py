import numpy as np
import pandas as pd
import tensorflow as tf

from matplotlib.mlab import PCA

prices = pd.read_csv('stocks.csv')

prices['Date'] = pd.to_datetime(prices['Date'], infer_datetime_format=True)

prices = prices.sort_values(['Date'], ascending=[True])

prices = prices[['ADBE', 'MDLZ', 'SBUX']]

print(prices.head())

returns = prices[[key for key in dict(prices.dtypes) if dict(prices.dtypes)[key] in ['float64', 'int64']]].pct_change()

# There is no first data item
returns = returns[1:]

print(returns.head())

returns_arr = returns.as_matrix()[:10]

print(returns_arr.shape)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

returns_arr_scaled = scaler.fit_transform(returns_arr)

print(returns_arr_scaled)

results = PCA(returns_arr_scaled, standardize=False)

print(results.fracs)

print(results.Y)

print(results.Wt)

print(returns_arr_scaled)

n_inputs = 3
n_hidden = 2  # codings -> reduced dimensionality
n_outputs = n_inputs

learning_rate = 0.01

tf.reset_default_graph()

X = tf.placeholder(tf.float32, shape=[None, n_inputs])

hidden = tf.layers.dense(X, n_hidden)

outputs = tf.layers.dense(hidden, n_outputs)

reconstruction_loss = tf.reduce_mean(tf.square(outputs - X))

optimizer = tf.train.AdamOptimizer(learning_rate)
training_op = optimizer.minimize(reconstruction_loss)

init = tf.global_variables_initializer()

n_iterations = 10000

with tf.Session() as sess:
    init.run()

    for iteration in range(n_iterations):
        training_op.run(feed_dict={X: returns_arr_scaled})

    outputs_val = outputs.eval(feed_dict={X: returns_arr_scaled})
    print(outputs_val)

print(np.dot(results.Y[:, [0, 1]], results.Wt[[0, 1]]))
