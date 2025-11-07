"""
Given a set burn time, the following code calculates the nozzle geometry and chamber properties at a 
variety of OF ratios and a variety of chamber pressures. 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from calculations import getOptimumExpansionRatio
from calculations import getMassFlow
from calculations import getExhaustVelocity
from calculations import getThroatDiameter
from calculations import getExitDiameter
from calculations import getDivergingLength

impulse = 40960 #in N, harcoded constant
burn_time = 5.1 #in s, hardcoded constant
thrust_avg = impulse / burn_time


def getData(paths, pressure):

    df = pd.read_csv(paths[0])
    
    OF = df["OF_RATIO"].to_numpy()
    ISP = df["ISP"].to_numpy()
    TEMP = df["CHAMBER_TEMP"].to_numpy()
    CP_CV = df["CP_CV"].to_numpy()
    MOL_WEIGHT = df["MOL_WEIGHT"].to_numpy()


    fig, axs = plt.subplots(6, figsize = (8,15))  
    """
    Plot in the following order:
    Graphs for ISP v.s. OF, 
    Temperature v.s. OF, 
    Expansion Ratio v.s. OF
    """
    """ISP v.s. OF Plot"""
    axs[0].plot(OF,ISP)
    axs[0].set_xlabel("OF Ratio")
    axs[0].set_ylabel("ISP")
    axs[0].set_title(f"ISP v.s. OF at {pressure} psi")


    """Temp v.s. OF Plot"""
    axs[1].plot(OF,TEMP)
    axs[1].set_xlabel("OF Ratio")
    axs[1].set_ylabel("Temperature (K)")
    axs[1].set_title(f"Chamber Temp (K) v.s. OF at {pressure} psi")

    """expansion ratio calculation (Ae / A*) and epsilon v.s. OF"""
    exp_ratios = []
    for i in range(len(df)):
        exp_ratios.append(getOptimumExpansionRatio(TEMP[i], CP_CV[i], pressure))
                          
    exp_ratios = np.array(exp_ratios)
    axs[2].scatter(OF, exp_ratios, color = "blue", marker = ".")
    axs[2].set_xlabel("OF Ratio")
    axs[2].set_ylabel("Expansion Ratio")
    axs[2].set_title(f"Expansion Ratio v.s. OF at {pressure} psi")

    """throat diameter v.s. OF plot"""
    throat_diameter = []
    for i in range(len(df)):
        c = getExhaustVelocity(ISP[i])
        mdot = getMassFlow(thrust_avg, c)
        throat_diameter.append(getThroatDiameter(mdot, pressure, MOL_WEIGHT[i], TEMP[i], CP_CV[i]))
    #print(exp_ratios)
    throat_diameter = np.array(throat_diameter)
    axs[3].scatter(OF, throat_diameter, color = "blue", marker = ".")
    axs[3].set_xlabel("OF Ratio")
    axs[3].set_ylabel("Throat Diameter (inches)")
    axs[3].set_title(f"Throat Diameter v.s. OF at {pressure} psi")
    #print(throat_diameter)

    """exit cone diameter calculations"""
    exit_diameter = []
    for i in range(len(df)):
        exit_diameter.append(getExitDiameter(exp_ratios[i], throat_diameter[i]))
    exit_diameter = np.array(exit_diameter)

    axs[4].scatter(OF, exit_diameter, color = "blue", marker = ".")
    axs[4].set_xlabel("OF Ratio")
    axs[4].set_ylabel("Exit Diameter (inches)")
    axs[4].set_title(f"Exit Diameter v.s. OF at {pressure} psi")

    """exit length calculations"""
    diverging_length = []
    for i in range(len(df)):
        diverging_length.append(getDivergingLength(throat_diameter[i], exp_ratios[i], conical = True))
    np.array(diverging_length)
    axs[5].scatter(OF, diverging_length, color = "blue", marker = ".")
    axs[5].set_xlabel("OF Ratio")
    axs[5].set_ylabel("Diverging Length (inches)")
    axs[5].set_title(f"Diverging Length v.s. OF at {pressure} psi")


    fig.tight_layout() #no overlapp of titles

    #plt.subplots_adjust(hspace = 8)

    plt.savefig(paths[1])
    #plt.show()
    
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

    





