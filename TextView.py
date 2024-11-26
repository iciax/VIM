import MyString


class TextView:
    def __init__(self, observer):
        self.text = MyString("")
        self.observer = observer
        self.current_line = 0

    def write_line(self, line: str):
        """
        Записать строку в текст.
        """
        self.text.append(line + '\n')

    def clear_line(self, line_number: int):
        """
        Очистить строку.
        """
        lines = self.text.split('\n')
        if 0 <= line_number < len(lines):
            lines[line_number] = ""
        self.text = MyString("\n".join(lines))

    def move_to_line(self, line_number: int):
        """
        Переместиться к строке.
        """
        self.current_line = max(0, min(line_number, len(self.text.split('\n')) - 1))

    def pg_down(self):
        """
        Переместиться на страницу вниз.
        """
        self.current_line += 10

    def pg_up(self):
        """
        Переместиться на страницу вверх.
        """
        self.current_line = max(0, self.current_line - 10)
