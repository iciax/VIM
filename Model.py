from .IMode import IMode
from .text_buffer import TextBuffer
from .data import Data
from .view_observer import IViewObserver


class Model:
    def __init__(self):
        self.mode: IMode = None  # Текущий режим работы
        self.buffer: TextBuffer = TextBuffer()  # Текстовый буфер
        self.view_obs: IViewObserver = None  # Наблюдатель для обновления вида
        self.data: Data = Data()  # Бэкап данных

    def notify_view_obs(self):
        """
        Уведомляет наблюдателя об изменении модели.
        """
        if self.view_obs:
            self.view_obs.updateStatus()
            self.view_obs.updateText()
            self.view_obs.updateCursorPos()

    def update_mode(self, new_mode: IMode):
        """
        Обновляет текущий режим работы.
        """
        self.mode = new_mode

'''
class TextBuffer:
    def __init__(self, initial_text=""):
        self.text = MyString.MyString(initial_text)
        self.lines = MyString.MyString("\n".join(initial_text.splitlines()))

    def set_text(self, new_text):
        self.text = MyString.MyString(new_text)
        self.lines = MyString.MyString("\n".join(new_text.splitlines()))

    def get_text(self):
        return str(self.text)

    def insert_line(self, line_index, new_line):
        lines = self.get_lines_as_list()
        lines.insert(line_index, new_line)
        self.set_text("\n".join(lines))

    def remove_line(self, line_index):
        lines = self.get_lines_as_list()
        if 0 <= line_index < len(lines):
            lines.pop(line_index)
        self.set_text("\n".join(lines))

    def get_line(self, line_index):
        lines = self.get_lines_as_list()
        if 0 <= line_index < len(lines):
            return lines[line_index]
        return ""

    def get_lines_as_list(self):
        return str(self.lines).splitlines()

    def clear(self):
        self.set_text("")

    def line_count(self):
        return len(self.get_lines_as_list())


class Data:
    def __init__(self):
        self.text = TextBuffer()

    def update_data(self, new_text):
        self.text.set_text(new_text)


class Model:
    def __init__(self, mode, status_bar, controller):
        self.mode = mode
        self.buffer = TextBuffer()
        self.status_bar = status_bar
        self.controller = controller
        self.data = Data()

    def execute_command(self):
        pass

    def update_mode(self):
        pass


buffer = TextBuffer("Hello\nWorld")
print(buffer.get_text())
print(buffer.get_line(1))
buffer.insert_line(1, "New Line")
print(buffer.get_text())
buffer.remove_line(0)
print(buffer.get_text())

data = Data()
data.update_data("New Text")
print(data.text.get_text())

model = Model(None, None, None)
model.buffer.set_text("Model Text\nLine 2")
print(model.buffer.get_text())
'''