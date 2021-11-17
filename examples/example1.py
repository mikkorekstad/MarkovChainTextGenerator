# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

"""
This is an example of how to use the markov chain text generator!
"""

from textpredictor.graph import MarkovChain

markov_graph = MarkovChain(case_sensitivity=False)
markov_graph.train_path(file_path='../text_files/lipsum.txt')
print(markov_graph.predict('lorem', 10))