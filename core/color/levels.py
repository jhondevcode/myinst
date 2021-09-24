import core.color.colors as colors


def info(message: str):
    print(colors.bcyan(message))


def warn(message: str):
    print(colors.byellow(message))


def error(message: str):
    print(colors.bred(message))


def success(message: str):
    print(colors.bgreen(message))
