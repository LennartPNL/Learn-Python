import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random

# Generate some random X and Y points for three clusters

input_2d_x_1 = np.array([[random.randint(1, 10000) for i in range(2)] for j in range(100)], dtype=np.float32)
input_2d_x_2 = np.array([[random.randint(7000, 20000) for i in range(2)] for j in range(100)], dtype=np.float32)
input_2d_x_3 = np.array([[random.randint(17000, 30000) for i in range(2)] for j in range(100)], dtype=np.float32)

input_2d_x = np.append(np.append(input_2d_x_1, input_2d_x_2, axis=0), input_2d_x_3, axis=0)


# Function that specifies features and labels

def input_fn_2d(input_2d):
    input_t = tf.convert_to_tensor(input_2d, dtype=tf.float32)

    return (input_t, None)


# Visualize the data

plt.scatter(input_2d_x[:, 0], input_2d_x[:, 1], s=100, color="blue")
plt.show()

from tensorflow.contrib.learn.python.learn.estimators import kmeans

# We have three clusters
k_means_estimator = kmeans.KMeansClustering(num_clusters=3)

fit = k_means_estimator.fit(input_fn=lambda: input_fn_2d(input_2d_x), steps=1000)

# Get the cluster center points
clusters_2d = k_means_estimator.clusters()

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(input_2d_x[:, 0], input_2d_x[:, 1], s=100, marker='o', color="blue")
ax1.scatter(clusters_2d[:, 0], clusters_2d[:, 1], c='r', s=300, marker='s')

plt.show()

print(k_means_estimator.get_params())

'''
{'params': 
{'num_clusters': 3, 'training_initial_clusters': 'random', 
'distance_metric': 'squared_euclidean', 
'random_seed': 0, 'use_mini_batch': True, 
'mini_batch_steps_per_iteration': 1, 'kmeans_plus_plus_num_retries': 2, 
'relative_tolerance': None}
}
'''

# Setting a datapoint to predict
ex_2d_x = np.array([[1700, 1700]], dtype=np.float32)

# Predicting in which cluster the point belongs
predict = k_means_estimator.predict(input_fn=lambda: input_fn_2d(ex_2d_x), as_iterable=False)

print(predict)
