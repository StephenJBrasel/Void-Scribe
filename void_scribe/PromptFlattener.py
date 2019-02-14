from nlglib.realisation.simplenlg.realisation import Realiser
from nlglib.microplanning import *
import json
import random
from void_scribe import NameGenerator
import pkg_resources
import os

realise = Realiser(host='nlg.kutlak.info')

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
    for elementComponent in elementJSON:
        if "Generate" in elementComponent.keys():
            elementParts.append(selectNameTypeAndGenerateWord(elementComponent["Generate"]))
        if "Choose" in elementComponent.keys():
            elementParts.append(chooseWord(elementComponent["Choose"]))
        if "Word" in elementComponent.keys():
            elementParts.append(elementComponent["Word"])
    elementPartCount = len(elementParts)
    if elementPartCount == 0:
        return elementParts[0]
    else:
        return " ".join(elementParts)
        
def contructClauseArguments(promptJSON):
    # Given a prompt JSON object this will flatten it.
    # Loops through each element, then appends features and complements
    clauseConstructorArguments = {}
    for argument in promptJSON['phrase'].keys():
        elementData = promptJSON['phrase'][argument]
        clauseConstructorArguments[argument] = generateElement(elementData)
    if 'features' in promptJSON.keys():
        clauseConstructorArguments['features'] = promptJSON['features']
    if 'complements' in promptJSON.keys():
        complements = []
        for complementElementData in promptJSON['complements']:
            complementElement = generateElement(complementElementData)
            complements.append(complementElement)
        clauseConstructorArguments['complements'] = complements

    return clauseConstructorArguments

def realisePrompt(clauseArguments):
    # Unpacks the the arguments into the Clause contructor
    # Runs the realization web requests then returns the result
    clause = Clause(**clauseArguments)

    return realise(clause)

class PromptIndex():
    def __init__(self):
        # __DATA_PATH__ is the folder in which pickled name files are stored
        self.__DATA_PATH__ = pkg_resources.resource_filename('void_scribe', 'data/PromptTemplates/')
        # __index__ maps each Prompt_Type string to the filepath of its pickle data
        self.__index__ = self.__createIndex__(self.__DATA_PATH__)

    def __loadPromptJSON__(self, Prompt_Type):
        # Loads a given json file and returns the data.
        # filepath specifies the location of the file.
        with open(self.__index__[Prompt_Type]) as f:
            data = json.load(f)
        return data

    def __getitem__(self, key):
        if key not in self.keys():
            raise KeyError(f"Provided key: '{key}' is not a valid Prompt_Type, or a dictionary for the Prompt_Type does not exist.")

        return self.__loadPromptJSON__(key)

    def __len__(self):
        return len(self.__index__)

    def __createIndex__(self, path):
        #helper function, yields all files in a directory
        def files(path):  
            for file in os.listdir(path):
                if os.path.isfile(os.path.join(path, file)):
                    yield file

        index = {}
        for file in files(path):
            key = file.split('.')[0]
            index[key] = path + file
        return index

    def __updateIndex__(self):
        self.__index__ = self.__createIndex__(self.__DATA_PATH__)

    def __delitem__(self, key):
        self.remove(key)

    def __iter__(self):
        return self.__index__.__iter__()

    def keys(self):
        return list(self.__index__.keys())

    def items(self):
        for key in self.keys():
            yield (key, self.__getitem__(key))

    def values(self):
        for key in self.keys():
            yield self.__getitem__(key)
            
    def remove(self, prompt_type):
        # Returns True if an entry was removed, False if not found
        # CAUTION WILL DELETE DATA FROM DISK
        if type(prompt_type) != type(""):
            raise ValueError("Argument 'prompt_type' was not required type: {}, 'prompt_type' is of type: {}.".format(type(""), type(prompt_type)))
        elif prompt_type not in self.keys():
            return False
        else:
            # Delete pickle file
            os.remove(self.__index__[prompt_type])
            # Update index
            self.__updateIndex__()

PI = PromptIndex()
print(PI.keys())
for key in PI.keys():
    if key == 'harm':
        continue
    args = contructClauseArguments(PI[key])
    print(realisePrompt(args))
