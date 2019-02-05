from void_scribe import NameGenerator
from void_scribe.data.Stories import data
import tracery
from tracery.modifiers import base_english
import random
# from nltk.parse.generate import generate, demo_grammar
# from nltk import CFG
# import spacy
import pynlg
import pickle
import requests


"""
    Naming conventions:
        obj = Object
        com = component
        helper = a helper function.
"""


def getStoryPrefabs():
    ret = []
    for i in data:
        ret.append(i)
    return ret


def generateTraceryStory(
        dataObject=None,
        Sentence_Type='quest',
        amount=3):
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


# Objects


class objEntity():
    """  This holds components.
        """

    def __init__(self,
            world=None,
            nameEntity="",
            x = 0,
            y = 0,
            z = 0,
            creature=None,
            AI=None,
            item=None,
            container=None):
        self.world = world
        self.nameEntity = nameEntity
        self.x = x
        self.y = y
        self.z = z

        self.creature = creature
        if self.creature:
            self.creature.owner = self

        self.AI = AI
        if self.AI:
            self.AI.owner = self

        self.item = item
        if self.item:
            self.item.owner = self

        self.container = container
        if self.container:
            self.container.owner = self


class objSimulation:
    def __init__(self,
            genres = None, 
            actions = None, 
            occupations = None, 
            goals = None, 
            traits = None, 
            personalityFacets = None
        ):
        self.nameSimulation = "universe"
        
        self.genres = genres
        self.actions = actions
        self.occupations = occupations
        self.goals = goals
        self.traits = traits
        self.personalityFacets = personalityFacets

        self.history = []
        self.items = []
        self.creatures = []
        self.places = []

    def addEvent(self, event):
        """
        Appends an event to the history of the world.
        event is a tuple in the form of (sentenceStruct, lemmasInOrderOfSentenceStruct, tense, sentenceType).
        """
        self.history.append(event)

    def packageEvent(self,
            sentenceStruct = ["verb", "Subject", "Direct Object"],
            lemmasInStructOrder = ["live", "I", "here"],
            tense = "present",
            sentenceType = "imperative"):
        """ 
        valid sentence types: declarative, imperative, (can|may|would|should|could), (who|what|when|where|why|how), question
        valid tenses: past, present, progressive, past_progressive, future, infinitive 
        """
        ret = {}
        for i, pos in enumerate(sentenceStruct):
            ret[pos] = lemmasInStructOrder[i]
        return ret

    def addCreature(self, entity):
        # Verb, Subject, listObjects
        if len(self.creatures) == 0:
            self.protagonist = entity
        self.creatures.append(entity)
        self.addEvent(entity.creature.nameLivingThing.capitalize() + " is a " + entity.nameEntity.lower() + " living in the " + self.nameSimulation + ".")
        # self.addEvent(("live", entity.creature.nameLivingThing, entity.nameEntity, self.nameSimulation))
            # [entity.creature.nameLivingThing] is a [entity.nameEntity] living in the [self.nameSimulation].
                # Bob is a human living in the universe.

# Components


class comLivingThing:
    def __init__(self,
                 nameLivingThing="",
                 hp=1, 
                 Strength=10,
                 Constitution=10,
                 Dexterity=10,
                 Charisma=10, # May conflict with personality traits/facets. Think of this as their physical beauty
                 Wisdom=10,
                 Intelligence=10):
        self.nameLivingThing = nameLivingThing
        self.hp = hp
        self.Strength = Strength
        self.Constitution = Constitution
        self.Dexterity = Dexterity
        self.Charisma = Charisma
        self.Wisdom = Wisdom
        self.Intelligence = Intelligence


class comAI:
    """ comAI have
    a list of goals,
    a dict of personality traits
    """

    def __init__(self,
                 quests=None,
                 traits=None,
                 facets=None):
        # print("They're here.")
        self.quests = quests
        self.traits = traits
        self.facets = facets

    def randomize_traits(self, traitMin=-50, traitMax=50):
        if self.traits is not None:
            helper_randomizeWithinConstraints(
                -50, 50, traitMin, traitMax, self.traits)
        # else:
        #     return helper_func_failure("comAI.randomize_traits")

    def randomize_personality(self, facetMin=0, facetMax=100):
        if self.facets is not None:
            helper_randomizeWithinConstraints(
                0, 100, facetMin, facetMax, self.facets)
        # else:
        #     return helper_func_failure("comAI.randomize_personality")

    def take_turn(self):
        # Character selects one of it's available goals (ordered by urgency/optionality)
        # if not character.mainGoal:
        #     character.mainGoal = character.goals.pop()
        self.currentQuest = self.quests[0]
        helper_thinkingActing(self.owner, self.currentQuest)
        print("it's MY turn.")

class comPlace:
    def __init__(self,
            namePlace="",
            environmentType="",
            government="",
            population=[]):
        self.namePlace = namePlace 
        self.environmentType = environmentType 
        self.government = government 
        self.population = population 
    
    @property
    def totalPopulation(self):
        return len(self.population)


class comItem:
    def __init__(self,
            nameItem="",
            typeItem="",
            volume=0,
            weight=0):
        self.nameItem = nameItem
        self.typeItem = typeItem
        self.volume = volume
        self.weight = weight

    def acquire(self, actor):
        if actor.container:
            if actor.container.volume + self.volume > actor.container.max_volume:
                # TODO add new event to history that says the actor could not carry the item
                print("Could not acquire item.")
            else:
                # TODO add new event to history saying the item was picked up by [actor].
                actor.container.inventory.append(self.owner)
                self.container = actor.container

    def drop(self): # TODO drop the item in a place. (x, y, z)
        if self.container:
            self.container.inventory.remove(self.owner)

    def use(self):
        if self.owner.equipment:
            self.owner.equipment.toggle_equip()
            return "no-action"

        if self.use_function:  # """ == cast_heal """
            result = self.use_function(self.container.owner, self.value)
            if result is not None:
                print("use_function failed.")
            else:
                self.container.inventory.remove(self.owner)
                return result
    
    # def give(self, entity):
        # TODO implement
        # if self.owner.equipment:



class comContainer:
    def __init__(self, 
            inventory = [],
            volumeMax = 1,
            weightMax = 1, 
            closed = True):
        self.inventory = []
        self.volumeMax = volumeMax
        self.weightMax = weightMax
        self.closed = closed


class comEquipment:
    def __init(self,
            slot=None, 
            warmth=None):
        self.slot=slot
        self.warmth=warmth

# AI

# Generators

def generatePlace(seed=None, # Randonimity
        world=None,
        population=[],
        generateName=True
        ):

    placeCom = comPlace()
    place = objEntity(
        world=world,
        nameEntity="place",
        place=comPlace,
        creature=None,
        AI=None,
        item=None,
        container=None)


