from ostr.commands.command_list import commands


def main_loop():
    while True:
        user_input = input("ostr: ")

        if user_input == "":
            continue  # Eat dead input

        command_parts: list = user_input.split(" ", 1)
        command_keyword = command_parts[0]
        command_args = ""
        if len(command_parts) > 1:
            command_args = command_parts[1]
        try:
            command_class = commands[command_keyword]
            c = command_class()
            command_class.run_command(c.parse_args(command_args))
        except KeyError:
            print(f"Unrecognized command '{command_keyword}'.")

