import numpy as np
from calculations import getOxMassFlow, getBurnTime, getFuelMass
"""
methodology detailed here: 
https://docs.google.com/document/d/1mcrzB8ezUHT-8gzcfrp7zFrYqLWTqfUR3aNArxDt_qg/edit?tab=t.0.
The following calculations are performed in SI units and converted to imperial upon printing. 
"""

#fixed constants:
total_impulse = 40960 #Ns
a = 0.000188 #regression coefficient, in SI units
n = 0.347 #regression exponent, dimensionless
outer_diameter = 5 * .0254 #conversion from 5 inches to meters
mdot_ox = getOxMassFlow() #in kg/s
fuel_mass = getFuelMass()
burn_time = getBurnTime() #in s
htpb_density = 920 #in kg/m^3

outer_radius = outer_diameter / 2
const = float(2*n + 1)
inner_radius = np.power(np.power(outer_radius, const) - const*a*np.power(mdot_ox/ np.pi, n)*burn_time, 1/const)

grain_length = getFuelMass() / (np.pi * htpb_density * (outer_radius**2 - inner_radius**2))
