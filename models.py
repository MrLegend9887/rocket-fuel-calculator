class RocketStage:
    def __init__(self, dry_mass, propellant_mass, isp, payload_mass):
        self.dry_mass = dry_mass
        self.propellant_mass = propellant_mass
        self.isp = isp
        self.payload_mass = payload_mass
    

stage1 = RocketStage(4000, 20000, 300, 2000)

print(stage1.dry_mass)
print(stage1.propellant_mass)
print(stage1.isp)
print(stage1.payload_mass)