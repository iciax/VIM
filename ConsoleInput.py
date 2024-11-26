import IInput

class ConsoleInput(IInput):
    def __init__(self, curses_adapter):
        self.curses_adapter = curses_adapter

    def get_user_input(self):
        """
        Получение ввода пользователя через curses.
        """
        return chr(self.curses_adapter.get_input())
