# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

"""
This module contain the main function in the Markov Chain Text Generator.
"""


class Node:
    """
    In the Markov Chain Text Generator, the nodes (or vertices) represent words. The connections
    (or the edges) in this graph algorithm represents the probability weights.
    """

    def __init__(self, node):
        """
        Constructor of class Node takes parameter node (name of the word) in string form.
        :param node: str
        """
        self.node = node


class MarkovChain:
    """
    This class should take the name of a text file in string format and create a Markov Chain graph
    with information about the probabilities of different words following each other.

    An object from this class should be able to give a prediction of the n next words when given
    a starting point. The starting point have to be a word within the training dataset.
    """
    def __init__(self, text_path):
        """
        Constructor takes the path to the text file as a string and trains a Markov Chain Text -
        Generator object from this.
        :param text_path: str
        """
        self.text_path = text_path
        self.some_val = 0

    def predict(self, starting_node, n):
        """
        Takes in a word in string format as a starting node, and an integer value n to predict the
        n next words.
        :param starting_node: str
        :param n: int
        :return: array
        """
        pass


if __name__ == '__main__':
    print('markov chains are cool')