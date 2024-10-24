#pylint: disable=unused-variable, ungrouped-imports
'''Test command plugins'''
from decimal import Decimal
from unittest.mock import MagicMock
import pytest
from app.commands import Command_Handler
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.exit import ExitCommand
from app.plugins.menu import MenuCommand


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

def test_menu_command(capfd):
    '''Test menu menu command'''
    command_handler = Command_Handler()
    command_handler.register_command("subtract", MagicMock())
    command_handler.register_command("menu", MagicMock())
    command = MenuCommand()
    command.execute(command_handler, None)
    out, err = capfd.readouterr()
    assert "Available commands:" in out
    assert "- subtract" in out
    assert "- menu" in out
