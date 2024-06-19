"""Module for testing user_configurtion.py's functions."""

from user_configuration import get_session_length
from unittest.mock import patch


def test_get_session_length_correct_input() -> None:
    """Tests that the get_session_length function returns the correct input."""
    with patch("builtins.input", side_effect=["5"]):
        mock_input = get_session_length()
        assert mock_input == 5


def test_get_session_length_user_quits() -> None:
    """Tests that the get_session_length function returns 0 if user quits."""
    with patch("builtins.input", side_effect=["x", "q"]):
        mock_input = get_session_length()
        assert mock_input == 0


def test_get_session_length_no_valid_answer() -> None:
    """Tests that the get_session_length function returns 0 if user doesn't provide valid input."""
    with patch("builtins.input", side_effect=["h", "e", "l", "l", "o"]):
        mock_input = get_session_length()
        assert mock_input == 0
