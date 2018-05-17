"""
cec2014.pyx

simple cython test of accessing a numpy array's data

the C function: c_multiply multiplies all the values in a 2-d array by a scalar, in place.

"""

import cython

# import both numpy and the Cython declarations for numpy
import numpy as np
cimport numpy as np

# declare the interface to the C code
cdef extern from "cec2014_func.cpp":
  double cec14_test_func_rev(double *x, int nx, int func_num)

#@cython.boundscheck(False)
#@cython.wraparound(False)
def cec14(np.ndarray[double, ndim=1, mode="c"] input not None, int func_num):
  n = input.shape[0]
  return cec14_test_func_rev(&input[0], n, func_num)
