from decimal import Decimal
from typing import List, Callable
from calculator.calculation import Calculation

class Calculations:
    active_history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.active_history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.active_history

    @classmethod
    def clear_history(cls):
        cls.active_history.clear()
    
    @classmethod
    def get_latest(cls) -> Calculation:
        if cls.active_history:
            return cls.active_history[-1]
        return None

    @classmethod
    def get_by_op(cls, operation: str) -> List[Calculation]:
        '''check each calc in history, create list of calcs with matching op'''
        return [c for c in cls.active_history if c.op.__name__ == operation]