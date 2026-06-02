# UEDGE vs. COGENT comparison
This repo contains a 1D UEDGE model for comparison with COGENT. Run the case with run_uedge.py. All settings for the model are in uedge_settings.py.

This 1D model assumes no flux expansion and a reflective upstream boundary. A deuterium-only plasma is used, along with a diffusive neutral model. 0.25 MW of heating power is applied in the core region, and 99% of ions incident on the target are recycled as neutrals. 

Some important points:
- The (spatially constant) neutral gas diffusion is controlled with 
```
bbb.isgasdc = 1
bbb.difcng = NUMBER
```
- The pitch angle is controlled with 
```
grd.btfix = TOROIDAL_FIELD    #  [T]
grd.bpolfix = POLOIDAL FIELD  #  [T]
```
- The grid resolution is set with 
```
com.nxleg[0,1] = POLOIDAL_CELLS_IN_LEG
com.nxcore[0,1] = POLOIDAL_CELLS_IN_CORE
```
- Given we have <100% recycling, particle balance is achieved at steady state with a particle flux entering via the core, which is set with `bbb.curcore`. This is dependent on the particle flux to the target, which is a function of transport processes along the flux tube, so should be tuned to match with COGENT once there is confidence in agreement in the treatment of transport. 

# Install UEDGE
`pip install uedge`

# Run UEDGE
`python -i run_uedge.py`

# Plot 1D variables
```python
from plots import *
plot1d(bbb.ne, ylabel=r"$n_e$ [m$^{-3}$]")
```
