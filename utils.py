# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import sqrt from math 
def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """

    rep=1
    i=1
    while i>n:
        rep *= n
        i += 1
    return rep

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """

    root=()
    delta = (b**2) - (4*a*c)
    if delta == 0:
        root=((-b)/(2*a))
        return (root,)
    elif delta > 0:
        root=((-b + sqrt(delta))/(2*a),(-b - sqrt(delta))/(2*a))
        return root
    else:
        return root

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    rep = (upper - lower)*(eval(function, {'x': lower}) + (eval(function, {'x': upper})))/2 
    return rep

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))
    