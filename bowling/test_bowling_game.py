
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

    def test_TC02_spare(self):
        self.roll_spare()
        self.game.roll(5)
        self.roll_many(17, 0)
        self.assertEqual(self.game.score(), 20)

    def test_TC03_strike(self):
        self.roll_strike()
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(16, 0)
        self.assertEqual(self.game.score(), 24)

    def test_TC04_two_strikes(self):
        self.roll_strike()
        self.roll_strike()
        self.game.roll(4)
        self.game.roll(2)
        self.roll_many(14, 0)
        self.assertEqual(self.game.score(), 46)


if __name__ == '__main__':
    unittest.main()
