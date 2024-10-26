from decimal import Decimal, InvalidOperation
import logging
import os
import pandas as pd
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from app.commands import Command

class LoadCsvCommand(Command):
    def execute(self, a, b):
        self.file = b
        app = a

        # Get Absolute Path
        try:
            data_dir = app.settings.get('DATA_PATH')
            if not data_dir:
                data_dir = './data'
            file_path = os.path.join(os.path.abspath(data_dir), self.file)

            if not file_path.endswith('.csv'):
                error_message = f"Invalid file type: {self.file}. Only CSV files allowed."
                logging.error(error_message)
                print(error_message)
                return

            Calculations.clear_history()
            try:
                df_calc = pd.read_csv(file_path)
                for op_name, op_a, op_b in df_calc.itertuples(index=False):
                    try:
                        logging.debug(f"{op_name}, {Decimal(op_a)}, {Decimal(op_b)}")
                        op = app.command_handler.commands[op_name]
                        calc = Calculation.create(Decimal(op_a), Decimal(op_b), op)
                        calc.op.__name__ = op_name
                        Calculations.add_calculation(calc)
                        logging.debug(f"Calculation logged: {op_name}, {Decimal(op_a)}, {Decimal(op_b)}")
                    except KeyError:
                        logging.error(f"No such command: {op_name}")
                        print(f"No such command: {op_name}")
                    except InvalidOperation:
                        logging.error(f"Error: {op_a} or {op_b} is invalid")
                        print(f"Error: {op_a} or {op_b} is invalid")
            except FileNotFoundError:
                logging.error(f"File not found {file_path}")
                print(f"File not found {file_path}")
        except TypeError:
            logging.error("Please provide the correct number of arguments. Usage <load_csv> <file_name>")


