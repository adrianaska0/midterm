'''Test command methods'''
import pytest
from decimal import Decimal
from app.commands import Command, Command_Handler

class TestCommand(Command):
    '''Command used for testing'''
    def execute(self, a, b):
        self.a = a
        self.b = b
        print(a * b)

@pytest.fixture
def sample_handler():
    command_handler = Command_Handler()
    command_handler.register_command("test", TestCommand())
    yield command_handler

def test_register_command(sample_handler):
    '''Test command registration'''
    assert "test" in sample_handler.commands, "Command not in commands"

def test_execute_command(sample_handler, capfd):
    '''Test command execution'''
    sample_handler.execute_command("test", Decimal('5'), Decimal('10'))
    out, err = capfd.readouterr()
    assert out == "50\n", "Command execution failed: The answer should be 50."

def test_execute_unknown(sample_handler, capfd):
    '''Test execute unknonwn command'''
    with pytest.raises(KeyError):
        sample_handler.execute_command("random", None, None)
    out, err = capfd.readouterr()
    assert out == "No such command random\n"

def test_execute():
    command = TestCommand()
    command.execute(Decimal('2'), Decimal('5'))
    assert command.a == Decimal('2')
    assert command.b == Decimal('5')