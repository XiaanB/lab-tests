# test_bowling.py

import pytest
from bowling_game import BowlingGame  # Adjust this import if your file/class is named differently

@pytest.fixture
def game():
    return BowlingGame()

def roll_many(game, rolls, pins):
    for _ in range(rolls):
        game.roll(pins)

def roll_spare(game):
    game.roll(5)
    game.roll(5)

def roll_strike(game):
    game.roll(10)

def test_all_gutter_balls(game):
    roll_many(game, 20, 0)
    assert game.score() == 0

def test_all_ones(game):
    roll_many(game, 20, 1)
    assert game.score() == 20

def test_one_spare(game):
    roll_spare(game)        # 5 + 5
    game.roll(3)            # Bonus = 3
    roll_many(game, 17, 0)
    assert game.score() == 16  # 10 + 3 + rest 0s

def test_one_strike(game):
    roll_strike(game)       # 10
    game.roll(3)            # Bonus 1
    game.roll(4)            # Bonus 2
    roll_many(game, 16, 0)
    assert game.score() == 24  # 10 + 3 + 4 + rest 0s

def test_perfect_game(game):
    roll_many(game, 12, 10)
    assert game.score() == 300

def test_all_spares(game):
    for _ in range(10):
        roll_spare(game)
    game.roll(5)  # Bonus roll
    assert game.score() == 150

def test_strike_in_last_frame(game):
    roll_many(game, 18, 0)
    roll_strike(game)
    game.roll(10)
    game.roll(10)
    assert game.score() == 30

def test_spare_in_last_frame(game):
    roll_many(game, 18, 0)
    roll_spare(game)
    game.roll(5)
    assert game.score() == 15

def test_invalid_roll_negative(game):
    with pytest.raises(ValueError):
        game.roll(-1)

def test_invalid_roll_too_high(game):
    with pytest.raises(ValueError):
        game.roll(11)
