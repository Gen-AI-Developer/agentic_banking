from pprint import pprint
from colorama import Fore, Style, init
from dataclasses import asdict
init(autoreset=True)

def colorize(value):
    if isinstance(value, str):
        return Fore.LIGHTGREEN_EX + repr(value) + Style.RESET_ALL
    elif value is None:
        return Fore.LIGHTMAGENTA_EX + "None" + Style.RESET_ALL
    elif isinstance(value, bool):
        return Fore.LIGHTBLUE_EX + str(value) + Style.RESET_ALL
    elif isinstance(value, (int, float)):
        return Fore.LIGHTRED_EX + str(value) + Style.RESET_ALL
    else:
        return str(value)

def printt(data, prefix=""):
    data = asdict(data) if hasattr(data, '__dataclass_fields__') else data
    if isinstance(data, dict):
        items = list(data.items())
        for i, (key, value) in enumerate(items):
            is_last = i == len(items) - 1
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{Fore.LIGHTYELLOW_EX}{key}{Style.RESET_ALL}:", end="")
            if isinstance(value, (dict, list)):
                print()
                new_prefix = prefix + ("    " if is_last else "│   ")
                printt(value, new_prefix)
            else:
                print(f" {colorize(value)}")
    elif isinstance(data, list):
        for i, item in enumerate(data):
            is_last = i == len(data) - 1
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{Fore.LIGHTCYAN_EX}Item {i}{Style.RESET_ALL}")
            new_prefix = prefix + ("    " if is_last else "│   ")
            printt(item, new_prefix)
    else:
        print(f"{prefix}{colorize(data)}")

def pprintt(data):
    """
    Pretty print a data structure with colorized output.
    
    Args:
        data: The data structure to print (can be dict, list, or any other type).
    """
    return pprint(data)