from .IMode import IMode
from .text_buffer import TextBuffer


class ConsoleSearchMode(IMode):
    """
    Режим поиска текста.
    """

    def __init__(self, buffer: TextBuffer):
        self.text_buff = buffer
        self.last_target: str = ""
        self.target: str = ""

    def update_mode(self):
        """
        Обновляет режим работы на 'search'.
        """
        print("Switching to search mode.")

    def edit(self):
        """
        Поиск не редактирует текст.
        """
        raise NotImplementedError("Editing is not available in search mode.")

    def execute_methods(self):
        """
        Выполняет команды поиска.
        """
        print("Executing search mode methods.")

    def search_forward(self, target: str):
        """
        Поиск строки вниз.
        """
        self.target = target
        print(f"Searching forward for: {target}")

    def search_backward(self, target: str):
        """
        Поиск строки вверх.
        """
        self.target = target
        print(f"Searching backward for: {target}")

    def repeat_search(self):
        """
        Повторяет последний поиск.
        """
        print(f"Repeating search for: {self.last_target}")
