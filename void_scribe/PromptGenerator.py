from void_scribe import NameGenerator
import random
import pickle
import requests # Datamuse, ConceptNet
import pkg_resources
from nlglib.realisation.simplenlg.realisation import Realiser
from nlglib.lexicalisation import Lexicaliser
from nlglib.macroplanning import *
from nlglib.microplanning import *
from nlglib.features import TENSE
import void_scribe

nameType = [
    "americanForenames",
    "dutchForenames",
    "frenchForenames",
    "germanForenames",
    "iselandicForenames",
    "indianForenames",
    "irishForenames",
    "italianForenames",
    "japaneseForenames",
    # "romanEmperorForenames",
    "russianForenames",
    "spanishForenames",
    "swedishForenames"

    # "scottishSurnames",

    # "tolkienesqueForenames",
    # "werewolfForenames"
    ]

actions = {# destroy, create, modify, interact
    "None":[],
    "think":[],
    "observe":[],

    "travel":[],
    "lead":[],
    "follow":[],
    "interact":[], # give quest to someone else, get information
    
    "acquire":[], # gather resources/items
    "give":[],
    "drop":[],
    "utilize":[],

    "harm":[],
    "heal":[],
    "guard":[],
    "craft":[]
}

templates={
    'travel': Clause(Var(0), VP('travel', complements=[PP('to', Var(1))], features={'TENSE' : 'future', 'MOOD': 'IMPERATIVE'})),
    "lead": Clause(Var(0), VP('lead', Var(1), complements=[PP('to', Var(2))], features={'TENSE':'future'})), 
    "follow": Clause(Var(0), ),
    "interact": Clause(Var(0), ),
    
    "acquire": Clause(Var(0), ),
    "give": Clause(Var(0), ),
    "drop": Clause(Var(0), ),
    "utilize": Clause(Var(0), ),

    "harm": Clause(Var(0), ),
    "heal": Clause(Var(0), ),
    "guard": Clause(Var(0), ),
    "craft": Clause(Var(0), )
    }

lex = Lexicaliser(templates)

realise_en = Realiser(host='nlg.kutlak.info', port=40000)

def loadPickle(data = None, fileName = "ActionVerbs.p"):
    path = pkg_resources.resource_filename('void_scribe', 'data/')
    path += fileName
    with open(path, "rb") as JamsJelliesAndPreserves:
        data = pickle.load(JamsJelliesAndPreserves)
    return data

def lexicalizeString(stringy):
    return realise_en(lex(formula_to_rst(expr(stringy))))

def synonym(stringy, pos='v'):
    ret = []
    obj1 = requests.get("https://api.datamuse.com/words?rel_syn=" + stringy).json()
    obj2 = requests.get("https://api.datamuse.com/words?ml=" + stringy).json()
    for i, item in enumerate(obj2):
        if('score' in item.keys()):
            if(item['score'] > 50):
                if('tags' in item.keys()):
                    if(pos in item['tags']):
                        ret.append(item['word'])
        # ret.append(item['word'] if (item['score'] > 100 and 'v' in item['tags']))
    print(stringy)
    return ret

def generatePrompt(seed = None, promptType = None):
    random.seed(seed)
    ND = void_scribe.NamesDictionary()

    ActionVerbs = loadPickle()
    currentVerb = random.choice(ActionVerbs)
    characters = []
    places = []
    verbs = []
    tempPlaceNames = ND.filterNameTypes(tags=["Reality"], category="Places")
    placeNames = []
    for item in tempPlaceNames:
        if "placeName" not in item:
            placeNames.append(item)
        

    characters.append(NameGenerator.realNames(Name_Type=random.choice(nameType), amount = 1)[0].capitalize())
    places.append(NameGenerator.realNames(Name_Type=random.choice(placeNames), amount = 1)[0].capitalize())
    verbs.append('travel')

    ret = lexicalizeString(f'travel({characters[0]}, {places[0]})')
    print(ret)
    return ret


if __name__ == "__main__":
    # print(synonym('travel', 'v'))
    # lexicalizeString(r'travel(arthur, Camelot)')
    generatePrompt()