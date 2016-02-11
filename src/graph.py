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

    def clear(self):
        self.nodes.clear()

    def paths(self, start, end):
        return findPaths(self.nodes, start, end)

def findPaths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = findPaths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

