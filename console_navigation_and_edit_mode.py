from .IMode import IMode
from .text_buffer import TextBuffer


class ConsoleNavigationAndEditMode(IMode):
    """
    Режим навигации и редактирования текста.
    """

    def __init__(self, buffer: TextBuffer):
        self.text_buff = buffer

    def update_mode(self):
        """
        Обновляет режим работы на 'navigation and edit'.
        """
        print("Switching to navigation and edit mode.")

    def edit(self, text: str):
        """
        Изменяет текст в буфере.
        """
        print(f"Editing text: {text}")
        self.text_buff.append(text)

    def execute_methods(self):
        """
        Выполняет команды навигации и редактирования.
        """
        print("Executing navigation and edit mode methods.")
