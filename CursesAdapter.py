import curses
import ICurses


class CursesAdapter(ICurses):
    def __init__(self):
        self.screen = None
        self.status_bar_height = 1

    def initialize(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        curses.start_color()
        self.screen.clear()

    def terminate(self):
        if self.screen:
            curses.nocbreak()
            self.screen.keypad(False)
            curses.echo()
            curses.endwin()

    def get_input(self):
        return self.screen.getch()

    def render_text(self, text_lines, cursor_pos):
        self.screen.clear()
        for i, line in enumerate(text_lines):
            self.screen.addstr(i, 0, line)
        self.screen.move(cursor_pos[0], cursor_pos[1])
        self.screen.refresh()

    def render_status_bar(self, status_text):
        height, width = self.screen.getmaxyx()
        self.screen.addstr(height - self.status_bar_height, 0, status_text[:width], curses.A_REVERSE)
        self.screen.refresh()

    def resize_handler(self):
        curses.resizeterm(*self.screen.getmaxyx())

    def get_screen_size(self):
        return self.screen.getmaxyx()
