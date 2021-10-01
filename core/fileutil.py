#!/usr/bin/python

"""
This module provides specialized classes to safely operate text files. Among
its uses are: searching, adding, replacing and deleting lines of text from
non-binary files.
"""

from typing import List
from os import path
from json import load
from core import logger


def contains_line(file: str, line: str) -> bool:
    """
    This function will check if a given string is inside a text file, in case
    it has located the first occurrence of the string it will return true.
    """
    if path.isfile(file):
        with open(file, mode="r", encoding="utf-8") as text_file:
            state = line in text_file.read()
        return state
    else:
        logger.logger.error(f'The file "{file}" does not exist')
        return False


def contains_lines(file: str, lines: List[str]) -> bool:
    """
    This function will go through a list of words looking for the existence of
    each word within the file and incrementing a counter for each time it finds
    the word and at the end it will verify that the number of occurrences is
    equal to the number of strings given.
    """
    if path.isfile(file):
        line_counter = 0
        text_file = open(file, mode="r", encoding="utf-8")
        data = text_file.read()
        text_file.close()
        for line in lines:
            if line in data:
                line_counter += 1
        return line_counter == len(lines)
    else:
        logger.logger.error(f'The file "{file}" does not exist')
        return False


def dict_from_json(file: str, key):
    if path.isfile(file):
        json_file = open(file, mode="r", encoding="utf-8")
        data = load(json_file)
        json_file.close()
        if key in data:
            return data[key]
        else:
            return None
    return None


def replace_line(file: str, old: str, new: str):
    """This function replaces an old string with a new string within a text file."""
    if path.isfile(file):
        with open(file, mode="r", encoding="utf-8") as f_in:
            data = f_in.read()
        with open(file, mode="w", encoding="utf-8") as f_out:
            f_out.write(data.replace(old, new))
    else:
        logger.logger.error(f'The file "{file}" does not exist')


def replace_lines(file: str, olds: List[str], news: List[str]):
    """
    This replace function replaces each of the old strings within its corresponding
    list with the new strings that are also in its list, all of this is done within
    the specified text file.
    """
    if len(olds) == len(news):
        if path.isfile(file):
            with open(file, mode="r", encoding="utf-8") as f_in:
                data = f_in.read()
            list_index = 0
            while list_index < len(olds):
                data = data.replace(olds[list_index], news[list_index])
                list_index += 1
            with open(file, mode="w", encoding="utf-8") as f_out:
                f_out.write(data)
        else:
            logger.logger.error(f'The file "{file}" does not exist')
    else:
        logger.logger.error(
            "The function received two lists with different amounts of elements"
        )


def write_line(file: str, line: str):
    """This function writes a string at the end of the file."""
    if path.isfile(file):
        with open(file, mode="a", encoding="utf-8") as text_file:
            text_file.write(line)
    else:
        logger.logger.error(f'The file "{file}" does not exist')


def write_lines(file: str, lines: List[str]):
    """This function writes a list of strings at the end of the file."""
    if path.isfile(file):
        with open(file, mode="a", encoding="utf-8") as text_file:
            text_file.writelines(map(lambda line: line + "\n", lines))
    else:
        logger.logger.error(f'The file "{file}" does not exist')
