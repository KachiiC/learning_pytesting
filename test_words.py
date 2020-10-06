import pytest

#Captial case
def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)

# Upper case
def upper_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.upper()


def test_capital_case():
    assert upper_case('semaphore') == 'SEMAPHORE'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        upper_case(9)