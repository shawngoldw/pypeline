from pypeline import _Container

import numpy as np
from sklearn.neighbors.kde import KernelDensity


def _ix(x, fill_zeros):
    ix = x.isna()
    if fill_zeros:
        ix = ix | (x == 0)
    return ix


def gaussian(data, col, bandwidth, fill_zeros=False):
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(data[col].dropna().values.reshape(-1, 1))
    return _Container(_gaussian, {'kde': kde, 'col': col, 'fill_zeros': fill_zeros})


def _gaussian(data, kde, col, fill_zeros):
    ix = _ix(data[col], fill_zeros)
    data.loc[ix, col] = kde.sample(sum(ix))
    return data


def frequency(data, col, fill_zeros=False):
    uniques, counts = np.unique(data[col].dropna(), return_counts=True)
    p = counts / sum(counts)
    return _Container(_frequency, {'col': col, 'uniques': uniques, 'p': p, 'fill_zeros': fill_zeros})


def _frequency(data, col, uniques, p, fill_zeros=False):
    ix = _ix(data[col], fill_zeros)
    data.loc[ix, col] = np.random.choice(uniques, sum(ix), p=p)
    return data
