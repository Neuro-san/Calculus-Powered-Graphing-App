from sympy import symbols, sympify
# import pretty if need human-readable function

def parse_function(function, value):
    x = symbols('x')
    
    result = sympify(function).subs(x, value)
    
    return result