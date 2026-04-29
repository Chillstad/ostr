
def ask_yes_or_no(question : str) -> bool:
    answer : str = input(f"{question} (y/n): ")
    while not (answer in ["y", "n", "yes", "no"]):
        print(f"Invalid input: {answer}")
        answer = input(f"{question} (y/n): ")
    return answer in ["y", "yes"]
