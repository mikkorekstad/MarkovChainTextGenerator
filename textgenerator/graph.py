# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

"""
This module contain the MarkovChain class. A MarkovChain object is in this case a graph that can
be used to calculate probabilities and predict the n next words after receiving training data.
"""


class MarkovChain:
    """
    This class should take the name of a text file in string format and create a Markov Chain graph
    with information about the probabilities of different words following each other.

    An object from this class should be able to give a prediction of the n next words when given
    a starting point. The starting point have to be a word within the training dataset.
    """
    def __init__(self):
        """
        Constructor takes no arguments.
        """
        self.file_path = None
        self.nodes = {}
        self.some_val = 0

    def train_path(self, file_path):
        """
        Takes a file path as input and trains the Markov Chain on the data contained in the file.
        :param file_path: str
        """
        pass

    def predict(self, starting_node, n):
        """
        Takes in a word in string format as a starting node, and an integer value n to predict the
        n next words.
        :param starting_node: str
        :param n: int
        :return: array
        """
        pass