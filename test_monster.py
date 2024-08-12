import unittest
from dungeongame import Monster, Player, SpecialAbility, fire_breath

class TestMonster(unittest.TestCase):

    def setUp(self):
        self.monster = Monster(name="Goblin", level=1, base_hp=30, base_attack=5)
        self.player = Player()

    def test_initial_attributes(self):
        self.assertEqual(self.monster.name, "Goblin")
        self.assertEqual(self.monster.hp, 30)
        self.assertEqual(self.monster.attack, 5)
        self.assertEqual(self.monster.level, 1)

    def test_take_turn_attack(self):
        initial_hp = self.player.hp
        self.monster.take_turn(self.player)
        self.assertLess(self.player.hp, initial_hp)

    def test_take_turn_special_ability(self):
        special_ability = SpecialAbility(name="Fire Breath", effect=fire_breath)
        self.monster.abilities = [special_ability]
        self.monster.take_turn(self.player)
        self.assertTrue(self.player.hp < self.player.max_hp or self.player.is_burning)

if __name__ == '__main__':
    unittest.main()

