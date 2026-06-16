from uedge import *
from uedge.hdf5 import *

aph.aphdir = "/Users/power8/Documents/01_code/01_uedge/uedge/aph"

bbb.mhdgeo=-1     #-set cartesian geometry
bbb.isfixlb=2     #left boundary as sym. plane; no flux at cut


# Set the geometry
grd.radx = 0.01   #-outer "radial" wall
grd.radm = -1e-6  #-minimum "radial" position
grd.rad0 = 0.0
grd.alfyt=-2.0    #-radial nonuniformity factor; < 0 => expanding
grd.za0 = 0.      #-poloidal symmetry plane location
grd.zaxpt=1.5     #-poloidal location of x-point
grd.zax=2.0       #-poloidal location of divertor plate   
grd.alfxt= 1.0    #poliodal nonuniformity factor

grd.btfix = 3*0.994521895368273   #  Tesla
grd.bpolfix = 3*0.104528463267653 #  Tesla
# grd.btfix = 3.0   #  Tesla
# grd.bpolfix = 0.1 #  Tesla

bbb.ngrid=1
com.nxleg[0,0]=0
com.nxleg[0,1]=40
com.nxcore[0,0]=0
com.nxcore[0,1]=20
com.nycore[0]=0
com.nysol[0]=1


bbb.isphion=1


#-Boundary conditions

#-upstream BC
# bbb.isfixlb=1     #left end fixed
# bbb.nib[0]=5.0e18 #plasma
# bbb.nib[1]=1e12   #gas   
# bbb.upb[0]=0.0    #plasma
# bbb.upb[1]=0.0    #gas
# bbb.teb=15.       #ev
# bbb.tib=15.       #ev
bbb.isfixlb=2


#-core boundary
bbb.isnicore[0]=0
bbb.curcore=0.0#13.8 #8.0
# bbb.ncore[0]=0.5e19   
bbb.iflcore=1
bbb.isupcore=0      #if 1 then slip, if 0 vel =0 on core bndry
bbb.pcoree = 0.125e6 #0.125e6
bbb.pcorei = 0.125e6 #0.125e6

#-outer wall boundary
bbb.istewc=0        #wall has zero temp. deriv.  
bbb.istiwc=0
bbb.isnwcono=0
bbb.isupwo=0   #slip

#-private region boundary
bbb.istepfc=0        #priv. flux has zero temp. deriv. 
bbb.istipfc=0
bbb.isnwconi=0
bbb.isupwi=0   #slip        

bbb.recycp = 1.00            # plate recycling coeff.
bbb.recycm = 0.0 
bbb.bcee = 5.               #energy transmission coeffs. for electrons
bbb.bcei = 3.5              #energy transmission coeffs. for ions
bbb.isupss = 1              #parallel vel sonic


#-Transport coefficients
bbb.difni[0] = 0.1          # anomalous hydrogenic particle diff. coeff.
bbb.kye = 0.1               # anomalous elec. & ion energy diff. coeff.
bbb.kyi = 0.1               # anomalous elec. & ion energy diff. coeff.
bbb.travis[0]=0.1           # anomalous viscosity coeff.
bbb.isgasdc = 1
# bbb.difcng = 1.38e5
bbb.difcng = 0.1*138411.1/9.514364454222624

#-Flux limiters
bbb.flalfe=1e20
bbb.flalfi=1e20
bbb.flalfgx=1e20
bbb.flalfgy=1e20
bbb.flalfgxy=1e20
bbb.flalfv=1e20


# Finite difference algorithms
bbb.methe=33;bbb.methu=33;bbb.methg=33
bbb.methn=33;bbb.methi=33


#-Solver package
bbb.svrpkg = "nksol"    #Newton solver using Krylov method
bbb.mfnksol=-3
bbb.iscolnorm = 3
bbb.epscon1=0.005
bbb.ftol=1e-8
bbb.premeth = "ilut"    #Solution method for precond. Jacobian matrix
bbb.runtim=1e-07
bbb.rlx=0.4



#-Neutral gas propeties
bbb.cngfx=0.
bbb.cngfy=0.       #turn-on grad(T_g) flux if =1
bbb.cngflox=0.
bbb.cngfloy=0.   #turn-on drift with ions if =1
bbb.cngmom = 0.             #ion-gas momentum transfer
bbb.eion = 5.0               #birth energy of ions
bbb.ediss = 0.             #dissoc. energy lost from elecs (eion=2*ediss)
bbb.isrecmon = 0            #=1 turns on recombination
bbb.sxgsol = 1.             #poloidal stretching factor for gas in SOL
bbb.sxgpr = 1.              #poloidal stretching factor for gas in priv. fl
# bbb.ngbackg = 1.e11         # applies for all species
bbb.ngbackg = 1e9

#-Parallel neutral momentum equation
bbb.isupgon[0]=0

if (bbb.isupgon[0] == 1):
    bbb.isngon=0               
    com.ngsp=1                
    com.nhsp=2                
    bbb.ziin[0]=1
    bbb.ziin[1]=0

    #-the following are probably default, set them anyway to be sure
    bbb.cngmom=0
    bbb.cmwall=0
    bbb.cngtgx=0
    bbb.cngtgy=0
    bbb.kxn=0
    bbb.kyn=0


#-Currents and potential parameters
bbb.isphion=1
bbb.rsigpl=1.e-8            #anomalous cross-field conductivity
bbb.cfjhf=0.                #turn-on heat flow from current (fqp)
bbb.jhswitch=0              #Joule Heating switch


# Atomic physics packages
com.istabon=10             #DEGAS rates
# com.istabon=0               #-analytic rates

bbb.minu = 2.0                    #hydrogen
# bbb.fnuizx=0                    #no nuiz contribution for gas diff.
bbb.flalfgx=1e20                #no flux-limiter for gas diffusion
bbb.flalfgy=1e20  
# aph.issgvcxc=2
# aph.sgvcxc=5e-19    #constant CX crossection (gas diffusion)
# bbb.sigcx=5e-19     #using same value for neutral viscosity
# bbb.rnn2cx=0        #eliminate n-n effects in neutral viscosity
bbb.istgcon=1
bbb.tgas=5.0


bbb.cnucx = 0.0 # Turn off CX???
bbb.cfneutsor_ei=0.0 # coeff. for fluid neutral energy source in resei
bbb.cfticx = 0.0 # Turn off CX in Ti eqn???

# Particular values for test
# bbb.minu[0] = 1.    # ion mass relative to mp (hydrogen)
bbb.minu[0] = 2.0    # ion mass relative to mp (hydrogen)
# bbb.lnlam = 10.     # Coulomb logarithm
# bbb.cthe = 0.       # thermal force coeff. for || mom. eq. (0.71 default)


#-Misc
bbb.restart=0

#new setting initial/background fields:
bbb.allocate()
bbb.tes=10.*bbb.ev
bbb.tis=10.*bbb.ev
bbb.nis=1.e19
bbb.ups=1e4
bbb.ngs=1e18
bbb.restart = 1

bbb.oldseec=0
