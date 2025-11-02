from math import sqrt
from math import pow

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


