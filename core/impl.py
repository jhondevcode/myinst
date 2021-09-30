"""
This module contains unimplemented abstract classes, the classes present here
are used for multiple purposes.
"""

from core.color import info, error
from core.constants import EXIT_SUCCESS


class InstallWizard:
    """Template for creating classes for install wizard"""

    def __init__(self):
        super(InstallWizard, self).__init__()

    def check_exit_code(self, value: int, name: str):
        if value == EXIT_SUCCESS:
            info(f"The {name} installation completed successfully.")
        else:
            error(f"{name} could not be installed.")

    def run(self):
        """This method will be used to launch the installation wizard"""
        pass
