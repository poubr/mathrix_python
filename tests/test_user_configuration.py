"""Module for testing user_configurtion.py's functions."""
import pytest

from user_configuration import get_session_length, get_operations_list, get_session_difficulty, convert_difficulty_input
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


input_mapper = [
    ("b", 20),
    ("i", 100),
    ("e", 1000)
]


@pytest.mark.parametrize("input_key, expected_value", input_mapper)
def convert_difficulty_input(input_key, expected_value):
    actual_value = convert_difficulty_input(input_key)
    assert actual_value == expected_value
