#!/usr/bin/env python

# import abjad
from itertools import combinations

class Superset():

    def __init__(self, pset, cardinalities):
        self.pset = pset
        self.collections = []
        # self.score = abjad.Score()

        # cardinalities = [6,7,8]
        for n in cardinalities:
            supersets = generateCollections(set(pset), n)
            self.collections.append(supersets)

        filtered_collections = []
        for coll in self.collections:
            filtered_collections.append(filterCollection(coll,10))
        self.collections = filtered_collections


# from Jeffrey Trevino's pitchCollections.py
def generateCollections(baseSet,collectionSize):
    chromaticSet = set(range(0,12))
    possibilities = chromaticSet.difference(baseSet)
    numberOfPitchesToChoose = collectionSize - len(baseSet)
    collections = []
    for combo in combinations(possibilities, numberOfPitchesToChoose):
        collections.append( baseSet.union(combo) )
    return collections


def intervalVector(pset):
    pset = list(pset)
    vector = [0] * 6

    for i in range(len(pset)):
        if i < len(pset):
            for j in range(i+1,len(pset)):
                interval = pset[j] - pset[i]
                if interval > 6:
                    interval = 12 - interval
                vector[interval-1] += 1
    return vector


def filterCollection(collection, min_width):
    pitch_sets = list(collection)
    scales = []

    for pset in pitch_sets:
        pset = list(pset)
        m2_count = 0

        for i in range(len(pset)):
            if m2_count > 2 or (pset[-1]-pset[0]) < min_width:
                break

            elif i < len(pset)-1:
                interval = pset[i+1] - pset[i]
                if interval == 1:
                    m2_count += 1
                elif interval > 2:
                    break
                else:
                    m2_count = 0

            elif i == len(pset)-1 and m2_count <= 1:
                scales.append(set(pset))

    return scales


def printCollection(collection):
    for pset in collection:
        pset = list(pset)
        print pset
    return


# def notateCollection(subset, collection):
    # abjad.abjad_configuration.set_default_accidental_spelling('flats')
    # subset_staff   = abjad.Staff()
    # superset_staff = abjad.Staff()

    # chord = abjad.Chord(subset, (1,1))
    # subset_staff.append(chord)

    # for pset in collection:
        # chord = abjad.Chord(pset, (1,1))
        # superset_staff.append(chord)

    # score = abjad.Score([subset_staff, superset_staff])
    # for chord in score[1]:
        # abjad.topleveltools.mutate(chord).respell_with_flats()
    # return score

