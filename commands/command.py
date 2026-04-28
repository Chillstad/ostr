class Command:
    KEYWORD : str = "debug"
    VALID_ARGUMENTS : list[str] = ["debug"]
    DESCRIPTION : str = "This is a debug description."

    def parse_args(self, args_str : str) -> dict:
        args_list = args_str.split(" ")
        args : dict = {}
        collected_str : list[str] = []
        current_arg : str = None
        for arg in args_list:
            if any(arg == f"--{valid_arg}" for valid_arg in self.VALID_ARGUMENTS):
                if current_arg != None:
                    args[current_arg] = " ".join(collected_str)
                current_arg = arg.removeprefix("--")
                collected_str = []
            elif "--" in arg:
                if current_arg != None:
                    args[current_arg] = " ".join(collected_str)
                current_arg = None
                collected_str = []
            else:
                collected_str.append(arg)  
        if current_arg != None:
            args[current_arg] = " ".join(collected_str)

        return args

    ## For changing by other commands.
    def run_command(args : dict):
        raise NotImplementedError