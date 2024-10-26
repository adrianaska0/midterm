#pylint: disable=unused-argument, redefined-outer-name
'''Test calculations module'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, multiply, subtract

@pytest.fixture
def test_calculations():
    '''Setup test calculations'''
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('5'), Decimal('8'), add))
    Calculations.add_calculation(Calculation(Decimal('4'), Decimal('12'), multiply))
    Calculations.add_calculation(Calculation(Decimal('3'), Decimal('3'), add))

def test_add_calculation(test_calculations):
    '''Test add calculation to history'''
    calc = Calculation(Decimal('2'), Decimal('3'), multiply)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Add calculation to history failed"

def test_get_history(test_calculations):
    '''Test get calculation history'''
    history = Calculations.get_history()
    assert len(history) == 3, "Wrong expected number of calculations in history"

def test_clear_history(test_calculations, capfd):
    '''Test clear calculation history'''
    Calculations.clear_history()
    with pytest.raises(KeyError):
        Calculations.get_history()

def test_get_latest(test_calculations):
    '''Test get latest item in calculation history'''
    c = Calculation(Decimal('0'), Decimal('4'), subtract)
    Calculations.add_calculation(c)
    assert Calculations.get_latest() == c, "Get latest not returning latest calc"

def test_get_latest_empty(test_calculations):
    '''Test repsonse for empty history'''
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Did not show None for empty history (get latest)"

def test_get_by_op(test_calculations):
    '''Test fetch calculation by operation'''
    b = Calculations.get_by_op("add")
    assert len(b) == 2, "Did not find correct number of calculations"
    b = Calculations.get_by_op("multiply")
    assert len(b) == 1, "Did not find correct number of operations"
