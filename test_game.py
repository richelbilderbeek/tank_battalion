import unittest
from game import *
from direction import Direction
from key import Key

# Tests the Game class
class TestGame(unittest.TestCase):

    def test_default_construction(self):
        game = Game()
        self.assertEqual(0, game.get_player().get_dx())
        self.assertEqual(0, len(game.get_keys_pressed()))

    def test_default_construction(self):
        game = Game()
        self.assertFalse(game.get_quit())
        game.set_quit(True)
        self.assertTrue(game.get_quit())

    def test_add_key(self):
        game = Game()
        self.assertEqual(0, len(game.get_keys_pressed()))
        game.add_key(Key.DOWN)
        self.assertEqual(1, len(game.get_keys_pressed()))

