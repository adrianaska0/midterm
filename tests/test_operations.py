'''Test operations'''
from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide

def test_add_operation():
    assert add(Decimal('10'), Decimal('3')) == 13

def test_subtract_operation():
    assert subtract(Decimal('10'), Decimal('3')) == 7

def test_multiply_operation():
    assert multiply(Decimal('10'), Decimal('3')) == 30

def test_divide_operation():
    assert divide(Decimal('10'), Decimal('5')) == 2
