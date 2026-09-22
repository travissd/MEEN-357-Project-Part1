#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect
from subfunctions import F_net, get_gear_ratio, rover
planet = {'g': 3.72}

#defs and labels
Crr = 0.15
slope_array_deg = np.linspace(-15, 35, 25)
v_max = np.zeros(len(slope_array_deg))
omega_min = 0.0
omega_max = rover['wheel_assembly']['motor']['speed_noload']
r = rover['wheel_assembly']['wheel']['radius']
Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])

# iterate thru slope for velocity
for i, slope in enumerate(slope_array_deg):
    
    def target_net_force(omega):
        return F_net(omega, slope, rover, planet, Crr)
    
    try:
        #shaft speed when force is 0 
        omega_root = bisect(target_net_force, omega_min, omega_max)
        v_max[i] = r * (omega_root / Ng)            # converts
        
    except ValueError:
        # for no root
        v_max[i] = np.nan

# Plot the results
plt.figure()
plt.plot(slope_array_deg, v_max, marker='o', linestyle='-')
plt.xlabel("Terrain Slope [deg]")
plt.ylabel("Maximum Rover Velocity [m/s]")
plt.title("Max Attainable Speed vs Terrain Slope (Crr = 0.15)")
plt.grid(True)
plt.show()