import IController
import CommandManager

class NavigationAndEditController(IController):
    def __init__(self, command_manager: CommandManager):
        self.command_manager = command_manager

    def write_command(self, command: str):
        """
        Навигация и редактирование текста.
        """
        self.command_manager.add_command(command)
        print(f"Navigation/Edit executed: {command}")

