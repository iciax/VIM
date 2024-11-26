class MainController:
    def __init__(self, input_adapter: IInput, controller_inter: IController):
        self.input_adapter = input_adapter
        self.controller_inter = controller_inter
        self.run_status = True

    def select_controller(self, mode: str):
        """
        Выбор контроллера на основе текущего режима.
        """
        if mode == "command":
            return CommandController()
        elif mode == "input":
            return InputController()
        elif mode == "search":
            return SearchController()
        elif mode == "navigation":
            return NavigationAndEditController()
        else:
            raise ValueError(f"Неизвестный режим: {mode}")

    def get_user_input(self):
        """
        Получение пользовательского ввода.
        """
        return self.input_adapter.get_user_input()

    def run(self):
        """
        Запуск главного контроллера в бесконечном цикле.
        """
        while self.run_status:
            user_input = self.get_user_input()
            mode = self.controller_inter.write_command(user_input)

            controller = self.select_controller(mode)
            controller.write_command(user_input)
