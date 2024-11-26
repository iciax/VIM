import ICursor

class ConsoleCursor(ICursor):
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_cursor(self, x: int, y: int):
        """
        Перемещение курсора в заданную позицию.
        """
        self.x = x
        self.y = y

    def get_position(self):
        """
        Получить текущую позицию курсора.
        """
        return self.y, self.x

    def render_cursor(self):
        """
        Отобразить курсор.
        """
        print(f"Cursor position: ({self.y}, {self.x})")  # Для отладки.
