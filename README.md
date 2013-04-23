PyASTRAToolbox
==============

## Information
The [PyASTRAToolbox](http://dmpelt.github.io/pyastratoolbox/) is a Python interface to the [ASTRA Toolbox](https://code.google.com/p/astra-toolbox/),
a tomography toolbox based on high-performance GPU primitives for 2D and 3D tomography.

The Python interface aims to expose all features of the ASTRA toolbox to Python, providing a high-performance
tomography toolbox for Python users. PyASTRAToolbox is released under the open-source GPLv3 license.

The current version is 1.0, released on 2013-04-23.

[\[Download latest version\]](http://dmpelt.github.io/pyastratoolbox/releases/PyASTRAToolbox-1.0.tar.gz)

## Useful links
* [\[Documentation\]](http://dmpelt.github.io/pyastratoolbox/doc1.0/index.html)
* [\[Bug Tracker\]](https://github.com/dmpelt/pyastratoolbox/issues)

## Installation
To install PyASTRAToolbox on UNIX systems, use the included `install.sh` file:

    Usage: ./install.sh [-i astra_include_path] [-l astra_library_path] [-p python_executable_path] [-c cuda_path]

        -i astra_include_path:          specify path to astra header files (without trailing astra/) (Optional)
        -l astra_library_path:          specify parent path of astra library file (Optional)
        -p python_executable_path:      specify path to python executable (Optional)
        -c cuda_path:                   path to CUDA (Optional)
        -h:                             print this help (Optional)

On Windows systems, you should be able to run `python builder.py install`, if all needed libraries and headers are in
the correct `PATH` variables.

## Releases
* [\[1.0\]](http://dmpelt.github.io/pyastratoolbox/releases/PyASTRAToolbox-1.0.tar.gz)

## Version history
    1.0, released 2013-04-23
        * Initial version

