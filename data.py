import MyString
from .text_buffer import TextBuffer


class Data:
    def __init__(self):
        self.text: MyString = MyString()  # Текст хранится как MyString

    def update_data(self, buffer: TextBuffer):
        """
        Обновляет данные из текстового буфера.
        """
        self.text = MyString(buffer.text.data())  # Копируем данные из буфера
