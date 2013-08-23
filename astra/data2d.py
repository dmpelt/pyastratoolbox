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
import data2d_c as d

def clear():
    """Clear all 2D data objects."""
    return d.clear()

def delete(ids):
    """Delete a 2D object.
    
    :param ids: ID or list of ID's to delete.
    :type ids: :class:`int` or :class:`list`
    
    """
    return d.delete(ids)

def create(datatype, geometry, data=None):
    """Create a 2D object.
        
    :param datatype: Data object type, '-vol' or '-sino'.
    :type datatype: :class:`string`
    :param geometry: Volume or projection geometry.
    :type geometry: :class:`dict`
    :param data: Data to fill the constructed object with, either a scalar or array.
    :type data: :class:`float` or :class:`numpy.ndarray`
    :returns: :class:`int` -- the ID of the constructed object.
    
    """
    return d.create(datatype,geometry,data)

def store(i, data):
    """Fill existing 2D object with data.
    
    :param i: ID of object to fill.
    :type i: :class:`int`
    :param data: Data to fill the object with, either a scalar or array.
    :type data: :class:`float` or :class:`numpy.ndarray`
    
    """
    return d.store(i, data)
    
def get_geometry(i):
    """Get the geometry of a 2D object.
    
    :param i: ID of object.
    :type i: :class:`int`
    :returns: :class:`dict` -- The geometry of object with ID ``i``.
    
    """
    return d.get_geometry(i)

def change_geometry(i, geom):
    """Change the geometry of a 2D object.
    
    :param i: ID of object.
    :type i: :class:`int`
    :param geom: new geometry.
    :type geom: :class:`dict`
    
    """
    return d.change_geometry(i, geom)
    
def get(i):
    """Get a 2D object.
    
    :param i: ID of object to get.
    :type i: :class:`int`
    :returns: :class:`numpy.ndarray` -- The object data.
    
    """
    return d.get(i)

def get_shared(i):
    """Get a 2D object with memory shared between the ASTRA toolbox and numpy array.
    
    :param i: ID of object to get.
    :type i: :class:`int`
    :returns: :class:`numpy.ndarray` -- The object data.
    
    """
    return d.get_shared(i)


def get_single(i):
    """Get a 2D object in single precision.
    
    :param i: ID of object to get.
    :type i: :class:`int`
    :returns: :class:`numpy.ndarray` -- The object data.
    
    """
    return d.get_single(i)

def info():
    """Print info on 2D objects in memory."""
    return d.info()
