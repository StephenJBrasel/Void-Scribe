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
    from void_scribe.NameGenerator import NameGenerator
    nameGenerator = NameGenerator()
    chosenNameType = random.randint(0, len(nameTypes) - 1)
    chosenNameType = nameTypes[chosenNameType]
    generatedWord = nameGenerator.retreiveNames(chosenNameType, 1)[0]
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
    # Takes a promptType, loads associated JSON file from Void-Web
    # Creates componet dictionary
    # Runs argument and realization for each clause
    # joins clauses
    from requests import post
    url = 'http://www.voidscribe.com//data/prompts'
    json = {"promptType":promptType}
    resp = post(url=url, json=json)

    if resp.status_code != 200:
        raise Exception('Encountered Network Error With Void-Web when requesting prompt type data')

    promptJSON = resp.json()
    
    componetDictionary = generateComponetDictionary(promptJSON['componets'])
    clauses = []
    for clauseJSON in promptJSON['clauses']:
        clauseContructorArguments = contructClauseArguments(componetDictionary, clauseJSON)
        clause = realiseClause(clauseContructorArguments)
        clauses.append(clause)
    return " ".join(clauses)

print(generatePrompt('acquire'))

