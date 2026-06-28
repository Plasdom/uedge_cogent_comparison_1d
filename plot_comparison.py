from uedge.uedge_lists import *
import matplotlib.pyplot as plt
import pycogent as pc
from uedge import *
from uedge.hdf5 import *
import uedge_settings
import plots

# Specify locations of both runs
UEDGE_RUN = "ue1d.h5"
COGENT_RUN = "cogent_run"

# Load UEDGE run
hdf5_restore(UEDGE_RUN)
bbb.dtreal=1e-12
bbb.exmain()

# Load COGENT run
ds = pc.read_cogent_dataset(COGENT_RUN)

# Retrieve UEDGE plot variables
x = plots.get_x_coord("pol")
x = x[1:-1]
ni = bbb.ni[1:-1,1,0]
ne = bbb.ne[1:-1,1]
ng = bbb.ng[1:-1,1]
ti = bbb.ti[1:-1,1]/bbb.ev
te = bbb.te[1:-1,1]/bbb.ev

# Retrieve COGENT plot variables
L_norm = float(ds.input["units.length"])
n_norm = float(ds.input["units.number_density"])
T_norm = float(ds.input["units.temperature"])
x2 = ds.z * L_norm 
nn2 = ds["nn"].isel(t=-1) * n_norm
ne2 = -ds["ne"].isel(t=-1) * n_norm
Ti2 = ds["Td"].isel(t=-1) * 50
Te2 = ds["Te"].isel(t=-1) * 50

# Plot
fig,ax = plt.subplots(nrows=2,figsize=(5,5),sharex=True)
ax[0].plot(x, ng, linestyle="-", color="red")
ax[0].plot(x, ne, linestyle="-", color="black")
ax[0].plot(x2, nn2, linestyle="--", color="red")
ax[0].plot(x2, ne2, linestyle="--", color="black")
ax[0].grid()
ax[0].set_ylabel("$n$ [m$^{-3}$]")
ax[0].plot([],[],label="UEDGE", linestyle="-",color="black")
ax[0].plot([],[],label="COGENT",linestyle="--",color="black")
axb = ax[0].twinx()
axb.plot([],[],label="$n_e$",color="black")
axb.plot([],[],label="$n_n$",color="red")
axb.legend(loc="center left")
axb.set_yticks([])
ax[0].legend()
ax[1].plot(x, ti, linestyle="-", color="black")
ax[1].plot(x, te, linestyle="-", color="red")
ax[1].plot(x2, Ti2, linestyle="--", color="black")
ax[1].plot(x2, Te2, linestyle="--", color="red")
ax[1].grid()
ax[1].set_xlabel("Poloidal distance [m]")
ax[1].set_ylabel("$T$ [eV]")
ax[1].plot([],[],label="$T_e$",color="red")
ax[1].plot([],[],label="$T_i$",color="black")
ax[1].legend()
fig.tight_layout()
plt.show()