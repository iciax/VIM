from abc import ABC, abstractmethod


class IController(ABC):
    @abstractmethod
    def write_command(self, command: str):
        """
        Передача команды для обработки.
        """
        pass
