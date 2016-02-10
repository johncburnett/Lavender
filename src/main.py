#!/usr/bin/env python

import sys
from abjad import *
from graph import Graph
from superset import Superset

sets = [
        [0, 1, 5, 6],
        [1, 4, 5, 7],
        [2, 3, 9, 11],
        [3, 5, 10, 11]]
cardinalities = [6, 7, 8]

supersets = list()
graph = Graph()
sequence = list()
seq_i = list()


def main():

    # generate supersets
    for pset in sets:
        superset = Superset(pset, cardinalities)
        supersets.append(superset)

    while True:
        chain = raw_input("Enter a sequence: ")
        tokens = chain.split()
        if tokens[0] == 'exit':
            return
        if tokens[0] == 'generate':
            generate()
            continue
        execute(tokens)


def execute(tokens):
    j = 0 # where we are in the sequence
    for i, e in enumerate(tokens):
        if e.isdigit():
            index = int(e)

            if i == 0:
                sequence = list()
                seq_i = list()
                sequence.append(set(sets[index]))
                seq_i.append(index)
                continue

            operator = tokens[i-1]
            if operator == '->':
                sequence.append(bestFit(sequence[j], supersets[index].collections))
                seq_i.append(index)
                graph.connectNodes(supersets[index], supersets[seq_i[j-1]])
            elif operator == '!':
                continue
            j += 1

    print sequence
    return


def generate():
    print graph.nodes
    return


def bestFit(pset, collections):
    best_fit = set()
    max_tones = 0

    for collection in collections:
        for superset in collection:
            pset = set(pset)
            common_tones = pset.intersection(superset)
            if len(common_tones) > max_tones:
                best_fit = superset
                max_tones = len(common_tones)
    return best_fit

main()
