# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:03:01 2026

@author: tomis
"""

# Imports

import matplotlib.pyplot as py
import numpy as np
from subfunctions import tau_dcmotor
from rover_dict import rover

# Graph details
py.figure(figsize=(6,10))

# Motor shaft calculations
motor_dict = rover['wheel_assembly']['motor']
omega_mss = np.linspace(0,motor_dict['speed_noload'], 100)
torque_vss = tau_dcmotor(omega_mss, motor_dict)
power_vss = omega_mss*torque_vss

# Graph 1
py.subplot(3,1,1)
py.plot(torque_vss,omega_mss, color='green', linewidth = 2)
py.title('Motor Shaft Speed vs Motor Torque')
py.xlabel("Motor Torque (N-m)")
py.ylabel("Motor Shaft Speed (rad/s)")

# Graph 2
py.subplot(3,1,2)
py.plot(torque_vss,power_vss, color ='blue', linewidth = 2)
py.title('Motor Power vs Motor Torque')
py.xlabel("Motor Torque (N-m)")
py.ylabel("Motor Shaft Power (W)")

# Graph 3
py.subplot(3,1,3)
py.plot(omega_mss,power_vss, color ='red', linewidth = 2)
py.title('Motor Power vs Motor Shaft Speed')
py.xlabel("Motor Shaft Speed (rad/s)")
py.ylabel("Motor Shaft Power (W)")

# Adjustments
py.tight_layout()
py.show() 