from .IMode import IMode
from .text_buffer import TextBuffer


class ConsoleInputMode(IMode):
    """
    Режим ввода текста.
    """

    def __init__(self, buffer: TextBuffer):
        self.text_buff = buffer

    def update_mode(self):
        """
        Обновляет режим работы на 'input'.
        """
        print("Switching to input mode.")

    def edit(self, text: str):
        """
        Запись текста в буфер.
        """
        print(f"Appending text: {text}")
        self.text_buff.append(text)

    def execute_methods(self):
        """
        Выполняет команды режима ввода.
        """
        print("Executing input mode methods.")

    def input_process(self, text: str):
        """
        Обрабатывает ввод пользователя.
        """
        self.edit(text)
