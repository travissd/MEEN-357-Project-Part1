# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:29:53 2026

@author: tomis
"""
# Imports

import numpy as np

# Overal function

def F_drive(omega, rover):
    
    #Test Inputs
    
    if not (isinstance(omega, np.ndarray) or isinstance(omega, (int, float))):        
        raise Exception("Omega must be an array")
    if not isinstance(rover, dict):
        raise Exception("Rover must be a dictionary")
    
    #Inputs from library
    
    r = rover['wheel_assembly']['wheel']['radius']
    speed_reducer = rover['wheel_assembly']['speed_reducer']
    motor = rover['wheel_assembly']['motor']
    
    #Function calls
    
    Ng = get_gear_ratio(speed_reducer)
    tau = tau_dcmotor(omega, motor)
    
    #Calculations
    
    Fd = 6*tau*Ng/r
    return Fd

