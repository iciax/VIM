class ModelControl:
    def __init__(self, model):
        self.model = model

    def take_user_input(self, user_input: str):
        """
        Передача пользовательского ввода в модель.
        """
        self.model.add_input(user_input)

    def set_mode(self, mode: str):
        """
        Установка режима работы модели.
        """
        self.model.set_mode(mode)
