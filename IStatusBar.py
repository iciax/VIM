from abc import ABC, abstractmethod


class IStatusBar(ABC):
    @abstractmethod
    def update_status_bar(self):
        """
        Обновить статус бар с актуальной информацией.
        """
        pass
