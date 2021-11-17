# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

"""
This module contain the main function in the Markov Chain Text Generator.
"""

from graph import MarkovChain


def main(file_path, case_sensitivity=False):
    markov_graph = MarkovChain(case_sensitivity=case_sensitivity)
    markov_graph.train_path(file_path=file_path)
    return markov_graph


if __name__ == '__main__':
    graph = main('../text_files/numbers.txt')
    print(graph.predict('0', 100))
