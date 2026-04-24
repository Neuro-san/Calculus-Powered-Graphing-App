# Calculus-Powered-Graphing-App
A Python-based application that visualizes functions and their derivatives/integrals using computational methods.

# Objective:
Develop a Python-based application that visualizes functions and their derivatives/integrals using computational
methods.

# Learning Outcomes:
1. Apply numerical differentiation and integration techniques in programming.
2. Use Python libraries (NumPy, SciPy, Matplotlib) for mathematical computations and visualization.
3. Understand the practical applications of calculus in computer science, such as data analysis, physics
simulations, and machine learning.

# Project Requirements:
1. The program should allow users to input a mathematical function.
2. Compute and visualize:
  o The original function
  o Its first derivative (using numerical differentiation)
  o Its integral (using numerical integration)
  o Solve areas under the curves and between curves
3. Display all graphs using Matplotlib for easy interpretation.
4. Provide an interactive user interface (either a simple CLI or a basic GUI using Tkinter).
# Implementation Steps:
1. Function Input:
  o Allow users to input a function in Python syntax (e.g., x**2 + 3*x + 5).
  o Use sympy to parse the function.
2. Numerical Differentiation:
  o Use scipy.misc.derivative() or implement finite difference approximation.
3. Numerical Integration:
  o Use scipy.integrate.quad() to approximate the integral.
4. Graph Visualization:
  o Use matplotlib to plot the original function, its derivative, and its integral over a specified
    range.
5. User Interaction:
  o Allow users to select the range of x values and choose between differentiation and integration.
# Extensions (Optional):
  • Allow users to compute higher-order derivatives.
  • Implement a GUI using Tkinter or PyQt.
  • Save graphs as images.
