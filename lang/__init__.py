"""
This module has all the necessary functionalities to install, update and
configure different programming languages.
"""

from core.utilities import clear, get_os_name, ARCH, MANJARO, DEBIAN, FEDORA
from core.color import error
from lang.debian import DebianLangInstaller
from lang.arch import ArchLangInstaller, ManjaroLangInstaller
from lang.fedora import FedoraLangInstaller


def execute_lang_module():
    clear()
    os_name = get_os_name()
    if os_name == DEBIAN:
        DebianLangInstaller().run()
    elif os_name == ARCH:
        ArchLangInstaller().run()
    elif os_name == MANJARO:
        ManjaroLangInstaller().run()
    elif os_name == FEDORA:
        FedoraLangInstaller().run()
    else:
        error("Your operating system is not supported")
