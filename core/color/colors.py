from colorama import Fore, Style, init

init()


def green(string: str):
    return f"{Fore.GREEN}{string}{Fore.RESET}"


def yellow(string: str):
    return f"{Fore.YELLOW}{string}{Fore.RESET}"


def cyan(string: str):
    return f"{Fore.CYAN}{string}{Fore.RESET}"


def red(string: str):
    return f"{Fore.RED}{string}{Fore.RESET}"


def blue(string: str):
    return f"{Fore.BLUE}{string}{Fore.RESET}"


def magenta(string: str):
    return f"{Fore.MAGENTA}{string}{Fore.RESET}"


def white(string: str):
    return f"{Fore.WHITE}{string}{Fore.RESET}"


def bgreen(string: str):
    return f"{Style.BRIGHT}{green(string)}{Style.RESET_ALL}"


def byellow(string: str):
    return f"{Style.BRIGHT}{yellow(string)}{Style.RESET_ALL}"


def bcyan(string: str):
    return f"{Style.BRIGHT}{cyan(string)}{Style.RESET_ALL}"


def bred(string: str):
    return f"{Style.BRIGHT}{red(string)}{Style.RESET_ALL}"


def bblue(string: str):
    return f"{Style.BRIGHT}{blue(string)}{Style.RESET_ALL}"


def bmagenta(string: str):
    return f"{Style.BRIGHT}{magenta(string)}{Style.RESET_ALL}"


def bwhite(string: str):
    return f"{Style.BRIGHT}{white(string)}{Style.RESET_ALL}"
