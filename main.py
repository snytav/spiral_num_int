import numpy as np

# https://docs.sympy.org/latest/guides/solving/solve-ode.html#numerically-solve-an-ode-in-scipy

from sympy import symbols, lambdify
import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
# Create symbols y0, y1, and y2
y = symbols('y:2')
k, m = symbols('k m')
# rf = kf * y[0]**2 * y[1]
# rb = kb * y[2]**2
# Derivative of the function y(t); values for the three chemical species
# for input values y, kf, and kb
ydot = [y[1], -k/m*y[0]]
ydot
t = symbols('t') # not used in this case
# Convert the SymPy symbolic expression for ydot into a form that
# SciPy can evaluate numerically, f
f = lambdify((t, y, k, m), ydot)
k_vals = np.array([1.0, 1.0]) # arbitrary in this case
y0 = [1,  0] # initial condition (initial values)
t_eval = np.linspace(0, 10, 50) # evaluate integral from t = 0-10 for 50 points
# Call SciPy's ODE initial value problem solver solve_ivp by passing it
#   the function f,
#   the interval of integration,
#   the initial state, and
#   the arguments to pass to the function f
solution = scipy.integrate.solve_ivp(f, (0, 10), y0, t_eval=t_eval, args=k_vals)
# Extract the y (concentration) values from SciPy solution result
y = solution.y
# Plot the result graphically using matplotlib
plt.plot(t_eval, y.T)
# Add title, legend, and axis labels to the plot
plt.title('Weight on a spring')
plt.legend(['Position', 'Velocity'], shadow=True)
plt.xlabel('time')
plt.savefig('weight_spring.png')
# Finally, display the annotated plot
plt.show()
qq = 0