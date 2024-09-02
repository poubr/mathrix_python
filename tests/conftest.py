import pytest

from session_manager import SessionManager


@pytest.fixture(scope="session")
def session_manager() -> None:
    test_user_configuration = {
        'session_length': 10,
        'list_of_operations': ['addition', 'subtraction'],
        'difficulty': 100
    }

    session_manager = SessionManager(test_user_configuration)
    return session_manager
