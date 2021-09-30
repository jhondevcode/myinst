"""
This module provides classes and functions that work on all supported Linux
distros.
"""

from core.color import info
from core.impl import InstallWizard
from core.logger import logger
from core.utilities import clear
from os import system


class CommonInstallations(InstallWizard):
    """
    This class provides common installation methods for each distribution, as
    well as some of its own.

    The inheriting installer classes offer two ways to install: official
    repository, latest version (language website).
    """

    def __init__(self):
        super(CommonInstallations, self).__init__()

    def install_go(self):
        """
        This method will install go from the official tarball of the go
        website, with that you will have the latest version of the language.
        """
        pass

    def install_groovy(self):
        """
        This method installs the groovy programming language from an official
        tarball.
        """
        pass

    def install_jdk(self):
        """
        This method will be customized for each distribution, the jdk versions
        will be obtained from the distribution's repositories.
        """
        pass

    def install_kotlin(self):
        """This method installs kotlin from an official tarball."""
        pass

    def install_nodejs(self):
        """
        This method installs nodejs from a tarball. It offers two versions of
        installation: LTS, Current.
        """
        pass

    def install_ruby(self):
        """The ruby distribution will be different in each distribution."""
        clear()
        info(f"Installing Ruby...\n")
        logger.info(f"Installing Ruby")

    def install_rust(self) -> int:
        """
        This method does the installation of rust and its tools through rustup
        so it will not depend on the distribution.
        """
        clear()
        info("Installing the rust programming language...")
        return system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")

    def install_scala(self):
        """
        This method offers the installation of scala to the latest version from
        a tarball.
        """
        pass

    def register_processes(self):
        self.add_process(["Apache groovy", self.install_groovy])
        self.add_process(["Golang", self.install_go])
        self.add_process(["Kotlin", self.install_kotlin])
        self.add_process(["NodeJS", self.install_nodejs])
        self.add_process(["OpenJDK", self.install_jdk])
        self.add_process(["Ruby", self.install_ruby])
        self.add_process(["Rust", self.install_rust])
        self.add_process(["Scala", self.install_scala])

    def run(self):
        self.add_item(2, "Apache groovy")\
            .add_item(3, "Golang")\
            .add_item(4, "Kotlin")\
            .add_item(5, "NodeJS")\
            .add_item(6, "OpenJDK")\
            .add_item(7, "Ruby")\
            .add_item(8, "Rust")\
            .add_item(9, "Scala")
