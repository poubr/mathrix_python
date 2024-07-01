"""Module for testing user_configurtion.py's functions."""
import user_configuration
from user_configuration import get_session_length, get_operations_list
from unittest.mock import patch


def test_get_session_length_correct_input() -> None:
    """Tests that the get_session_length function returns the correct input."""
    with patch("builtins.input", side_effect=["5"]):
        mock_session_length = get_session_length()
        assert mock_session_length == 5


def test_get_session_length_user_quits() -> None:
    """Tests that the get_session_length function returns 0 if user quits."""
    with patch("builtins.input", side_effect=["x", "q"]):
        mock_session_length = get_session_length()
        assert mock_session_length == 0


def test_get_session_length_no_valid_answer() -> None:
    """Tests that the get_session_length function returns 0 if user doesn't provide valid input."""
    with patch("builtins.input", side_effect=["h", "e", "l", "l", "o"]):
        mock_session_length = get_session_length()
        assert mock_session_length == 0


def test_get_operations_list() -> None:
    """Tests that the get_operations_list function returns the correct input."""
    with patch("builtins.input", side_effect=["Y", "N", "Y", "N"]):
        mock_operations_list = get_operations_list()
        assert mock_operations_list == ["addition", "multiplication"]


def test_get_operations_list_user_quits() -> None:
    """Tests that the get_operations_list function returns an empty list if user quits."""
    with patch("builtins.input", side_effect=["n", "n", "n", "n", "q"]):
        mock_operations_list = get_operations_list()
        assert mock_operations_list == []


def test_get_operations_list_no_valid_input() -> None:
    """Tests that the get_operations_list function returns an empty list if user doesn't provide valid input."""
    mock_inputs = ['x' for _ in range(16)]
    with patch("builtins.input", side_effect=mock_inputs):
        mock_operations_list = get_operations_list()
        assert mock_operations_list == []


def test_get_session_difficulty_correct_input() -> None:
    """Tests that the get_session_difficulty function returns the correct input."""
    with patch("builtins.input", side_effect=["I"]), \
         patch("user_configuration.convert_difficulty_input", return_value=20):
        mock_session_length = get_session_difficulty()
        assert mock_session_length == 20


def test_get_session_difficulty_user_quits() -> None:
    """Tests that the get_session_difficulty function returns 0 if user quits."""
    with patch("builtins.input", side_effect=["x", "q"]):
        mock_session_length = get_session_difficulty()
        assert mock_session_length == 0


def test_get_session_difficulty_no_valid_answer() -> None:
    """Tests that the get_session_difficulty function returns 0 if user doesn't provide valid input."""
    with patch("builtins.input", side_effect=["f", "r", "o", "d", "o"]):
        mock_session_length = get_session_difficulty()
        assert mock_session_length == 0



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
