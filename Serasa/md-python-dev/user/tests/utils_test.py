import pytest

from utils.response_generator import response
from utils.validators import is_valid_id


def test_response_success_case():
    data = {
        "message": "Invalid user",
        "data": [],
        "status_code": 200
    }
    response_return = response(**data)
    assert response_return.status_code == data.get('status_code')
    assert response_return.body.find(b'Invalid user') == 12


def test_id_validation_success_case():
    assert is_valid_id('5f276c2523bd3ebf871808c1') is True


def test_id_validation_fail_case():
    with pytest.raises(Exception):
        is_valid_id()
    assert is_valid_id('5f276c2523bd3ebf871808c') is False
