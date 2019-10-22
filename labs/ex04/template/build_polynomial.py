# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    n = x.shape[0]
    tx_poly = np.zeros((n,degree))
    for i in range(n):
        for j in range(degree):
            tx_poly[i,j] = x[i]**j
            
    return tx_poly