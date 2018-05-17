"""
cec2014.pyx

Define cec14 que llama a la función objetivo en C++
"""

import cython
import numpy as np
cimport numpy as np

cdef extern from "cec2014_func.cpp":
  double cec14_test_func_rev(double *x, int nx, int func_num)

@cython.boundscheck(False)
@cython.wraparound(False)
def cec14(np.ndarray[double, ndim=1, mode="c"] input not None, int func_num):
  return cec14_test_func_rev(&input[0], input.shape[0], func_num)
