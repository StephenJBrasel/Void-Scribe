from void_scribe import NameGenerator
import random
import pickle
import requests
import pkg_resources
import nlglib

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
    subject = NameGenerator.getNames(amount = 1)[0]
    direct_object = NameGenerator.getNames(amount = 1)[0]
    print(f"{subject} {currentVerb} {direct_object}.")
    # print(currentVerb)
    # obj = requests.get("http://api.conceptnet.io/c/en/" + currentVerb).json()
    # for key in obj['edges']:
    #     print(f'{key}')
    #     print()
    # print(currentVerb)

if __name__ == "__main__":
    generatePrompt()