import commands as c
from commands.command import Command
import importlib
import os

commands : dict = {}

forbidden_files = ["command_list.py", "command.py"]

commands_path = c.__path__[0]

for filename in os.listdir(commands_path):
    if filename.endswith(".py") and not (filename in forbidden_files):
        module_name = f"commands.{filename[:-3]}"
        module = importlib.import_module(module_name)

        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and issubclass(obj, Command) and obj is not Command:
                commands[obj.KEYWORD] = obj

