class CommandManager:
    def __init__(self):
        self.history = []

    def add_command(self, command: str):
        """
        Добавление команды в историю.
        """
        self.history.append(command)
