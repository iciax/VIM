import MyString


class TextBuffer:
    def __init__(self):
        self.text: MyString = MyString()  # Текст в формате MyString
        self.lines: list[MyString] = []  # Линии текста

    def clear(self):
        """
        Очищает текстовый буфер.
        """
        self.text.clear()
        self.lines.clear()

    def split_lines(self):
        """
        Разделяет текст на линии.
        """
        self.lines = [MyString(line) for line in str(self.text).split('\n')]

    # Прямое использование методов из MyString
    def append(self, text: str):
        self.text.append(text)

    def insert(self, index: int, text: str):
        self.text.insert(index, text)

    def erase(self, index: int, count: int):
        self.text.erase(index, count)

    def substr(self, index: int, count: int = None):
        return self.text.substr(index, count) if count else self.text.substr(index)
