import unittest
from dungeongame import Dungeon, Monster

class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.dungeon = Dungeon()

    def test_initial_dungeon(self):
        self.assertIsNotNone(self.dungeon.player)
        self.assertEqual(self.dungeon.turn, 0)

    def test_combat_scenario(self):
        monster = Monster(name="Goblin", level=1, base_hp=30, base_attack=5)
        result = self.dungeon.dungeoncombat(monster, floor=1)
        self.assertTrue(result or not self.dungeon.player.hp > 0)

    def test_clear_floor(self):
        initial_score = self.dungeon.player.score
        self.dungeon.clear_floor(floor=1)
        self.assertEqual(self.dungeon.player.score, initial_score + 1)
        self.assertGreater(self.dungeon.player.gold, 0)

if __name__ == '__main__':
    unittest.main()

