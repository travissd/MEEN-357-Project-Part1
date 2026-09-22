#Imports
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d.axes3d import Axes3D
from scipy.optimize import root_scalar #bisect
import subfunctions as sub #Imports all functions for basic calculations
Crr_array = np.linspace(0.01,0.5,25)
slope_array_deg = np.linspace(-15,35,25)
CRR, SLOPE = np.meshgrid(Crr_array, slope_array_deg)
VMAX = np.zeros(np.shape(CRR), dtype = float)
#Initializing Constant Data Values
ω_min = 0
ω_max = sub.rover["wheel_assembly"]['motor']['speed_noload']
r = sub.rover["wheel_assembly"]['wheel']["radius"]
Ng = sub.get_gear_ratio(sub.rover['wheel_assembly']['speed_reducer'])
rows, cols = np.shape(CRR)
for i in range(rows):
    for j in range(cols):
        Crr_sample = float(CRR[i,j])
        terrangle = float(SLOPE[i,j]) #v = rω = r * (ω_in/Ng)
        #Initializing force equation
        F = lambda ω: sub.F_net(ω, terrangle, sub.rover, sub.planet, Crr_sample)
        try:
            sol = root_scalar(F, method='bisect', bracket = [ω_min, ω_max]) #Root Finding through Bisection method
            ω_in = sol.root
            VMAX[i,j] = r * (ω_in / Ng) #VMAX Value
        except (ValueError, RuntimeError): #Error Handling
            VMAX[i,j] = np.nan
        
#Plotting Results
#3D Surface Gradient Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surface = ax.plot_surface(CRR, SLOPE, VMAX, cmap = 'viridis')
ax.set_xlabel("Rolling Resistance Coefficient (CRR)")
ax.set_ylabel("Terrain Slope (deg)")
ax.set_zlabel("Maximum Velocity (VMAX, m/s)")
ax.set_title("Rover Speed vs. Combined Terrain Parameters")
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label='VMAX (m/s)')
#2D Contour Plot
fig1, ax1 = plt.subplots()
cont = plt.contourf(CRR, SLOPE, VMAX, 25)
ax1.set_xlabel("Rolling Resistance Coefficient (CRR)")
ax1.set_ylabel("Terrain Slope (deg)")
ax1.set_title("Rover Speed vs. Combined Terrain Parameters")
cbar = fig1.colorbar(cont)
cbar.set_label("Maximum Velocity (VMAX, m/s)")

