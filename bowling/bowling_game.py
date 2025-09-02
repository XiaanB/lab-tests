"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    def __init__(self):
        # Initialize a new game
        # `rolls` stores the number of pins knocked down in each roll sequentially
        self.rolls = []
        # `current_roll` could track the roll number (currently unused)
        self.current_roll = 0

    def roll(self, pins):
        """
        Record a roll in the game.
        Args:
            pins (int): Number of pins knocked down in this roll.
        Raises:
            TypeError: If pins is not an integer.
            ValueError: If pins is not between 0 and 10, or frame total exceeds 10.
        """
        # Validate input
        if not isinstance(pins, int):
            raise TypeError("Pins must be an integer")
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")

        # ------------------------------
        # Determine the current frame (1-9)
        # ------------------------------
        frame = 0  # frame counter
        i = 0      # index to traverse existing rolls

        while frame < 9 and i < len(self.rolls):
            if self.rolls[i] == 10:  # strike: frame ends after 1 roll
                i += 1
            else:
                # otherwise, 2 rolls per frame
                i += 2
            frame += 1
        # At this point, `frame` is the current frame number (0-based for frames 1-9)
        # `i` points to the roll index in `self.rolls` where the current frame starts

        # ------------------------------
        # Validate the frame total (except 10th frame)
        # ------------------------------
        if frame < 9 and len(self.rolls) > 0:
            rolls_in_current_frame = []

            # Collect previous rolls in this frame to check total pins
            j = len(self.rolls) - 1
            while j >= 0 and len(rolls_in_current_frame) < 2:
                # Skip strike if it's counted as first roll, unless second roll
                if self.rolls[j] != 10 or len(rolls_in_current_frame) == 1:
                    rolls_in_current_frame.insert(0, self.rolls[j])
                j -= 1

            # If first roll already exists in frame, ensure frame total <= 10
            if len(rolls_in_current_frame) == 1 and rolls_in_current_frame[0] + pins > 10:
                raise ValueError("Frame total cannot exceed 10 pins")

        # ------------------------------
        # Record the roll
        # ------------------------------
        self.rolls.append(pins)
        # At this point:
        # - `self.rolls` contains all rolls so far
        # - Frame-tracking will continue correctly on the next call

    def score(self):
        """
        Calculate the total score for the game.
        Handles strikes and spares including bonus rolls.
        Returns:
            int: Total game score.
        """
        score = 0
        frame_index = 0

        # There are exactly 10 frames in a game
        for _ in range(10):
            if self._is_strike(frame_index):
                # Strike: 10 points + next 2 rolls as bonus
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare: 10 points + next roll as bonus
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame: sum of the two rolls
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return score

    def _is_strike(self, i):
        """
        Check if a roll is a strike.
        Args:
            i (int): Index of roll to check.
        Returns:
            bool: True if roll is a strike.
        """
        return i < len(self.rolls) and self.rolls[i] == 10

    def _is_spare(self, i):
        """
        Check if a frame is a spare.
        Args:
            i (int): Index of first roll in frame.
        Returns:
            bool: True if frame is a spare.
        """
        return i + 1 < len(self.rolls) and self.rolls[i] + self.rolls[i + 1] == 10

    def _strike_bonus(self, i):
        """
        Calculate bonus for a strike.
        Args:
            i (int): Index of strike roll.
        Returns:
            int: Sum of next two rolls.
        """
        return sum(self.rolls[i + 1:i + 3])

    def _spare_bonus(self, i):
        """
        Calculate bonus for a spare.
        Args:
            i (int): Index of first roll in spare frame.
        Returns:
            int: Next roll as bonus (0 if no roll exists).
        """
        return self.rolls[i + 2] if i + 2 < len(self.rolls) else 0
