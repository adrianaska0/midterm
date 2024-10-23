from abc import ABC, abstract method
import logging

class Command(ABC):
    '''Command Class'''
    @abstract method
    def execute(self, a, b):
        '''Abstract execute method'''
        self.a = a
        self.b = b
        pass

class Command_Handler:
    '''Command Handler for enrolling and executing commands'''
    def __init__(self):
        self.commands = {}
    
    def register_command(self, command_name: str, command: Command):
        '''Register a command to the dictionary'''
        self.commands[command_name] = command
    
    def execute_command(self, command_name: str, a, b):
        '''Execute command from dictionary'''
        try:
            self.commands[command_name].execute(a, b)
        except KeyError:
            print(f"No such command {command_name}")
            logging.error(f"No such command {command_name}")
