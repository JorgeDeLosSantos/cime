from sympy import *
from sympy.matrices import *
import numpy as np
import matplotlib.pyplot as plt
init_printing(use_latex=True)

r1,r2,r3,r4,r5,r6,r7,r8,r9 = symbols("r_1:10")
t1,t2,t3,t4,t5,t6,t7,t8,t9 = symbols("\\theta_1:10")

rad2deg = lambda x: (x*pi/180).evalf() # degrees to radians
deg2rad = lambda x: (x*180/pi).evalf() # radians to degrees

def newton_raphson(J,b,X0,vals={},eps=1e-6):
    """ Método de Newton-Raphson multivariable """
    k = 1
    b = b.subs(vals).evalf()
    while True:
        x = ((J.subs(X0).subs(vals)).inv()*b.subs(X0)).evalf()
        if x.norm()<eps: break
        for jj,ky in enumerate(X0):
            X0[ky] += (x[jj]).evalf()
        k += 1
    return X0,x,k

def vexp(r,theta,f="r"):
    """
    Convierte un vector de la forma [r e^{j theta}] a la correspondiente 
    [r*cos(theta),  r*sin(theta)].
    """
    if f == 'j':
        return Matrix([-r*sin(theta), r*cos(theta)])
    else:
        return Matrix([r*cos(theta), r*sin(theta)])
    
def plotlink(p0, u, *args, **kwargs):
    """ Grafica una línea, dados el punto inicial (p0x,p0y) y sus compontes (ux,uy) """
    plt.plot([p0[0],p0[0]+u[0]], [p0[1],p0[1]+u[1]], *args, **kwargs)
