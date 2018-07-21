'''
Before starting:
>py -m tensorboard.main --logdir [your_log_dir]

if you have spaces in the name of your folders use quotation marks around the path ["Your Log Dir"]
'''

import tensorflow as tf

# Defining constants

a = tf.constant(6.5, name='constant_a')

b = tf.constant(3.4, name='constant_b')
c = tf.constant(3.0, name='constant_c')

d = tf.constant(100.2, name='constant_d')

# Using the math functions in TensorFlow

add = tf.add(a, b, name="add_ab")
subtract = tf.subtract(b, c, name="subtract_bc")
square = tf.square(d, name="square_d")

final_sum = tf.add_n([add, subtract, square], name="final_sum")

with tf.Session() as sess:
    print("a + b: ", sess.run(add))

    print("b - c: ", sess.run(subtract))

    print("Square of d: ", sess.run(square))

    print("Final sum", sess.run(final_sum))

    another_sum = tf.add_n([a, b, c, d, square], name="another_sum")
    print("Another sum ", sess.run(another_sum))

# Creates a folder called SimpleMath and writes out the computational graphs

writer = tf.summary.FileWriter('./SimpleMath', sess.graph)
writer.close()


'''
After running, navigate to localhost:6006 or your_pc_name:6006
Here you will see a graphical representation of the code that we just executed!
'''