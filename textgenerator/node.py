# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

"""
This module contains the node class which describe nodes in the graph algorithm.
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
        self.connections = {}

    def update_connection(self, node):
        """
        Takes node as input. Trains the connection by adding a value to the input node.
        If this is the first instance of the current word, we are adding it to connections.
        :param node: str
        """
        self.connections[node] = self.connections.get(node, 0) + 1

    def get_probabilities(self):
        """
        Calculates the probability for each word in the dict of connections.
        Returns the array of probabilities and the array of words with the associated probabilities.
        :return: array of probabilities, array of nodes
        """
        if not self.connections:
            print('This node has no connections!')
            return [], []
        else:
            total_connections = sum(self.connections.values())
            print(total_connections)
            nodes = []
            probabilities = []
            for node, count in self.connections.items():
                nodes.append(node)
                probabilities.append(count / total_connections)
                print(f'appended{count / total_connections}')
            return probabilities, nodes
