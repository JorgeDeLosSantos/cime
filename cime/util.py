from sympy import *
 
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


if __name__=="__main__":
    print(deg2rad(90))
    print(rad2deg(pi/4))

