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
        


class ClosedLoopVector(object):
    def __init__(self, *vectors):
        k = 1
        for vector in vectors:
            vector.set_label(str(k))
            vector.update_kin_symbols()
            k += 1
        self.vectors = vectors
            
    def get_pos_eqs(self):
        pos_eqs = vexp(0,0)
        for vec in self.vectors:
            pos_eqs += vexp(vec.r, vec.theta)
        return pos_eqs
    
    def get_vel_eqs(self):
        pass
            
    def solve_pos(self):
        pass
        

class VectorKin(object):
    def __init__(self, case, **props):
        self.__dict__ = props
        self.case = case
        _kprops = {"r":"r",
                   "theta":"\\theta",
                   "omega":"\\omega",
                   "rp":"\\dot{r}",
                   "alpha":"\\alpha",
                   "rpp":"\\ddot{r}"}
        if self.case == 1:
            self.rp = 0
            self.rpp = 0
        elif self.case == 2:
            self.omega = 0
            self.alpha = 0
        elif self.case == 3:
            pass
        elif self.case == 4:
            self.omega = 0
            self.alpha = 0
            self.rp = 0
            self.rpp = 0
        for kprop in _kprops:
            if kprop not in props:
                self.__dict__.update({kprop:symbols(_kprops[kprop])})
        self.label = ""
        
    
    def set_label(self,label):
        self.label = label
        
    def update_kin_symbols(self):
        _kprops = {"r":"r_{"+self.label+"}",
                   "theta":"\\theta_{"+self.label+"}",
                   "omega":"\\omega_{"+self.label+"}",
                   "rp":"\\dot{r}_{"+self.label+"}",
                   "alpha":"\\alpha_{"+self.label+"}",
                   "rpp":"\\ddot{r}_{"+self.label+"}"}
        for kprop in _kprops:
            if not(type(self.__dict__[kprop]) is int 
               or type(self.__dict__[kprop]) is float 
               or type(self.__dict__[kprop]) is Float 
               or type(self.__dict__[kprop]) is Mul
               or type(self.__dict__[kprop]) is Add):
                self.__dict__.update({kprop:symbols(_kprops[kprop])})
        
    def __str__(self):
        return "S"


class _Vec(Matrix):
    pass
    # ~ def __init__(self, *args, **kwargs):
        # ~ Matrix.__init__(self, *args, **kwargs)
    

class _Vector3D_(object):
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


class _Vector2D_(object):
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
        



if __name__=="__main__":
    r = symbols("r")
    th = symbols("theta")
    u = VectorKin(1,omega=10)
    s = _Vec([1,2,3])
    print(s)
    
