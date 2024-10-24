from calculator import Calculator
from app.commands import Command
import logging

class SubtractCommand(Command):
    '''Perform subtract command'''
    def execute(self, a, b):
        logging.info('Executing subtract command')
        print(Calculator.subtract(a, b))