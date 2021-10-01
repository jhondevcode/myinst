"""
This module offers classes for installing programming languages on archlinux
and arch-based distributions.
"""

from os import chdir
from subprocess import call
from lang.common import CommonInstallations
from core.color import info, error, print_cyan
from core.color.colors import green
from core.constants import EXIT_SUCCESS, EXIT_FAILURE
from core.logger import logger
from core.utilities import clear
from core.dirtemp import prepare, get_path


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
        clear()
        info("Installing base-devel...\n")
        logger.info("Installing base-devel")
        return call("sudo pacman -S base-devel --noconfirm".split(" "))

    def install_jdk(self):
        """
        This method shows a wizard with all the versions of the JDK available
        in the official arch repositories.
        """
        jdk_versions = [7, 8, 11, 16]
        clear()
        while True:
            info("=====> OpenJDK installer <=====")
            for index, version in enumerate(jdk_versions):
                print_cyan(f"{index + 1}) OpenJDK {version}")
            print_cyan("5) Back")
            entered = input(green("Option [1-6]: "))
            if entered.isnumeric():
                entered = int(entered) - 1
                if 0 <= entered <= 2:
                    clear()
                    info(f"Installing OpenJDK {jdk_versions[entered]}...\n")
                    logger.info(f"Installing OpenJDK {jdk_versions[entered]}")
                    return call(f"sudo pacman -S jdk{jdk_versions[entered]}-openjdk --noconfirm".split(" "))
                elif entered == 3:
                    info(f"Installing OpenJDK {jdk_versions[entered]}...\n")
                    logger.info(f"Installing OpenJDK {jdk_versions[entered]}")
                    return call(f"sudo pacman -S jdk-openjdk --noconfirm".split(" "))
                elif entered == 4:
                    clear()
                    break
                else:
                    clear()
                    error("The requested option is not available")
            else:
                clear()
                error("The entered value is not valid")

    def install_ruby(self):
        """
        This method performs the installation of the ruby language from the
        official arch linux repositories.
        """
        clear()
        info("Installing ruby...\n")
        logger.info("Installing ruby")
        return call("sudo pacman -S ruby --noconfirm".split(" "))

    def install_yay(self):
        """
        This method install yay from the source code as it is not available
        in the official repositories.
        """
        prepare()
        chdir(get_path())
        exit_code = call("git clone https://aur.archlinux.org/yay.git".split(" "))
        if exit_code == EXIT_SUCCESS:
            chdir("yay")
            return call("makepkg -si --noconfirm".split(" "))
        else:
            return EXIT_FAILURE

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
        info("Installing yay...\n")
        logger.info("Installing yay")
        return call("sudo pacman -Syu yay --noconfirm".split(" "))

    def run(self):
        pass
