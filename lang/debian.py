from lang.common import CommonInstallations
from core.color.colors import green
from core.color import info, error, print_yellow, print_cyan
from core.utilities import clear
from core.logger import logger
from subprocess import call


class DebianLangInstaller(CommonInstallations):

    def __init__(self):
        super(DebianLangInstaller, self).__init__()

    def install_build_essential(self):
        clear()
        info("Installing build-essential...\n")
        logger.info("Installing build-essential")
        return call("sudo apt install build-essential -y".split(" "))

    def install_jdk(self):
        clear()
        jdk_versions = [8, 11, 13, 16, 17]
        while True:
            info("=====> OpenJDK installer <=====")
            for index, version in enumerate(jdk_versions):
                print_cyan(f"{index + 1}) OpenJDK {version}")
            print_cyan("6) Back")
            entered = input(green("Option [1-6]: "))
            if entered.isnumeric():
                entered = int(entered) - 1
                if 0 <= entered <= 4:
                    clear()
                    info(f"Installing OpenJDK {jdk_versions[entered]}...\n")
                    logger.info(f"Installing OpenJDK {jdk_versions[entered]}")
                    return call(f"sudo apt install openjdk-{jdk_versions[entered]}-jdk -y".split(" "))
                elif entered == 5:
                    clear()
                    break
                else:
                    clear()
                    error("The requested option is not available")
            else:
                clear()
                error("The entered value is not valid")

    def install_ruby(self):
        """Install ruby in debian"""
        super().install_ruby()
        return call("sudo apt install ruby -y".split(" "))

    def register_processes(self):
        self.add_process(["build-essential", self.install_build_essential])
        super().register_processes()

    def run(self):
        clear()
        self.add_item(1, "build-essential")
        super().run()
        while True:
            print(green("=====> Programming language installer <====="))
            for order, name in self.get_items().items():
                print_yellow(f"{order}) Install {name}")
            print_yellow("10) Back")
            entered = input(green(f"Option [1-10]: "))
            if entered.isnumeric():
                entered = int(entered) - 1
                if 0 <= entered <= 8:
                    process = self.get_process(entered)
                    self.check_exit_code(process[1](), process[0])
                elif entered == 9:
                    clear()
                    break
                else:
                    clear()
                    error("The requested option is not available")
            else:
                clear()
                error("The entered value is not valid")
