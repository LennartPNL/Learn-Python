# Clustering is not actually good for image recognition,
# but this is a good way of showing how clustering works

import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# Just turning off the annoying messages in the console
tf.logging.set_verbosity(tf.logging.ERROR)
import matplotlib
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets("mnist_data/")

training_digits, training_labels = mnist.train.next_batch(2000)

test_digits, test_labels = mnist.test.next_batch(5)



def display_digit(digit):
    plt.imshow(digit.reshape(28, 28), cmap="Greys", interpolation='nearest')


display_digit(training_digits[0])

plt.show()

from tensorflow.contrib.learn.python.learn.estimators import kmeans


def input_fn(digits):
    input_t = tf.convert_to_tensor(digits, dtype=tf.float32)

    return (input_t, None)


k_means_estimator = kmeans.KMeansClustering(num_clusters=10)

# 100 steps results in 0% for me. I don't dare to try more steps because my computer might explode then...

fit = k_means_estimator.fit(input_fn=lambda: input_fn(training_digits), steps=100)

clusters = k_means_estimator.clusters()

for i in range(10):
    plt.subplot(2, 5, i + 1)
    display_digit(clusters[i])

cluster_labels = [9, 1, 6, 8, 0, 3, 0, 6, 1, 9]

for i in range(5):
    plt.subplot(1, 5, i + 1)
    display_digit(test_digits[i])

predict = k_means_estimator.predict(input_fn=lambda: input_fn(test_digits), as_iterable=False)


print([cluster_labels[i] for i in predict['cluster_idx']])

for i in range(5):
    plt.subplot(1, 5, i + 1)
    display_digit(test_digits[i])


predict_train = k_means_estimator.predict(input_fn=lambda: input_fn(test_digits), as_iterable=False)


def display_accuracy(cluster_labels, cluster_idx, actual_labels):
    predict_labels = [cluster_labels[i] for i in cluster_idx]

    num_accurate_predictions = (list(predict_labels == actual_labels)).count(True)

    print("Number of accurate predictions: ", num_accurate_predictions)

    pctAccuracy = float(num_accurate_predictions) / float(len(actual_labels))

    print("% accurate predictions: ", pctAccuracy)


display_accuracy(cluster_labels, predict_train['cluster_idx'], test_labels)

plt.show()