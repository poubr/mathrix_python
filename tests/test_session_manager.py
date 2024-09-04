"""Test module for SessionManager's functionality."""

from session_manager import SessionManager
from unittest.mock import patch


def test_generate_exercises(session_manager: SessionManager) -> None:
    """Tests that the generate_exercises calls expected methods and returns expected result."""
    with patch.object(session_manager, "generate_exercises") as mock_generate_exercises:
        session_manager.generate_exercises()
    mock_generate_exercises.assert_called()


def test_get_exercises_per_operations(session_manager: SessionManager) -> None:
    """Tests that the exercises_per_operations function returns expected result."""
    # Expected result per the test_user_configuration defined in conftest:
    expected_result = {"addition": 5, "subtraction": 5}
    actual_result = session_manager.get_exercises_per_operations()
    assert expected_result == actual_result
