from void_scribe import MarkovIndex, NamesDictionary, MarkovGen

MI = MarkovIndex()

def generateMarkovNames(Name_Type = None, amount = 1):
    namesMarkovDictionary = MI[Name_Type]
    names = MarkovGen.markovGenerate(namesMarkovDictionary, 3, amount)
    for i in range(0, len(names)):
        names[i] = "".join(names[i])
    return names

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

print(generateMarkovNames('pokemon', 5))