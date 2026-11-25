import unittest
from models import Rocket, RocketStage


class TestRocket(unittest.TestCase):

    def setUp(self):
        self.stage1 = RocketStage(4000, 20000, 300, 0)
        self.stage2 = RocketStage(1000, 5000, 350, 0)
        self.rocket = Rocket([self.stage1, self.stage2], 100)

    def test_rocket_stage_count(self):
        self.assertEqual(len(self.rocket.stages), 2)

    def test_total_delta_v(self):
        self.rocket.calculate_payload()
        result = self.rocket.total_delta_v()
        self.assertGreater(result, 0)

    def test_calculate_payload(self):
        result = self.rocket.calculate_payload()
        self.assertEqual(result, [6100, 100])

    def test_empty_stages(self):
        with self.assertRaises(ValueError):
            Rocket([], 100)


if __name__ == "__main__":
    unittest.main()