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