import numpy as np
import matplotlib.pyplot as plt
 

def plotlink(p0, u, *args, **kwargs):
    """ Grafica una línea, dados el punto inicial (p0x,p0y) y sus compontes (ux,uy) """
    plt.plot([p0[0],p0[0]+u[0]], [p0[1],p0[1]+u[1]], *args, **kwargs)



    
def plot_coupler_curve(a,b,c,d):
    pass
    
    
if __name__=="__main__":
    plotlink([5,5],[1,1])
    plt.show()

