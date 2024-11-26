import IController
import CommandManager

class SearchController(IController):
    def __init__(self, command_manager: CommandManager):
        self.command_manager = command_manager

    def write_command(self, command: str):
        """
        Поиск в тексте.
        """
        self.command_manager.add_command(command)
        print(f"Search performed: {command}")
