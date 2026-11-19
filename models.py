import math
class RocketStage:
    def __init__(self, dry_mass, propellant_mass, isp, payload_mass):
        self.dry_mass = dry_mass
        self.propellant_mass = propellant_mass
        self.isp = isp
        self.payload_mass = payload_mass
        self.valueValidate()
    
    def valueValidate(self):
        if any(isinstance(value, bool) for value in (self.dry_mass, self.propellant_mass, self.isp, self.payload_mass)):
            raise TypeError("Boolean values are not allowed")
        if not isinstance(self.dry_mass, (int,float)) or not isinstance(self.propellant_mass, (int,float)) or not isinstance(self.isp, (int,float)) or not isinstance(self.payload_mass, (int,float)):
            raise TypeError("all entered value must be numeric")
        elif not math.isfinite(self.dry_mass) or not math.isfinite(self.propellant_mass) or not math.isfinite(self.isp) or not math.isfinite(self.payload_mass):
            raise ValueError("all entered value must be numeric")
        elif self.dry_mass <= 0:
            raise ValueError("dry mass cannot be zero or negative")
        elif self.propellant_mass <= 0:
            raise ValueError("propellant cannot be zero or negative")
        elif self.isp <= 0:
            raise ValueError("isp cannot be zero or negative")
        elif self.payload_mass < 0:
            raise ValueError("payload cannot be negative")

    def initial_mass(self):
        initial_mass = self.dry_mass + self.propellant_mass + self.payload_mass
        return initial_mass

    def final_mass(self):
        final_mass = self.dry_mass + self.payload_mass 
        return final_mass

    def mass_ratio(self):
        initial_mass = self.initial_mass()
        final_mass = self.final_mass()
        return initial_mass / final_mass
    
stage1 = RocketStage(4000, 20000, 300, 2000)
print("Initial mass:", stage1.initial_mass())
print("Final mass:", stage1.final_mass())
print("Mass ratio:", stage1.mass_ratio())