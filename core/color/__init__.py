"""
This package provides functions for the output of colored text in the terminal.
It is a binding for the colorama library.
"""

from core.color.levels import *
from core.color import colors


def print_blue(message: str):
    print(colors.bblue(message))


def print_cyan(message: str):
    print(colors.cyan(message))


def print_green(message: str):
    print(colors.green(message))


def print_magenta(message: str):
    print(colors.magenta(message))


def print_red(message: str):
    print(colors.red(message))


def print_yellow(message: str):
    print(colors.yellow(message))


def print_white(message: str):
    print(colors.white(message))


def print_bblue(message: str):
    print(colors.bblue(message))


def print_bmagenta(message: str):
    print(colors.bmagenta(message))


def print_bwhite(message: str):
    print(colors.bwhite(message))
