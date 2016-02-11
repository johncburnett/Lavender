#!/usr/bin/env python

import sys
# from abjad import *
from random import choice
from graph import Graph
from superset import Superset

sets = [
        [0, 1, 5, 6],
        [1, 4, 5, 7],
        [2, 3, 9, 11],
        [3, 5, 10, 11]]
cardinalities = [6, 7, 8]

supersets = list()
sequence = list()
seq_i = list()
graph = Graph()


def main():

    # generate supersets
    for pset in sets:
        superset = Superset(pset, cardinalities)
        supersets.append(superset)

    while True:
        chain = raw_input("<~lavender~>$ ")
        tokens = chain.split()

        if check(tokens):
            continue

        if tokens[0] == 'exit':
            return

        elif tokens[0] == 'generate':
            if len(tokens) < 3:
                print "Error: generate takes 2 arguments (start, end)"
                continue
            start = int(tokens[1])
            end = int(tokens[2])
            generate(start, end)

        elif tokens[0] == 'add':
            new_set = eval(tokens[1])
            new_superset = Superset(new_set, cardinalities)
            sets.append(new_set)
            supersets.append(new_superset)

        elif tokens[0] == 'list':
            for x in sets:
                print x

        elif tokens[0] == 'clear':
            clear()

        else:
            execute(tokens)


def execute(tokens):
    j = 0 # where we are in the sequence
    for i, e in enumerate(tokens):
        if e.isdigit():
            index = int(e)

            if i == 0:
                del sequence[:]
                del seq_i[:]
                sequence.append(set(sets[index]))
                seq_i.append(index)
                continue

            operator = tokens[i-1]
            if operator == '->':
                sequence.append(bestFit(sequence[j], supersets[index].collections))
                seq_i.append(index)
                graph.connectNodes(seq_i[j], seq_i[j+1])
            elif operator == '!':
                continue

            j += 1

    to_print = list()
    for x in sequence:
        y = list(x)
        y.sort()
        to_print.append(y)
    print to_print
    return


def generate(start, end):
    if start not in range(len(sets)) or end not in range(len(sets)):
        print "Error: Index out of bounds."
        return
    paths = graph.paths(start, end)
    path = choice(paths)

    path = [ str(x) for x in path ]
    operators = ['->'] * len(path)
    tokens = [ item for pair in zip(path,operators) for item in pair ]
    tokens.pop()
    execute(tokens)
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


def check(tokens):
    for x in tokens:
        if x.isdigit():
            if int(x) > len(sets)-1:
                print "Error: There are only " + str(len(sets)) + " sets in the pset bank."
                return True
    return False

def clear():
    del sets[:]
    del supersets[:]
    del sequence[:]
    del seq_i[:]
    graph.clear()


main()
