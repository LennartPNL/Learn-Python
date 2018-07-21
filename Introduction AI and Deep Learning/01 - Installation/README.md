## TensorFlow Installation Instructions

First of all, you will need to install TensorFlow.

Installing TensorFlow goes as follows:

```shell
C:\> pip install tensorflow
```

Now validate if your TensorFlow is installed correctly:

```python
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

'''
If everything went good, it outputs; Hello, TensorFlow!
'''
```

When I ran this code, it showed me an error.
```
Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
```

So I decided to try out the GPU version of TensorFlow, for which you will also need:
https://developer.nvidia.com/cuda-90-download-archive (depending on your OS up to 1.6GB, and make sure you use v9.0)

Make sure you have a compatible GPU, check Nvidia's website!

```shell
C:\> pip install tensorflow-gpu
```

After doing this you have to download and install cuDNN, by following their guide:
https://developer.nvidia.com/cudnn

Note that after adding the cuDNN folder to your PATH, you should reboot your pc, otherwise you will spend 
a lot of time trying to figure out why the installation went wrong....

Now when you run the test script, you should be welcomed by about ten red warning lines in your console,
which is actually good! One of the lines should show your GPU:

```
Found device 0 with properties: 
name: GeForce GTX 660 Ti major: 3 minor: 0 memoryClockRate(GHz): 1.0975
```

You can test if the script works on your GPU by opening task control -> Performance -> GPU [number]
and then run the test script. My GPU Usage jumps to 10% when I execute the script.. 

Now you are pretty much good to go!

Installing the GPU version is not mandatory, but if you have a compatible GPU 
it is strongly advised you use this version. Compared to your CPU, it should be much faster.  

You can read all about TensorFlow here: 

https://www.tensorflow.org/



