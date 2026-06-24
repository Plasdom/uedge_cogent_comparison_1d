from uedge_settings import *

import matplotlib.pyplot as plt


try:
    import uedge_mvu.utils as mu
    import uedge_mvu.plot as mp
except:
    pass
try:
    import uedge_dcp.plotting as dp
except:
    pass
try:
    from plots import *
except:
    pass

from uedge import *
from uedge.rundt import *
from uedge.uedge_lists import *
from power_balance_1d import *

hdf5_restore("ue1d.h5")

#-short run to initialize everything
# bbb.ftol=1e8; 
bbb.dtreal=1e-9
bbb.exmain()
# bbb.ftol=1e-8

# #-run to steady state
# bbb.restart=1; bbb.ftol=1e-8;
# bbb.dtreal=1e-10; bbb.isbcwdt=1; bbb.exmain()
# bbb.icntnunk=0
# bbb.dtreal=1e20; bbb.isbcwdt=0; bbb.exmain()

# ub = UeBalance()
# ub.engbal()
# ub.print_balance_power()