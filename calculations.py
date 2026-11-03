import math

def calculate_mass_ratio(initial_mass, final_mass):
    if final_mass <= 0:
        raise ValueError("Final mass must be greater than 0.")
    elif initial_mass <= final_mass:
        raise ValueError("Initial mass must be greater than final mass.")
    else:
        mass_ratio = initial_mass / final_mass
        return mass_ratio

def calculate_delta_v(initial_mass, final_mass, isp):
    g0 = 9.80665
    if isp <= 0:
        raise ValueError("isp should be greater than 0")
    else:
        delta_v = isp * g0 * math.log(calculate_mass_ratio(initial_mass, final_mass))
        return delta_v

def calculate_required_propellant(final_mass, target_delta_v, isp):
    g0 = 9.80665
    if target_delta_v <= 0:
        raise ValueError("target delta v should be greater than 0")
    elif final_mass <= 0 :
        raise ValueError("final mass should be greater than 0")
    elif isp <= 0 :
        raise ValueError("isp should be greater than 0")
    else:
        required_propellant = final_mass * math.expm1(target_delta_v / (isp * g0))
        
        return required_propellant
    
print(calculate_required_propellant(13000, 4000, 350))