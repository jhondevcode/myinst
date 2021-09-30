"""
This module offers classes for installing programming languages on archlinux
and arch-based distributions.
"""

from subprocess import call
from lang.common import CommonInstallations


# noinspection PyMethodMayBeStatic
class ArchLangInstaller(CommonInstallations):
    """
    This class provides specific methods to install programming languages from
    official repositories.
    """

    def __init__(self):
        super(ArchLangInstaller, self).__init__()

    def install_base_devel(self):
        """
        This method performs the installation of the basic development
        components: gcc, g ++, make, etc, in arch.
        """
        return call("sudo pacman -S base-devel --noconfirm".split(" "))

    def install_jdk(self):
        """
        This method shows a wizard with all the versions of the JDK available
        in the official arch repositories.
        """
        jdk_versions = [7, 8, 11, 16]

    def install_ruby(self):
        """
        This method performs the installation of the ruby language from the
        official arch linux repositories.
        """
        return call("sudo pacman -S ruby --noconfirm".split(" "))

    def install_yay(self):
        """
        This method install yay from the source code as it is not available
        in the official repositories.
        """
        pass

    def run(self):
        pass


class ManjaroLangInstaller(ArchLangInstaller):
    """
    This class allows you to install programming languages from the official
    manjaro repositories.
    """

    def __init__(self):
        super(ManjaroLangInstaller, self).__init__()

    def install_yay(self):
        """This method install yay from the official manjaro repositories."""
        pass

    def run(self):
        pass
