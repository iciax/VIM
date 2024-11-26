from abc import ABC, abstractmethod


class IMode(ABC):
    """
    Интерфейс для различных режимов работы редактора.
    """

    @abstractmethod
    def update_mode(self):
        """
        Устанавливает новый режим работы.
        """
        pass

    @abstractmethod
    def edit(self):
        """
        Изменяет текст в буфере.
        """
        pass

    @abstractmethod
    def execute_methods(self):
        """
        Выполняет набор команд редактора.
        """
        pass
