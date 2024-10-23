from decimal import Decimal
from calculator import Calculator

def test_add_operation():
    assert Calculator.add(3, 2) == 5, "Failed add operation"

def test_subtract_operation():
    assert Calculator.subtract(10, 2) == 8, "Failed subtract operation"

def test_multiply_operation():
    assert Calculator.multiply(3, 4) == 12, "Failed multiply operation"

def test_divide_opeartion():
    assert Calculator.divide(14, 7) == 2, "Failed divide operation"