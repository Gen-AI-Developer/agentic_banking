from colorama import Fore, Style, init
init(autoreset=True)

def colorize(value):
    if isinstance(value, str):
        return Fore.YELLOW + repr(value) + Style.RESET_ALL
    elif value is None:
        return Fore.MAGENTA + "None" + Style.RESET_ALL
    elif isinstance(value, bool):
        return Fore.BLUE + str(value) + Style.RESET_ALL
    elif isinstance(value, (int, float)):
        return Fore.GREEN + str(value) + Style.RESET_ALL
    else:
        return str(value)

def print_tree(data, prefix=""):
    if isinstance(data, dict):
        items = list(data.items())
        for i, (key, value) in enumerate(items):
            is_last = i == len(items) - 1
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{Fore.CYAN}{key}{Style.RESET_ALL}:", end="")
            if isinstance(value, (dict, list)):
                print()
                new_prefix = prefix + ("    " if is_last else "│   ")
                print_tree(value, new_prefix)
            else:
                print(f" {colorize(value)}")
    elif isinstance(data, list):
        for i, item in enumerate(data):
            is_last = i == len(data) - 1
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{Fore.CYAN}Item {i}{Style.RESET_ALL}")
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(item, new_prefix)
    else:
        print(f"{prefix}{colorize(data)}")