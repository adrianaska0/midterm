import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self, a=None, b=None):
        sys.exit("Exiting...")