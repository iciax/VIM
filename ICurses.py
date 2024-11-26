from abc import ABC, abstractmethod


class ICurses(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def terminate(self):
        pass

    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def render_text(self, text_lines, cursor_pos):
        pass

    @abstractmethod
    def render_status_bar(self, status_text):
        pass

    @abstractmethod
    def resize_handler(self):
        pass

    @abstractmethod
    def get_screen_size(self):
        pass
