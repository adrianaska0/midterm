'''Calculations Module'''
from typing import List
from calculator.calculation import Calculation

class Calculations:
    '''Calculations Class'''
    active_history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        '''add calculation to history'''
        cls.active_history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''fetch history of calculations'''
        return cls.active_history

    @classmethod
    def clear_history(cls):
        '''clear calculation history'''
        cls.active_history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        '''get latest calculation from history'''
        if cls.active_history:
            return cls.active_history[-1]
        return None

    @classmethod
    def get_by_op(cls, operation: str) -> List[Calculation]:
        '''check each calc in history, create list of calcs with matching op'''
        return [c for c in cls.active_history if c.op.__name__ == operation]
