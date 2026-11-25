import unittest
from calculations import (
    calculate_mass_ratio,
    calculate_delta_v,
    calculate_required_propellant
)


class TestMassRatio(unittest.TestCase):

    def test_mass_ratio_calculation(self):
        result = calculate_mass_ratio(100, 20)
        self.assertEqual(result, 5.0)

    def test_invalid_mass_ratio(self):
        with self.assertRaises(ValueError):
            calculate_mass_ratio(20, 20)


class TestDeltaV(unittest.TestCase):

    def test_delta_v_calculation(self):
        result = calculate_delta_v(100, 20, 300)
        self.assertAlmostEqual(result, 4734.95829119156)

    def test_invalid_isp(self):
        with self.assertRaises(ValueError):
            calculate_delta_v(100, 20, 0)


class TestRequiredPropellant(unittest.TestCase):

    def test_required_propellant_calculation(self):
        result = calculate_required_propellant(100, 1000, 300)
        self.assertAlmostEqual(result, 40.481469488507344)

    def test_invalid_target_delta_v(self):
        with self.assertRaises(ValueError):
            calculate_required_propellant(100, 0, 300)


if __name__ == "__main__":
    unittest.main()