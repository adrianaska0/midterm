from app.commands import Command
from calculator import Calculator
import logging

class AddCommand(Command):
    '''Perform Add Command'''
    def execute(self, a, b):
        logging.info('Executing add command')
        print(Calculator.add(a, b))