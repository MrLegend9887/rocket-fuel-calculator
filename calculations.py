import math


def calculate_mass_ratio(initial_mass, final_mass):
    # Boolean values are rejected because Python treats True and False
    # as integers, which could otherwise pass numeric calculations.
    if isinstance(initial_mass, bool) or isinstance(final_mass, bool):
        raise ValueError("Mass values cannot be boolean")

    # The final mass must remain positive for the rocket equation.
    if final_mass <= 0:
        raise ValueError("Final mass must be greater than 0.")

    # A rocket must lose mass during propellant consumption, so its
    # initial mass must be greater than its final mass.
    elif initial_mass <= final_mass:
        raise ValueError("Initial mass must be greater than final mass.")

    else:
        # Mass ratio represents the rocket's initial mass divided by
        # its mass after propellant has been consumed.
        mass_ratio = initial_mass / final_mass

    # Prevent invalid numerical results such as infinity.
    if not math.isfinite(mass_ratio):
        raise ValueError("Mass ratio must be finite")

    return mass_ratio


def calculate_delta_v(initial_mass, final_mass, isp):
    # Standard gravitational acceleration at Earth's surface, in m/s².
    # This constant is used to convert specific impulse into exhaust velocity.
    g0 = 9.80665

    # Reject Boolean values before numerical validation.
    if isinstance(isp, bool):
        raise ValueError("ISP cannot be boolean")

    # Specific impulse must be a finite value.
    if not math.isfinite(isp):
        raise ValueError("ISP must be finite")

    # Specific impulse must be positive for this calculation.
    if isp <= 0:
        raise ValueError("isp should be greater than 0")

    else:
        # Tsiolkovsky's ideal rocket equation:
        # Δv = Isp × g0 × ln(initial_mass / final_mass)
        #
        # The mass ratio is calculated separately to keep the
        # mathematical logic modular and reusable.
        delta_v = isp * g0 * math.log(calculate_mass_ratio(initial_mass, final_mass))

    # Ensure the calculated delta-v is numerically valid.
    if not math.isfinite(delta_v):
        raise ValueError("Delta V must be finite")

    return delta_v


def calculate_required_propellant(final_mass, target_delta_v, isp):
    # Reject Boolean values across all inputs because bool is a subclass
    # of int in Python.
    if any(isinstance(value,bool) for value in (final_mass, target_delta_v, isp)):
        raise ValueError("Input values cannot be boolean")

    # Validate that the final mass is numerically finite.
    if not math.isfinite(final_mass):
        raise ValueError("Final mass must be finite")

    # Validate that the target delta-v is numerically finite.
    if not math.isfinite(target_delta_v):
        raise ValueError("Target delta V must be finite")

    # Validate that the specific impulse is numerically finite.
    if not math.isfinite(isp):
        raise ValueError("ISP must be finite")

    # Standard gravitational acceleration at Earth's surface, in m/s².
    g0 = 9.80665

    # The target delta-v must be positive.
    if target_delta_v <= 0:
        raise ValueError("target delta v should be greater than 0")

    # Final mass must be positive because it is the mass remaining
    # after the propellant has been consumed.
    elif final_mass <= 0:
        raise ValueError("final mass should be greater than 0")

    # Specific impulse must be positive.
    elif isp <= 0:
        raise ValueError("isp should be greater than 0")

    else:
        # Rearranged rocket equation to calculate required propellant:
        #
        # Δv = Isp × g0 × ln((final_mass + propellant) / final_mass)
        #
        # Rearranging gives:
        # propellant = final_mass × (exp(Δv / (Isp × g0)) - 1)
        #
        # expm1(x) calculates exp(x) - 1 with improved numerical
        # precision when x is very small.
        try:
            required_propellant = final_mass * math.expm1(target_delta_v / isp / g0)

        # Exponential calculations can overflow for extremely large inputs.
        # Convert that numerical failure into a controlled error.
        except OverflowError:
            raise ValueError("Input Values must be finite")

        # Ensure the resulting propellant mass is a finite number.
        if not math.isfinite(required_propellant):
            raise ValueError("Required propellant mass must be finite")

        return required_propellant