#!/usr/bin/python

"""
This module provides the functions to access the temporary directory in which
the files will be downloaded, in the same way it provides the necessary
abstraction to operate on the temporary directory.
"""
from os import mkdir
from os.path import join, isdir
from shutil import rmtree
from core.utilities import get_user_home

__temp_dir__ = ""
__temp_dir_name__ = "mi_temp"


def __get_download_dir() -> str:
    download_dir = "/tmp"
    user_home = get_user_home()
    with open(
        join(join(user_home, ".config"), "user-dirs.dirs"), "r", encoding="utf-8"
    ) as xdg_file:
        for line in xdg_file:
            if "XDG_DOWNLOAD_DIR" in line:
                download_dir = (
                    line.replace("\n", "")
                    .replace('"', "")
                    .replace("$HOME", str(user_home))
                    .split("=")[1]
                )
                break
    return download_dir


def get_path():
    global __temp_dir__
    if __temp_dir__ == "":
        __temp_dir__ = join(__get_download_dir(), __temp_dir_name__)
    return __temp_dir__


def delete():
    if isdir(get_path()):
        rmtree(get_path())


def prepare():
    if not isdir(get_path()):
        mkdir(get_path())
