from sympy import sympify, pretty
from sympy.abc import x

def parse_function(function_str, x_value=None, evaluate=False):
    f_callable = sympify(function_str)

    if not evaluate:
        return pretty(f_callable)    # returns input_function
        
    result = float(f_callable.subs(x, x_value))
    return result   #returns a value substituted from input_function