from pypeline import _Container

import numpy as np
from sklearn.preprocessing import OrdinalEncoder


def ordinate(data, col):
    if data[col].dtype == bool:
        return _Container(_ordinate, {'col': col})
    else:
        enc = OrdinalEncoder().fit(data[col].values.reshape(-1, 1))
        return _Container(_ordinate, {'col': col, 'enc': enc})


def _ordinate(data, col, enc=None):
    if enc is None:
        data[col] = data[col].astype(np.int32)
    else:
        data[col] = enc.transform(data[col].values.reshape(-1, 1))[:, 0]
    return data