'''Calculations Module'''
from typing import Dict, List, Optional, Tuple
from calculator.calculation import Calculation
import logging

class Calculations:
    '''Calculations Class'''
    active_history: Dict[int, Calculation] = {}
    _next_id: int = 1

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        '''add calculation to history'''
        cls.active_history[cls._next_id] = calculation
        cls._next_id += 1

    @classmethod
    def get_history(cls) -> List[Tuple[int, Calculation]]:
        '''fetch history of calculations'''
        if cls.active_history:
            return [(f"id: {calc_id}", f"operation: {calc.op.__name__}", str(calc.a), str(calc.b)) for calc_id, calc in cls.active_history.items()]
        else:
            logging.error("No history")
            raise KeyError

    @classmethod
    def clear_history(cls):
        '''clear calculation history'''
        cls.active_history.clear()
        cls._next_id = 1

    @classmethod
    def get_latest(cls) -> Calculation:
        '''get latest calculation from history'''
        if cls.active_history:
            return cls.active_history[max(cls.active_history.keys())]
        return None

    @classmethod
    def get_by_op(cls, operation: str) -> List[Calculation]:
        '''check each calc in history, create list of calcs with matching op'''
        return [c for c in cls.active_history.values() if c.op.__name__ == operation]

    @classmethod
    def delete_calculation(cls, id: int) -> Calculation:
        '''delete calculation by id'''
        return cls.active_history.pop(id)
