from app.commands import Command
from calculator import Calculator
import logging

class DivideCommand(Command):
    '''Perform divide command'''
    def execute(self, a, b):
        logging.info('Executing divide command')
        print(Calculator.divide(a, b))