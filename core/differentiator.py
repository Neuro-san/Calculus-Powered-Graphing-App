from scipy.differentiate import derivative
from sympy import sympify, diff, lambdify, pretty
from sympy.abc import x

def differentiate(function_str, x_value=None, evaluate=False):
    sympified = sympify(function_str)

    if not evaluate:
        return pretty(diff(sympified))  # returns the 1st derivative
    
    df_callable = lambdify(x, sympified, "numpy")
    result =  derivative(df_callable, x_value) 
    return result.df    # returns value substituted from 1st derivative