import unittest
from models import RocketStage


class TestRocketStage(unittest.TestCase):

    def setUp(self):
        self.stage = RocketStage(
            dry_mass=4000,
            propellant_mass=20000,
            isp=300,
            payload_mass=2000
        )

    def test_initial_mass(self):
        self.assertEqual(self.stage.initial_mass(), 26000)

    def test_final_mass(self):
        self.assertEqual(self.stage.final_mass(), 6000)

    def test_mass_ratio(self):
        self.assertAlmostEqual(self.stage.mass_ratio(), 26000 / 6000)

    def test_delta_v(self):
        self.assertAlmostEqual(
            self.stage.calculate_delta_v(),
            4313.956324704918
        )

    def test_invalid_dry_mass(self):
        with self.assertRaises(ValueError):
            RocketStage(0, 20000, 300, 2000)


if __name__ == "__main__":
    unittest.main()