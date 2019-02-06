from void_scribe import MarkovIndex
from void_scribe import MarkovGen

MI = MarkovIndex.MarkovIndex()

def generateMarkovNames(Name_Type = None, amount = 1):
    namesMarkovDictionary = MI['Name_Type']
    return MarkovGen.markovGenerate(namesMarkovDictionary, 2, amount)

def validNameTypes():
    return MI.keys()

