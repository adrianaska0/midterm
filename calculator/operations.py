'''Arithmetic Opeartions'''
from decimal import Decimal

__all__ = ['add', 'subtract', 'multiply', 'divide']

def add(a: Decimal, b: Decimal) -> Decimal:
    '''add operation'''
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    '''subtract operation'''
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    '''multiply operation'''
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    '''divide operation'''
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
