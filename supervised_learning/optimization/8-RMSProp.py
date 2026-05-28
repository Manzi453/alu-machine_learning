#!/usr/bin/env python3
""" Training with RMSProp
"""

import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """ creates the training operation for a neural network in tensorflow
        using the RMSProp optimization algorithm
        Args:
            loss: is the loss of the network
            alpha: is the learning rate
            beta2: is the RMSProp weight
            epsilon: is a small number to avoid division by zero
        Returns: the RMSProp optimization operation
    """

    optimizer = tf.compat.v1.train.RMSPropOptimizer(
        alpha,
        rho=beta2,
        momentum=0.0,
        epsilon=epsilon
    )
    return optimizer.minimize(loss)
