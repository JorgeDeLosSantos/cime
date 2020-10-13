from sympy import *
from sympy.matrices import *
from sympy.physics.mechanics import dynamicsymbols, init_vprinting
import matplotlib.pyplot as plt
init_vprinting()

def kinvars(*args,**kwargs):
    return dynamicsymbols(*args,**kwargs)

class Vector2D(object):
    def __init__(self,*args,**kwargs):
        if "x" in kwargs and "y" in kwargs:
            self._x = kwargs["x"]
            self._y = kwargs["y"]
            self._calculate_magnitude_and_angle()
        elif "r" in kwargs and "theta" in kwargs:
            self._r = kwargs["r"]
            self._theta = kwargs["theta"]
            self._calculate_rect_components()
        if len(args) == 2:
            self._r = args[0]
            self._theta = args[1]
            self._calculate_rect_components()

    def _calculate_rect_components(self):
        self._x = self.r*cos(self.theta)
        self._y = self.r*sin(self.theta)

    def _calculate_magnitude_and_angle(self):
        self._theta = atan2(self.y, self.x)
        self._r = sqrt(self.x**2 + self.y**2)

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self,theta):
        self._theta = theta
    
    @property
    def r(self):
        return self._r

    @r.setter
    def r(self,r):
        self._r = r

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,y):
        self._y = y

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

    def diff(self,var,order=1):
        dx = diff(self.x, var, order)
        dy = diff(self.y, var, order)
        return Vector2D(x=dx, y=dy)

    def subs(self,vals):
        for old,new in vals.items():
            self.x = self.x.subs(old,new)
            self.y = self.y.subs(old,new)
                
    def __add__(self, other):
        ux, uy = self.x, self.y
        vx, vy = other.x, other.y
        return Vector2D(x = ux + vx, y = uy + vy)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __neg__(self):
        return Vector2D(x = -self.x, y=-self.y)
                
    def __sub__(self, other):
        ux, uy = self.x, self.y
        vx, vy = other.x, other.y
        return Vector2D(x = ux - vx, y = uy - vy)

    def __str__(self):
        s = "<{x}, {y}>".format(x=self.x, y=self.y)
        return s

    def __repr__(self):
        s = "<{x}, {y}>".format(x=self.x, y=self.y)
        return s
        # from sympy.printing.latex import latex
        # s = latex(self, mode='plain')
        # return "$\\displaystyle %s$" % s

    def _repr_html_(self):
        from sympy.printing.latex import LatexPrinter
        from sympy.physics.vector import vlatex
        lp = LatexPrinter()
        x = vlatex(self.x)
        y = vlatex(self.y)
        # return lp.doprint("$$ \\langle {0}, \\\\ {1} \\rangle $$".format(x,y))
        return lp.doprint(r"$$ \begin{bmatrix} {%s} \\ {%s} \end{bmatrix} $$"%(x,y))

    
class VectorLoop(object):
    def __init__(self,*vectors):
        self.vectors = []
        for vector in vectors:
            self.vectors.append(vector)

        self._loop = sum(self.vectors)

    def add_vector(self,vector):
        self.vectors.append(vector)
        self._loop = sum(self.vectors)

    @property
    def loop(self):
        return self._loop

    def diff(self,var,order=1):
        vds = []
        for vector in self.vectors:
            dv = vector.diff(var,order)
            vds.append(dv)
        return VectorLoop(*vds)

    def solve(self,vars,values):
        x = self.loop.x.subs(values)
        y = self.loop.y.subs(values)
        sols = solve([x,y], vars)
        return sols

    def draw(self,values={}):
        xcoords = [0]
        ycoords = [0]
        for vector in self.vectors:
            if isinstance(vector.x, (float, int)):
                _cx = vector.x + xcoords[-1]
                _cy = vector.y + ycoords[-1]
            else:
                _cx = vector.x.subs(values) + xcoords[-1]
                _cy = vector.y.subs(values) + ycoords[-1]
            xcoords.append(_cx)
            ycoords.append(_cy)
        plt.plot(xcoords, ycoords, "-o")
        return xcoords,ycoords

    def __str__(self):
        s = "<{x}, {y}>".format(x=self.loop.x, y=self.loop.y)
        return s

    def __repr__(self):
        s = "<{x}, {y}>".format(x=self.loop.x, y=self.loop.y)
        return s

    def _repr_html_(self):
        from sympy.printing.latex import LatexPrinter
        from sympy.physics.vector import vlatex
        lp = LatexPrinter()
        x = vlatex(self.loop.x)
        y = vlatex(self.loop.y)
        return lp.doprint(r"$$ \begin{bmatrix} {%s} \\ {%s} \end{bmatrix} $$"%(x,y))




if __name__ == '__main__':
    t = symbols("t")
    r1,r2 = symbols("r_1:3")
    t1,t2 = dynamicsymbols("\\theta_1:3")
    v1 = Vector2D(x=1,y=2)
    v2 = Vector2D(x=3,y=4)
    v3 = Vector2D(r1,t1)
    # print(f"{v1} + {v2} = {v1+v2}")
    # print(f"{v1} - {v2} = {v1-v2}")
    # print(f"{v1} . {v2} = {v1.dot(v2)}")
    # print(f"D_v3 = {v3.diff(t,2)}")
    print(v3._repr_html_())