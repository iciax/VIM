import IStatusBar

class ConsoleStatusBar(IStatusBar):
    def __init__(self, filename=None, line_number=1, total_lines=1, mode="Normal"):
        self.filename = filename
        self.line_number = line_number
        self.total_lines = total_lines
        self.mode = mode

    def update_status_bar(self):
        """
        Обновить строку состояния.
        """
        status = f"File: {self.filename or 'None'} | Line: {self.line_number}/{self.total_lines} | Mode: {self.mode}"
        print(status)  # Для отладки (в консоль), заменится на curses.
