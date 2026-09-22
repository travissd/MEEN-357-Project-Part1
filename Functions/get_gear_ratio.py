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

# Based on constants in Appendix A
test_sr = {
    'type': 'reverted',
    'diam_pinion': 0.04,
    'diam_gear': 0.07,
    'mass': 1.5
}


''' Test Cases
# Test 1: Normal execution
print("Test 1 (Normal):", np.isclose(get_gear_ratio(test_sr), 3.0625))

# Test 2: Case-insensitive check
test_sr_caps = {'type': 'REvERtED', 'diam_pinion': 0.04, 'diam_gear': 0.07, 'mass': 1.5}
print("Test 2 (Caps):", np.isclose(get_gear_ratio(test_sr_caps), 3.0625))
print("Actual output:", get_gear_ratio(test_sr))
'''