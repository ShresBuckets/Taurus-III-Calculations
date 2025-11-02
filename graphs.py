import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df450 = pd.read_csv("data/450psi.csv")

"""
Graphs for ISP v.s. OF, 
Temperature v.s. OF, 
Expansion Ratio v.s. OF
"""
OF = df450["OF_RATIO"].to_numpy()
ISP = df450["ISP"].to_numpy()
plt.plot(OF,ISP)
plt.show()

