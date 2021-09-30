"""
This module has all the necessary functionalities to install, update and
configure different programming languages.
"""

from core.utilities import clear, get_os_name, ARCH, MANJARO, DEBIAN, FEDORA
from core.color import error
from core.logger import logger


def execute_lang_module():
    clear()
    os_name = get_os_name()
    if os_name == DEBIAN:
        try:
            from lang.debian import DebianLangInstaller
            installer = DebianLangInstaller()
            installer.run()
        except ImportError as ex:
            logger.error(ex)
    elif os_name == ARCH:
        try:
            from lang.arch import ArchLangInstaller
            installer = ArchLangInstaller()
            installer.run()
        except ImportError as ex:
            logger.error(ex)
    elif os_name == MANJARO:
        try:
            from lang.arch import ManjaroLangInstaller
            installer = ManjaroLangInstaller()
            installer.run()
        except ImportError as ex:
            logger.error(ex)
    elif os_name == FEDORA:
        try:
            from lang.fedora import FedoraLangInstaller
            installer = FedoraLangInstaller()
            installer.run()
        except ImportError as ex:
            logger.error(ex)
    else:
        error("Your operating system is not supported")
