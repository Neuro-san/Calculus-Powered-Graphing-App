from sympy import symbols, sympify
# import 'pretty' as well if need human-readable function

def parse_function(input_function, value, evaluate=True):
    x = symbols('x')
    
    sympified = sympify(input_function)

    if evaluate:
        result = float(sympified.subs(x, value))
        return result   #returns a value substituted from input_function
    else:
        return sympified    #returns input_function