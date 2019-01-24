from sympy import *
from sympy.matrices import *
import numpy as np
import matplotlib.pyplot as plt
init_printing(use_latex=True)


def newton_raphson(J,b,X0,vals={},eps=1e-6, debug=False):
    """ Método de Newton-Raphson multivariable """
    k = 1
    b = b.subs(vals).evalf()
    while True:
        x = ((J.subs(X0).subs(vals)).inv()*b.subs(X0)).evalf()
        if x.norm()<eps: break
        if debug:
            print(x.norm(), x)
        for jj,ky in enumerate(X0):
            X0[ky] += (x[jj]).evalf()
        k += 1
    return X0,x,k


    

if __name__=="__main__":
    print( generate_grashof_fourbar(100, 1.6) )
        
    
