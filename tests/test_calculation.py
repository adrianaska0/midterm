#pylint: disable=wildcard-import, unnecessary-dunder-call
'''Test Calculation'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import *

@pytest.mark.parametrize("a, b, op, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('5'), divide, Decimal('2'))
])

def test_calculator(a, b, op, expected):
    '''Test calulator functionality'''
    c = Calculation(a, b, op)
    assert c.execute() == expected, f"Failed {op.__name__} operation with {a}, {b}"

def test_calculation_repr():
    '''Test repr for calc class'''
    c = Calculation(Decimal('20'), Decimal('7'), subtract)
    assert c.__repr__() == "Calculation(20, 7, subtract)", "Failed __repr__ function."

def test_divide_zero():
    '''Test divide by zero error handling'''
    c = Calculation(Decimal('15'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        c.execute()
