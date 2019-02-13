from nlglib.realisation.simplenlg.realisation import Realiser
from nlglib.microplanning import *
import json
import random
from void_scribe import NameGenerator

realise = Realiser(host='nlg.kutlak.info')

leadExamplePath = 'C:/Users/thepe_000/Desktop/PP5/Void-Scribe/void_scribe/data/PromptTemplates/lead.json'

def loadPromptFromJSON(filepath):
    # Loads a given json file and returns the data.
    # filepath specifies the location of the file.
    with open(filepath) as f:
        data = json.load(f)
    return data

def selectNameTypeAndGenerateWord(nameTypes):
    # Selects a random NameType from the list passed, then calls for generation.
    # Currently utilizes realNames over generateMarkovNames
    # Additionally capitalizes words. (though this should be a functionality moved to NameGenerator)
    chosenNameType = random.randint(0, len(nameTypes) - 1)
    chosenNameType = nameTypes[chosenNameType]
    generatedWord = NameGenerator.realNames(chosenNameType, 1)[0]
    generatedWord = generatedWord.capitalize()
    return generatedWord

def chooseWord(words):
    # Simply chooses a random word from a list of such.
    chosenWord = random.randint(0, len(words) - 1)
    return words[chosenWord]

def generateElement(elementJSON):
    # Generates an element as defined by nlglib
    # It is given the JSON encoding for the element and
    # runs corresponding process to generate or pick the word.
    # Should an element have more than one componet (ie 'to place' rather than 'place')
    # this will join them with space characters
    elementParts = []
    for elementComponet in elementJSON:
        if "Generate" in elementComponet.keys():
            elementParts.append(selectNameTypeAndGenerateWord(elementComponet["Generate"]))
        if "Choose" in elementComponet.keys():
            elementParts.append(chooseWord(elementComponet["Choose"]))
        if "Word" in elementComponet.keys():
            elementParts.append(elementComponet["Word"])
    elementPartCount = len(elementParts)
    if elementPartCount == 0:
        return elementParts[0]
    else:
        return " ".join(elementParts)
        
def contructClauseArguments(promptJSON):
    # Given a prompt JSON object this will flatten it.
    # Loops through each element, then appends features
    clauseConstructorArguments = {}
    for argument in promptJSON['phrase'].keys():
        elementData = promptJSON['phrase'][argument]
        clauseConstructorArguments[argument] = generateElement(elementData)
    if 'features' in promptJSON.keys():
        clauseConstructorArguments['features'] = promptJSON['features']
    return clauseConstructorArguments

def realisePrompt(clauseArguments):
    # Unpacks the the arguments into the Clause contructor
    # Runs the realization web requests then returns the result
    clause = Clause(**clauseArguments)

    return realise(clause)
