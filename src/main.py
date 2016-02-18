#!/usr/bin/env python

import sys
# from abjad import *
from random import choice, shuffle
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

        if tokens[0] == 'generate':
            if len(tokens) < 2:
                print "Error: generate takes 1 argument (n)"
                continue
            n = int(tokens[1])
            generate(n)

        elif tokens[0] == 'path':
            if len(tokens) < 3:
                print "Error: path takes 2 arguments (start, end)"
                continue
            start = int(tokens[1])
            end = int(tokens[2])
            path(start, end)

        elif tokens[0] == 'add':
            new_set = eval(tokens[1])
            new_set.sort()
            new_superset = Superset(new_set, cardinalities)
            sets.append(new_set)
            supersets.append(new_superset)

        elif tokens[0] == 'add_r':
            if len(tokens) == 1:
                n = 1
            else:
                n = int(tokens[1])
            for i in range(n):
                new_set = randomPset()
                new_superset = Superset(new_set, cardinalities)
                sets.append(new_set)
                supersets.append(new_superset)

        elif tokens[0] == 'list':
            for x in sets:
                print x

        elif tokens[0] == 'clear':
            clear()

        elif tokens[0] == 'populate':
            if len(tokens) < 3:
                print "Error: populate takes 2 arguments (num_sets, train)"
                continue
            n = int(tokens[1])
            m = int(tokens[2])
            populate(n, m)

        elif tokens[0] == 'train':
            if len(tokens) < 2:
                print "Error: populate takes 1 argument (n)"
                continue
            n = int(tokens[1])
            train(n)

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


def path(start, end):
    if start not in range(len(sets)) or end not in range(len(sets)):
        print "Error: Index out of bounds."
        return
    paths = graph.paths(start, end)
    path = choice(paths)
    tokens = makeTokens(path)
    execute(tokens)
    return


def generate(n):
    path = graph.walk(n)
    tokens = makeTokens(path)
    execute(tokens)
    return


def populate(n, m):
    clear()
    [ sets.append(randomPset()) for i in range(n) ]

    for pset in sets:
        superset = Superset(pset, cardinalities)
        supersets.append(superset)

    train(m)


def train(n):
    for i in range(n):
        chain = list()
        r = range(len(sets))
        shuffle(r)
        [ chain.append(r.pop()) for i in range(len(sets)) ]
        tokens = makeTokens(chain)
        execute(tokens)
    return


def makeTokens(l):
    l = [ str(x) for x in l ]
    op = ['->'] * len(l)
    tokens = [ item for pair in zip(l,op) for item in pair ]
    tokens.pop()
    return tokens


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
    exclude = ['generate', 'populate', 'train', 'add_r']

    for x in tokens:
        if x.isdigit():
            if int(x) > len(sets)-1 and tokens[0] not in exclude:
                print "Error: There are only " + str(len(sets)) + " sets in the pset bank."
                return True
    return False


def randomPset():
    tones = range(12)
    shuffle(tones)
    pset = list()
    for i in range(choice([3,4,5])):
        pset.append(tones.pop())
    pset.sort()
    return pset


def clear():
    del sets[:]
    del supersets[:]
    del sequence[:]
    del seq_i[:]
    graph.clear()


main()
