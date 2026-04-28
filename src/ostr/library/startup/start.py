from library.input.question_handlers import ask_yes_or_no
from library.main_loop.main_loop import main_loop
from pathlib import Path

def create_project() -> int:
    project : Path = Path("./Project")
    project.mkdir()
    return 0

def check_for_project() -> int:
    project : Path = Path("./Project")

    if project.is_dir():
        return 0
    else:
        print("It looks like a project is not yet initialized here.")
        should_create_project : bool = ask_yes_or_no("Do you want to create one?")
        return create_project() if should_create_project == True else -1

def start_program() -> int:
    continue_startup : int = check_for_project()
    if continue_startup == -1:
        print("No project, exiting program...")
        return -1
    
    main_loop()
    
    return 0

