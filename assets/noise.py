#!/usr/bin/env python

import numpy as np
from astropy.io import fits

np.random.seed(3534)
data = np.random.normal(loc=0.0, scale=1.0, size=(200, 200))

fits.writeto("noise.fits", data, overwrite=True)