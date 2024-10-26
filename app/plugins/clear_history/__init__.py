from app.commands import Command
from calculator.calculations import Calculations
import logging

class ClearHistoryCommand(Command):
    '''Clear calculation active history'''
    def execute(self, a=None, b=None):
        Calculations.clear_history()
        logging.info("History cleared")
        print("History cleared")