from sympy import *
from sympy.matrices import *
import numpy as np
import matplotlib.pyplot as plt
# ~ init_printing(use_latex=True)


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
    links = [l1,l2,l3,l4]
    S = min(links) # Shortest link
    L = max(links) # Largest link
    idxL = links.index(L)
    idxS = links.index(S)
    P, Q = [links[idx] for idx in range(len(links)) if not(idx in (idxL,idxS))] #other links
    if (S + L) <= (P + Q): # Checks Grashof condition
        return True
    else:
        return False
        
        
class Link(object):
    pass
    
    
class ClosedChain(object):
    pass


class Vector3D(object):
    def __init__(self,x,y,z):
        self.components = x,y,z
        self.x = x 
        self.y = y
        self.z = z
        
    def get_orientation(self):
        """ Dir Cosines """
        thx = acos( self.x / self.get_norm() )
        thy = acos( self.y / self.get_norm() )
        thz = acos( self.z / self.get_norm() )
        return thx,thy,thz
        
    def get_norm(self):
        n = sqrt( self.x**2 + self.y**2 + self.z**2 )
        return n
        
    def __str__(self):
        s = "[{x}\n{y}\n{z}]".format(x=self.x, y=self.y ,z=self.z)
        return s
    



class Vector2D(object):
    def __init__(self,x,y):
        self.components = x,y
        self.x = x 
        self.y = y
        
    @property
    def theta(self):
        return self.get_orientation()
    
    @property
    def r(self):
        return self.get_norm()
        
    def get_orientation(self):
        """ Dir Cosines """
        th = atan2(self.y, self.x)
        return th
        
    def get_norm(self):
        n = sqrt( self.x**2 + self.y**2)
        return n
        
    def dot(self, other):
        ux, uy = self.x, self.y
        vx, vy = other.x, other.y
        dp = ux*vx + uy*vy
        return dp
        
    def cross(self, other):
        ux, uy = self.x, self.y
        vx, vy = other.x, other.y
        wz = ux*vy - uy*vx
        return Vector3D(0,0,wz)
                
    def __add__(self, other):
        ux, uy = self.x, self.y
        vx, vy = other.x, other.y
        return Vector2D(ux + vx, uy + vy)
    
    def __str__(self):
        s = "[{x}, {y}]".format(x=self.x, y=self.y)
        return s
        

class PositionVector2D(object):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        print(vars(self))
        if "x" in vars(self) and "y" in vars(self):
            self.r = sqrt(self.x**2 + self.y**2)
            self.theta = atan2(self.y, self.x)
        elif "r" in vars(self) and "theta" in vars(self):
            self.x = self.r*cos(self.theta)
            self.y = self.r*sin(self.theta)
    
    def velocity(self):
        pass
        
    def __str__(self):
        return "S"


if __name__=="__main__":
    r = symbols("r", cls=Function)
    th = symbols("theta", cls=Function)
    u = PositionVector2D(r = r, theta = th)
    print(u)
    
        
    
