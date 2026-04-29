from sympy import symbols, sympify, lambdify, integrate
import scipy.integrate as integration

def integration(user_input, value1, value2, evaluate=True):
    x = symbols('x')

    sympified = sympify(user_input)

    if evaluate:
        function = lambdify(x, sympified, "numpy")
        result = integration.quad(function, value1, value2)
        return result[0]    # returns a value from the definite integral
    else:
        return integrate(sympified) # returns anti-derivative (indefinite integral)