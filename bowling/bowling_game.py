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
        if not isinstance(pins, int):
            raise TypeError("Pins must be an integer")
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")

        frame = 0
        i = 0

        # Determine current frame based on rolls so far
        while frame < 9 and i < len(self.rolls):
            if self.rolls[i] == 10:
                i += 1
            else:
                i += 2
            frame += 1

        # ❗ Only validate rolls in frames 1–9
        if frame < 9:
            frame_roll_count = 0
            frame_start = 0
            j = 0
            while frame_roll_count < frame and j < len(self.rolls):
                if self.rolls[j] == 10:
                    j += 1
                else:
                    j += 2
                frame_roll_count += 1
            frame_start = j

            # If one roll already in current frame and not a strike
            if len(self.rolls) > frame_start:
                first_roll = self.rolls[frame_start]
                if first_roll != 10 and first_roll + pins > 10:
                    raise ValueError("Frame total cannot exceed 10 pins")

        # ✅ No validation in 10th frame — bonus rolls allowed
        self.rolls.append(pins)

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
