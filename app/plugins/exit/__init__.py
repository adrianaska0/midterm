import sys
from app.commands import Command
import logging

class ExitCommand(Command):
    def execute(self, a=None, b=None):
        logging.info('Application shutting down')
        sys.exit("Exiting...")