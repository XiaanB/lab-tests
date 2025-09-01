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
        """
        Calculate the total score for the game, including bonus rolls in the 10th frame.

        Returns:
            int: The total score for the current game.
        """
        score = 0
        frame_index = 0

        for frame in range(10):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
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
        bonus = 0
        if frame_index + 1 < len(self.rolls):
            bonus += self.rolls[frame_index + 1]
        if frame_index + 2 < len(self.rolls):
            bonus += self.rolls[frame_index + 2]
        return bonus

    def _spare_bonus(self, frame_index):
        if frame_index + 2 < len(self.rolls):
            return self.rolls[frame_index + 2]
        return 0