def generateItem(seed=None, # Randonimity
        world=None,
        generateName=True,
        nameItem="",
        typeItem=""
        ):

    if nameItem != "":
        itemName = nameItem
    elif generateName:
        itemName = NameGenerator.MarkovName(
            Name_Type='breads',
            amount=1,
            order=3,
            minlength=3,
            maxlength=0,
            seed=seed,
            prior=0
            )[0]
    else:
        itemName = NameGenerator.getNames(
            Name_Type='breads',
            amount=1,
            seed=seed
            )[0]

    itemCom = comItem(
            nameItem=itemName,
            typeItem=typeItem,
            volume=0,
            weight=0)

    item = objEntity(
        world=world,
        nameEntity="item",
        creature=None,
        AI=None,
        item=itemCom,
        container=None)
    return item


def generateCharacter(seed=None,  # Randonimity
        world=None,

        quests=None,  # AI
        traits=None,
        facets=None,
        isRandomizingTraits=True,
        traitMin=-50,
        traitMax=50,
        isRandomizingFacets=True,
        facetMin=0,
        facetMax=100,

        generateName=True,
        nameLivingThing="",  # Living
        hp=1,
        ):
    AI_com = comAI(
        quests=quests,
        traits=traits,
        facets=facets)

    if isRandomizingTraits:
        AI_com.randomize_traits(
            traitMin=traitMin,
            traitMax=traitMax)

    if isRandomizingFacets:
        AI_com.randomize_personality(
            facetMin=facetMin,
            facetMax=facetMax)

    nameType = {
        "americanForenames",
        "dutchForenames",
        "frenchForenames",
        "germanForenames",
        "icelandicForenames",
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
        }

    if nameLivingThing != "":
        creatureName = nameLivingThing
    elif generateName:
        creatureName = NameGenerator.MarkovName(
            Name_Type='americanForenames',
            amount=1,
            order=3,
            minlength=3,
            maxlength=0,
            seed=seed,
            prior=0
            )[0]
    else:
        creatureName = NameGenerator.getNames(
            Name_Type='americanForenames',
            amount=1,
            seed=seed
            )[0]

    if hp == 0:
        hp = random.randint(8, 14)
    creature_com = comLivingThing(
        nameLivingThing=creatureName,
        hp=hp)
    Character = objEntity(
        world=world,
        nameEntity="human",
        creature=creature_com,
        AI=AI_com,
        item=None,
        container=[])
    # print(Character.creature.nameLivingThing.capitalize() + " is a " +
    #     Character.nameEntity.lower() + " living in " +
    #     "the world.")  # TODO make places before people
    return Character

# Helper Functions


def helper_funcFailure(string=""):
    return ("Function failed: " + string)


def helper_randomizeWithinConstraints(c_min, c_max, r_min, r_max, dictionary):
        if r_min < c_min: r_min = c_min
        if r_min > c_max: r_min = c_max
        if r_max < c_min: r_max = c_min
        if r_max > c_max: r_max = c_max
        for key in dictionary:
            dictionary[key] = random.randint(r_min, r_max)


def helper_thinkingActing(character, quest):
    accomplished = False

    if quest[0] == "acquire":
        # find the nearest item of type quest[1]
        listOfItemType = []
        for thing in character.world.items:
            if thing.item.typeItem == quest[1]:
                listOfItemType.append(thing)
        # get the distance to the nearest item to be acquired.
        if len(listOfItemType) > 0:
            listOfItemType[0].item.acquire(character)
            # Verb Subject Object  = acquire, creature, potion
            character.world.addEvent(character.creature.nameLivingThing.capitalize() + " acquired a " + listOfItemType[0].item.typeItem + ".")
            accomplished = True

    if accomplished:
        character.AI.quests.remove(quest)

# def helper_getTAGNodes(goal):
#     return [goal for edge in TAG(GOAL)]

def loadPickle(data = None, fileName = "data/ActionVerbs.p"):
    with open(fileName, "rb") as file:
        data = pickle.load(file)
    return data

# Simulation Main

