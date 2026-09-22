# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:51:38 2026

@author: tomis
"""

import numpy as np
def F_net(omega, terrain_angle, rover, planet, Crr):
    
    #Validation checks
    if not (isinstance(omega, np.ndarray) or isinstance(omega, (int, float))):  
        raise Exception("omega should be vectors or scalars. ")
    if not (isinstance(terrain_angle, np.ndarray) or isinstance(terrain_angle, (int, float))):  
        raise Exception("terrain_angle should be vectors or scalars. ")
    if isinstance(omega, np.ndarray) and isinstance(terrain_angle, np.ndarray):
        if omega.size != terrain_angle.size:
            raise Exception("omega and terrain_angle should have the dsame amount of elements")
    try:
        for elements in terrain_angle:
            if int(elements) < -75 or int(elements) > 75:
                raise Exception("Elements in terrain_angle should be between -75 degrees and +75 degrees")
    except:
        if int(terrain_angle) < -75 or int(terrain_angle) > 75:
            raise Exception("Elements in terrain_angle should be between -75 degrees and +75 degrees")
    if not (isinstance(rover, dict)):
        raise Exception("rover should have a dictionary input")
    if not (isinstance(planet, dict)):
        raise Exception("planet should have a dictionary input")
    if not(isinstance(Crr, (float, int))) or Crr <= 0:
        raise Exception("Crr should be a positive integer")
 
    # Function inputs
    Fd = F_drive(omega, rover)
    Fgt = F_gravity(terrain_angle, rover, planet)
    Frr = F_rolling(omega, terrain_angle, rover, planet, Crr)
    
    # Net force aclculations
    Fnet = Fd + Fgt + Frr
    return Fnet
    