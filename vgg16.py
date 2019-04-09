import numpy as np
import tensorflow as tf

def get_weight_variable(shape):
    return tf.get_variable('weight',shape= shape,
                           initialization=tf.truncated_normal_initializer(stddev=0.1))



def get_bias_variable(shape):
    return tf.get_variable('bias',shape=shape,
                           initializer=tf.constant_initializer(0))


def conv2d (x,w,padding='SAME',s=1):
    x= tf.nn.conv2d (x,w,strides=[1,s,s,1],padding=padding)

    return x

def maxPoolLayer (x):
    return tf.nn.max_pool (x,ksize=[1,2,2,1],
                           strides=[1,2,2,1],padding='SAME')


def conv2d_layer (x,in_chs,out_chs,ksize,layer_name):
    with tf.variable_scope (layer_name):
        w= get_weight_variable ([ksize,ksize,in_chs,out_chs])
        b= get_bias_variable ([out_chs])
        y= tf.nn.relu (tf.bias_add (conv2d (x,w,padding='SAME',s=1),b))
    return y


def fc_layer (x,in_kernels,out_kernels,layer_name):
    with tf.variable_scope (layer_name):
        w = get_weight_variable ([in_kernels,out_kernels])
        b = get_bias_variable ([out_kernels])
        y = tf.nn.relu (tf.bias_add (tf.matmul (x,w),b))

    return y

def VGG16 (x):
    conv1_1 = conv2d_layer (x,tf.get_shape (x).as_list () [-1],64,3,'conv1_1')
    conv1_2= conv2d_layer (conv1_1,64,64,3,'conv1_2')
    pool_1 = maxPoolLayer (conv1_2)

    conv2_1 = conv2d_layer (pool_1,64,128,3,'conv2_1')
    conv2_2 = conv2d_layer (conv2_1,128,128,3,'conv2_2')
    pool_2 = maxPoolLayer (conv2_2)

    
    conv3_1 = conv2d_layer (pool_2,128,256,3,'conv3_1')
    conv3_2 = conv2d_layer (conv3_1,256,256,3,'conv3_2')
    conv3_3 = conv2d_layer (conv3_3,256,256,3,'conv3_3')
    pool_3 = maxPoolLayer (conv3_3)

    conv4_1 =conv2d_layer (pool_3,256,512,3,'conv4_1')
    conv4_2 = conv2d_layer (conv4_1,512,512,3,'conv4_2')
    conv4_3 = conv2d_layer (conv4_2,512,512,3,'conv4_3')
    pool_4 = maxPoolLayer (conv4_3)

    conv5_1 = conv2d_layer (pool_4,512,512,3,'conv5_1')
    conv5_2 = conv2d_layer (conv5_1,512,512,3,'conv5_2')
    conv5_3 = conv2d_layer (conv5_2,512,512,3,'conv5_3')
    pool_5 = maxPoolLayer (conv5_3)

    pool5_flatten_dims =
    int (np.prood (pool_5.get_shape ().as_list () [1:]))
    pool5_flatten = tf.reshape (pool_5,
    [-1,pool5_flatten_dims])

    fc_6 = fc_layer (pool5_flatten,pool5_flatten_dims,4096,
                     'fc6')
    fc_7 = fc_layer (fc_6,4096,4096,'fc7')
    fc_8 = fc_layer (fc_7,4096,10,'fc8')

    return fc_8
