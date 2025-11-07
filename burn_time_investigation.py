"""
The following code determines the effect of increasing burn time on nozzle geometry as a percent change in length
away from an initial design choice at t_burn = 5.1 s (impulse of 40960 Ns)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from calculations import getDivergingLength, getExhaustVelocity, getExitDiameter, getMassFlow, getOptimumExpansionRatio, getThroatDiameter

t = 5.1 #initial burn time
time = np.linspace(t,9,50)
impulse = 40960 # in Ns
pressure = 350 #in psi, fix this
csv_path = [f"data/{pressure}psi.csv"]
#csv_path = [f"data/{pressure}psi.csv" for pressure in range(350,551,25)]

of_ratio_index = 16  #fix this, corresponds to an OF ratio of 5 but the index in the csv is the 6th row

for path in csv_path:
    fig, axs = plt.subplots(3, figsize = (8, 20)) 

    thrust_avg = impulse / time #array of average thrust
    df = pd.read_csv(path)
    
    OF = df["OF_RATIO"].to_numpy()[of_ratio_index]
    ISP = df["ISP"].to_numpy()[of_ratio_index]
    TEMP = df["CHAMBER_TEMP"].to_numpy()[of_ratio_index]
    CP_CV = df["CP_CV"].to_numpy()[of_ratio_index]
    MOL_WEIGHT = df["MOL_WEIGHT"].to_numpy()[of_ratio_index]

    exp_ratio = getOptimumExpansionRatio(TEMP, CP_CV, pressure) #note, expansion ratio does NOT have a dependency on burn time
    throat_diameter = []
    exit_diameter = []
    diverging_length = []

    for thrust in thrust_avg:
        c = getExhaustVelocity(ISP)
        mdot = getMassFlow(thrust, c)
        throat_diameter.append(getThroatDiameter(mdot, pressure, MOL_WEIGHT, TEMP, CP_CV))

                          
    
    for i in range(len(thrust_avg)):
        exit_diameter.append(getExitDiameter(exp_ratio, throat_diameter[i]))

    for i in range(len(thrust_avg)):
        diverging_length.append(getDivergingLength(throat_diameter[i], exp_ratio, conical = True))
    
    diverging_length = np.array(diverging_length)
    throat_diameter = np.array(throat_diameter)
    exit_diameter = np.array(exit_diameter)

    for i in range(1, len(thrust_avg)):
        diverging_length[i] = abs(diverging_length[i]-diverging_length[0]) / diverging_length[0]
        throat_diameter[i] = abs(throat_diameter[i]-throat_diameter[0]) / throat_diameter[0]
        diverging_length[i] = abs(exit_diameter[i]-exit_diameter[0]) / exit_diameter[0]

        #print(abs(throat_diameter[i]-throat_diameter[i-1]))
        #print(abs(diverging_length[i]-diverging_length[i-1]))

    axs[0].plot(time[1:], throat_diameter[1:])
    axs[0].set_xlabel("burn time")
    axs[0].set_ylabel("percent change in throat diameter")
    axs[0].set_title("Percent Change in Throat Diameter v.s. Burn Time")

    axs[1].plot(time[1:], exit_diameter[1:])
    axs[1].set_xlabel("burn time")
    axs[1].set_ylabel("percent change in exit diameter")
    axs[1].set_title("Percent Change in Exit Diameter v.s. Burn Time")

    axs[2].plot(time[1:], diverging_length[1:])
    axs[2].set_xlabel("burn time")
    axs[2].set_ylabel("percent change in diverging length in inches")
    axs[2].set_title("Percent Change in Diverging Length v.s. Burn Time")

    #print(throat_diameter)

    fig.tight_layout()
    plt.savefig("burn_time.png")
print("success")











