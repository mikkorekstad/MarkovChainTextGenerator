# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

import pytest
import textgenerator.main as chain


def test_markov_chain_text_generator():
    """
    Just some test.
    """
    assert chain.MarkovChain().some_val == 0

