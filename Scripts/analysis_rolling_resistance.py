#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect
from subfunctions import F_net, get_gear_ratio, rover
planet = {'g': 3.72}

#defs and labels
Crr = np.linspace(0.1, 0.5, 25)
slope_array_deg = 0
v_max = np.zeros(len(Crr))
omega_min = 0.0
omega_max = rover['wheel_assembly']['motor']['speed_noload']
r = rover['wheel_assembly']['wheel']['radius']
Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])

# iterate thru constant for velocity
for i, c in enumerate(Crr):
    
    def target_net_force(omega):
        return F_net(omega, slope_array_deg, rover, planet, c)
    
    try:
        #shaft speed when force is 0 
        omega_root = bisect(target_net_force, omega_min, omega_max)        
        v_max[i] = r * (omega_root / Ng)    #converts
        
    except ValueError:
        # for no root
        v_max[i] = np.nan

# Plot the results
plt.figure()
plt.plot(Crr, v_max, marker='o', linestyle='-')
plt.xlabel("Rolling Resistance Coefficient (Crr")
plt.ylabel("Maximum Rover Velocity [m/s]")
plt.title("Max Attainable Speed vs Rolling Resistance (Slope = 0 deg)")
plt.grid(True)
plt.show()