import logging
import os
import pandas as pd
from calculator.calculations import Calculations
from app.commands import Command
from app import App

class LoadCalcCommand(Command):
    def execute(self, a, b=None):
        self.file = a

        # Get Absolute Path
        data_dir = App().get_environment_variable('DATA_PATH')
        file_path = os.path.join(os.path.abspath(data_dir), self.file)
        print(file_path)