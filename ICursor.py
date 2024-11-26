from abc import ABC, abstractmethod


class ICursor(ABC):
    @abstractmethod
    def move_cursor(self, x: int, y: int):
        """
        Перемещение курсора в заданную позицию.
        """
        pass

    @abstractmethod
    def get_position(self):
        """
        Получить текущую позицию курсора.
        """
        pass

    @abstractmethod
    def render_cursor(self):
        """
        Отобразить курсор в текущей позиции.
        """
        pass
