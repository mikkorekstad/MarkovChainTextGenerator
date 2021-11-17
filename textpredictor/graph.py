# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

"""
This module contain the MarkovChain class. A MarkovChain object is in this case a graph that can
be used to calculate probabilities and predict the n next words after receiving training data.
"""

from .file_reader import create_file_reader
from .node import Node
import random


class MarkovChain:
    """
    This class should take the name of a text file in string format and create a Markov Chain graph
    with information about the probabilities of different words following each other.

    An object from this class should be able to give a prediction of the n next words when given
    a starting point. The starting point have to be a word within the training dataset.
    """
    def __init__(self, case_sensitivity=False):
        """
        Constructor takes no arguments.
        """
        self.file_path = None
        self.case_sensitivity = case_sensitivity
        self.nodes = {}

    def train_path(self, file_path):
        """
        Takes a file path as input and trains the Markov Chain on the data contained in the file.
        :param file_path: str
        """
        file_reader = create_file_reader(file_path=file_path, case_sensitive=self.case_sensitivity)
        previous_word = None
        for word in file_reader:
            if previous_word:
                self.nodes[previous_word].update_connection(word)
            if word not in self.nodes:
                self.nodes[word] = Node(word)
            previous_word = word

    def show_nodes(self):
        """Print out information about the nodes and the associated probabilities."""
        for node_name, node in self.nodes.items():
            probabilities, nodes = node.get_probabilities()
            print(f'{node_name}:')
            for probability, node_ in zip(probabilities, nodes):
                print(f'{node_} {probability * 100} % ')
            print('-' * 20)

    def predict(self, starting_node, n=1):
        """
        Takes in a word in string format as a starting node, and an integer value n to predict the
        n next words.
        :param starting_node: str
        :param n: int
        :return: array
        """

        # Check user input
        if not self.case_sensitivity:
            starting_node = starting_node.lower()
        if starting_node not in self.nodes:
            raise ValueError(f'Starting word: {starting_node} is not in the training data!')
        if type(n) != int:
            raise ValueError('Please insert n as an integer value!')

        # Create predictions
        predictions = []
        current_word = starting_node
        for i in range(n):
            probabilities, nodes = self.nodes[current_word].get_probabilities()
            if not probabilities:
                print(f'The word {current_word} has no subsequent connections.')
                return predictions
            prediction = random.choices(nodes, probabilities)[0]
            predictions.append(prediction)
            current_word = prediction
        return predictions
