from math import sqrt
from math import pow
from math import pi

def getOptimumExpansionRatio(T, k, P0):
    """
    Returns the optimum expansion ratio assuming the 
    ambient pressure is 14.7 psi. Assumes T is in K, P0 is in PSI (ratio with 14.7 is dimensionless), k is dimensionless
    """
    pressure_ratio = 14.7/P0
    first_term = pow((k + 1) / 2, 1 / (k-1))
    second_term = pow(pressure_ratio, 1 / k)
    third_term = sqrt((k+1)/(k-1) * pow(pressure_ratio, (k-1) / k))
    
    epsilon = 1 / (first_term * second_term * third_term)
    return epsilon

def getExhaustVelocity(thrust, burntime):
    return thrust / burntime

def getMassFlow(thrust, c):
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




