from void_scribe import MarkovIndex, NamesDictionary, MarkovGen

MI = MarkovIndex()

def generateMarkovNames(Name_Type = None, amount = 1):
    namesMarkovDictionary = MI[Name_Type]
    return MarkovGen.markovGenerate(namesMarkovDictionary, 3, amount)

def realNames(Name_Type = 'americanForenames', amount = 1):
    from void_scribe import NamesDictionary
    from random import choice
    ND = NamesDictionary()
    ret = []
    for i in range(amount + 1):
        ret.append(choice(ND[Name_Type]['Data']))
    return ret

def validNameTypes():
    return MI.keys()


for key in validNameTypes():
    print(key)