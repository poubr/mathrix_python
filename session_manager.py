"""Class for creating and managing the practice session."""

from random import choice


class SessionManager:
    """
    Generates exercises for the practice session.
    Args: user_session: dictionary containing user configuration.
    """
    def __init__(self, user_configuration: dict) -> None:
        self.session_length = user_configuration["session_length"]
        self.list_of_operations = user_configuration["list_of_operations"]
        self.difficulty = user_configuration["difficulty"]
        self.exercises = None
        # # {'session_length': 10, 'list_of_operations': ['addition', 'subtraction'], 'difficulty': 100}

    def generate_exercises(self):
        """Wrapper method for generating exercises."""
        exercises_per_operation = self.get_exercises_per_operations()
        print(exercises_per_operation)

    def get_exercises_per_operations(self) -> dict:
        """
        Method which generates how many exercises per operations.
        First assigns an even number of exercises to each,
        and in case of a remainder, evenly distributes it.
        """

        exercises_per_operation = {}
        for operation in self.list_of_operations:
            exercises_per_operation[operation] = self.session_length // len(self.list_of_operations)

        remainder = self.session_length % len(self.list_of_operations)
        for _ in range(0, remainder):
            operation = choice(self.list_of_operations)
            exercises_per_operation[operation] += 1

        return exercises_per_operation
