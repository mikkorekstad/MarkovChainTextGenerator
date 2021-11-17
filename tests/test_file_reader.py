# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

import pytest
import unittest
import textpredictor.file_reader as file_reader


class TestingFileReader(unittest.TestCase):
    def test_file_reader(self):
        """Test some basic functionality of the file reader."""
        reader = iter(file_reader.FileReader('../text_files/numbers.txt'))

        for i in range(0, 51):
            assert next(reader) == str(i)
        with self.assertRaises(StopIteration):
            next(reader)
