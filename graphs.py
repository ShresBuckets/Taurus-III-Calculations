import pandas as pd
import numpy as np
df450 = pd.read_csv("data/450psi.csv")

"""
Graphs for ISP v.s. OF, 
Temperature v.s. OF, 
Expansion Ratio v.s. OF
"""
OF = df450["OF_RATIO"].to_numpy()
print("works")
