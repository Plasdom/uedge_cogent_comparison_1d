import matplotlib.pyplot as plt
from uedge import *
import numpy as np

def get_x_coord(xaxis: str = "pol", iy: int = 1):
    """Get x-coordinate, either in poloidal or parallel direction or in the index space.

    :param xaxis: "pol", "par" or "index", defaults to "pol"
    :param iy: y-index, defaults to 1
    :return: numpy array of x-axis coordinates
    """
    # Retrieve grid variables
    dx = com.dx
    rr = com.rr

    # Retrieve variables along the flux tube
    xpar = np.zeros(com.nx+2)
    xpol = np.zeros(com.nx+2)
    xpar[0] = dx[0, iy] / rr[0, iy]
    xpol[0] = dx[0, iy]
    xind = [0]
    for ix, posx in enumerate(range(com.nx+2)):
        xpar[ix] = xpar[ix - 1] + dx[posx, iy] / rr[posx, iy]
        xpol[ix] = xpol[ix - 1] + dx[posx, iy]
        xind.append(str(posx))
    
    if xaxis == "pol":
        x = xpol
    elif xaxis == "par":
        x = xpar
    elif xaxis == "index":
        x = xind
    
    return x

def plot1d(var, iy: int = 1, xaxis: str = "pol", ylabel: str = ""):
    """Plot 1D variable

    :param var: UEDGE variable
    :param xaxis: "pol", "par" or "index", defaults to "pol"
    :param ylabel: Label for y-axis, defaults to ""
    :return: axes
    """
    fig,ax = plt.subplots(1)
    x = get_x_coord(xaxis, iy=iy)
    ax.plot(x[1:-1],var[1:-1,iy])
    ax.grid()

    if xaxis == "pol":
        xlabel = r"$s_{\theta}$ [m]"
    elif xaxis == "par":
        xlabel = r"$s_{\parallel}$ [m]"
    elif xaxis == "index":
        xlabel = "Index"
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    return ax