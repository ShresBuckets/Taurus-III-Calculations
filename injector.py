"""These calculations will be split up into two sections: configuration calculations v.s. geometric calculations"""


"""
Configuration:
The team has decided to use a doublet impinging injector design.
"""
from calculations import getOxMassFlow, getManifoldPressure

n = 16 #number of holes
mdot = getOxMassFlow()
nitrous_density = 908 #in kg/m^3, varies with pressure
orifice_diameter = 3./32 #in inches
chamber_pressure = 450 #in psi


manifold_pressure = getManifoldPressure()
stiffness = (manifold_pressure - chamber_pressure) / chamber_pressure * 100 #pressure drop as a percentage of chamber pressure







