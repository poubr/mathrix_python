"""Module for testing user_configurtion.py's functions."""

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
    """Tests that the get_operations_list function  returns an empty list if user doesn't provide valid input."""
    with patch("builtins.input", side_effect=["t", "h", "e", "r", "e"]):
        mock_operations_list = get_operations_list()
        assert mock_operations_list == []

s