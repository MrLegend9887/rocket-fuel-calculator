import math
from calculations import calculate_delta_v as calculate_delta_v_formula
from calculations import calculate_required_propellant as calculate_required_propellant


class RocketStage:
    # Represents a single rocket stage and stores its physical properties.
    def __init__(self, dry_mass, propellant_mass, isp, payload_mass):
        self.dry_mass = dry_mass
        self.propellant_mass = propellant_mass
        self.isp = isp
        self.payload_mass = payload_mass

        # Validate the stage data immediately so an invalid object cannot
        # be initialized successfully.
        self.validate_values()

    def validate_values(self):
        # Boolean values are technically integers in Python, so they must be
        # rejected explicitly before performing numeric type validation.
        if any(isinstance(value, bool) for value in (self.dry_mass, self.propellant_mass, self.isp, self.payload_mass)):
            raise TypeError("Boolean values are not allowed")

        # Ensure all physical inputs are numeric before performing calculations.
        if not isinstance(self.dry_mass, (int,float)) or not isinstance(self.propellant_mass, (int,float)) or not isinstance(self.isp, (int,float)) or not isinstance(self.payload_mass, (int,float)):
            raise TypeError("all entered value must be numeric")

        # Reject NaN and infinite values because they can produce unreliable
        # results during mathematical calculations.
        elif not math.isfinite(self.dry_mass) or not math.isfinite(self.propellant_mass) or not math.isfinite(self.isp) or not math.isfinite(self.payload_mass):
            raise ValueError("all entered value must be numeric")

        # A stage must have positive dry mass, propellant mass and specific impulse.
        elif self.dry_mass <= 0:
            raise ValueError("dry mass cannot be zero or negative")
        elif self.propellant_mass <= 0:
            raise ValueError("propellant cannot be zero or negative")
        elif self.isp <= 0:
            raise ValueError("isp cannot be zero or negative")

        # Payload can be zero, but it cannot be negative.
        elif self.payload_mass < 0:
            raise ValueError("payload cannot be negative")

    def initial_mass(self):
        # Initial mass includes the stage structure, its propellant and
        # the payload carried before the stage begins its burn.
        initial_mass = self.dry_mass + self.propellant_mass + self.payload_mass

        # Guard against overflow caused by adding extremely large mass values.
        if not math.isfinite(initial_mass):
            raise ValueError("Initial mass must be finite")

        return initial_mass

    def final_mass(self):
        # After the propellant is consumed, the remaining mass consists of
        # the dry structure and the payload carried by this stage.
        final_mass = self.dry_mass + self.payload_mass

        # Guard against overflow in the final mass calculation.
        if not math.isfinite(final_mass):
            raise ValueError("Final mass must be finite")

        return final_mass

    def mass_ratio(self):
        # The rocket equation uses the ratio of initial mass to final mass.
        initial_mass = self.initial_mass()
        final_mass = self.final_mass()
        mass_ratio = initial_mass / final_mass

        # Ensure the calculated ratio is numerically valid.
        if not math.isfinite(mass_ratio):
            raise ValueError("Mass ratio must be finite")

        return mass_ratio

    def calculate_delta_v(self):
        # Delegate the rocket equation calculation to the calculation module.
        # This keeps mathematical logic separate from the stage data model.
        delta_v = calculate_delta_v_formula(self.initial_mass(), self.final_mass(), self.isp)
        return delta_v

    def calculate_required_propellant(self, target_delta_v):
        # Estimate the propellant needed to achieve a target delta-v using
        # the current stage's final mass and specific impulse.
        required_propellant = calculate_required_propellant(self.final_mass(), target_delta_v, self.isp)
        return required_propellant


class Rocket:
    # Represents a complete rocket composed of multiple stages and a payload.
    def __init__(self, stages, payload_mass):
        self.stages = stages
        self.payload_mass = payload_mass
        self.validate_values()

    def validate_values(self):
        # Reject Boolean payload values because bool is a subclass of int.
        if isinstance(self.payload_mass, bool):
            raise TypeError("Boolean values are not allowed")

        # The payload must be a numeric value.
        elif not isinstance(self.payload_mass, (int,float)):
            raise TypeError("all entered value must be numeric")

        # The rocket must receive its stages as a list.
        elif not isinstance(self.stages, list):
            raise TypeError("stages must be list")

        # A rocket cannot be constructed without at least one stage.
        elif self.stages == []:
            raise ValueError("Stages cannot be empty")

        # Reject infinite or NaN payload values.
        elif not math.isfinite(self.payload_mass):
            raise ValueError("all entered value must be numeric")

        # The total payload mass cannot be negative.
        elif self.payload_mass < 0:
            raise ValueError("payload mass cannot be negative")

        # Ensure the list contains RocketStage objects rather than
        # unrelated objects that do not support the expected methods.
        elif any(not isinstance(value,RocketStage) for value in self.stages):
            raise TypeError("Every element of stages must be a instance of RocketStage class")

    def calculate_delta_v(self):
        # Calculate the delta-v of every stage individually and collect
        # the results in a list in the same order as the stages.
        delta_v = []
        for stage in self.stages:
            delta_v.append(stage.calculate_delta_v())
        return delta_v

    def total_delta_v(self):
        # Obtain the individual stage delta-v values before summing them.
        total_delta_v = 0
        delta_v = self.calculate_delta_v()

        # Under the ideal model, stage delta-v values are additive.
        for stage_delta_v in delta_v:
            total_delta_v += stage_delta_v
        return total_delta_v

    def calculate_payload(self):
        # Determine how much mass each stage must carry.
        # Upper stages, their propellant and the final payload are carried
        # by the stages below them during their respective burns.
        stages = self.stages
        stages_payload = []

        for i in range(len(stages)):
            stage_payload = 0

            # Calculate the mass of all stages positioned above the current stage.
            for k in range(i + 1, len(stages)):
                stage_payload += stages[k].dry_mass + stages[k].propellant_mass

            # The final payload is carried by every stage.
            stage_payload += self.payload_mass
            stages_payload.append(stage_payload)

            # Update the RocketStage object with the mass it must carry.
            self.stages[i].payload_mass = stages_payload[i]

        return stages_payload