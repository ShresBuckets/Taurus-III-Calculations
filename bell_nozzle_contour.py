import pandas as pd
import sympy as sp
from sympy import rad
from sympy import sin
from sympy import cos
from sympy import tan
from sympy import symbols
"""
To calculate the bell nozzle spline, the following inputs are needed:
- throat radius 
- expansion ratio (calculated)
- Length of a conical nozzle with 80% half angle and same expansion ratio/throat radius (contained in calculations.py)

(the next two are derived from a graph shown in Huzel/Huang):
- initial diverging half angle
- exit diverging half angle
"""


def getParametricValues(throat_radius, exit_radius, diverging_length, theta_n, theta_e):
    """
    Returns a matrix consisting of the six canted parabola values in the following order:

    """
    theta_n = rad(theta_n)
    theta_e = rad(theta_e)

    R_1 = 1.5*throat_radius #rule of thumb from Huzel and Huang
    R_2 = 0.382 * throat_radius #rule of thumb from Huzel and Huang
    z_n = R_2 * sin(theta_n)
    r_n = throat_radius + R_2*(1-cos(theta_n))
    z_e = diverging_length #80% bell nozzle for taurus iii
    r_e = exit_radius

    m, h, k, psi, t_n, t_e = sp.symbols("m h k psi t_n t_e")

    sol = sp.nsolve([t_n*(-m*sin(psi)*t_n + cos(psi)) + h - z_n
                     ,t_n * (m*cos(psi)*t_n + sin(psi)) + k - r_n
                     ,t_e * (-m*sin(psi)*t_e + cos(psi)) + h - z_e
                     ,t_e*(m*cos(psi)*t_e + sin(psi)) + k - r_e
                     ,(-2*m*cos(psi)*t_n - sin(psi)) / (2*m*sin(psi)*t_n-cos(psi)) - tan(theta_n)
                     ,(-2*m*cos(psi)*t_e - sin(psi)) / (2*m*sin(psi)*t_e-cos(psi)) - tan(theta_e)
                     ], [m,h,k,psi,t_n,t_e], [0.02, 0.0, 1.5, 0.25, 0.1, 0.9], tol = 1e-14, prec = 30)

    return sol
     
print(getParametricValues(1.87/2, 2, 0.8*2.55,22.5,13.4))