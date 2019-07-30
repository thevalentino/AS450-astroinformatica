#!/usr/bin/env python

import numpy as np
from astropy.io import fits

np.random.seed(3534)
scale = 49.
data = np.random.normal(loc=0.0, scale=scale, size=(200, 200))

fits.writeto("01-noise.fits", data, overwrite=True)
