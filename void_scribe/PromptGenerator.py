from void_scribe import NameGenerator
import random
import pickle
import requests # Datamuse, ConceptNet
import pkg_resources
from nlglib.realisation.simplenlg.realisation import Realiser
from nlglib.microplanning import *
from nlglib.features import TENSE

realise_en = Realiser(host='nlg.kutlak.info', port=40000)

def loadPickle(data = None, fileName = "ActionVerbs.p"):
    path = pkg_resources.resource_filename('void_scribe', 'data/')
    path += fileName
    with open(path, "rb") as JamsJelliesAndPreserves:
        data = pickle.load(JamsJelliesAndPreserves)
    return data

def generatePrompt(seed = None):
    random.seed(seed)

    ActionVerbs = loadPickle()
    currentVerb = random.choice(ActionVerbs)
    nouns = []

    nouns.append(NameGenerator.realNames(amount = 1)[0].capitalize())
    nouns.append(NameGenerator.realNames(amount = 1)[0].capitalize())

    p = Clause(NP(nouns[0]), VP(currentVerb), NP(nouns[1]))
    p[TENSE] = TENSE.future
    print(p)
    ret = realise_en(p)
    print(ret)
    # obj = requests.get("http://api.conceptnet.io/c/en/" + currentVerb).json()
    # for key in obj['edges']:
    #     print(f'{key}')
    #     print()
    # print(currentVerb)
    return ret


if __name__ == "__main__":
    generatePrompt()