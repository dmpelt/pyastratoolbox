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
"""Additional functions for PyAstraToolbox.

.. moduleauthor:: Daniel M. Pelt <D.M.Pelt@cwi.nl>


"""

import creators as ac
import numpy as np
import scipy.weave

import data2d
import data3d
import projector
import algorithm



def clear():
    """Clears all used memory of the ASTRA Toolbox.
    
    .. note::
        This is irreversible.
        
    """
    data2d.clear()
    data3d.clear()
    projector.clear()
    algorithm.clear()


def data_op(op, data, scalar, gpu_core, mask=None):
    """Perform data operation on data.

    :param op: Operation to perform.
    :param data: Data to perform operation on.
    :param scalar: Scalar argument to data operation.
    :param gpu_core: GPU core to perform operation on.
    :param mask: Optional mask.
    
    """

    cfg = ac.astra_dict('DataOperation_CUDA')
    cfg['Operation'] = op
    cfg['Scalar'] = scalar
    cfg['DataId'] = data
    if not mask == None:
        cfg['MaskId'] = mask
    cfg['option']['GPUindex'] = gpu_core
    alg_id = at.algorithm('create', cfg)
    at.algorithm('run', alg_id)
    at.algorithm('delete', alg_id)


def add_noise_to_sino(sinogram_in, I0):
    """Adds Poisson noise to a sinogram.

    :param sinogram_in: Sinogram to add noise to.
    :type sinogram_in: :class:`numpy.ndarray`
    :param I0: Background intensity. Lower values lead to higher noise.
    :type I0: :class:`float`
    :returns:  :class:`numpy.ndarray` -- the sinogram with added noise.

    """
    if isinstance(sinogram_in, np.ndarray):
        sinogramRaw = sinogram_in
    else:
        sinogramRaw = at.data2d('get', sinogram_in)
    max_sinogramRaw = sinogramRaw.max()
    sinogramRawScaled = sinogramRaw / max_sinogramRaw
    # to detector count
    sinogramCT = I0 * np.exp(-sinogramRawScaled)
    # add poison noise
    sinogramCT_C = np.zeros_like(sinogramCT)
    for i in xrange(sinogramCT_C.shape[0]):
        for j in xrange(sinogramCT_C.shape[1]):
            sinogramCT_C[i, j] = np.random.poisson(sinogramCT[i, j])
    # to density
    sinogramCT_D = sinogramCT_C / I0
    sinogram_out = -max_sinogramRaw * np.log(sinogramCT_D)

    if not isinstance(sinogram_in, np.ndarray):
        at.data2d('store', sinogram_in, sinogram_out)
    return sinogram_out

def geom_size(geom, dim=None):
	if 'GridSliceCount' in geom:
		# 3D Volume geometry?
		s = (geom['GridRowCount'], geom['GridColCount'], geom['GridSliceCount'])
	elif 'GridColCount' in geom:
		# 2D Volume geometry?
		s = (geom['GridRowCount'], geom['GridColCount'])
	elif geom['type'] == 'parallel' or geom['type'] == 'fanflat':
		s = (len(geom['ProjectionAngles']), geom['DetectorCount'])
	elif geom['type'] == 'parallel3d' or geom['type'] == 'cone':
		s = (len(geom['ProjectionAngles']), geom['DetectorColCount'], geom['DetectorRowCount'])
	elif geom['type'] == 'fanflat_vec':
		s = (geom['Vectors'].shape[0], geom['DetectorCount'])
	elif geom['type'] == 'parallel3d_vec' or geom['type'] == 'cone_vec':
		s = (geom['Vectors'].shape[0], geom['DetectorColCount'], geom['DetectorRowCount'])
	
	if dim != None:
		s = s[dim]
	
	return s
