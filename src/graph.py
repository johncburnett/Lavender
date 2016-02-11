#!/usr/bin/env python

from random import choice

class Graph():

    def __init__(self):
        self.nodes = dict()

    def addNode(self, data):
        if data not in self.nodes:
            self.nodes[data] = list()

    def connectNodes(self, a, b):
        self.addNode(a)
        self.addNode(b)
        self.nodes[a].append(b)

    def clear(self):
        self.nodes.clear()

    def paths(self, start, end):
        return findPaths(self.nodes, start, end)

    def walk(self, n):
        key = choice(self.nodes.keys())
        path = [key]
        for i in range(n):
            key = choice(self.nodes[key])
            path.append(key)
        return path

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

