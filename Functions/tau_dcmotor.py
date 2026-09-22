
import numpy as np

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

''' This is a test for tau_dcmotor
# Based on constants in Appendix A
test_motor = {
    'torque_stall': 170.0,
    'torque_noload': 0.0,
    'speed_noload': 3.80,
    'mass': 5.0 
}
# Test 1: Normal Scalar
print("Test 1 (Normal):", tau_dcmotor(1.9, test_motor) == 85.0)

# Test 2: Negative Speed
print("Test 2 (Negative):", tau_dcmotor(-2.5, test_motor) == 170.0)

# Test 3: Overspeed
print("Test 3 (Overspeed):", tau_dcmotor(5.0, test_motor) == 0.0)

# Test 4: Vectorized
omega_array = np.array([-1.0, 0.0, 1.9, 3.80, 5.5])
expected_array = np.array([170.0, 170.0, 85.0, 0.0, 0.0])
result_array = tau_dcmotor(omega_array, test_motor)
print("Test 4 (Vector):", np.allclose(result_array, expected_array))
'''