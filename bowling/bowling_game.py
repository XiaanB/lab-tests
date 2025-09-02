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


class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        if not isinstance(pins, int):
            raise TypeError("Pins must be an integer")
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")

        # Determine the current frame (frames 1-9)
        frame = 0
        i = 0
        while frame < 9 and i < len(self.rolls):
            if self.rolls[i] == 10:  # strike
                i += 1
            else:
                i += 2
            frame += 1

        # Check if this is the second roll in a frame and exceeds 10
        if frame < 9:
            if len(self.rolls) > 0:
                # Last roll in this frame (if not strike)
                last_roll = self.rolls[-1]
                # Only check if last roll was not a strike and we are still in the same frame
                rolls_in_current_frame = []
                j = len(self.rolls) - 1
                while j >= 0 and len(rolls_in_current_frame) < 2:
                    if self.rolls[j] != 10 or len(rolls_in_current_frame) == 1:
                        rolls_in_current_frame.insert(0, self.rolls[j])
                    j -= 1
                if len(rolls_in_current_frame) == 1 and rolls_in_current_frame[0] + pins > 10:
                    raise ValueError("Frame total cannot exceed 10 pins")

        self.rolls.append(pins)

    def score(self):
        """Calculate the total score for the game, including bonus rolls in the 10th frame."""
        score = 0
        frame_index = 0

        for _ in range(10):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += sum(self.rolls[frame_index:frame_index + 2])
                frame_index += 2

        return score

    def _is_strike(self, i):
        return i < len(self.rolls) and self.rolls[i] == 10

    def _is_spare(self, i):
        return i + 1 < len(self.rolls) and self.rolls[i] + self.rolls[i + 1] == 10

    def _strike_bonus(self, i):
        return sum(self.rolls[i + 1:i + 3])

    def _spare_bonus(self, i):
        return self.rolls[i + 2] if i + 2 < len(self.rolls) else 0

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
        """Return True if the roll at frame_index is a strike (10 pins)."""
        return self.rolls[frame_index:frame_index + 1] == [10]

    def _is_spare(self, frame_index):
        """Return True if the two rolls starting at frame_index form a spare (sum to 10)."""
        return sum(self.rolls[frame_index:frame_index + 2]) == 10 and len(self.rolls[frame_index:frame_index + 2]) == 2

    def _strike_bonus(self, frame_index):
        """Return the sum of the next two rolls after a strike (0 if missing)."""
        return sum(self.rolls[frame_index + 1: frame_index + 3])

    def _spare_bonus(self, frame_index):
        """Return the next roll after a spare (0 if missing)."""
        return self.rolls[frame_index + 2] if frame_index + 2 < len(self.rolls) else 0
