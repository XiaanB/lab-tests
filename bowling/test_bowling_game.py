
import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, rolls, pins):
        for _ in range(rolls):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)

    def test_TC01_open_frame(self):
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(18, 0)
        self.assertEqual(self.game.score(), 7)


if __name__ == '__main__':
    unittest.main()
