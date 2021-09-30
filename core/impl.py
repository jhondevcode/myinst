"""
This module contains unimplemented abstract classes, the classes present here
are used for multiple purposes.
"""

from core.color import success, error
from core.constants import EXIT_SUCCESS
from core.utilities import clear


class InstallWizard:
    """Template for creating classes for install wizard"""

    def __init__(self):
        super(InstallWizard, self).__init__()
        self.__objectives = {}
        self.__process = []
        self.register_processes()

    def add_item(self, key, value):
        self.__objectives[key] = value
        return self

    def get_items(self):
        return self.__objectives

    def add_process(self, process):
        self.__process.append(process)

    def get_process(self, index: int):
        return self.__process[index]

    def check_exit_code(self, value: int, name: str, for_clear=True):
        if for_clear:
            clear()
        if value == EXIT_SUCCESS:
            success(f"The {name} installation completed successfully.")
        else:
            error(f"{name} could not be installed.")

    def register_processes(self):
        pass

    def run(self):
        """This method will be used to launch the installation wizard"""
        pass
