# -*- coding: utf-8 -*-

__author__ = 'Mikko Rekstad'
__email__ = 'mikkreks@nmbu.no'

import pytest
import textgenerator.node as node


@pytest.fixture
def dummy_node():
    """Create a dummy node for testing below."""
    return node.Node('Hello')


def test_create_node():
    """
    Test that a node is constructed.
    """
    assert node.Node('Hello')


@pytest.mark.parametrize("start_node, connecting_node, amount",
                         [('Hello', 'World', 100), ('I', 'Am', 10),
                          ('My', 'Name', 25), ('Lorem', 'Ipsum', 30)])
def test_update_connection(start_node, connecting_node, amount):
    """
    Test that we can create a node and then add an amount of connection to another node.
    """
    test_node = node.Node(start_node)
    for _ in range(amount):
        test_node.update_connection(connecting_node)

    # Assertions:
    assert test_node.node == start_node
    assert test_node.connections[connecting_node] == amount


@pytest.mark.parametrize("start_node, connecting_node, amount",
                         [('Hello', 'World', 100), ('I', 'Am', 10),
                          ('My', 'Name', 25), ('Lorem', 'Ipsum', 30)])
def test_probabilities_single_connection(start_node, connecting_node, amount):
    """
    Test that the probability to another node is 1 when there are only one connecting node.
    """
    test_node = node.Node(start_node)
    for _ in range(amount):
        test_node.update_connection(connecting_node)
    probabilities, nodes = test_node.get_probabilities()

    # Assertions:
    assert probabilities[0] == 1
    assert nodes[0] == connecting_node


@pytest.mark.parametrize("words, amounts, expected_probabilities",
                         [(['Hello', 'World'], [100, 100], [0.5, 0.5]),
                          (['Markov', 'Chain', 'Algorithm'], [10, 10, 20], [0.25, 0.25, 0.5]),
                          (['Hello', 'World', 'Hello'], [10, 20, 10], [0.5, 0.5])])
def test_get_probabilities(dummy_node, words, amounts, expected_probabilities):
    """Test get_probabilities in some different scenarios."""
    for i, word in enumerate(words):
        [dummy_node.update_connection(word) for _ in range(amounts[i])]
    probabilities, nodes = dummy_node.get_probabilities()

    # Assertions:
    assert probabilities == expected_probabilities
