import os
import pandas as pd
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from app.commands import Command
import logging

class SaveCsvCommand(Command):
    def execute(self, a, b):
        self.file = b
        app = a

        try:
            # Get Absolute Path
            data_dir = app.settings.get('DATA_PATH')
            if not data_dir:
                data_dir = './data'

            os.makedirs(os.path.abspath(data_dir), exist_ok=True)
            
            file_path = os.path.join(os.path.abspath(data_dir), self.file)

            if not file_path.endswith('.csv'):
                error_message = f"Invalid file type: {self.file}. Only CSV files allowed."
                logging.error(error_message)
                print(error_message)
                return

            try:
                history = Calculations.get_history()
                data = [
                    (calc[1].replace('operation: ', ''), calc[2], calc[3])
                    for calc in history
                ]
                df = pd.DataFrame(data, columns=['operation', 'op_a', 'op_b'])
                df.to_csv(file_path, index=False)
                print(f"Calculations saved successfully in {file_path}")
                logging.info(f"Calculations saved successfully in {file_path}")
            except KeyError:
                logging.error("No data in history to save")
                print("No data in history to save")
            except Exception as e:
                logging.error(f"An error occured: {e}")
                print(f"An error occured: {e}")
        except TypeError:
            logging.error("Please provide the correct number of arguments. Usage <save_csv> <file_name>")