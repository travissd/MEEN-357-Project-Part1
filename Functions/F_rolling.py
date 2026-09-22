import numpy as np
import math
def F_rolling(ohm, terrangle, rov, plan, Crr):
    #Input Criteria Check
    if not isinstance(ohm, (np.ndarray, int, float, np.number)):
        raise Exception("The omega input(s) must be a scalar or vector")
    if not isinstance(terrangle,(np.ndarray, int, float, np.number)):
        raise Exception("The terrain input(s) must be a scalar or vector")
    elif type(terrangle) is np.ndarray:
        for i in terrangle:
            if i < -75 or i > 75:
                raise Exception("The terrain angle must be between -75 and 75 degrees")
    elif type(terrangle) is not np.ndarray:
        if terrangle < -75 or terrangle > 75:
            raise Exception("The terrain angle must be between -75 and 75 degrees")
    if type(rov) is not dict or type(plan) is not dict:
            raise Exception("The rover and/or planet input must be a dictionary.")
    if not isinstance(Crr, (int,float, np.number)) or Crr < 0:
        raise Exception("The rolling resistance coefficient must be a positive scalar.")
    #Simple Rolling Resistance Force
    m = get_mass(rov)
    g = plan['g']
    Fn = -m * g * np.cos(terrangle * (np.pi/180)) #Conversion of angle to radians
    F_rrsimp = Crr * Fn
    Ng = get_gear_ratio(rov['wheel_assembly']['speed_reducer'])
    omega_out = ohm/Ng
    r = rov["wheel_assembly"]['wheel']['radius']
    v = r * omega_out
    F_rr = F_rrsimp*math.erf(40*v)
    return F_rr


       