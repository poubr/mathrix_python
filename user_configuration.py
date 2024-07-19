"""Module for retrieving user input."""


def get_user_input() -> dict:
    """Retrieves the configs for the practice session via user input."""

    session_length = get_session_length()
    if session_length == 0:
        return {}

    list_of_operations = get_operations_list()
    if not list_of_operations:
        return {}

    difficulty = get_session_difficulty()
    if difficulty == 0:
        return {}

    user_configuration = {
        "session_length": session_length,
        "list_of_operations": list_of_operations,
        "difficulty": difficulty
    }

    return user_configuration


def get_session_length() -> int:
    """Retrieves session length from user input. Asks once before offering option to quit."""
    print("First, choose how many exercises you would like to do.")
    for i in range(4):
        prompt = "Enter 5, 10, or 15: "
        if i > 0:
            prompt = f"{prompt[:-2]}, or 'Q to quit: "
        user_input = input(prompt)
        if user_input in ["5", "10", "15"]:
            return int(user_input)
        elif i > 0 and user_input.lower() == "q":
            print("Ending session.")
            return 0
        elif i == 3:
            print("It seems you don't want to practice math today! Exiting...")
        else:
            print("Please insert a valid answer.")
    return 0


def get_operations_list() -> list:
    """Retrieves the list of operations from user input."""
    print("Next, what operations would you like to include? Type 'Y' to choose or 'N' to skip: ")
    available_operations = ["Addition", "Subtraction", "Multiplication", "Division"]
    user_operations = []

    for operation in available_operations:
        for i in range(4):
            prompt = f"{operation} Y/N: "
            if i > 0:
                prompt = f"Type 'Y' to choose {operation.lower()}, 'N' to skip {operation.lower()}, or 'q' to quit: "
            user_input = input(prompt)
            if user_input.lower() == "y":
                user_operations.append(operation.lower())
                break
            elif user_input.lower() == "n" or i == 3:
                print(f"Skipping {operation.lower()}.")
                break
            elif i > 0 and user_input.lower() == "q":
                print("Ending session.")
                return []
            else:
                print("Please insert a valid answer.")
    if not user_operations:
        print("You haven't selected anything to practice! Exiting...")

    mapped_user_operations = convert_operations_input(user_operations)

    return mapped_user_operations


def get_session_difficulty() -> int:
    """Retrieves session difficulty from user input, returns an empty string if answer was not provided."""
    print("Got it! Finally, choose your difficulty: Beginner, Intermediate, or Expert?")

    for i in range(4):
        prompt = "Type 'B', 'I', or 'E': "
        if i > 0:
            prompt = f"{prompt[:-2]}, or 'Q to quit: "
        user_input = input(prompt)
        if user_input.lower() in ["b", "i", "e"]:
            difficulty = convert_difficulty_input(user_input.lower())
            return difficulty
        elif i > 0 and user_input.lower() == "q":
            print("Ending session.")
            return 0
        elif i == 3:
            print("It seems you don't want to practice math today! Exiting...")
        else:
            print("Please insert a valid answer.")
    return 0


def convert_difficulty_input(user_input: str) -> int:
    """Converts the alphabetic input to a corresponding integer.
    'b' (beginner) == calculations within 20
    'i' (intermediate) == calculations within 100
    'e' (expert) == calculations within 1000
    """
    difficulty_mapping = {
        "b": 20,
        "i": 100,
        "e": 1000
    }

    return difficulty_mapping[user_input]


def convert_operations_input(operations: list) -> list:
    """Converts the operations from tokens to the corresponding symbols."""

    operations_mapping = {
        "addition": "+",
        "subtraction": "-",
        "multiplication": "*",
        "division": "/"
    }

    mapped_operations = [operations_mapping[operation] for operation in operations]

    return mapped_operations
