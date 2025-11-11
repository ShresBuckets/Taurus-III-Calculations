from math import sqrt
from math import pow
from math import pi
from math import tan
from math import cos

def getOptimumExpansionRatio(T, k, P0, ambient):
    """
    Returns the optimum expansion ratio assuming the 
    ambient pressure is ambient_pressure (in psi). Assumes T is in K, P0 is in PSI (ratio with 14.7 is dimensionless), k is dimensionless
    """
    pressure_ratio = ambient/P0
    first_term = pow((k + 1) / 2, 1 / (k-1))
    second_term = pow(pressure_ratio, 1 / k)
    third_term = sqrt((k+1)/(k-1) * pow(pressure_ratio, (k-1) / k))
    
    epsilon = 1 / (first_term * second_term * third_term)
    return epsilon

def getExhaustVelocity(isp): 
    return isp * 9.81

def getMassFlow(thrust, c): #T = mdot * c
    return thrust / c

def getThroatDiameter(mdot, P0, molecular_mass, T0, k): 
    """Returns the throat diameter. P0 is the chamber pressure, T0 is the chamber temperature. 
        Assumes mdot is in kg/s, P0 is in psi, molecular mass is in g/mol, T0 is in K, k is dimensionless.
    """

    P0 *= 6894.76 #convert psi to pascal
    molecular_mass /= 1000 #convert g/mol to kg/mol
    R = 8.314 / molecular_mass #J/(K*kg), specific gas constant

    term1 = sqrt(k / (R * T0))
    term2 = pow(2 / (k+1), (k+1)/(2*(k-1)))
    area = mdot / (P0 * term1 * term2)
    #pi/4 * d^2 = area
    diameter = sqrt(area * 4 / pi) #in meters

    diameter *= 39.3701 #convert meters to inches

    return diameter

def getExitDiameter(exp_ratio, throat_diameter):
    return sqrt(throat_diameter**2 * exp_ratio)
    #Ae = ep * At
    #de^2 = ep * dt^2
def getDivergingLength(throat_diameter, exp_ratio, half_angle = 15, conical = False, bell = False, bell_fraction = 0.8):
    """
    Returns the length from the throat section to the end of the diverging section for different nozzle configurations. 
    Throat_diameter should be in inches, half angle
    is in degrees. 
    """

    throat_radius = throat_diameter / 2
    trapezoidal_comp = throat_radius * (sqrt(exp_ratio) - 1) / tan(half_angle)
    R = 1.5 * throat_radius #rule of thumb, see construction
    arc_comp = R * ((1.0/cos(half_angle)) - 1) / tan(half_angle)
    L_n =  trapezoidal_comp + arc_comp #distance from throat to exit section

    if conical:
        """
        Conical nozzle constructed as follows: draw an arc of a circle with radius R = 1.5 * R_throat. Draw the tangent line to the arc
        at the end of the arc and extend it (this is the diverging section)
        """
        return L_n

    elif bell:
        return L_n * bell_fraction

