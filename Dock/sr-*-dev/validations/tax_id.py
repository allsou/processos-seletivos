"""
Tax id validation module
"""
import re

from mongoengine.errors import ValidationError

DIVISOR = 11
PHYSICAL_WEIGHTS = (
    (10, 9, 8, 7, 6, 5, 4, 3, 2),
    (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
)


def _calculate_first_digit(number):
    """ This function calculates the first check digit of a
        cpf or cnpj.
        :param number: cpf (length 9) or cnpf (length 12)
            string to check the first digit. Only numbers.
        :type number: string
        :returns: string -- the first digit
    """

    sum_result = 0
    weights = PHYSICAL_WEIGHTS[0]

    for i in range(len(number)):
        sum_result = sum_result + int(number[i]) * weights[i]
    rest_division = sum_result % DIVISOR
    if rest_division < 2:
        return '0'
    return str(11 - rest_division)


def _calculate_second_digit(number):
    """ This function calculates the second check digit of
        a cpf or cnpj.
        **This function must be called after the above.**
        :param number: cpf (length 10) or cnpj
            (length 13) number with the first digit. Only numbers.
        :type number: string
        :returns: string -- the second digit
    """

    sum_result = 0
    weights = PHYSICAL_WEIGHTS[1]

    for i in range(len(number)):
        sum_result = sum_result + int(number[i]) * weights[i]
    rest_division = sum_result % DIVISOR
    if rest_division < 2:
        return '0'
    return str(11 - rest_division)


def _only_digits_of_string(text):
    """This function returns only number of strings
        :param text: a CPF/CNPJ number to be validated.  Only numbers.
        :type text: string
        :return: string
        """
    return re.sub("[^0-9]", '', text)


def is_physical_tax_id(tax_id):

    _tax_id = _only_digits_of_string(tax_id)

    if (len(_tax_id) != 11 or
            len(set(_tax_id)) == 1):
        return False

    first_part = _tax_id[:9]
    second_part = _tax_id[:10]
    first_digit = _tax_id[9]
    second_digit = _tax_id[10]

    if (first_digit == _calculate_first_digit(first_part) and
            second_digit == _calculate_second_digit(second_part)):
        return True

    return False


def is_tax_id_valid(tax_id) -> bool:
    if not is_physical_tax_id(tax_id):
        raise ValidationError("Invalid tax id")
