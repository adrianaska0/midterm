#pylint: disable=unused-variable, ungrouped-imports
'''Test command plugins'''
from decimal import Decimal
from unittest.mock import MagicMock
import pytest
from app.commands import Command_Handler
from calculator.calculations import Calculations
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.exit import ExitCommand
from app.plugins.menu import MenuCommand
from app.plugins.delete_calc import DeleteCalculationCommand
from app.plugins.clear_history import ClearHistoryCommand
from app.plugins.show_history import ShowHistoryCommand


def test_add_command(capfd):
    '''Test add command'''
    command = AddCommand()
    command.execute(Decimal('3'), Decimal('5'))
    out, err = capfd.readouterr()
    assert out == "8\n", "The answer should be 8"

def test_subtract_command(capfd):
    '''Test subtract command'''
    command = SubtractCommand()
    command.execute(Decimal('10'), Decimal('6'))
    out, err = capfd.readouterr()
    assert out == "4\n", "The answer should be 4"

def test_multiply_command(capfd):
    '''Test multiply command'''
    command = MultiplyCommand()
    command.execute(Decimal('6'), Decimal('3'))
    out, err = capfd.readouterr()
    assert out == "18\n", "The answer should be 18"

def test_divide_command(capfd):
    '''Test divide command'''
    command = DivideCommand()
    command.execute(Decimal('20'), Decimal('5'))
    out, err = capfd.readouterr()
    assert out == "4\n", "The answer should be 4"

def test_divide_zero_command(capfd):
    '''Test divide by zero handling'''
    command = DivideCommand()
    with pytest.raises(ValueError):
        command.execute(Decimal('15'), Decimal('0'))
    out, err = capfd.readouterr()
    assert out == "Cannot divide by zero\n", "Should return 'Cannot divide by zero'"

def test_exit_command():
    '''Test program exit command'''
    command = ExitCommand()
    with pytest.raises(SystemExit) as excinfo:
        command.execute()
    assert str(excinfo.value) == "Exiting..."

@pytest.fixture
def sample_handler():
    command_handler = Command_Handler()
    command_handler.register_command("subtract", MagicMock())
    yield command_handler

def test_menu_command(sample_handler, capfd):
    '''Test menu menu command'''
    sample_handler.register_command("menu", MagicMock())
    MenuCommand().execute(sample_handler, None)
    out, err = capfd.readouterr()
    assert "Available commands:" in out
    assert "- subtract" in out
    assert "- menu" in out

def test_show_history_command(capfd):
    Calculations.clear_history()
    AddCommand().execute(Decimal('5'), Decimal('5'))
    DivideCommand().execute(Decimal('15'), Decimal('3'))
    ShowHistoryCommand().execute()
    out, err = capfd.readouterr()
    assert "('id: 1', 'operation: add', '5', '5')" in out, "Calculation not in output"
    assert "('id: 2', 'operation: divide', '15', '3')" in out, "Calculation not in output"

def test_show_history_empty_command(capfd):
    Calculations.clear_history()
    ShowHistoryCommand().execute()
    out, err = capfd.readouterr()
    assert "No history\n" in out

def test_clear_history_command(capfd):
    '''Test clear history command'''
    Calculations.clear_history()
    SubtractCommand().execute(Decimal('3'), Decimal('1'))
    assert len(Calculations.get_history()) == 1
    ClearHistoryCommand().execute()
    with pytest.raises(KeyError):
        Calculations.get_history()
    res = capfd.readouterr()
    assert "History cleared\n" in res.out

def test_delete_calculation_command(capfd):
    '''Test delete calc by id'''
    Calculations.clear_history()
    AddCommand().execute(Decimal('3'), Decimal('5'))
    MultiplyCommand().execute(Decimal('3'), Decimal('3'))
    DeleteCalculationCommand().execute('1')
    out, err = capfd.readouterr()
    assert "Record with id 1 deleted.\n" in out, "Did not recieve response on delete"
    assert len(Calculations.get_history()) == 1, "Record not deleted properly"

def test_delete_calculation_error_command(capfd):
    '''Test error handling in delete calc'''
    Calculations.clear_history()
    DeleteCalculationCommand().execute('a')
    DeleteCalculationCommand().execute('1')
    out, err = capfd.readouterr()
    assert "Usage: delete_calc <id>\n" in out
    assert "Calculation with id 1 does not exist" in out

