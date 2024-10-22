from decimal import Decimal
from typing import Callable
from calculator.operations import *

class Calculation:
    def __init__(self, a: Decimal, b:Decimal, op: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.op = op

    @staticmethod
    def create(a: Decimal, b: Decimal, op: Callable[[Decimal, Decimal], Decimal]):
        '''Return Calculation object'''
        return Calculation(a, b, op)

    def execute(self) -> Decimal:
        '''Perform calculation operation'''
        return self.op(self.a, self.b)
    
    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.op.__name__})"