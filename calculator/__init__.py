#pylint: disable=line-too-long, no-self-argument
'''Calculator Module'''
from decimal import Decimal
from typing import Callable
from calculator.operations import *
from calculator.calculation import Calculation
from calculator.calculations import Calculations

class Calculator:
    '''Calculator Class'''
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        '''perform operation'''
        calc = Calculation(a, b, operation)
        Calculations.add_calculation(calc)
        return calc.execute()

    def add(a: Decimal, b: Decimal) -> Decimal:
        '''add operation'''
        return Calculator._perform_operation(a, b, add)

    def subtract(a: Decimal, b: Decimal) -> Decimal:
        '''subtract operation'''
        return Calculator._perform_operation(a, b, subtract)

    def multiply(a: Decimal, b: Decimal) -> Decimal:
        '''multiply operation'''
        return Calculator._perform_operation(a, b, multiply)

    def divide(a: Decimal, b: Decimal) -> Decimal:
        '''divide operation'''
        return Calculator._perform_operation(a, b, divide)