def simulation_init(seed=None):
    random.seed(seed)

    # Story Elements
    genres = {
        "action": {
            "characterCountMin":1,
            "goal": "STAY_ALIVE"
        },
        "adventure": {},
        "horror": {},
        "thriller": {},
        "romance": {
            "characterCountMin":2,
            "goal": "START_A_FAMILY"
        }
    }

    structures = {
        "Hero's Journey":[
        ]
    }

    # AI Components
    occupations = [
        "warrior",
        "baker",
        "blacksmith",
        "fisherman",
        "none"]

    goals = {
        "thing": [  # (book, throne, sword)
            "STAY_ALIVE",
            "MAINTAIN_ENTITY_STATUS",
            # dreams of ruling the world
            "RULE_THE_POWER_STRUCTURE(powerStructure=governments)",
            # dreams of bringing (lasting) #ideal#(peace, war, religion, value) to the person/place (world)
            "BRING_IDEAL_TO_THE_NOUN(ideal='peace',noun='world')",
            # dreams of becoming a legendary #occupation#(warrior, smith)
            "BECOME_A_LEGENDARY_ITEM(type='sword')"
        ],
        "person": [  # /animal (from http://dwarffortresswiki.org/index.php/DF2014:Personality_trait)
            "STAY_ALIVE",
                # keep self.creature.hp > 0
            "MAINTAIN_ENTITY_STATUS",
                # maintainingVals = values.
                # interpolate all stats for all obj.s. to values that they were in maintaiingVals
            "START_A_FAMILY",
                # dreams of raising a family    Goal completed upon giving birth/fathering an infant.
                # depending on self.meanings.family:
                # if self.family:
                #     self.owner.goals.remove(self)
                # if self.owner.meanings.family == "group of people that care about each other and look after each other":
                #   if len(self.owner.relationships) < 2:
                #       self.owner.goals.push(getRelationships, priorityHighten(thisGoal[1]))
                # elif self.meanings.family == "kin":
                #   # take into account
                    #   # their romantic situation, their relationships,
                    #   # whether or not they consider homosexual relationships morally correct,
                    #   # whether they want a child,
                #   if romanticInterest and
                #      self.owner.relationships.
                #
                #
            # dreams of ruling the world
            "RULE_THE_POWER_STRUCTURE(powerStructure=governments)",
            # dreams of creating a great work of art	Goal completed upon creation of Artifact or Masterpiece
            "CREATE_A_GREAT_WORK_OF_ART",
            # dreams of crafting a masterwork someday	Goal completed upon creation of Artifact or Masterpiece
            "CRAFT_A_MASTERWORK",
            # dreams of bringing lasting #ideal#(peace, war, religion, value) to the person/place (world)
            "BRING_IDEAL_TO_THE_NOUN(ideal='peace',noun='world')",
            # dreams of becoming a legendary #occupation#(warrior, smith)
            "BECOME_A_LEGENDARY_OCCUPATION(occupation='warrior')",
            # dreams of mastering a skill	Goal completed upon reaching Legendary skill status.
            "MASTER_A_SKILL(skill='smithing')",
            # dreams of experiencing(falling in) an ideal state (love)
            "EXPERIENCE_IDEAL(ideal='love')",
            # dreams of seeing the great (natural) places of the world
            "SEE_THE_GREAT_NATURAL_SITES(wonders=wonders)",
            "IMMORTALITY",
                # to remain conscious and capable of change forever.
                    # ascension to deification
                    # descend to demonification
                        # possible necromancy
                    # remain in purgatorification
                        # possible necromancy
                # Find all ways to die,
                    # hp going below zero,
                    # remaining indefinitely incapable of change
                        # unconsciousness
                        # trapped after mitigating health going below 0.
                # find everything that can mitigate those methods,
                    #
                # Apply those mitigations to at least your personal possible ways to die.
            # learn new knowledge, discover new places, meet new people,
            "DISCOVER(type='area')"
                # new to you, to society, to your people
        ],
        "place": [  # location
            "STAY_ALIVE",
            "MAINTAIN_ENTITY_STATUS",
            # (center of trade, politics, education, technology, culture)
            "BECOME_CENTER_OF_#IDEA#"
        ],
        "quality": [
            "STAY_ALIVE",
            "MAINTAIN_ENTITY_STATUS",
            # dreams of bringing lasting #ideal#(peace, war, religion, value) to the person/place (world)
            "BRING_#IDEAL#_TO_THE_#PERSON/PLACE#"
        ],
        "idea": [
            "STAY_ALIVE",
            "MAINTAIN_ENTITY_STATUS",
            # dreams of bringing lasting #ideal#(peace, war, religion, value) to the person/place (world)
            "BRING_#IDEAL#_TO_THE_#PERSON/PLACE#"
        ],
        "action": [
            "STAY_ALIVE",
            "MAINTAIN_ENTITY_STATUS",
            # dreams of bringing lasting #ideal#(peace, war, religion, value) to the person/place (world)
            "BRING_#IDEAL#_TO_THE_#PERSON/PLACE#"
        ],
        "state": [
            "STAY_ALIVE",
            "MAINTAIN_ENTITY_STATUS",
            # dreams of becoming a legendary #occupation#(warrior, smith)
            "BECOME_A_LEGENDARY_#OCCUPATION#"
        ]
    }

    traits = {
        "ARTWORK": 0,
            # +41 to +50	believes that the creation and appreciation of artwork is one of the highest ideals
            # +26 to +40	greatly respects artists and their works
            # +11 to +25	values artwork
            # −10 to +10	doesn't care about art one way or another
            # −25 to −11	finds artwork boring
            # −40 to −26	sees the whole pursuit of art as silly
            # −50 to −41	finds art offensive and would have it destroyed whenever possible
        "COMMERCE": 0,
            # +41 to +50	sees engaging in commerce as a high ideal in life
            # +26 to +40	really respects commerce and those that engage in trade
            # +11 to +25	respects commerce
            # −10 to +10	doesn't particularly respect commerce
            # −25 to −11	is somewhat put off by trade and commerce
            # −40 to −26	finds those that engage in trade and commerce to be fairly disgusting
            # −50 to −41	holds the view that commerce is a vile obscenity
        "COMPETITION": 0,
            # +41 to +50	holds the idea of competition among the most important and would encourage it wherever possible
            # +26 to +40	views competition as a crucial driving force in the world
            # +11 to +25	sees competition as reasonably important
            # −10 to +10	doesn't have strong views on competition
            # −25 to −11	sees competition as wasteful and silly
            # −40 to −26	deeply dislikes competition
            # −50 to −41	finds the very idea of competition obscene
        "COOPERATION": 0,
            # +41 to +50	places cooperation as one of the highest ideals
            # +26 to +40	sees cooperation as very important in life
            # +11 to +25	values cooperation
            # −10 to +10	doesn't see cooperation as valuable
            # −25 to −11	dislikes cooperation
            # −40 to −26	views cooperation as a low ideal not worthy of any respect
            # −50 to −41	is thoroughly disgusted by cooperation
        "CRAFTSMANSHIP": 0,
            # +41 to +50	holds crafts[man]ship to be of the highest ideals and celebrates talented artisans and their masterworks
            # +26 to +40	has a great deal of respect for worthy crafts[man]ship
            # +11 to +25	values good crafts[man]ship
            # −10 to +10	doesn't particularly care about crafts[man]ship
            # −25 to −11	considers crafts[man]ship to be relatively worthless
            # −40 to −26	sees the pursuit of good crafts[man]ship as a total waste
            # −50 to −41	views crafts[man]ship with disgust and would desecrate a so-called masterwork or two if [he/she] could get away with it
        "CUNNING": 0,
            # +41 to +50	holds well-laid plans and shrewd deceptions in the highest regard
            # +26 to +40	greatly respects the shrewd and guileful
            # +11 to +25	values cunning
            # −10 to +10	does not really value cunning and guile
            # −25 to −11	sees guile and cunning as indirect and somewhat worthless
            # −40 to −26	holds shrewd and crafty individuals in the lowest esteem
            # −50 to −41	is utterly disgusted by guile and cunning
        "DECORUM": 0,
            # +41 to +50	views decorum as a high ideal and is deeply offended by those that fail to maintain it
            # +26 to +40	greatly respects those that observe decorum and maintain their dignity
            # +11 to +25	values decorum, dignity and proper behavior
            # −10 to +10	doesn't care very much about decorum
            # −25 to −11	finds maintaining decorum a silly, fumbling waste of time
            # −40 to −26	sees those that attempt to maintain dignified and proper behavior as vain and offensive
            # −50 to −41	is affronted by the whole notion of maintaining decorum and finds so-called dignified people disgusting
        "ELOQUENCE": 0,
            # +41 to +50	believes that artful speech and eloquent expression are of the highest ideals
            # +26 to +40	deeply respects eloquent speakers
            # +11 to +25	values eloquence
            # −10 to +10	doesn't value eloquence so much
            # −25 to −11	finds eloquence and artful speech off-putting
            # −40 to −26	finds [him/her]self somewhat disgusted with eloquent speakers
            # −50 to −41	sees artful speech and eloquence as a wasteful form of deliberate deception and treats it as such
        "FAIRNESS": 0,
            # +41 to +50	holds fairness as one of the highest ideals and despises cheating of any kind
            # +26 to +40	has great respect for fairness
            # +11 to +25	respects fair-dealing and fair-play
            # −10 to +10	does not care about fairness
            # −25 to −11	sees life as unfair and doesn't mind it that way
            # −40 to −26	finds the idea of fair-dealing foolish and cheats when [he/she] finds it profitable
            # −50 to −41	is disgusted by the idea of fairness and will freely cheat anybody at any time
        "FAMILY": 0,
            # +41 to +50	sees family as one of the most important things in life
            # +26 to +40	values family greatly
            # +11 to +25	values family
            # −10 to +10	does not care about family one way or the other
            # −25 to −11	is put off by family
            # −40 to −26	lacks any respect for family
            # −50 to −41	finds the idea of family loathsome
        "FRIENDSHIP": 0,
            # +41 to +50	believes friendship is a key to the ideal life
            # +26 to +40	sees friendship as one of the finer things in life
            # +11 to +25	thinks friendship is important
            # −10 to +10	does not care about friendship
            # −25 to −11	finds friendship burdensome
            # −40 to −26	is completely put off by the idea of friends
            # −50 to −41	finds the whole idea of friendship disgusting
        "HARD_WORK": 0,
            # +41 to +50	believes that hard work is one of the highest ideals and a key to the good life
            # +26 to +40	deeply respects those that work hard at their labors
            # +11 to +25	values hard work
            # −10 to +10	doesn't really see the point of working hard
            # −25 to −11	sees working hard as a foolish waste of time
            # −40 to −26	thinks working hard is an abject idiocy
            # −50 to −41	finds the proposition that one should work hard in life utterly abhorrent
        "HARMONY": 0,
            # +41 to +50	would have the world operate in complete harmony without the least bit of strife or disorder
            # +26 to +40	strongly believes that a peaceful and ordered society without dissent is best
            # +11 to +25	values a harmonious existence
            # −10 to +10	sees equal parts of harmony and discord as part of life
            # −25 to −11	doesn't respect a society that has settled into harmony without debate and strife
            # −40 to −26	can't fathom why anyone would want to live in an orderly and harmonious society
            # −50 to −41	believes deeply that chaos and disorder are the truest expressions of life and would disrupt harmony wherever it is found
        "INDEPENDENCE": 0,
            # +41 to +50	believes that freedom and independence are completely non-negotiable and would fight to defend them
            # +26 to +40	treasures independence
            # +11 to +25	values independence
            # −10 to +10	doesn't really value independence one way or another
            # −25 to −11	finds the ideas of independence and freedom somewhat foolish
            # −40 to −26	sees freedom and independence as completely worthless
            # −50 to −41	hates freedom and would crush the independent spirit wherever it is found
        "INTROSPECTION": 0,
            # +41 to +50	feels that introspection and all forms of self-examination are the keys to a good life and worthy of respect
            # +26 to +40	deeply values introspection
            # +11 to +25	sees introspection as important
            # −10 to +10	doesn't really see the value in self-examination
            # −25 to −11	finds introspection to be a waste of time
            # −40 to −26	thinks that introspection is valueless and those that waste time in self-examination are deluded fools
            # −50 to −41	finds the whole idea of introspection completely offensive and contrary to the ideals of a life well-lived
        "KNOWLEDGE": 0,
            # +41 to +50	finds the quest for knowledge to be of the very highest value
            # +26 to +40	views the pursuit of knowledge as deeply important
            # +11 to +25	values knowledge
            # −10 to +10	doesn't see the attainment of knowledge as important
            # −25 to −11	finds the pursuit of knowledge to be a waste of effort
            # −40 to −26	thinks the quest for knowledge is a delusional fantasy
            # −50 to −41	sees the attainment and preservation of knowledge as an offensive enterprise engaged in by arrogant fools
        "LAW": 0,
        	# +41 to +50	is an absolute believer in the rule of law
            # +26 to +40	has a great deal of respect for the law
            # +11 to +25	respects the law
            # −10 to +10	doesn't feel strongly about the law
            # −25 to −11	does not respect the law
            # −40 to −26	disdains the law
            # −50 to −41	finds the idea of laws abhorrent
        "LEISURE_TIME": 0,
            # +41 to +50	believes that it would be a fine thing if all time were leisure time
            # +26 to +40	treasures leisure time and thinks it is very important in life
            # +11 to +25	values leisure time
            # −10 to +10	doesn't think one way or the other about leisure time
            # −25 to −11	finds leisure time wasteful
            # −40 to −26	is offended by leisure time and leisurely living
            # −50 to −41	believes that those that take leisure time are evil and finds the whole idea disgusting
        "LOYALTY": 0,
            # +41 to +50	has the highest regard for loyalty
            # +26 to +40	greatly prizes loyalty
            # +11 to +25	values loyalty
            # −10 to +10	doesn't particularly value loyalty
            # −25 to −11	views loyalty unfavorably
            # −40 to −26	disdains loyalty
            # −50 to −41	is disgusted by the idea of loyalty
        "MARTIAL_PROWESS": 0,
            # +41 to +50	believes that martial prowess defines the good character of an individual
            # +26 to +40	deeply respects skill at arms
            # +11 to +25	values martial prowess
            # −10 to +10	does not really value skills related to fighting
            # −25 to −11	finds those that develop skill with weapons and fighting distasteful
            # −40 to −26	thinks that the pursuit of the skills of warfare and fighting is a low pursuit indeed
            # −50 to −41	abhors those that pursue the mastery of weapons and skill with fighting
        "MERRIMENT": 0,
            # +41 to +50	believes that little is better in life than a good party
            # +26 to +40	truly values merrymaking and parties
            # +11 to +25	finds merrymaking and partying worthwhile activities
            # −10 to +10	doesn't really value merrymaking
            # −25 to −11	sees merrymaking as a waste
            # −40 to −26	is disgusted by merrymakers
            # −50 to −41	is appalled by merrymaking, parties and other such worthless activities
        "NATURE": 0,
            # +41 to +50	holds nature to be of greater value than most aspects of civilization	Receives unhappy thought when slaughtering/caging animals and felling trees.v0.42.01
            # +26 to +40	has a deep respect for animals, plants and the natural world
            # +11 to +25	values nature
            # −10 to +10	doesn't care about nature one way or another
            # −25 to −11	finds nature somewhat disturbing	Receives happy thought when slaughtering/caging animals and felling trees.v0.42.01
            # −40 to −26	has a deep dislike of the natural world
            # −50 to −41	would just as soon have nature and the great outdoors burned to ashes and converted into a great mining pit
        "PEACE": 0,
            # +41 to +50	believes the idea of war is utterly repellent and would have peace at all costs
            # +26 to +40	believes that peace is always preferable to war
            # +11 to +25	values peace over war
            # −10 to +10	doesn't particularly care between war and peace
            # −25 to −11	sees war as a useful means to an end
            # −40 to −26	believes war is preferable to peace in general
            # −50 to −41	thinks that the world should be engaged in perpetual warfare
        "PERSEVERANCE": 0,
            # +41 to +50	believes that perseverance is one of the greatest qualities somebody can have
            # +26 to +40	greatly respects individuals that persevere through their trials and labors
            # +11 to +25	respects perseverance
            # −10 to +10	doesn't think much about the idea of perseverance
            # −25 to −11	sees perseverance in the face of adversity as bull-headed and foolish
            # −40 to −26	thinks there is something deeply wrong with people that persevere through adversity
            # −50 to −41	finds the notion that one would persevere through adversity completely abhorrent
        "POWER": 0,
            # +41 to +50	believes that the acquisition of power over others is the ideal goal in life and worthy of the highest respect
            # +26 to +40	sees power over others as something to strive for
            # +11 to +25	respects power
            # −10 to +10	doesn't find power particularly praiseworthy
            # −25 to −11	has a negative view of those who exercise power over others
            # −40 to −26	hates those who wield power over others
            # −50 to −41	finds the acquisition and use of power abhorrent and would have all masters toppled
        "ROMANCE": 0,
            # +41 to +50	sees romance as one of the highest ideals
            # +26 to +40	thinks romance is very important in life
            # +11 to +25	values romance
            # −10 to +10	doesn't care one way or the other about romance
            # −25 to −11	finds romance distasteful
            # −40 to −26	is somewhat disgusted by romance
            # −50 to −41	finds even the abstract idea of romance repellent
        "SACRIFICE": 0,
            # +41 to +50	finds sacrifice to be one of the highest ideals
            # +26 to +40	believes that those who sacrifice for others should be deeply respected
            # +11 to +25	values sacrifice
            # −10 to +10	doesn't particularly respect sacrifice as a virtue
            # −25 to −11	sees sacrifice as wasteful and foolish
            # −40 to −26	finds sacrifice to be the height of folly
            # −50 to −41	thinks that the entire concept of sacrifice for others is truly disgusting
        "SELF_CONTROL": 0,
            # +41 to +50	believes that self-mastery and the denial of impulses are of the highest ideals
            # +26 to +40	finds moderation and self-control to be very important
            # +11 to +25	values self-control
            # −10 to +10	doesn't particularly value self-control
            # −25 to −11	finds those that deny their impulses somewhat stiff
            # −40 to −26	sees the denial of impulses as a vain and foolish pursuit
            # −50 to −41	has abandoned any attempt at self-control and finds the whole concept deeply offensive
        "SKILL": 0,
            # +41 to +50	believes that the mastery of a skill is one of the highest pursuits
            # +26 to +40	really respects those that take the time to master a skill
            # +11 to +25	respects the development of skill
            # −10 to +10	doesn't care if others take the time to master skills
            # −25 to −11	finds the pursuit of skill mastery off-putting
            # −40 to −26	believes that the time taken to master a skill is a horrible waste
            # −50 to −41	sees the whole idea of taking time to master a skill as appalling
        "STOICISM": 0,
            # +41 to +50	views any show of emotion as offensive
            # +26 to +40	thinks it is of the utmost importance to present a bold face and never grouse, complain or even show emotion
            # +11 to +25	believes it is important to conceal emotions and refrain from complaining
            # −10 to +10	doesn't see much value in being stoic
            # −25 to −11	sees no value in holding back complaints and concealing emotions
            # −40 to −26	feels that those who attempt to conceal their emotions are vain and foolish
            # −50 to −41	sees concealment of emotions as a betrayal and tries [his/her] best never to associate with such secretive fools
        "TRADITION": 0,
            # +41 to +50	holds the maintenance of tradition as one of the highest ideals
            # +26 to +40	is a firm believer in the value of tradition
            # +11 to +25	values tradition
            # −10 to +10	doesn't have any strong feelings about tradition
            # −25 to −11	disregards tradition
            # −40 to −26	finds the following of tradition foolish and limiting
            # −50 to −41	is disgusted by tradition and would flout any [he/she] encounters if given a chance
        "TRANQUILITY": 0,
            # +41 to +50	views tranquility as one of the highest ideals
            # +26 to +40	strongly values tranquility and quiet
            # +11 to +25	values tranquility and a peaceful day
            # −10 to +10	doesn't have a preference between tranquility and tumult
            # −25 to −11	prefers a noisy, bustling life to boring days without activity
            # −40 to −26	is greatly disturbed by quiet and a peaceful existence
            # −50 to −41	is disgusted by tranquility and would that the world would constantly churn with noise and activity
        "TRUTH": 0
            # +41 to +50	believes the truth is inviolable regardless of the cost
            # +26 to +40	believes that honesty is a high ideal
            # +11 to +25	values honesty
            # −10 to +10	does not particularly value the truth
            # −25 to −11	finds blind honesty foolish
            # −40 to −26	sees lying as an important means to an end
            # −50 to −41	is repelled by the idea of honesty and lies without compunction
    }

    personalityFacets = {
        "ABSTRACT_INCLINED": 0,
            # 91-100	eschews practical concerns for philosophical discussion, puzzles, riddles and the world of ideas
            # 76-90	strongly prefers discussions of ideas and abstract concepts over handling specific practical issues
            # 61-75	has a tendency to consider ideas and abstractions over practical applications
            # 25-39	likes to keep things practical, without delving too deeply into the abstract
            # 10-24	dislikes abstract discussions and would much rather focus on practical examples
            # 0-9	is concerned only with matters practical to the situation at hand, with absolutely no inclination toward abstract discussion
        "ACTIVITY_LEVEL": 0,
            # 91-100	is driven by a bouncing frenetic energy
            # 76-90	lives at a high-energy kinetic pace
            # 61-75	lives a fast-paced life
            # 25-39	likes to take it easy
            # 10-24	lives at a slow-going and leisurely pace
            # 0-9	has an utterly languid pace of easy living, calm and slow
        "ALTRUISM": 0,  # Conflicts with trait SACRIFICE
            # 91-100	is truly fulfilled by assisting those in need	Receives Happy Thought from recovering wounded.
            # 76-90	finds helping others very emotionally rewarding
            # 61-75	finds helping others emotionally rewarding
            # 25-39	does not go out of [his/her] way to help others
            # 10-24	dislikes helping others	Receives Unhappy Thought from recovering wounded.
            # 0-9	feels helping others is an imposition on [his/her] time
        "AMBITION": 0,
            # 91-100	has a relentless drive, completely consumed by ambition
            # 76-90	is very ambitious, always looking for a way to better [his/her] situation
            # 61-75	is quite ambitious
            # 25-39	isn't particularly ambitious
            # 10-24	is not driven and rarely feels the need to pursue even a modest success
            # 0-9	has no ambition whatsoever
        "ART_INCLINED": 0,  # Conflicts with traits ARTWORK and NATURE
            # 91-100	can easily become absorbed in art and the beauty of the natural world
            # 76-90	greatly moved by art and natural beauty
            # 61-75	is moved by art and natural beauty
            # 25-39	does not have a great aesthetic sensitivity
            # 10-24	is not readily moved by art or natural beauty
            # 0-9	is completely unmoved by art or the beauty of nature
        "ASSERTIVENESS": 0,
            # 91-100	is assertive to the point of aggression, unwilling to let others get a word in edgewise when [he/she] has something to say
            # 76-90	has an overbearing personality
            # 61-75	is assertive
            # 25-39	tends to be passive in discussions
            # 10-24	only rarely tries to assert [him/her]self in conversation
            # 0-9	would never under any circumstances speak up or otherwise put forth [his/her] point of view in a discussion
        "BASHFUL": 0,
            # 91-100	is gripped by a crippling shyness
            # 76-90	is bashful
            # 61-75	tends to consider what others think of [him/her]
            # 25-39	is not particularly interested in what others think of [him/her]
            # 10-24	is generally unhindered by the thoughts of others concerning [his/her] actions
            # 0-9	is shameless, absolutely unfazed by the thoughts of others
        "BRAVERY": 0,
            # 91-100	is utterly fearless when confronted with danger, to the point of lacking common sense
            # 76-90	is incredibly brave in the face of looming danger, perhaps a bit foolhardy
            # 61-75	is brave in the face of imminent danger
            # 25-39	is somewhat fearful in the face of imminent danger
            # 10-24	has great trouble mastering fear when confronted by danger
            # 0-9	is a coward, completely overwhelmed by fear when confronted with danger
        "CONFIDENCE": 0,
            # 91-100	presupposes success in any venture requiring [his/her] skills with what could be called blind overconfidence
            # 76-90	is extremely confident of [him/her]self in situations requiring [his/her] skills
            # 61-75	is generally quite confident of [his/her] abilities when undertaking specific ventures
            # 25-39	sometimes acts with little determination and confidence
            # 10-24	lacks confidence in [his/her] abilities
            # 0-9	has no confidence at all in [his/her] talent and abilities
        "CLOSEMINDED": 0,
            # 91-100	is completely closed-minded and never changes [his/her] mind after forming an initial idea
            # 76-90	is intellectually stubborn, rarely changing [his/her] mind during a debate regardless of the merits
            # 61-75	tends to be a bit stubborn in changing [his/her] mind about things
            # 25-39	doesn't cling tightly to ideas and is open to changing [his/her] mind
            # 10-24	often finds [him/her]self changing [his/her] mind to agree with somebody else
            # 0-9	easily changes [his/her] mind and will generally go with the prevailing view on anything
        "CRUELTY": 0,  # Conflicts with trait POWER
            # 91-100	is deliberately cruel to those unfortunate enough to be subject to [his/her] sadism
            # 76-90	is sometimes cruel
            # 61-75	generally acts impartially and is rarely moved to mercy
            # 25-39	often acts with compassion
            # 10-24	is easily moved to mercy
            # 0-9	always acts with mercy and compassion at the forefront of [his/her] considerations
        "CURIOUS": 0,
            # 91-100	is implacably curious, without any respect for propriety or privacy
            # 76-90	is very curious, sometimes to [his/her] detriment
            # 61-75	is curious and eager to learn
            # 25-39	isn't particularly curious about the world
            # 10-24	is very rarely moved by curiosity
            # 0-9	is incurious and never seeks out knowledge or information to satisfy [him/her]self
        "DISCORD": 0,  # Conflicts with trait HARMONY
            # 91-100	revels in chaos and discord, and [he/she] encourages it whenever possible
            # 76-90	finds a chaotic mess preferable to the boredom of harmonious living
            # 61-75	doesn't mind a little tumult and discord in day-to-day living
            # 25-39	prefers that everyone live as harmoniously as possible
            # 10-24	feels best when everyone gets along without any strife or contention
            # 0-9	would be deeply satisfied if everyone could live as one in complete harmony
        "DISDAIN_ADVICE": 0,
            # 91-100	disdains even the best advice of associates and family, relying strictly on [his/her] own counsel
            # 76-90	dislikes receiving advice, preferring to keep [his/her] own counsel
            # 61-75	has a tendency to go it alone, without considering the advice of others
            # 25-39	tends to ask others for help with difficult decisions
            # 10-24	relies on the advice of others during decision making
            # 0-9	is unable to make decisions without a great deal of input from others
        "DUTIFULNESS": 0,  # Conflicts with traits LAW, LOYALTY, and INDEPENDENCE
            # 91-100	has a profound sense of duty and obligation
            # 76-90	has a strong sense of duty
            # 61-75	has a sense of duty
            # 25-39	finds obligations confining
            # 10-24	dislikes obligations and will try to avoid being bound by them
            # 0-9	hates vows, obligations, promises and other binding elements that could restrict [him/her]
        "EMOTIONALLY_OBSESSIVE": 0,
            # 91-100	is emotionally obsessive, forming life-long attachments even if they aren't reciprocated
            # 76-90	forms strong emotional bonds with others, at times to [his/her] detriment
            # 61-75	has a tendency toward forming deep emotional bonds with others
            # 25-39	tends to form only tenuous emotional bonds with others
            # 10-24	forms only fleeting and rare emotional bonds with others
            # 0-9	does not have feelings of emotional attachment and has never felt even a moment's connection with another being
        "EXCITEMENT_SEEKING": 0,  # Conflicts with trait TRANQUILITY
            # 91-100	never fails to seek out the most stressful and even dangerous situations
            # 76-90	seeks out exciting and adventurous situations
            # 61-75	likes a little excitement now and then
            # 25-39	doesn't seek out excitement
            # 10-24	actively avoids exciting or stressful situations
            # 0-9	does everything in [his/her] power to avoid excitement and stress
        "FRIENDLINESS": 0,  # Conflicts with traits HARMONY and FRIENDSHIP
            # 91-100	is quite a bold flatterer, extremely friendly but just a little insufferable
            # 76-90	is very friendly and always tries to say nice things to others
            # 61-75	is a friendly individual
            # 25-39	is somewhat quarrelsome
            # 10-24	is unfriendly and disagreeable
            # 0-9	is a dyed-in-the-wool quarreler, never missing a chance to lash out in verbal hostility
        "GRATITUDE": 0,
            # 91-100	unerringly returns favors and has a profound sense of gratitude for the kind actions of others
            # 76-90	feels a strong need to reciprocate any favor done for [him/her]
            # 61-75	is grateful when others help [him/her] out and tries to return favors
            # 25-39	takes offered help and gifts without feeling particularly grateful
            # 10-24	accepts favors without developing a sense of obligation, preferring to act as the current situation demands
            # 0-9	does not feel the slightest need to reciprocate favors that others do for [him/her], no matter how major the help or how much [he/she] needed it
        "GREED": 0,
            # 91-100	is as avaricious as they come, obsessed with acquiring wealth
            # 76-90	is very greedy
            # 61-75	has a greedy streak
            # 25-39	doesn't focus on material goods
            # 10-24	desires little for [him/her]self in the way of possessions
            # 0-9	often neglects [his/her] own wellbeing, having no interest in material goods
        "GREGARIOUSNESS": 0,
            # 91-100	truly treasures the company of others
            # 76-90	enjoys being in crowds
            # 61-75	enjoys the company of others
            # 25-39	tends to avoid crowds
            # 10-24	prefers to be alone
            # 0-9	considers spending time alone much more important than associating with others
        "HOPEFUL": 0,
            # 91-100	has such a developed sense of optimism that [he/she] always assumes the best outcome will eventually occur, no matter what
            # 76-90	is an optimist
            # 61-75	generally finds [him/her]self quite hopeful about the future
            # 25-39	tends to assume the worst of two outcomes will be the one that comes to pass
            # 10-24	is a pessimist
            # 0-9	despairs of anything positive happening in the future and lives without feelings of hope
        "HUMOR": 0,
            # 91-100	finds something humorous in everything, no matter how serious or inappropriate
            # 76-90	finds the humor in most situations
            # 61-75	has an active sense of humor
            # 25-39	has little interest in joking around
            # 10-24	does not find most jokes humorous
            # 0-9	is utterly humorless
        "IMAGINATION": 0,
            # 91-100	is bored by reality and would rather disappear utterly and forever into a world of made-up fantasy
            # 76-90	is given to flights of fancy to the point of distraction
            # 61-75	has an active imagination
            # 25-39	isn't given to flights of fancy
            # 10-24	is grounded in reality
            # 0-9	is interested only in facts and the real world
        "IMMODERATION": 0,  # Conflicts with trait SELF_CONTROL
            # 91-100	is ruled by irresistible cravings and urges
            # 76-90	feels strong urges and seeks short-term rewards
            # 61-75	occasionally overindulges
            # 25-39	doesn't often experience strong cravings or urges
            # 10-24	only rarely feels strong cravings or urges
            # 0-9	never feels tempted to overindulge in anything
        "IMMODESTY": 0,
            # 91-100	always presents [him/her]self as extravagantly as possible, displaying a magnificent image to the world
            # 76-90	likes to present [him/her]self boldly, even if it would offend an average sense of modesty
            # 61-75	doesn't mind wearing something special now and again
            # 25-39	prefers to present [him/her]self modestly
            # 10-24	presents [him/her]self modestly and frowns on any flashy accoutrements
            # 0-9	cleaves to an austere lifestyle, disdaining even minor immodesties in appearance
        "ORDERLINESS": 0,
            # 91-100	is obsessed with order and structure in [his/her] own life, with everything kept in its proper place
            # 76-90	lives an orderly life, organized and neat
            # 61-75	tries to keep [his/her] things orderly
            # 25-39	tends to make a small mess with [his/her] own possessions
            # 10-24	is sloppy with [his/her] living space
            # 0-9	is completely oblivious to any conception of neatness and will just leave things strewn about without a care
        "PERFECTIONIST": 0,
            # 91-100	is obsessed with details and will often take a great deal of extra time to make sure things are done the right way
            # 76-90	is a perfectionist
            # 61-75	tries to do things correctly each time
            # 25-39	doesn't try to get things done perfectly
            # 10-24	is inattentive to detail in [his/her] own work
            # 0-9	is frustratingly sloppy and careless with every task [he/she] sets to carry out
        "PERSEVEREANCE": 0,  # Conflicts with trait PERSEVERANCE
            # 91-100	is unbelievably stubborn, and will stick with even the most futile action once [his/her] mind is made up
            # 76-90	is very stubborn
            # 61-75	is stubborn
            # 25-39	has a noticeable lack of perseverance
            # 10-24	doesn't stick with things if even minor difficulties arise
            # 0-9	drops any activity at the slightest hint of difficulty or even the suggestion of effort being required
        "POLITENESS": 0,  # Conflicts with trait DECORUM
            # 91-100	exhibits a refined politeness and is determined to keep the guiding rules of etiquette and decorum as if life itself depended on it
            # 76-90	is very polite and observes appropriate rules of decorum when possible
            # 61-75	is quite polite
            # 25-39	could be considered rude
            # 10-24	is very impolite and inconsiderate of propriety
            # 0-9	is a vulgar being who does not care a lick for even the most basic rules of civilized living
        "PRIDE": 0,
            # 91-100	is absorbed in delusions of self-importance
            # 76-90	has an overinflated sense of self-worth
            # 61-75	thinks [he/she] is fairly important in the grand scheme of things
            # 25-39	is very humble
            # 10-24	has a low sense of self-esteem
            # 0-9	is completely convinced of [his/her] own worthlessness
        "PRIVACY": 0,  # Conflicts with trait STOICISM
            # 91-100	shares intimate details of life without sparing a thought to repercussions or propriety
            # 76-90	is not a private person and freely shares details of [his/her] life
            # 61-75	tends to share [his/her] own experiences and thoughts with others
            # 25-39	tends not to reveal personal information
            # 10-24	has a strong tendency toward privacy
            # 0-9	is private to the point of paranoia, unwilling to reveal even basic information about [him/her]self
        "PROPENSITY_ANGER": 0,
            # 91-100	is in a constant state of internal rage	More likely to throw tantrums and go berserk.
            # 76-90	is very quick to anger
            # 61-75	is quick to anger
            # 25-39	is slow to anger
            # 10-24	is very slow to anger
            # 0-9	never becomes angry
        "PROPENSITY_ANXIETY": 0,
            # 91-100	is a nervous wreck	More likely to stumble obliviously and go stark raving mad.
            # 76-90	is always tense and jittery
            # 61-75	is often nervous
            # 25-39	has a calm demeanor
            # 10-24	has a very calm demeanor
            # 0-9	has an incredibly calm demeanor
        "PROPENSITY_CHEER": 0,  # Conflicts with trait MERRIMENT
            # 91-100	often feels filled with joy
            # 76-90	can be very happy and optimistic
            # 61-75	is often cheerful
            # 25-39	is rarely happy or enthusiastic
            # 10-24	is dour as a rule
            # 0-9	is never the slightest bit cheerful about anything
        "PROPENSITY_DEPRESSION": 0,
            # 91-100	is frequently depressed	More likely to slip into depression and be stricken by melancholy.
            # 76-90	is often sad and dejected
            # 61-75	often feels discouraged
            # 25-39	rarely feels discouraged
            # 10-24	almost never feels discouraged
            # 0-9	never feels discouraged
        "PROPENSITY_ENVY": 0,
            # 91-100	is consumed by overpowering feelings of jealousy
            # 76-90	is prone to strong feelings of jealousy
            # 61-75	often feels envious of others
            # 25-39	doesn't often feel envious of others
            # 10-24	is rarely jealous
            # 0-9	never envies others their status, situation or possessions
        "PROPENSITY_HATE": 0,
            # 91-100	is often inflamed by hatred and easily develops hatred toward things
            # 76-90	is prone to hatreds and often develops negative feelings
            # 61-75	is quick to form negative views about things
            # 25-39	does not easily hate or develop negative feelings
            # 10-24	very rarely develops negative feelings toward things
            # 0-9	never feels hatred toward anyone or anything
        "PROPENSITY_LOVE": 0,  # Conflicts with trait ROMANCE
            # 91-100	is always in love with somebody and easily develops positive feelings
            # 76-90	very easily falls into love and develops positive feelings
            # 61-75	can easily fall in love or develop positive sentiments
            # 25-39	does not easily fall in love and rarely develops positive sentiments
            # 10-24	is not the type to fall in love or even develop positive feelings
            # 0-9	never falls in love or develops positive feelings toward anything
        "PROPENSITY_LUST": 0,
            # 91-100	is constantly ablaze with feelings of lust
            # 76-90	is prone to strong feelings of lust
            # 61-75	often feels lustful
            # 25-39	does not often feel lustful
            # 10-24	rarely looks on others with lust
        "PROPENSITY_STRESS": 0,
            # 91-100	becomes completely helpless in stressful situations	50% chance to become catatonic
            # 76-90	cracks easily under pressure
            # 61-75	doesn't handle stress well
            # 25-39	can handle stress
            # 10-24	is confident under pressure
            # 0-9	is impervious to the effects of stress
        "SINGLEMINDED": 0,
            # 91-100	pursues matters with a single-minded focus, often overlooking other matters
            # 76-90	can be very single-minded
            # 61-75	generally acts with a narrow focus on the current activity
            # 25-39	can occasionally lose focus on the matter at hand
            # 10-24	is somewhat scatterbrained
            # 0-9	is a complete scatterbrain, unable to focus on a single matter for more than a passing moment
        "SWAYED_BY_EMOTIONS": 0,
            # 91-100	is buffeted by others' emotions and can't help but to respond to them
            # 76-90	is swayed by emotional appeals
            # 61-75	tends to be swayed by the emotions of others
            # 25-39	tends not to be swayed by emotional appeals
            # 10-24	does not generally respond to emotional appeals
            # 0-9	is never moved by the emotions of others
        "THOUGHTLESSNESS": 0,
            # 91-100	never deliberates before acting, to the point of being considered thoughtless
            # 76-90	doesn't generally think before acting
            # 61-75	can sometimes act without deliberation
            # 25-39	tends to think before acting
            # 10-24	can get caught up in internal deliberations when action is necessary
            # 0-9	never acts without prolonged deliberation, even to [his/her] own detriment and the harm of those around [him/her]
        "TOLERANT": 0,
            # 91-100	is not bothered in the slightest by deviations from the norm or even extreme differences in lifestyle or appearance
            # 76-90	is very comfortable around others that are different from [him/her]
            # 61-75	is quite comfortable with others that have a different appearance or culture
            # 25-39	is somewhat uncomfortable around those that appear unusual or live differently from [him/her]
            # 10-24	is made deeply uncomfortable by differences in culture or appearance
            # 0-9	cannot tolerate differences in culture, lifestyle or appearance
        "TRUST": 0,
            # 91-100	is naturally trustful of everybody
            # 76-90	is very trusting
            # 61-75	is trusting
            # 25-39	is slow to trust others
            # 10-24	does not trust others
            # 0-9	sees others as selfish and conniving
        "VANITY": 0,
            # 91-100	is completely wrapped up in [his/her] own appearance, abilities and other personal matters
            # 76-90	is greatly pleased by [his/her] own looks and accomplishments
            # 61-75	is pleased by [his/her] own appearance and talents
            # 25-39	is not inherently proud of [his/her] talents and accomplishments
            # 10-24	takes no pleasure in [his/her] talents and appearance
            # 0-9	could not care less about [his/her] appearance, talents or other personal vanities
        "VENGEFUL": 0,
            # 91-100	is vengeful and never forgets or forgives past grievances
            # 76-90	has little time for forgiveness and will generally seek retribution
            # 61-75	tends to hang on to grievances
            # 25-39	doesn't tend to hold on to grievances
            # 10-24	does not generally seek retribution for past wrongs
            # 0-9	has no sense of vengeance or retribution
        "VIOLENT": 0,  # Conflicts with TRANQUILITY and MARTIAL_PROWESS
            # 91-100	is given to rough-and-tumble brawling, even to the point of starting fights for no reason	This does not actually cause a dwarf to randomly start a fistfight.
            # 76-90	would never pass up a chance for a good fistfight
            # 61-75	likes to brawl
            # 25-39	tends to avoid any physical confrontations	This does not affect a soldier's will to fight, but will cause civilians to flee from danger.Verify
            # 10-24	does not enjoy participating in physical confrontations
            # 0-9	would flee even the most necessary battle to avoid any form of physical confrontation
        "WASTEFULNESS": 0,
            # 91-100	is completely careless with resources when completing projects, and invariably wastes a lot of time and effort
            # 76-90	is not careful with resources when working on projects and often spends unnecessary effort
            # 61-75	tends to be a little wasteful when working on projects
            # 25-39	tends to be a little tight with resources when working on projects
            # 10-24	is stingy with resources on projects and refuses to expend any extra effort
            # 0-9	cuts any corners possible when working on a project, regardless of the consequences, rather than wasting effort or resources
    }
    
    actions = {  
            # destroy, create, modify, interact
        "None":[],
        "think":[],
        "watch":[],

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


    # World generation
    WORLD = objSimulation(
        genres,
        actions,
        occupations,
        goals,
        traits,
        personalityFacets
    )

    for i in range(1):
        item = generateItem(seed=None, # Randonimity
            world=WORLD,
            generateName=False,
            nameItem="bravery",
            typeItem="potion"
            )
        WORLD.items.append(item)

    for i in range(1):
        creature = generateCharacter(
            seed = seed,
            world=WORLD,
            hp = 10,
            quests = [
                ["acquire", "potion"]
                ],
            traits = traits,
            facets = personalityFacets,
            isRandomizingTraits = True,
            isRandomizingFacets = True)
        WORLD.addCreature(creature)
    
    return WORLD

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

def simulation_main_loop(WORLD=None):
    quitSimulation = False
    while (len(WORLD.protagonist.AI.quests) > 0) and not quitSimulation:
        for entity in WORLD.creatures:
            entity.AI.take_turn()

        # uses filtering based on thinking-acting graph to decide on a single action
        # actionChoice = getThoughtOrAction(protagonist.mainGoal)

        # action is sent to language processing.
        # NLG(actionChoice)

        # action outcome is generated.
        #    the outcome of this action depends on character attributes as well as action interrupts.
        #       interrupts can result in action failures, character encounters, new mandatory or optional side quests of varying urgency or world events
        # actionOutcome = getWorldState(actionChoice)

        # Action outcome is then also sent to language processing.
        # NLG(actionOutcome)

        # New goals are added to goal stack according to urgency/optionality
        #   goals are mandatory if standing in the way of completing currently selected quest.
        #   goals are optional if they have no direct relation to quest at hand.
        # for goal in actionOutcome.goals():
        #     protagonist.goals().insert(goal)

        # The protagonist continues thinking-acting until goal-stack is resolved.
    
    for event in WORLD.history:
        print(event)

if __name__ == "__main__":
    def traceryTest():
        rules={
            "origin": ["#goodbye.capitalize#, #location#!"],
            "goodbye": ["goodbye", "sayonara", "adios", "good riddance"],
            "location": ["world", "solar system", "galaxy", "universe"]
        }
        items = generateTraceryStory()
        for i in items:
            print(i)
        items = generateTraceryStory(dataObject=rules)
        print()
        for i in items:
            print(i)
        items = generateTraceryStory(dataObject=None)
        print()
        for i in items:
            print(i)
        items = generateTraceryStory(dataObject=None, Sentence_Type='adjective', amount=10)
        print()
        for i in items:
            print(i)
        items = generateTraceryStory(dataObject=None, Sentence_Type=None)
        print()
        for i in items:
            print(i)
        items = generateTraceryStory(dataObject=None, Sentence_Type='quest')
        print()
        for i in items:
            print(i)

    # def nltkTest():
        # print('hi')
        # print("Demo grammar: " + demo_grammar)
        
        # grammar = CFG.fromstring(demo_grammar)
        # print("Grammar: " + str(grammar))

        # for sentence in generate(grammar, n=10):
        #     print(' '.join(sentence))

        # for sentence in generate(grammar, depth=6):
        #     print(' '.join(sentence))

    def spacyTest():
        print("hi!")
    
    def narrativeGenTest():
        ret = simulation_init()
        simulation_main_loop(ret)

    def conceptNetTest():
        ActionVerbs = loadPickle(data = None, fileName = "void_scribe/data/ActionVerbs.p")
        currentVerb = random.choice(ActionVerbs)
        obj = requests.get("http://api.conceptnet.io/c/en/" + "hello").json()
        for key in obj:
            print(f'{key} : {obj[key]}')
            print()


    # nltkTest()
    # narrativeGenTest()
    conceptNetTest()

