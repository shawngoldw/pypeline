from pypeline import _Container

import numpy as np


def normal(data, col):
    m = np.mean(data[col])
    std = np.std(data[col])
    return _Container(_normal, {'col': col, 'm': m, 'std': std})


def _normal(data, col, m, std):
    data[col] = (data[col] - m)/std
    return data
