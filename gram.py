import tensorflow as tf


def gram_matrix(input_tensor):
    """
    Computes the gram matrix of the input tensor, assuming it has exactly one layer.

    :param input_tensor: input tensor
    :return: gram matrix of the input tensor
    """

    temp = tf.squeeze(input_tensor)
    return tf.matmul(temp, tf.transpose(temp))