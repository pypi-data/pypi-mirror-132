# PyGRPY

Python port of Generalized Rotne Prager Yakamawa hydrodynamic tensors.
These are a convenient approximation for modeling hydrodynamic interactions in Stokes flow.

Now also supports jax, and jax.grad.

# Usage

Finding Stokes radius of rigid conglomerate of beads.

```Python
import pygrpy
import numpy as np
centres = np.array([[0,0,0],[0,0,1]])
radii = np.array([1,1])
print(pygrpy.grpy.stokesRadius(centres,radii)) # prints 1.18...
```


# Original code

Original code in Fortran90 by Pawel Jan Zuk here:
https://github.com/pjzuk/GRPY

# License

This software is licensed under GNU GPLv3

Copyright (c) Pawel Jan Zuk (2017) - unported code.

Copyright (c) Radost Waszkiewicz (2021) - python port.

# How to cite

Zuk, P. J., B. Cichocki, and P. Szymczak *GRPY - an accurate bead method for calculation of hydrodynamic
properties of rigid biomacromolecules*; Biophys. J. (submitted) (2017)
