import numpy as np
import tensorflow as tf
import sys
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets("mnist_data/")

tf.reset_default_graph()


def display_digit(digit):
    plt.imshow(digit.reshape(28, 28), cmap="Greys", interpolation='nearest')


def show_reconstructed_digits(X, outputs, model_path=None):
    with tf.Session() as sess:
        if model_path:
            saver.restore(sess, model_path)

        X_test = mnist.test.images[100: 102]
        outputs_val = outputs.eval(feed_dict={X: X_test})

    fig = plt.figure(figsize=(8, 6))

    for i in range(2):
        plt.subplot(2, 2, i * 2 + 1)
        display_digit(X_test[i])

        plt.subplot(2, 2, i * 2 + 2)
        display_digit(outputs_val[i])
    plt.show()


n_inputs = 28 * 28
n_hidden1 = 300
n_hidden2 = 150  # codings
n_hidden3 = n_hidden1
n_outputs = n_inputs

X = tf.placeholder(tf.float32, shape=[None, n_inputs])

dropout_rate = 0.0

training = tf.placeholder_with_default(False, shape=(), name='training')

X_drop = tf.layers.dropout(X, dropout_rate, training=training)

from functools import partial

dense_layer = partial(tf.layers.dense,
                      activation=tf.nn.relu)

hidden1 = dense_layer(X_drop, n_hidden1)
hidden2 = dense_layer(hidden1, n_hidden2)
hidden3 = dense_layer(hidden2, n_hidden3)

outputs = dense_layer(hidden3, n_outputs, activation=None)

reconstruction_loss = tf.reduce_mean(tf.square(outputs - X))

optimizer = tf.train.AdamOptimizer(0.01)
training_op = optimizer.minimize(reconstruction_loss)

init = tf.global_variables_initializer()
saver = tf.train.Saver()

n_epochs = 12
batch_size = 100

with tf.Session() as sess:
    init.run()

    for epoch in range(n_epochs):
        n_batches = mnist.train.num_examples // batch_size

        for iteration in range(n_batches):
            X_batch, _ = mnist.train.next_batch(batch_size)

            sess.run(training_op, feed_dict={X: X_batch, training: True})

        loss_train = reconstruction_loss.eval(feed_dict={X: X_batch})

        print("\r{}".format(epoch), "Train MSE:", loss_train)

        saver.save(sess, "./dropout_autoencoder.ckpt")

show_reconstructed_digits(X, outputs, "./dropout_autoencoder.ckpt")
