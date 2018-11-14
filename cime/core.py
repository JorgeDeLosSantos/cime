from sympy import *
from sympy.matrices import *
import numpy as np
import matplotlib.pyplot as plt
# ~ init_printing(use_latex=True)


def deg2rad(angle):
    """
    Converts degrees to radians
    
    Parameters
    ----------
    angle : float, int
        Angle in degrees
    
    
    Returns
    -------
    ar : float
        Angle in radians
    
    
    Examples
    --------
    >>> deg2rad(30)
    0.523598775598299
    >>> deg2rad(90)
    1.57079632679490
    >>> deg2rad(180)
    3.14159265358979
    """
    ar = ( (angle)*(pi/180) ).evalf()
    return ar
    
def rad2deg(angle):
    """
    Converts radians to degrees
    
    Parameters
    ----------
    angle : float, int
        Angle in radians
    
    
    Returns
    -------
    ad : float
        Angle in radians
        
    
    Examples
    --------
    >>> rad2deg(pi)
    180.000000000000
    >>> rad2deg(pi/2)
    90.0000000000000
    >>> rad2deg(2*pi)
    360.000000000000
    
    """
    ad = ( (angle)*(180/pi) ).evalf()
    return ad


def vexp(r, theta, j=False):
    """
    
    Parameters
    ----------
    r : int, float, symbol
        Vector magnitude
    theta : int, float, symbol
        Vector orientation
    j : bool
        ¿Is multiplied by "j"?
    
    Returns
    -------
    R : :class:`sympy.matrices.dense.MutableDenseMatrix`
        Vector in rectangular coordinates
    
    """
    if j:
        R = Matrix([-r*sin(theta), r*cos(theta)])
    else:
        R = Matrix([r*cos(theta), r*sin(theta)])
    return R


def grubler(L,J1,J2):
    """
    Calculates the DOF of a linkage using Grübler-Kutzbach criterion
    
    Parameters
    ----------
    L : int
        Number of links
    J1 : int
        1-DOF pairs
    J2 : int
        2-DOF pairs
        
    Returns
    -------
    M : int
        Degrees of freedom
    """
    M = 3*(L-1) - 2*J1 - J2
    return M
    

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
    
    
def isgrashof(l1,l2,l3,l4):
    """
    Determine if a four-bar linkage is Grashof class.
    """
    

if __name__=="__main__":
    print( generate_grashof_fourbar(100, 1.6) )
        
    
