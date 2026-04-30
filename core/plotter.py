from sympy import sympify, diff, integrate, lambdify
from sympy.abc import x
from numpy import linspace, ones_like
import matplotlib.pyplot as plt

def plot(function_str):
    sympified = sympify(function_str)   # original function
    differentiated = diff(sympified)    # derived function
    integrated = integrate(sympified)   # integrated function

    x_values = linspace(-10,10,500)    # range of x-axis

    f_callable = lambdify(x, sympified, "numpy")    
    df_callable = lambdify(x, differentiated, "numpy")
    integral_callable  = lambdify(x, integrated, "numpy")

    y_f = f_callable(x_values) * ones_like(x_values)
    y_df = df_callable(x_values) * ones_like(x_values)
    y_integral = integral_callable(x_values) * ones_like(x_values)

    plt.plot(x_values, y_f, label="f(x)")
    plt.plot(x_values, y_df, label="f'(x)")
    plt.plot(x_values, y_integral, label="∫f(x)dx")
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.show()