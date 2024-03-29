# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

"""
This module contain the FileReader class. This is an iterable object that contains all the words in
the text file in subsequent order. The __next__ function should return the next word in the file.
The iterator should be a generator.
"""

import re

class FileReader:
    """
    An iterable object that contains the words from the text-file in subsequent order.
    """

    def __init__(self, file_path=None, case_sensitive=False):
        """
        Constructs a generator-object from the class if the file is found and of the right type.
        The supported file types are mainly txt.
        Support for case sensitivity is planned to be added.
        :param file_path: str
        :param case_sensitive: bool
        """
        if case_sensitive:
            self.case_sensitive = True
        else:
            self.case_sensitive = False
        self.file_path = file_path

    def filter_string(self, row):
        """
        Remove all special characters, and turn the string into a list of words. If the FileReader
        is case-sensitive, turn all characters to lowercase.
        :param row: str
        :return: list
        """

        pattern = r'[^A-Za-z0-9- ]+'
        row = re.sub(pattern, '', row)
        # ''.join(entry for entry in row if entry.isalnum())
        if not self.case_sensitive:
            row = row.lower()
        res = row.split()
        return res

    def __iter__(self):
        """
        Iterate to the next value in this generator object.
        :return: str
        """
        for row in open(self.file_path, 'r'):
            res = self.filter_string(row)
            for word in res:
                yield word


def create_file_reader(file_path=None, case_sensitive=False):
    """
    This function returns an iterable rather than a generator object.
    :param file_path: str
    :param case_sensitive: bool
    :return: iterable object
    """
    return iter(FileReader(file_path=file_path, case_sensitive=case_sensitive))
