from void_scribe import NamesDictionary
from void_scribe import MarkovGen

ND = NamesDictionary.NamesDictionary()

def getNames(Name_Type = None, amount = 1):
    namesData = ND[Name_Type]
    markovDict = MarkovGen.createMarkovDictionary(namesData, 2)
    return MarkovGen.markovGenerate(markovDict, 2, amount)

def getNameTypes():
    return ND.keys()

