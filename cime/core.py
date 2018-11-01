from sympy import *
from sympy.matrices import *
import numpy as np
import matplotlib.pyplot as plt
init_printing(use_latex=True)


def deg2rad(angle):
    return ( (angle)*(pi/180) ).evalf()
    
def rad2deg(angle):
    return ( (angle)*(180/pi) ).evalf()


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


def vexp(r, theta, f="r"):
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
    

def grubler(L,J1,J2):
    """ Calcula los GDL de un mecanismo plano utilizando el criterio de Grübler-Kutzbach """
    return 3*(L-1) - 2*J1 - J2
    

def generate_grashof_fourbar(shortest=1, slfactor=2):
    """ S + L <= P + Q """
    done = False
    S = shortest
    L = S*slfactor
    while not(done):
        P = L*np.random.rand()
        Q = L*np.random.rand()
        if ( (S + L) < (P + Q) ) and (P>S) and (Q>S):
            done = True
    return S,L,P,Q
    

if __name__=="__main__":
    print( generate_grashof_fourbar(100, 1.6) )
        
    
