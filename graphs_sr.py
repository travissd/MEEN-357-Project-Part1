# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:54:23 2026

@author: tomis
"""

# Imports

import matplotlib.pyplot as py
import numpy as np
from subfunctions import tau_dcmotor 
from subfunctions import get_gear_ratio
from rover_dict import rover

# Graph details
py.figure(figsize=(6,10))

# Motor Shaft Calculations
motor_dict = rover['wheel_assembly']['motor']
omega_mss = np.linspace(0,motor_dict['speed_noload'], 100)
Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])
omega_msr = omega_mss/Ng
torque_vss = tau_dcmotor(omega_mss, motor_dict)
torque_vsr = Ng*torque_vss
power_vsr = omega_msr*torque_vsr

# Graph 1
py.subplot(3,1,1)
py.plot(torque_vsr,omega_msr, color='green', linewidth = 2)
py.title('Speed Reducer Speed vs Speed Reducer Torque')
py.xlabel("Speed Reducer Torque (N-m)")
py.ylabel("Speed Reducer Speed (rad/s)")

# Graph 2
py.subplot(3,1,2)
py.plot(torque_vsr,power_vsr, color ='blue', linewidth = 2)
py.title('Speed Reducer Power vs Torque')
py.xlabel("Speed Reducer Torque (N-m)")
py.ylabel("Speed Reducer Power (W)")

# Graph 3
py.subplot(3,1,3)
py.plot(omega_msr,power_vsr, color ='red', linewidth = 2)
py.title('Speed Reducer Power vs Speed Reducer Speed')
py.xlabel("Speed Reducer Speed (rad/s)")
py.ylabel("Speed Reducer Power (W)")


# Adjustments
py.tight_layout()
py.show() 