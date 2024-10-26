from app.commands import Command
from calculator.calculations import Calculations
import logging

class DeleteCalculationCommand(Command):
    def execute(self, a, b=None):
        self.a = a 
        try:
            logging.info(f"Deleted record: {Calculations.delete_calculation(int(a))}")
            print(f"Record with id {a} deleted.")
        except ValueError:
            logging.error("Usage: delete_calc <id>")
            print("Usage: delete_calc <id>")
        except KeyError:
            logging.error(f"Calculation with id {int(a)} does not exist")
            print(f"Calculation with id {int(a)} does not exist")