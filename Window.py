import IStatusBar
import ICursor
import ICurses


class Window:
    def __init__(self, cursor: ICursor, curses_adapter: ICurses, status_bar: IStatusBar):
        self.cursor = cursor
        self.curses_adapter = curses_adapter
        self.status_bar = status_bar

    def render_text(self, text_lines):
        """
        Отобразить текст.
        """
        cursor_pos = self.cursor.get_position()
        self.curses_adapter.render_text(text_lines, cursor_pos)

    def render_status_bar(self):
        """
        Отобразить статус бар.
        """
        self.status_bar.update_status_bar()

    def handle_input(self):
        """
        Обработать ввод пользователя.
        """
        return self.curses_adapter.get_input()

    def update_text(self, text_lines):
        """
        Обновить текст на экране.
        """
        self.render_text(text_lines)

    def update_cursor_pos(self, x, y):
        """
        Обновить позицию курсора.
        """
        self.cursor.move_cursor(x, y)
        self.cursor.render_cursor()

    def update_status(self):
        """
        Обновить статус бар.
        """
        self.render_status_bar()
