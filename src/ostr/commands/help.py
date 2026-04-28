import commands as c
from commands.command import Command

class HelpCommand(Command):
    KEYWORD = "help"
    VALID_ARGUMENTS = []
    DESCRIPTION = "Used to provide an overview of commands."

    def run_command(args):
        print("Available commands:")
        for command in c.command_list.commands.keys():
            command_class : Command = c.command_list.commands[command]
            print(f"-| {command}: {command_class.DESCRIPTION}")
            if len(command_class.VALID_ARGUMENTS) > 0:
                print(f"--| Valid arguments:")
                for arg in command_class.VALID_ARGUMENTS:
                    print(f"---| {arg}")