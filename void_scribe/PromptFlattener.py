from nlglib.realisation.simplenlg.realisation import Realiser
from nlglib.microplanning import *
import json
import random
import void_scribe
import pkg_resources
import os

realise = Realiser(host='nlg.kutlak.info')

def selectNameTypeAndGenerateWord(nameTypes):
    # Selects a random NameType from the list passed, then calls for generation.
    # Currently utilizes realNames over generateMarkovNames
    # Additionally capitalizes words. (though this should be a functionality moved to NameGenerator)
    chosenNameType = random.randint(0, len(nameTypes) - 1)
    chosenNameType = nameTypes[chosenNameType]
    generatedWord = void_scribe.realNames(chosenNameType, 1)[0]
    generatedWord = generatedWord.capitalize()
    return generatedWord

def chooseWord(words):
    # Simply chooses a random word from a list of such.
    chosenWord = random.randint(0, len(words) - 1)
    return words[chosenWord]

def generateComponet(componetJSON):
    # Generates an componet, defined as a single word that is part of a
    # element as defined by nlglib
    # It is given the JSON encoding for the componet and
    # runs corresponding process to generate or pick the word.
    if "Generate" in componetJSON.keys():
        return selectNameTypeAndGenerateWord(componetJSON["Generate"])
    if "Choose" in componetJSON.keys():
        return chooseWord(componetJSON["Choose"])
    if "Word" in componetJSON.keys():
        return componetJSON["Word"]

def generateComponetDictionary(componets):
    # Given the json dictionary of a prompt templates componets
    # This will run respective generation processes for each
    # and create a dictionary that has...
    # key as the hex id and value as the componet string
    componetDictionary = {}
    for componetID in componets.keys():
        componetDictionary[componetID] = generateComponet(componets[componetID])
    return componetDictionary

def contructClauseArguments(componetDictionary, clauseJSON):
    # Given a single clause's json structure and its associated
    # componet dictionary, this returns an unpackable argument argument
    # For the clause contructor

    def addBasicArgument(argument):
        # Helper function to avoid rewriting code
        if argument in clauseJSON.keys():
            componetIDs = clauseJSON[argument]
            elementComponets = []
            for componetID in componetIDs:
                componet = componetDictionary[componetID]
                elementComponets.append(componet)
            element = " ".join(elementComponets)
            clauseConstructorArguments[argument] = element

    clauseConstructorArguments = {}

    # Add basic arguments (one element arguments)
    addBasicArgument('subject')
    addBasicArgument('predicate')
    addBasicArgument('objekt')

    # Add features
    if 'features' in clauseJSON.keys():
        clauseConstructorArguments['features'] = clauseJSON['features']
    
    # Add complements
    if 'complements' in clauseJSON.keys():
        complements = []
        for complement in clauseJSON['complements']:
            complementComponets = []
            for componetID in complement:
                componet = componetDictionary[componetID]
                complementComponets.append(componet)
            complementElement = " ".join(complementComponets)
            complements.append(complementElement)
        clauseConstructorArguments['complements'] = complements

    return clauseConstructorArguments

def realiseClause(clauseArguments):
    # Unpacks the the arguments into the Clause contructor
    # Runs the realization web requests then returns the result
    clause = Clause(**clauseArguments)

    return realise(clause)

def generatePrompt(promptType):
    # Takes a promptType, loads associated JSON file
    # Creates componet dictionary
    # Runs argument and realization for each clause
    # joins clauses

    #Load prompt JSON from PromptIndex
    promptJSON = PI[promptType]
    
    componetDictionary = generateComponetDictionary(promptJSON['componets'])
    clauses = []
    for clauseJSON in promptJSON['clauses']:
        clauseContructorArguments = contructClauseArguments(componetDictionary, clauseJSON)
        clause = realiseClause(clauseContructorArguments)
        clauses.append(clause)
    return " ".join(clauses)

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

# PI = PromptIndex()
