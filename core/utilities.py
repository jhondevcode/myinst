#!/usr/bin/python

"""
Here utility functions are defined for all types of processing, from text to
links and files.
"""
from core.constants import EXIT_SUCCESS, EXIT_FAILURE, ARCH, DEBIAN, FEDORA, MANJARO
from pathlib import Path
from core import logger
from platform import release
import os
import tarfile
import zipfile


def clear():
    """This function runs the process to clean up the terminal."""
    os.system("clear")


def get_os_name() -> str:
    """This function is in charge of detecting the type of distribution to which the OS belongs."""
    if ARCH in release().lower():
        return ARCH
    elif MANJARO in release().lower():
        return MANJARO
    else:
        if os.path.isfile("/usr/bin/apt"):
            return DEBIAN
        elif os.path.isfile("/usr/bin/dnf"):
            return FEDORA
        else:
            return ""


def get_user_home():
    """This function returns the location of the user's home directory."""
    return Path.home()


def uncompress_zip(path: str, extract: str) -> bool:
    """This function is used to unzip a zip file to a specific location."""
    try:
        with zipfile.ZipFile(path, mode="r") as zip_file:
            zip_file.extractall(extract)
        zip_file.close()
        return EXIT_SUCCESS
    except Exception as ex:
        logger.logger.error(ex)
        return EXIT_FAILURE


def uncompress_tar(path: str, extract: str) -> bool:
    """This function is used to unzip a tar file to a specific location."""
    try:
        tar_file = tarfile.open(path)
        tar_file.extractall(extract)
        tar_file.close()
        return EXIT_SUCCESS
    except Exception as ex:
        logger.logger.error(ex)
        return EXIT_FAILURE
