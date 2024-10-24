from app.commands import Command
from calculator import Calculator
import logging

class MultiplyCommand(Command):
    '''Perform multiply command'''
    def execute(self, a, b):
        logging.info('Executing multiply command')
        print(Calculator.multiply(a, b))

