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
# distutils: language = c++
# distutils: libraries = astra

from libcpp.string cimport string
from libcpp cimport bool
cdef extern from "astra/Globals.h" namespace "astra":
    int getVersion()
    string getVersionString()
    bool cudaEnabled()

cdef extern from "../cuda/2d/darthelper.h" namespace "astraCUDA":
    bool setGPUIndex(int)

def credits():
    print "All Scale Tomographic Reconstruction Antwerp Toolbox (ASTRA-Toolbox) was developed at the University of Antwerp by"
    print " * Prof. dr. Joost Batenburg"
    print " * Andrei Dabravolski"
    print " * Gert Merckx"
    print " * Willem Jan Palenstijn"
    print " * Tom Roelandts"
    print " * Prof. dr. Jan Sijbers"
    print " * dr. Wim van Aarle"
    print " * Sander van der Maar"
    print " * dr. Gert Van Gompel"
    print ""
    print "Python interface written by"
    print " * Daniel M. Pelt (CWI, Amsterdam)"


def use_cuda():
    return cudaEnabled()


def version(printToScreen=False):
    if printToScreen:
        print getVersionString()
    else:
        return getVersion()

def set_gpu_index(idx):
    if use_cuda()==True:
        ret = setGPUIndex(idx)
        if not ret:
            print "Failed to set GPU " + str(idx)
