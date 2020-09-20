#! /usr/bin/env python
# -*- coding: utf-8 -*-

from . import dict_io as io
import numpy as np
from h5py import File
from scipy.io import loadmat, savemat
from silx.io.dictdump import dicttoh5, h5todict


# Conversion functions

def mat_to_h5(load_addr, h5_dir, **kwargs):
    """ Convert mat file to HDF5 via dictionary.
    """

    matdict = loadmat(load_addr)

    fconv = kwargs.pop('fconv', io.dict_to_h5)
    fconv(matdict, h5_dir, **kwargs)


def h5_to_mat(load_addr, mat_dir, **kwargs):
    """ Convert HDF5 to mat file via dictionary.
    """

    fconv = kwargs.pop('fconv', io.h5_to_dict)
    dct = fconv(load_addr)

    savemat(dct, mat_dir, **kwargs)
