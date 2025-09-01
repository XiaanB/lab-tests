"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    def __init__(self):
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []
        self.current_roll = 0  # This is unused in current logic but could track roll index

    def roll(self, pins):
        """
        Records a roll in the game.
        Args:
        pins: Number of pins knocked down in this roll
        """
        self.rolls.append(pins)
        self.current_roll += 1  # Tracking total rolls

    def score(self):
        """Calculate the score for the current game.

        ⚠️ BUG: Only scores 9 frames instead of 10.
        The loop should run 10 times (bowling has 10 frames),
        and the 10th frame requires special handling for extra rolls.
        """
        score = 0
        frame_index = 0

        # 🔴 BUG: Should be `range(10)` to include the 10th frame
        for frame in range(9):  # Only scoring 9 frames
            if self._is_strike(frame_index):
                # Strike: add 10 + next 2 rolls
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare: add 10 + next roll
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame: just sum the two rolls
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2
        return score

    def _is_strike(self, frame_index):
        """
        Check if the roll at frame_index is a strike (10 pins in one roll).
        """
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """
        Check if the sum of two rolls is a spare (exactly 10 pins over two rolls).
        """

        return (
            frame_index + 1 < len(self.rolls)
            and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10
        )

    def _strike_bonus(self, frame_index):
        """
        Bonus for a spare: the next roll.
        Assumes the roll exists — will throw IndexError if not.
        """
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        """
        Calculate the bonus for a spare.
        Args:
        frame_index: Index of the first roll in a spare
        Returns:
        The value of the roll after the spare
        """
        return self.rolls[frame_index + 2]
