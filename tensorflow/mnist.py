#from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import sys

if __name__ == '__main__':
    print(sys.path)
    hello = tf.constant('Hello')
    #mnist = input_data.read_data_sets("./samples/MNIST_data/", one_hot=True)