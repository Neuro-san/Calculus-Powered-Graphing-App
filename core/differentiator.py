from scipy.differentiate import derivative
from sympy import sympify, diff, symbols, lambdify

def differentiate(input_function, value, evaluate=True):
    x = symbols('x')

    sympified = sympify(input_function)

    if evaluate:
        function = lambdify(x, sympified, "numpy")
        result =  derivative(function, value) 
        return result.df    #returns value substituted from 1st derivative
    else:
        return diff(sympified) #returns the 1st derivative