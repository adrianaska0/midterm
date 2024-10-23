'''Test operations'''
from decimal import Decimal
from calculator.operations import add, subtract, divide, multiply

def test_add_operation():
    '''Test add operation'''
    assert add(Decimal('10'), Decimal('3')) == 13

def test_subtract_operation():
    '''Test subtract operation'''
    assert subtract(Decimal('10'), Decimal('3')) == 7

def test_multiply_operation():
    '''Test multiply operation'''
    assert multiply(Decimal('10'), Decimal('3')) == 30

def test_divide_operation():
    '''Test divide operation'''
    assert divide(Decimal('10'), Decimal('5')) == 2
