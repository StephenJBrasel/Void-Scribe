from void_scribe import NameGenerator
import random
import pickle
import requests
import pkg_resources
from nlglib.realisation.simplenlg.realisation import Realiser
from nlglib.realisation.simplenlg.realisation import BasicRealiser
from nlglib.microplanning import *

# realise_en = Realiser(host='nlg.kutlak.info', port=40000)
realise_en = BasicRealiser()

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
    subject = NameGenerator.getNames(amount = 1)[0].capitalize()
    direct_object = NameGenerator.getNames(amount = 1)[0].capitalize()
    p = Clause(NP(subject), VP(currentVerb), NP(direct_object))
    ret = realise_en(p)
    print(f"{subject} {currentVerb} {direct_object}.")
    print(ret)
    # obj = requests.get("http://api.conceptnet.io/c/en/" + currentVerb).json()
    # for key in obj['edges']:
    #     print(f'{key}')
    #     print()
    # print(currentVerb)
    return ret


if __name__ == "__main__":
    generatePrompt()