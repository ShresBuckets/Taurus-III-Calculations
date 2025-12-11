![alt text](https://sites.utexas.edu/sec/files/2020/09/LRA-Logo-James-A-Schoener.jpg)
# Taurus-III-Calculations
Taurus 3 Calculations and Data Visualizations

How to use this program to find nozzle dimensions:
1. Perform a parameteric sweep on PROPEP over a range of OF ratios at differing chamber pressures. Collect resulting data in a spreadsheet and calculate the ISP at each parameter (do not record the value of ISP* as this is the vacuum optimized ISP, a subtly different metric). 

2. Determine the impulse and burn time from requirements.

3. Import PROPEP data and ISP as a CSV. Change hardcoded values for impulse and burn time.

Investigation of Burn Time:
One of the early ambiguities the team faced was in determining the burn time. This was due to the fact that regression constants for the particular design had not been characterized in previous iterations of the engine. The extent to which nozzle geometry depends on burn time was investigated in burn_time_investigation.py (see Taurus III documentation for the current burn time determination metholodgy).



