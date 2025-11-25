import numpy as np
from calculations import getBurnTime, getMassFlow
"""
methodology detailed here: 
https://docs.google.com/document/d/1mcrzB8ezUHT-8gzcfrp7zFrYqLWTqfUR3aNArxDt_qg/edit?tab=t.0
"""

#fixed constants:
total_impulse = 40960 #Ns
a = 0.000188 #regression coefficient
n = 0.347 #regression exponent
outer_diameter = 5

outer_radius = outer_diameter / 2
inner_radius = 