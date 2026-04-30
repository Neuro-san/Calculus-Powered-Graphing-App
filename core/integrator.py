from sympy import sympify, lambdify, integrate, pretty
from sympy.abc import x
import scipy.integrate as integral

def integration(function_str, lower_limit=None, upper_limit=None, evaluate=False):
    sympified = sympify(function_str)

    if not evaluate:
        return pretty(integrate(sympified))     # returns anti-derivative (indefinite integral)
    
    integral_callable = lambdify(x, sympified, "numpy")
    result = integral.quad(integral_callable, lower_limit, upper_limit)
    return result[0]    # returns the value from the definite integral