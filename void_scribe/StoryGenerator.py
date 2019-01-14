from void_scribe import NameGenerator
from void_scribe.data.Stories import data
import tracery
from tracery.modifiers import base_english

# class Entity():
#     components = []

# def makeCharacter():
#     character = Entity()
#     return character

def getStoryPrefabs():
    ret = []
    for i in data:
        ret.append(i)
    return ret

def generateTraceryStory(
        dataObject = None,
        Sentence_Type = 'quest', 
        amount = 3):
    if (dataObject == None) and (Sentence_Type == None):
        dataObject = data['hi']
    elif (dataObject == None) and (Sentence_Type != None):
        dataObject = data[Sentence_Type]
    ret = []
    for i in range(amount):
        grammar = tracery.Grammar(dataObject)
        grammar.add_modifiers(base_english)
        ret.append(grammar.flatten('#origin#'))
    return ret

# implement entity-component system
class character():
    # list of list of goals, higher order lists are lower priority. 
    # Name
    #   option to generate name after race and cultural elements to more appropriately reflect IRL name creation.
    # Race
    # 
    # Health
    # 
    # dictionary of personality attributes.
    def __init__(self):
        print('hello, character!')
        self.goals = []
        self.goals.append(goal())
class goal():
    def __init__(self):
        print('GOOOOOOOOOOOOOAL!')
class item():
    def __init__(self):
        print('hi, item!')
class action():
    def __init__(self):
        print('hola, action!')

def generateStartingWorld(seed=None):
    world=None
    protagonist = character()
    # thing = item()
    # event = action()
    # print(event)
    # (randomly) select main goal [Vengeance, Power, Love, Family, Exploration]
    # goals should be the quest,
    # goals should have interrupts, [Vengeance: [deathOfAntagonist, protagonistNotStrongEnough, protagonistMoralShift], Power:[...],...]
    # goals should be modified based on character personality traits, values, and needs

    # "QuestType": [#destroy, create, modify, interact
    # "[questType:#travel#][reason:#travelReason#]", #go to [place]
    # "[questType:#escort#][reason:#escortReason#]", # #travel# #interact# #guard#
    # "[questType:#deliver#][reason:#deliverReason#]", #bring [noun] to [person] at [place] [in [place]]
    # "[questType:#fetch#][reason:#fetchReason#]", #get [thing:noun] from [place] and bring #thing# to [other place]

    # "[questType:#destroy#][reason:#destroyReason#]", #destroy something/someone
    # "#setGuardQuestType#", #guard something, and if threat: destroy threat.

    # # "[questType:#giveQuest#][reason:#questReason#]", #give someone a quest, usually because they're more qualified.
    # # "[questType:#skill#][reason:#skillReason#]", #perform [action] using only N skill(s).
    # "[questType:#craft#][reason:#craftReason#]", #make [item]

    # "[questType:#solve#][reason:#solveReason#]" #bypass or complete puzzle/test
    # ]

    # fill quest roles (prot, ant, side character) with acceptable (randomly) generated attributes.
    #   ranges for those attributes can be refined by quest requirements
    # for prototype in quest[questCharProtoList]: # prototype is a list of character arguments: (Name, Race, Health, etc.)
    #   char = character(prototype)

    # final goal + opposing starting condition selected based on quest type.
    return world

def generateListOfEvents(world=None, seed=None):
    world = None
    # while (len(protagonist.goals()) > 0):
        # Protagonist selects one of it's available goals (ordered by urgency/optionality) 
        # if not protagonist.mainGoal:
        #     protagonist.mainGoal = protagonist.goals.pop()

        # uses filtering based on thinking-acting graph to decide on a single action 
        # actionChoice = getThoughtOrAction(protagonist.mainGoal)

        # action is sent to language processing.
        # thread.start(NLG, actionChoice)

        # action outcome is generated.
        #    the outcome of this action depends on character attributes as well as action interrupts.
        #       interrupts can result in action failures, character encounters, new mandatory or optional side quests of varying urgency or world events
        # actionOutcome = getWorldState(actionChoice)

        # Action outcome is then also sent to language processing.
        # thread.start(NLG, actionOutcome)

        # New goals are added to goal stack according to urgency/optionality
        #   goals are mandatory if standing in the way of completing currently selected quest.
        #   goals are optional if they have no direct relation to quest at hand.
        # for goal in actionOutcome.goals():
        #     protagonist.goals().insert(goal)

        # The protagonist continues thinking-acting until goal-stack is resolved.
    return world

if __name__ == "__main__":
    def traceryTest():
        rules = {
            "origin": ["#goodbye.capitalize#, #location#!"],
            "goodbye": ["goodbye", "sayonara", "adios", "good riddance"],
            "location": ["world", "solar system", "galaxy", "universe"]
        }
        items = generateStory()
        for i in items:
            print(i)
        items = generateStory(dataObject=rules)
        print()
        for i in items:
            print(i)
        items = generateStory(dataObject=None)
        print()
        for i in items:
            print(i)
        items = generateStory(dataObject=None, Sentence_Type='adjective', amount=10)
        print()
        for i in items:
            print(i)
        items = generateStory(dataObject=None, Sentence_Type=None)
        print()
        for i in items:
            print(i)
        items = generateStory(dataObject=None, Sentence_Type='quest')
        print()
        for i in items:
            print(i)

    def narrativeGenTest():
        generateStartingWorld()

    # maintest()
    narrativeGenTest()

