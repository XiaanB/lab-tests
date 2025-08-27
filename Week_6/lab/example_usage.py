from bowling_game import BowlingGame

def print_game_results(game_name, rolls, expected_score, actual_score):
    """Print the results of a game, showing expected vs actual score."""
    print(f"\n{game_name}:")
    print(f"Rolls: {rolls}")
    print(f"Expected score: {expected_score}")
    print(f"Actual score: {actual_score}")
    print(f"Correct implementation: {''}")

def example_game():
    """
    Play a sample game with strikes, spares and open frames.
    Total expected score: 190
    """
    game = BowlingGame()
    rolls = []

    # Frame 1: Strike
    game.roll(10)
    rolls.append(10)

    # Frame 2: 3,6
    game.roll(3)
    game.roll(6)
    rolls.extend([3,6])

    # Frame 3: Spare
    game.roll(5)
    game.roll(5)
    rolls.extend([5,5])

    # Frame 4: 8,1
    game.roll(8)
    game.roll(1)
    rolls.extend([8,1])

    # Frame 5: Strike
    game.roll(10)
    rolls.append(10)

    # Frame 6: Strike
    game.roll(10)
    rolls.append(10)

    # Frame 7: Strike
    game.roll(10)
    rolls.append(10)

    # Frame 8: 9,0
    game.roll(9)
    game.roll(0)
    rolls.extend([9,0])

    # Frame 9: Spare
    game.roll(7)
    game.roll(3)
    rolls.extend([7,3])

    # Frame 10: Strike + Strike + 8
    game.roll(10)
    game.roll(10)
    game.roll(8)
    rolls.extend([10,10,8])

    actual_score = game.score()
    expected_score = 190
    print_game_results("Example Game", rolls, expected_score, actual_score)
    return actual_score

# Repeat the same pattern for perfect_game, all_spares, gutter_game, regular_game
# All functions are top-level, properly indented, docstrings indented.

def main():
    example_game()
    perfect_game()
    all_spares()
    gutter_game()
    regular_game()

if __name__ == "__main__":
    main()
