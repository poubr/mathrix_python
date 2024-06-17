"""Module for retrieving user input."""

from time import sleep


def get_user_input() -> dict:
    """Retrieves the configs for the practice session via user input."""

    print("Hello and welcome to ....")
    sleep(1)
    print('''                                  
     ##   ##   ##   ##### #    # #####  # #    # 
     # # # #  #  #    #   #    # #    # #  #  #  
     #  #  # #    #   #   ###### #    # #   ##   
     #     # ######   #   #    # #####  #   ##   
     #     # #    #   #   #    # #   #  #  #  #  
     #     # #    #   #   #    # #    # # #    # 
    ''')
    sleep(1)
    print("Mathrix, an app for practicing math.")
    sleep(1)
    print("Let's start!")
    print("First, choose how many exercises you would like to do.")

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

    print("Now let's practice!")
    sleep(1)
    print("Sorry, no math coded yet. Here's a cookie instead:")
    sleep(1)
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡶⠾⠟⠻⠶⣶⣤⣤⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣾⠋⠁⢀⣠⣤⣤⣀⠀⠉⠛⠛⠛⠛⠛⠛⠿⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⡶⠿⠿⠟⠛⠋⠁⠀⣰⣿⣟⣋⣻⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠬⣝⣻⣿⡷⠶⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⡏⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠳⢶⣬⣍⠛⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠟⢫⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣦⡘⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡾⢋⣥⣴⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⠏⣠⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡾⠃⣴⡿⠁⠀⠀⠀⠀⠀⢠⣶⣿⣿⢷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣯⠈⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⢿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡞⢀⣼⡟⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣄⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣷⣾⣿⡆⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢢⠘⢿⣦⡀⠀
⠀⠀⠀⠀⣴⠏⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣷⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠛⠿⣿⡿⠗⠀⠀⠀⢀⣴⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⣧⠘⣿⣷⠀
⠀⠀⢠⣾⠏⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡿⣛⣿⣿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡟⠙⣿⡇⠀⠀⠀⠀⢸⡇⣿⣿⠀
⠀⢠⣾⡏⠰⠁⠀⠀⠀⠀⣀⡄⠀⠀⠀⠀⠀⠀⠀⠋⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢀⣿⠁⣿⣇⠀
⠀⢸⣿⠀⠀⢠⡄⣀⣴⡿⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠿⣿⠿⠟⠁⠀⠀⠀⠀⠸⣿⡄⣿⣿⠀
⠀⢸⡏⠀⠀⠘⢿⣿⣿⣧⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⡼⣿⣇
⠀⣸⠇⠀⠀⠀⠈⢿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡷⣄⠀⠀⠀⠀⠀⠀⢀⣤⠀⢄⠀⢸⣿
⢀⡏⢠⠀⠀⠀⠀⠈⠻⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣏⠙⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠻⣿⣿⣿⣿⣿⡇⣼⠀⠀⠀⠀⠀⣴⣿⣿⡇⢸⡆⠀⣿
⣸⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣀⣀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣆⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⣸⣿⣿⣿⡿⠴⠃⠀⠀⠀⢠⡾⢻⣿⣿⡇⢀⡇⢀⣿
⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡟⠻⣷⡄⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⡿⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠐⠟⢷⣾⣿⣿⡇⢸⡇⣼⡟
⢹⣧⢻⣆⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣿⣿⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣛⣫⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⢠⡿⣹⡟⠀
⠀⢿⣎⢿⣦⣄⣠⣄⣀⣀⡀⠘⢿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⣵⡿⠀⠀
⠀⠈⢿⣦⣴⣿⣿⣮⣵⣿⣿⣷⣤⣽⣿⣟⡋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠇⣼⣿⡇⠀⠀
⠀⠀⠀⠻⠿⣛⣉⠙⢿⡿⠋⠉⠻⡿⠿⢿⣿⣿⣦⣄⡀⠀⠀⢀⣠⣤⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡏⢸⣿⡿⠃⠀⠀
⠀⠀⠀⠀⠀⢘⡻⣷⠌⠀⠀⠿⠿⠀⠀⠀⠿⠟⠻⣿⡿⠆⠀⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⡹⣿⡆⠀⠀⠀⠀⣠⢞⣼⣿⠃⣼⣿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣦⠘⣿⣿⣿⣿⣿⠟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣷⣾⡇⠀⠀⠀⣻⣷⣿⠟⢁⣼⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡿⠀⢟⠿⣿⣿⣯⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡿⢿⣿⠿⣿⠅⠀⢀⣾⣿⠟⣁⣴⣿⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠾⣷⣄⠈⠛⠶⠭⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠒⠛⠁⠀⢀⣼⡿⢣⣾⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣼⠄⢻⣿⠇⠀⠀⠀⠀⠀⠀⢀⣤⣤⡤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⢡⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠳⣿⣟⣀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣄⣾⣿⣧⠀⠀⣀⣀⣠⣴⣫⣾⡿⠿⠿⠿⠛⠛⣡⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣏⣷⣖⣒⣄⣚⠏⣿⣿⣿⣿⣿⣿⡟⢀⣾⠿⣛⡛⢛⣋⣥⣤⣴⣶⣶⣶⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣅⣿⣿⡛⢛⣛⣛⣓⡮⠻⠿⠿⠟⠋⢴⣋⣤⣯⣽⣶⣿⣿⡿⠟⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡿⣿⡟⠻⢿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⠿⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

    return user_configuration


def get_session_length() -> int:
    """Retrieves session length from user input. Asks once before offering option to quit."""
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
    print("Next, what operations would you like to include? Type 'Y' or 'N' to all that apply:")
    available_operations = ["Addition", "Subtraction", "Multiplication", "Division"]
    user_operations = []

    for operation in available_operations:
        for i in range(4):
            prompt = f"{operation} Y/N: "
            if i > 0:
                prompt = f"Type 'N' to choose {operation.lower()}, 'N' to skip {operation.lower()}, or 'q' to quit: "
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

    return user_operations


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
    input_mapping = {
        "b": 20,
        "i": 100,
        "e": 1000
    }

    return input_mapping[user_input]
