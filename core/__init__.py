#!/usr/bin/python

"""
The core package has the necessary modules to: operate files, detect the system,
verify updates, establish configurations and many more utilities.
"""

from core.utilities import clear
from core.color import print_bwhite
from core.color.levels import error, info, success
from core.color.colors import yellow
from config import execute_config_module
from lang import execute_lang_module
from tool import execute_tools_module


def welcome_screen():
    pass


def show_options():
    while True:
        print_bwhite("=> Enter an option <=")
        print_bwhite("1) Tools")
        print_bwhite("2) Languages")
        print_bwhite("3) Configurations")
        print_bwhite("4) Exit")
        option = input(yellow("Option [1-4]: "))
        if option == "1":
            execute_tools_module()
        elif option == "2":
            execute_lang_module()
        elif option == "3":
            execute_config_module()
        elif option == "4":
            clear()
            info("Please visit https://github.com/jhondevcode")
            success("Thanks for using the myinst script ;)")
            break
        else:
            clear()
            error("Requested option not found")


def start():
    clear()
    welcome_screen()
    show_options()
