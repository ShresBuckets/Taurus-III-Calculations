import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
df450 = pd.read_csv("data/450psi.csv")

"""
Graphs for ISP v.s. OF, 
Temperature v.s. OF, 
Expansion Ratio v.s. OF
"""
OF = df450["OF_RATIO"].to_numpy()
ISP = df450["ISP"].to_numpy()
TEMP = df450["CHAMBER_TEMP"].to_numpy()

fig, axs = plt.subplots(2)
axs[0].plot(OF,ISP)
axs[0].set_title("ISP v.s. OF at 450 psi")
axs[0].set_xlabel("OF Ratio")
axs[0].set_ylabel("ISP")

axs[1].plot(OF,TEMP)
axs[1].set_xlabel("OF Ratio")
axs[1].set_ylabel("Chamber Temperature (K)")
axs[1].set_title("Chamber Temp (K) v.s. OF at 450 psi")
#axs[0].xlabel("OF Ratio")
#axs[0].ylabel("ISP")
#axs[0].title(f"ISP v.s. OF at {450} psi")
plt.savefig("example.png")
print(matplotlib.get_backend())

