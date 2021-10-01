"""
This module provides classes and functions that work on all supported Linux
distros.
"""

from core.constants import EXIT_FAILURE
from core.color import error, info, print_cyan
from core.color.colors import green
from core.impl import InstallWizard
from core.installation import install
from core.logger import logger
from core.utilities import clear
from core.dirtemp import prepare, get_path
from core.fileutil import dict_from_json, download_file, URLError
from os import system, chdir
from os.path import join


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
        def download_install(node_url: str) -> int:
            try:
                file_path = download_file(node_url, get_path())
                return install(file_path, "node", "NODE_HOME", filetype="tar", category="lang", tobin=True)
            except URLError as ex:
                logger.error(ex)
                return EXIT_FAILURE

        clear()
        json_data = dict_from_json(join(str(__file__).replace("/common.py", ""), "list.json"), "node")
        if json_data is not None:
            prepare()
            chdir(get_path())
            name: str = json_data["name"]
            url: str = json_data["url"]
            versions: list = json_data["versions"]
            while True:
                info("=====> NodeJS installer <=====")
                print_cyan(f"1) {name} LTS {versions[0]}")
                print_cyan(f"2) {name} Current {versions[1]}")
                print_cyan(f"3) Back")
                entered = input(green("Option [1-3]: "))
                if entered == 1:
                    clear()
                    url = url.replace("{VERSION}", versions[0])
                    info(f"Downloading {name} {versions[0]} from {url}")
                    return download_install(url)
                elif entered == 2:
                    clear()
                    url = url.replace("{VERSION}", str(versions[1]))
                    info(f"Downloading {name} {versions[1]} from {url}")
                    return download_install(url)
                elif entered == 3:
                    clear()
                    break
                else:
                    clear()
                    error("The requested option is not available")
        else:
            logger.error("Cannot find Node JS metadata")
        return EXIT_FAILURE

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
