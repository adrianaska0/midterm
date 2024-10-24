from app.commands import Command
import logging

class MenuCommand(Command):
    '''Show command options'''
    def execute(self, a, b=None):
        logging.info('Executing Menu Command')
        print("Available commands:")
        for command_name in a.commands.keys():
            print(f"- {command_name}")