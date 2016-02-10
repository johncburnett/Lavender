#!/usr/bin/env python

from superset import Superset

class Graph():

    def __init__(self):
        self.nodes = dict()

    def addNode(self, data):
        if data not in self.nodes:
            self.nodes[data] = list()

    def connectNodes(self, a, b):
        if a not in self.nodes:
            self.addNode(a)
        if b not in self.nodes:
            self.addNode(b)
        self.nodes[a].append(b)
