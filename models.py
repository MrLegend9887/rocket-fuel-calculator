
import math
from calculations import calculate_delta_v as calculate_delta_v_formula
from calculations import calculate_required_propellant as calculate_required_propellant


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

    def calculate_required_propellant(self, target_delta_v):
        required_propellant = calculate_required_propellant(self.final_mass(), target_delta_v, self.isp)
        return required_propellant


class Rocket:
    def __init__(self, stages, payload_mass):
        self.stages = stages
        self.payload_mass = payload_mass
        self.validateValue()

    def validateValue(self):
        if isinstance(self.payload_mass, bool):
            raise TypeError("Boolean values are not allowed")
        elif not isinstance(self.payload_mass, (int,float)):
            raise TypeError("all entered value must be numeric")
        elif not isinstance(self.stages, list):
            raise TypeError("stages must be list")
        elif self.stages == []:
            raise ValueError("Stages cannot be empty")
        elif not math.isfinite(self.payload_mass):
            raise ValueError("all entered value must be numeric")
        elif self.payload_mass < 0:
            raise ValueError("payload mass cannot be negative")
        elif any(not isinstance(value,RocketStage) for value in self.stages):
            raise TypeError("Every element of stages must be a instance of RocketStage class")

    def calculate_delta_v(self):
        delta_v = []
        for stage in self.stages:
            delta_v.append(stage.calculate_delta_v())
        return delta_v

    def total_delta_v(self):
        total_delta_v = 0
        delta_v = self.calculate_delta_v()
        for stage_delta_v in delta_v:
            total_delta_v += stage_delta_v
        return total_delta_v

    def calculate_payload(self):
        stages = self.stages
        stages_payload = []
        for i in range(len(stages)):
            stage_payload = 0
            for k in range(i + 1, len(stages)):
                stage_payload += stages[k].dry_mass + stages[k].propellant_mass
            stage_payload += self.payload_mass
            stages_payload.append(stage_payload)
            self.stages[i].payload_mass = stages_payload[i]
        return stages_payload

stage1 = RocketStage(4000, 20000, 300, 0)
stage2 = RocketStage(2500, 10000, 340, 0)
stage3 = RocketStage(1000, 4000, 360, 0)

stages = [stage1, stage2, stage3]

rocket = Rocket(stages, 100)
