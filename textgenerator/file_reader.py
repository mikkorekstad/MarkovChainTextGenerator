# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

"""
This module contain the FileReader class. This is an iterable object that contains all the words in
the text file in subsequent order. The __next__ function should return the next word in the file.
The iterator should be a generator.
"""


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
        pass

    def __next__(self):
        """
        Iterate to the next value in this generator object.
        :return: str
        """
        pass