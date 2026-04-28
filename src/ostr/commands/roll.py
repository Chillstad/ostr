import commands as c
from commands.command import Command
import random as r

class RollCommand(Command):
    KEYWORD = "roll"
    VALID_ARGUMENTS = ["size", "amount", "bonus"]
    DESCRIPTION = "Used to roll [amount]d[size]+[bonus]."

    def run_command(args : dict):
        size = int(args["size"]) if ("size" in args.keys()) else 20
        amount = int(args["amount"]) if ("amount" in args.keys()) else 1
        bonus = int(args["bonus"]) if ("bonus" in args.keys()) else 0

        total : int = bonus
        for i in range(0, amount):
            total += r.randint(1, size)
        
        print(total)
