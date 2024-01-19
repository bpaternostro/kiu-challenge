import pytest

from .constants import MOCK_INPUT, DUMMY_DATE, DUMMY_RATE

@pytest.fixture
def mocker_open_file(mocker):
    mocked_input_data = mocker.mock_open(read_data=MOCK_INPUT)
    builtin_open = "builtins.open"
    mocker.patch(builtin_open, mocked_input_data)
