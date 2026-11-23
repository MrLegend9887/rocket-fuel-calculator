import math
from calculations import calculate_delta_v as calculate_delta_v_formula
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

    def calculate_delta_v(self):
        delta_v = calculate_delta_v_formula(self.initial_mass(), self.final_mass(), self.isp)
        return delta_v

class Rocket:
    def __init__(self, stages):
        self.stages = stages

    def calculate_delta_v(self):
        delta_v = []
        for stage in self.stages:
            delta_v.append(stage.calculate_delta_v())
        return delta_v

# Test And Dummy Data

stage1 = RocketStage(4000, 20000, 300, 2000)
stage2 = RocketStage(2500, 10000, 340, 500)
stage3 = RocketStage(1000, 4000, 360, 100)
stages = [stage1, stage2, stage3]

rocket = Rocket(stages)

# Stages Attributes Test

print("Initial mass:", stage1.initial_mass())
print("Final mass:", stage1.final_mass())
print("Mass ratio:", stage1.mass_ratio())
print("Delta V:", stage1.calculate_delta_v())

#Rocket Class Test

print(rocket.stages)
print(len(rocket.stages))
print(rocket.stages[0].isp)

for stage in rocket.stages:
    print(stage.calculate_delta_v())

# Rocket Class Method Test

rocket.calculate_delta_v()