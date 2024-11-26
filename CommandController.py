import IController
import CommandManager

class CommandController(IController):
    def __init__(self, command_manager: CommandManager):
        self.command_manager = command_manager

    def write_command(self, command: str):
        """
        Передача команды в модель.
        """
        self.command_manager.add_command(command)
        print(f"Command executed: {command}")
