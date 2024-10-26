from app.commands import Command
from calculator.calculations import Calculations
import logging

class ShowHistoryCommand(Command):
    '''Shows active history'''
    def execute(self, a=None, b=None):
        try:
            for item in Calculations.get_history():
                print(item)
        except KeyError:
            print("No history")