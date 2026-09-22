import numpy as np
def F_gravity(terrangle, rov, plan):
    #Error/Exception Considerations based on inputs
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
        raise Exception("The rover and/or planet input must be a dictionary")
    #Sum bro
    m = get_mass(rov)
    g = plan['g']
    F_gt = -m * g * np.sin(terrangle * (np.pi/180))
    return F_gt
'''def get_mass(r):
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
planet = {
        "g": 3.72
    }
terrain_angles = np.array([-75, -45, -30, -10, 0, 10, 30, 45, 75]) #Positive Angle results in negative force
print(type(terrain_angles))
F = F_gravity(terrain_angles, rover, planet)
print(F)
''' 