from .IMode import IMode

class ConsoleCommandMode(IMode):
    """
    Режим ввода команд.
    """

    def __init__(self):
        pass

    def update_mode(self):
        """
        Обновляет режим работы на 'command'.
        """
        print("Switching to command mode.")

    def edit(self):
        """
        Режим команд не редактирует текст.
        """
        raise NotImplementedError("Editing is not available in command mode.")

    def execute_methods(self):
        """
        Выполнение команд в режиме командного ввода.
        """
        print("Executing command mode methods.")