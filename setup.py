#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("cec2014",
                             sources=["cec2014.pyx", "cec2014_func.cpp"],
                             include_dirs=[numpy.get_include()])],
)
