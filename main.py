import curses
import CursesAdapter
import MainController
import ConsoleInput
import ModelControl
import CommandManager

def main(stdscr):
    curses_adapter = CursesAdapter()
    curses_adapter.initialize()

    command_manager = CommandManager()
    input_adapter = ConsoleInput(curses_adapter)
    model_control = ModelControl(None)  # Укажите вашу модель здесь
    main_controller = MainController(input_adapter, model_control)

    try:
        main_controller.run()
    finally:
        curses_adapter.terminate()

if __name__ == "__main__":
    curses.wrapper(main)
