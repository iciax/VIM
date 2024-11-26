import IController
import CommandManager

class InputController(IController):
    def __init__(self, command_manager: CommandManager):
        self.command_manager = command_manager

    def write_command(self, command: str):
        """
        Обработка ввода.
        """
        self.command_manager.add_command(command)
        print(f"Input handled: {command}")
