'''Subfunctions'''
# Imports

import numpy as np
import math

rover = {
        "wheel_assembly": {
            "wheel": {
                "radius": 0.30,
                "mass": 1.0
            },
            "speed_reducer": {
                "type": "reverted",
                "diam_pinion": 0.04,
                "diam_gear": 0.07,
                "mass": 1.5
            },
            "motor": {
                "torque_stall": 170,
                "torque_noload": 0,
                "speed_noload": 3.80,
                "mass": 5.0
            }
        },
        "chassis": {
            "mass": 659
        },
        "science_payload": {
            "mass": 75
        },
        "power_subsys": {
            "mass": 90
        }
}
planet = {"g" : 3.72}

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


def F_gravity(terrangle, rov, plan):
    #Error/Exception Considerations based on inputs
    if not isinstance(terrangle,(np.ndarray, int, float, np.number)):
        raise Exception("The terrain input(s) must be a scalar or vector")
    #Checking Angle based on data type
    elif type(terrangle) is np.ndarray:
        for i in terrangle:
            if i < -75 or i > 75:
                raise Exception("The terrain angle must be between -75 and 75 degrees")
    elif type(terrangle) is not np.ndarray:
        if terrangle < -75 or terrangle > 75:
            raise Exception("The terrain angle must be between -75 and 75 degrees")
    if type(rov) is not dict or type(plan) is not dict:
        raise Exception("The rover and/or planet input must be a dictionary")
    #Calculations
    m = get_mass(rov)
    g = plan['g']
    F_gt = -m * g * np.sin(terrangle * (np.pi/180))
    return F_gt


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


from scipy.special import erf
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
    F_rr = F_rrsimp * erf(40*v) 
    return F_rr


#Ethan John 9/17/2026
#verifies input and gear type and then outputs gear ratio
def get_gear_ratio(speed_reducer):
    valid_speed_reducer = isinstance(speed_reducer, dict)
    if valid_speed_reducer == False:
        raise Exception("Invalid Input: speed reducer must be a dictionary")
    #verifies gear type
    gear = speed_reducer['type']
    if gear.lower() != "reverted":
        raise Exception("Invalid Gear Type: must be \"reverted\"")
    #computes gear ratio
    d2 = speed_reducer['diam_gear']
    d1 = speed_reducer['diam_pinion']
    Ng = (d2/d1)**2
    return Ng

def get_mass(r):
    if type(r) != dict:
        raise Exception("The input for this function must be a dictionary")
    #Wheel Mass Total
    m_wheels = 6 * r["wheel_assembly"]["wheel"]["mass"]
    #Speed Reducer Assembly Total Mass
    m_speeducers = 6 * r["wheel_assembly"]["speed_reducer"]['mass']
    #Motor Total Mass
    m_motors = 6 * r["wheel_assembly"]['motor']['mass']
    #Chassis Mass
    m_chassis = r['chassis']['mass']
    #Science Payload Mass
    m_payload = r['science_payload']['mass']
    #Power Subsystem Mass
    m_powsub = r['power_subsys']['mass']
    #Total mass
    m_total = m_wheels + m_speeducers + m_motors + m_chassis + m_payload + m_powsub
    return m_total

#Ethan John 9/17/26
#verifies input and outputs torque of the motor
def tau_dcmotor(omega, motor):
    # check if omega is a scalar or a numpy array
    valid_omega = isinstance(omega, (int, float, np.ndarray))
    # check if motor is a dictionary
    valid_motor = isinstance(motor, dict)
    if (valid_omega == False):                  
        raise Exception('Invalid Input: omega must be an array or scalar')
    elif (valid_motor == False):
        raise Exception('Invalid Input: motor must be a dictionary')
  
    tau_s = motor['torque_stall']       #shoold be 170 Nm
    tau_nl = motor['torque_noload']     #should be 0 Nm
    omega_nl = motor['speed_noload']    #should be 3.80 rad/s
    
    # real equation
    tau = tau_s - ((tau_s - tau_nl) / omega_nl) * omega

    # use np.where to apply the boundaries element-by-element
    # np.where(condition, value_if_true, value_if_false)
    tau = np.where(omega > omega_nl, 0.0, tau)
    tau = np.where(omega < 0, tau_s, tau)

    if isinstance(omega, (int, float)):
        return float(tau)
    else:
        return tau