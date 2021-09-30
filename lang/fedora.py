from lang.common import CommonInstallations
from subprocess import call


# noinspection PyMethodMayBeStatic
class FedoraLangInstaller(CommonInstallations):

    def __init__(self):
        super(FedoraLangInstaller, self).__init__()

    def install_development_tools(self):
        return call("sudo dnf install @development-tools".split(" "))

    def install_jdk(self):
        pass

    def install_ruby(self):
        pass

    def run(self):
        pass
