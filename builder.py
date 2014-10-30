#-----------------------------------------------------------------------
#Copyright 2013 Centrum Wiskunde & Informatica, Amsterdam
#
#Author: Daniel M. Pelt
#Contact: D.M.Pelt@cwi.nl
#Website: http://dmpelt.github.io/pyastratoolbox/
#
#
#This file is part of the Python interface to the
#All Scale Tomographic Reconstruction Antwerp Toolbox ("ASTRA Toolbox").
#
#The Python interface to the ASTRA Toolbox is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#The Python interface to the ASTRA Toolbox is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with the Python interface to the ASTRA Toolbox. If not, see <http://www.gnu.org/licenses/>.
#
#-----------------------------------------------------------------------
import sys
import numpy as np

from distutils.version import LooseVersion
from distutils.core import setup
from distutils.extension import Extension

use_cython=False
try:
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize
    import Cython
    if LooseVersion(Cython.__version__)>=LooseVersion('0.13'):
        use_cython = True
except ImportError:
    use_cython = False

cmdclass = { }
ext_modules = [ ]

if use_cython:
    ext_modules = cythonize("astra/*.pyx")
    cmdclass = { 'build_ext': build_ext }
else:
    ext_modules += [
        Extension("astra.algorithm_c", [ "astra/algorithm_c.cpp" ],libraries = ['astra']),
        Extension("astra.astra_c", [ "astra/astra_c.cpp" ],libraries = ['astra']),
        Extension("astra.data2d_c", [ "astra/data2d_c.cpp" ],libraries = ['astra']),
        Extension("astra.data3d_c", [ "astra/data3d_c.cpp" ],libraries = ['astra']),
        Extension("astra.matrix_c", [ "astra/matrix_c.cpp" ],libraries = ['astra']),
        Extension("astra.projector_c", [ "astra/projector_c.cpp" ],libraries = ['astra']),
        Extension("astra.utils", [ "astra/utils.cpp" ],libraries = ['astra']),
        Extension("astra.extrautils", [ "astra/extrautils.c" ],libraries = ['astra']),
    ]





setup (name = 'PyASTRAToolbox',
       version = '1.1',
       description = 'Python interface to the ASTRA-Toolbox',
       author='D.M. Pelt',
       author_email='D.M.Pelt@cwi.nl',
       url='http://dmpelt.github.io/pyastratoolbox/',
       #ext_package='astra',
       #ext_modules = cythonize(Extension("astra/*.pyx",extra_compile_args=extra_compile_args,extra_linker_args=extra_compile_args)),
       license='GPLv3',
       ext_modules = ext_modules,
       include_dirs=[np.get_include()],
       cmdclass = cmdclass,       
       #ext_modules = [Extension("astra","astra/astra.pyx")],
       packages=['astra'],
       requires=['numpy'],
	)
