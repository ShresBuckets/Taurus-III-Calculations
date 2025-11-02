import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from calculations import getOptimumExpansionRatio

def getData(paths, pressure):

    df = pd.read_csv(paths[0])
    
    OF = df["OF_RATIO"].to_numpy()
    ISP = df["ISP"].to_numpy()
    TEMP = df["CHAMBER_TEMP"].to_numpy()
    CP_CV = df["CP_CV"].to_numpy()


    fig, axs = plt.subplots(3) 
    """
    Plot in the following order:
    Graphs for ISP v.s. OF, 
    Temperature v.s. OF, 
    Expansion Ratio v.s. OF
    """
    #ISP v.s. OF Plot
    axs[0].plot(OF,ISP)
    axs[0].set_xlabel("OF Ratio")
    axs[0].set_ylabel("ISP")
    axs[0].set_title(f"ISP v.s. OF at {pressure} psi")


    #Temp v.s. OF Plot
    axs[1].plot(OF,TEMP)
    axs[1].set_xlabel("OF Ratio")
    axs[1].set_ylabel("Temperature (K)")
    axs[1].set_title(f"Chamber Temp (K) v.s. OF at {pressure} psi")

    #expansion ratio calculation (Ae / A*) and epsilon v.s. OF
    exp_ratios = []
    for i in range(len(df)):
        exp_ratios.append(getOptimumExpansionRatio(TEMP[i], CP_CV[i], pressure))
                          
    exp_ratios = np.array(exp_ratios)
    axs[2].plot(OF, exp_ratios)
    axs[2].set_xlabel("OF Ratio")
    axs[2].set_ylabel("Expansion Ratio")
    axs[2].set_title(f"Expansion Ratio v.s. OF at {pressure} psi")


    fig.tight_layout()


    plt.savefig(paths[1])
    
def getPaths(pressure):
    source = f"data/{pressure}psi.csv"
    dest = f"graphs/{pressure}psi.png"
    return (source, dest)

getData(getPaths(350), 350)
getData(getPaths(375), 375)
getData(getPaths(400), 400)
getData(getPaths(425), 425)
getData(getPaths(450), 450)
getData(getPaths(475), 475)
getData(getPaths(500), 500)
getData(getPaths(525), 525)
#getData(getPaths(550), 550)
print("done")

    





