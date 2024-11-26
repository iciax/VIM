from abc import ABC, abstractmethod


class IInput(ABC):
    @abstractmethod
    def get_user_input(self):
        """
        Получение пользовательского ввода.
        """
        pass
