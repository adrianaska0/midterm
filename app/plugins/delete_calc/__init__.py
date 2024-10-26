from app.commands import Command
from calculator.calculations import Calculations
import logging

class DeleteCalculationCommand(Command):
    def execute(self, a, b):
        self.b = b
        try:
            logging.info(f"Deleted record: {Calculations.delete_calculation(int(b))}")
            print(f"Record with id {b} deleted.")
        except ValueError:
            logging.error("Usage: delete_calc <id>")
            print("Usage: delete_calc <id>")
        except KeyError:
            logging.error(f"Calculation with id {int(b)} does not exist")
            print(f"Calculation with id {int(b)} does not exist")