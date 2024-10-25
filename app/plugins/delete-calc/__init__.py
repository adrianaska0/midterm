from app.commands import Command
from calculator.calculations import Calculations
import logging

class DeleteCalculation(Command):
    def execute(self, a=None, b=None):
        self.a = a 
        try:
            logging.info(f"Deleted record: {Calculations.delete_calculation(int(a))}")
            print("Record deleted.")
        except TypeError:
            logging.error("Usage: delete-calc <id>")
            print("Usage: delete-calc <id>")