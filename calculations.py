import math

def calculate_mass_ratio(initial_mass, final_mass):
    if isinstance(initial_mass, bool) or isinstance(final_mass, bool):
        raise ValueError("Mass values cannot be boolean")
    if final_mass <= 0:
        raise ValueError("Final mass must be greater than 0.")
    elif initial_mass <= final_mass:
        raise ValueError("Initial mass must be greater than final mass.")
    else:
        mass_ratio = initial_mass / final_mass
    if not math.isfinite(mass_ratio):
        raise ValueError("Mass ratio must be finite")

    return mass_ratio

def calculate_delta_v(initial_mass, final_mass, isp):
    g0 = 9.80665
    if isinstance(isp, bool):
        raise ValueError("ISP cannot be boolean")
    if not math.isfinite(isp):
        raise ValueError("ISP must be finite")
    if isp <= 0:
        raise ValueError("isp should be greater than 0")
    else:
        delta_v = isp * g0 * math.log(calculate_mass_ratio(initial_mass, final_mass))
    if not math.isfinite(delta_v):
        raise ValueError("Delta V must be finite")
    return delta_v

def calculate_required_propellant(final_mass, target_delta_v, isp):
    if any(isinstance(value,bool) for value in (final_mass, target_delta_v, isp)):
        raise ValueError("Input values cannot be boolean")
    if not math.isfinite(final_mass):
        raise ValueError("Final mass must be finite")
    if not math.isfinite(target_delta_v):
        raise ValueError("Target delta V must be finite")
    if not math.isfinite(isp):
        raise ValueError("ISP must be finite")
    g0 = 9.80665
    if target_delta_v <= 0:
        raise ValueError("target delta v should be greater than 0")
    elif final_mass <= 0 :
        raise ValueError("final mass should be greater than 0")
    elif isp <= 0 :
        raise ValueError("isp should be greater than 0")
    else:
        try:
            required_propellant = final_mass * math.expm1(target_delta_v / isp / g0)
        except OverflowError:
            raise ValueError("Input Values must be finite")
        
        if not math.isfinite(required_propellant):
            raise ValueError("Required propellant mass must be finite")
        
        return required_propellant