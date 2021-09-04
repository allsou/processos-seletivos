import pytest

from models.user import User

data = {
    "name": "Allan",
    "cpf": "00000000191",
    "email": "a@a.com",
    "phone_number": "(12) 98202-9058"
}


def test_valid_instance_should_assert_correctly():
    user = User(
        **data
    )
    assert user.name == data.get('name')
    assert user.cpf == data.get('cpf')
    assert user.email == data.get('email')
    assert user.phone_number == data.get('phone_number')
    assert user.updated_at == []


def test_invalid_instance_should_raise_errors():
    with pytest.raises(Exception):
        User(name="").validate()
    with pytest.raises(Exception):
        User(cpf="0").validate()
    with pytest.raises(Exception):
        User(cpf="000000001910").validate()
    with pytest.raises(Exception):
        User(phone_number="12982029058").validate()


def test_populate_method():
    user = User()
    user.populate(data)
    assert user.name == data.get('name')
    assert user.cpf is None
    assert user.email == data.get('email')
    assert user.phone_number == data.get('phone_number')
