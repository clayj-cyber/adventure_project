import unittest
from copy import deepcopy

# Assuming Dungeon, Player, GameStateNode, etc. are imported from your main game module

class TestDungeonSaveLoad(unittest.TestCase):
    
    def setUp(self):
        self.dungeon = Dungeon()
        self.dungeon.player.hp = 100  # Set some initial state
        self.dungeon.player.gold = 50
        self.dungeon.player.stats.strength = 10
        self.dungeon.save_game()

    def test_save_and_load_game_state(self):
        # Modify the player's state
        self.dungeon.player.hp = 75
        self.dungeon.player.gold = 100
        self.dungeon.player.stats.strength = 15
        self.dungeon.save_game()

        # Load the previous state and check if it matches the original state
        self.dungeon.load_game()  # Should load the last state
        self.assertEqual(self.dungeon.player.hp, 75)
        self.assertEqual(self.dungeon.player.gold, 100)
        self.assertEqual(self.dungeon.player.stats.strength, 15)

        # Load the state before the last and check if it matches the initial state
        self.dungeon.load_game()  # Load from the left branch (initial state)
        self.assertEqual(self.dungeon.player.hp, 100)
        self.assertEqual(self.dungeon.player.gold, 50)
        self.assertEqual(self.dungeon.player.stats.strength, 10)

    def test_invalid_load(self):
        # Try to load from a non-existing branch and ensure it handles gracefully
        self.dungeon.load_game()  # Should load the last state
        self.dungeon.load_game()  # Should attempt to load from non-existent left branch (or right)
        self.dungeon.load_game()  # Now should load the existing state

        # Since only one state exists on the left, the hp should remain the same
        self.assertEqual(self.dungeon.player.hp, 100)

    def test_multiple_saves_and_loads(self):
        # Save multiple states and then load them in reverse order
        self.dungeon.player.hp = 90
        self.dungeon.save_game()

        self.dungeon.player.hp = 80
        self.dungeon.save_game()

        # Load the most recent state
        self.dungeon.load_game()
        self.assertEqual(self.dungeon.player.hp, 80)

        # Load the previous state
        self.dungeon.load_game()
        self.assertEqual(self.dungeon.player.hp, 90)

        # Load the initial state
        self.dungeon.load_game()
        self.assertEqual(self.dungeon.player.hp, 100)


if __name__ == '__main__':
    unittest.main()

