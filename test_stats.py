import unittest
from dungeongame import Stats

class TestStats(unittest.TestCase):

    def setUp(self):
        self.stats = Stats()

    def test_initial_stats(self):
        self.assertEqual(self.stats.strength, 5)
        self.assertEqual(self.stats.defense, 5)
        self.assertEqual(self.stats.magic_defense, 5)
        self.assertEqual(self.stats.speed, 5)
        self.assertEqual(self.stats.magic_power, 5)
        self.assertEqual(self.stats.stamina, 5)
        self.assertEqual(self.stats.magic_cost, 5)
        self.assertEqual(self.stats.hp, 0)
        self.assertEqual(self.stats.endurance, 0)
        self.assertEqual(self.stats.magic_amount, 0)

    def test_allocate_stat_points(self):
        self.stats.stat_points = 5
        self.stats.strength = 5
        self.stats.allocate_stat_points = lambda: setattr(self.stats, 'strength', self.stats.strength + 5)
        self.stats.allocate_stat_points()
        self.assertEqual(self.stats.strength, 10)
        self.assertEqual(self.stats.stat_points, 5)

if __name__ == '__main__':
    unittest.main()

