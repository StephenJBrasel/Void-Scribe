from void_scribe import NameGenerator
from void_scribe.data.Stories import data
import tracery
from tracery.modifiers import base_english
import random

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
class entity():
    # list of list of goals, higher order lists are lower priority. 
    # Name
    #   option to generate name after race and cultural elements to more appropriately reflect IRL name creation.
    # Race
    # Health
    # dictionary of personality attributes.
    def __init__(self, creature = None, intelligence = None):
        print('hello, world!')

        self.creature = creature
        if self.creature:
            self.creature.owner = self

        self.intelligence = intelligence
        if self.intelligence:
            self.intelligence.owner = self

class simulation():
    def __init__(self):
        self.items = []
        self.creatures = []
        self.places = []

class com_Creature:
    def __init__(self, hp):
        self.hp = hp

class com_Intelligences:
    """ com_Intelligences have 
    a name
    a list of goals, 
    a dict of personality traits
    """
    def __init__(self, goals = None, traits = None):
        # print("They're here.")

        self.goals = goals
        if self.goals:
            for goal in self.goals:
                goal.owner = self

        self.traits = traits
        if self.traits:
            self.traits.owner = self

    def randomize_traits():
        for key in self.traits:
            self.traits[key] = random.randint(-50, 50)

class com_Item:
    def __init__(self):
        print('Carry me.')
class com_Container:
    def __init__(self):
        print("GET IN MA BELLY.")
class com_Goal():
    def __init__(self):
        print('GOOOOOOOOOOOOOAL!')
class com_Action():
    def __init__(self):
        print('and... action!')

def generateCharacter(hp = 10):
    creature_com1 = com_Creature(hp)
    Character = entity(creature_com1)
    return Character

def simulation_init(seed=None):
    random.seed(seed)

    global DEFAULT_TRAITS, GOALS, WORLD

    DEFAULT_TRAITS= {
        "LAW": 0,
        	# +41 to +50	is an absolute believer in the rule of law
            # +26 to +40	has a great deal of respect for the law
            # +11 to +25	respects the law
            # −10 to +10	doesn't feel strongly about the law
            # −25 to −11	does not respect the law
            # −40 to −26	disdains the law
            # −50 to −41	finds the idea of laws abhorrent
        "LOYALTY": 0,
            # +41 to +50	has the highest regard for loyalty
            # +26 to +40	greatly prizes loyalty
            # +11 to +25	values loyalty
            # −10 to +10	doesn't particularly value loyalty
            # −25 to −11	views loyalty unfavorably
            # −40 to −26	disdains loyalty
            # −50 to −41	is disgusted by the idea of loyalty
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
        "POWER": 0,
            # +41 to +50	believes that the acquisition of power over others is the ideal goal in life and worthy of the highest respect
            # +26 to +40	sees power over others as something to strive for
            # +11 to +25	respects power
            # −10 to +10	doesn't find power particularly praiseworthy
            # −25 to −11	has a negative view of those who exercise power over others
            # −40 to −26	hates those who wield power over others
            # −50 to −41	finds the acquisition and use of power abhorrent and would have all masters toppled
        "TRUTH": 0,
            # +41 to +50	believes the truth is inviolable regardless of the cost
            # +26 to +40	believes that honesty is a high ideal
            # +11 to +25	values honesty
            # −10 to +10	does not particularly value the truth
            # −25 to −11	finds blind honesty foolish
            # −40 to −26	sees lying as an important means to an end
            # −50 to −41	is repelled by the idea of honesty and lies without compunction
        "CUNNING": 0,
            # +41 to +50	holds well-laid plans and shrewd deceptions in the highest regard
            # +26 to +40	greatly respects the shrewd and guileful
            # +11 to +25	values cunning
            # −10 to +10	does not really value cunning and guile
            # −25 to −11	sees guile and cunning as indirect and somewhat worthless
            # −40 to −26	holds shrewd and crafty individuals in the lowest esteem
            # −50 to −41	is utterly disgusted by guile and cunning
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
        "DECORUM": 0,
            # +41 to +50	views decorum as a high ideal and is deeply offended by those that fail to maintain it
            # +26 to +40	greatly respects those that observe decorum and maintain their dignity
            # +11 to +25	values decorum, dignity and proper behavior
            # −10 to +10	doesn't care very much about decorum
            # −25 to −11	finds maintaining decorum a silly, fumbling waste of time
            # −40 to −26	sees those that attempt to maintain dignified and proper behavior as vain and offensive
            # −50 to −41	is affronted by the whole notion of maintaining decorum and finds so-called dignified people disgusting
        "TRADITION":0,
            # +41 to +50	holds the maintenance of tradition as one of the highest ideals
            # +26 to +40	is a firm believer in the value of tradition
            # +11 to +25	values tradition
            # −10 to +10	doesn't have any strong feelings about tradition
            # −25 to −11	disregards tradition
            # −40 to −26	finds the following of tradition foolish and limiting
            # −50 to −41	is disgusted by tradition and would flout any [he/she] encounters if given a chance
        "ARTWORK": 0,
            # +41 to +50	believes that the creation and appreciation of artwork is one of the highest ideals
            # +26 to +40	greatly respects artists and their works
            # +11 to +25	values artwork
            # −10 to +10	doesn't care about art one way or another
            # −25 to −11	finds artwork boring
            # −40 to −26	sees the whole pursuit of art as silly
            # −50 to −41	finds art offensive and would have it destroyed whenever possible
        "COOPERATION": 0,
            # +41 to +50	places cooperation as one of the highest ideals
            # +26 to +40	sees cooperation as very important in life
            # +11 to +25	values cooperation
            # −10 to +10	doesn't see cooperation as valuable
            # −25 to −11	dislikes cooperation
            # −40 to −26	views cooperation as a low ideal not worthy of any respect
            # −50 to −41	is thoroughly disgusted by cooperation
        "INDEPENDENCE": 0,
            # +41 to +50	believes that freedom and independence are completely non-negotiable and would fight to defend them
            # +26 to +40	treasures independence
            # +11 to +25	values independence
            # −10 to +10	doesn't really value independence one way or another
            # −25 to −11	finds the ideas of independence and freedom somewhat foolish
            # −40 to −26	sees freedom and independence as completely worthless
            # −50 to −41	hates freedom and would crush the independent spirit wherever it is found
        "STOICISM": 0,
            # +41 to +50	views any show of emotion as offensive
            # +26 to +40	thinks it is of the utmost importance to present a bold face and never grouse, complain or even show emotion
            # +11 to +25	believes it is important to conceal emotions and refrain from complaining
            # −10 to +10	doesn't see much value in being stoic
            # −25 to −11	sees no value in holding back complaints and concealing emotions
            # −40 to −26	feels that those who attempt to conceal their emotions are vain and foolish
            # −50 to −41	sees concealment of emotions as a betrayal and tries [his/her] best never to associate with such secretive fools
        "INTROSPECTION": 0,
            # +41 to +50	feels that introspection and all forms of self-examination are the keys to a good life and worthy of respect
            # +26 to +40	deeply values introspection
            # +11 to +25	sees introspection as important
            # −10 to +10	doesn't really see the value in self-examination
            # −25 to −11	finds introspection to be a waste of time
            # −40 to −26	thinks that introspection is valueless and those that waste time in self-examination are deluded fools
            # −50 to −41	finds the whole idea of introspection completely offensive and contrary to the ideals of a life well-lived
        "SELF_CONTROL": 0,
            # +41 to +50	believes that self-mastery and the denial of impulses are of the highest ideals
            # +26 to +40	finds moderation and self-control to be very important
            # +11 to +25	values self-control
            # −10 to +10	doesn't particularly value self-control
            # −25 to −11	finds those that deny their impulses somewhat stiff
            # −40 to −26	sees the denial of impulses as a vain and foolish pursuit
            # −50 to −41	has abandoned any attempt at self-control and finds the whole concept deeply offensive
        "TRANQUILITY": 0,
            # +41 to +50	views tranquility as one of the highest ideals
            # +26 to +40	strongly values tranquility and quiet
            # +11 to +25	values tranquility and a peaceful day
            # −10 to +10	doesn't have a preference between tranquility and tumult
            # −25 to −11	prefers a noisy, bustling life to boring days without activity
            # −40 to −26	is greatly disturbed by quiet and a peaceful existence
            # −50 to −41	is disgusted by tranquility and would that the world would constantly churn with noise and activity
        "HARMONY": 0,
            # +41 to +50	would have the world operate in complete harmony without the least bit of strife or disorder
            # +26 to +40	strongly believes that a peaceful and ordered society without dissent is best
            # +11 to +25	values a harmonious existence
            # −10 to +10	sees equal parts of harmony and discord as part of life
            # −25 to −11	doesn't respect a society that has settled into harmony without debate and strife
            # −40 to −26	can't fathom why anyone would want to live in an orderly and harmonious society
            # −50 to −41	believes deeply that chaos and disorder are the truest expressions of life and would disrupt harmony wherever it is found
        "MERRIMENT": 0,
            # +41 to +50	believes that little is better in life than a good party
            # +26 to +40	truly values merrymaking and parties
            # +11 to +25	finds merrymaking and partying worthwhile activities
            # −10 to +10	doesn't really value merrymaking
            # −25 to −11	sees merrymaking as a waste
            # −40 to −26	is disgusted by merrymakers
            # −50 to −41	is appalled by merrymaking, parties and other such worthless activities
        "CRAFTSMANSHIP": 0,
            # +41 to +50	holds crafts[man]ship to be of the highest ideals and celebrates talented artisans and their masterworks
            # +26 to +40	has a great deal of respect for worthy crafts[man]ship
            # +11 to +25	values good crafts[man]ship
            # −10 to +10	doesn't particularly care about crafts[man]ship
            # −25 to −11	considers crafts[man]ship to be relatively worthless
            # −40 to −26	sees the pursuit of good crafts[man]ship as a total waste
            # −50 to −41	views crafts[man]ship with disgust and would desecrate a so-called masterwork or two if [he/she] could get away with it
        "MARTIAL_PROWESS": 0,
            # +41 to +50	believes that martial prowess defines the good character of an individual
            # +26 to +40	deeply respects skill at arms
            # +11 to +25	values martial prowess
            # −10 to +10	does not really value skills related to fighting
            # −25 to −11	finds those that develop skill with weapons and fighting distasteful
            # −40 to −26	thinks that the pursuit of the skills of warfare and fighting is a low pursuit indeed
            # −50 to −41	abhors those that pursue the mastery of weapons and skill with fighting
        "SKILL": 0,
            # +41 to +50	believes that the mastery of a skill is one of the highest pursuits
            # +26 to +40	really respects those that take the time to master a skill
            # +11 to +25	respects the development of skill
            # −10 to +10	doesn't care if others take the time to master skills
            # −25 to −11	finds the pursuit of skill mastery off-putting
            # −40 to −26	believes that the time taken to master a skill is a horrible waste
            # −50 to −41	sees the whole idea of taking time to master a skill as appalling
        "HARD_WORK": 0,
            # +41 to +50	believes that hard work is one of the highest ideals and a key to the good life
            # +26 to +40	deeply respects those that work hard at their labors
            # +11 to +25	values hard work
            # −10 to +10	doesn't really see the point of working hard
            # −25 to −11	sees working hard as a foolish waste of time
            # −40 to −26	thinks working hard is an abject idiocy
            # −50 to −41	finds the proposition that one should work hard in life utterly abhorrent
        "SACRIFICE": 0,
            # +41 to +50	finds sacrifice to be one of the highest ideals
            # +26 to +40	believes that those who sacrifice for others should be deeply respected
            # +11 to +25	values sacrifice
            # −10 to +10	doesn't particularly respect sacrifice as a virtue
            # −25 to −11	sees sacrifice as wasteful and foolish
            # −40 to −26	finds sacrifice to be the height of folly
            # −50 to −41	thinks that the entire concept of sacrifice for others is truly disgusting
        "COMPETITION": 0,
            # +41 to +50	holds the idea of competition among the most important and would encourage it wherever possible
            # +26 to +40	views competition as a crucial driving force in the world
            # +11 to +25	sees competition as reasonably important
            # −10 to +10	doesn't have strong views on competition
            # −25 to −11	sees competition as wasteful and silly
            # −40 to −26	deeply dislikes competition
            # −50 to −41	finds the very idea of competition obscene
        "PERSEVERANCE": 0,
            # +41 to +50	believes that perseverance is one of the greatest qualities somebody can have
            # +26 to +40	greatly respects individuals that persevere through their trials and labors
            # +11 to +25	respects perseverance
            # −10 to +10	doesn't think much about the idea of perseverance
            # −25 to −11	sees perseverance in the face of adversity as bull-headed and foolish
            # −40 to −26	thinks there is something deeply wrong with people that persevere through adversity
            # −50 to −41	finds the notion that one would persevere through adversity completely abhorrent
        "LEISURE_TIME": 0,
            # +41 to +50	believes that it would be a fine thing if all time were leisure time
            # +26 to +40	treasures leisure time and thinks it is very important in life
            # +11 to +25	values leisure time
            # −10 to +10	doesn't think one way or the other about leisure time
            # −25 to −11	finds leisure time wasteful
            # −40 to −26	is offended by leisure time and leisurely living
            # −50 to −41	believes that those that take leisure time are evil and finds the whole idea disgusting
        "COMMERCE": 0,
            # +41 to +50	sees engaging in commerce as a high ideal in life
            # +26 to +40	really respects commerce and those that engage in trade
            # +11 to +25	respects commerce
            # −10 to +10	doesn't particularly respect commerce
            # −25 to −11	is somewhat put off by trade and commerce
            # −40 to −26	finds those that engage in trade and commerce to be fairly disgusting
            # −50 to −41	holds the view that commerce is a vile obscenity
        "ROMANCE": 0,
            # +41 to +50	sees romance as one of the highest ideals
            # +26 to +40	thinks romance is very important in life
            # +11 to +25	values romance
            # −10 to +10	doesn't care one way or the other about romance
            # −25 to −11	finds romance distasteful
            # −40 to −26	is somewhat disgusted by romance
            # −50 to −41	finds even the abstract idea of romance repellent
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
        "KNOWLEDGE": 0
            # +41 to +50	finds the quest for knowledge to be of the very highest value
            # +26 to +40	views the pursuit of knowledge as deeply important
            # +11 to +25	values knowledge
            # −10 to +10	doesn't see the attainment of knowledge as important
            # −25 to −11	finds the pursuit of knowledge to be a waste of effort
            # −40 to −26	thinks the quest for knowledge is a delusional fantasy
            # −50 to −41	sees the attainment and preservation of knowledge as an offensive enterprise engaged in by arrogant fools
    }

    GOALS = {
        "thing": [#(book, throne, sword)
            "STAY_ALIVE",
            "MAINTAIN_ENTITY_STATUS",	
            "RULE_THE_POWER_STRUCTURE(powerStructure=governments)",	#dreams of ruling the world
            "BRING_IDEAL_TO_THE_NOUN(ideal='peace',noun='world')",	#dreams of bringing (lasting) #ideal#(peace, war, religion, value) to the person/place (world)
            "BECOME_A_LEGENDARY_ITEM(type='sword')"	#dreams of becoming a legendary #occupation#(warrior, smith)
        ],
        "person": [#/animal (from http://dwarffortresswiki.org/index.php/DF2014:Personality_trait)
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
            "RULE_THE_POWER_STRUCTURE(powerStructure=governments)",	#dreams of ruling the world
            "CREATE_A_GREAT_WORK_OF_ART",	#dreams of creating a great work of art	Goal completed upon creation of Artifact or Masterpiece
            "CRAFT_A_MASTERWORK",	#dreams of crafting a masterwork someday	Goal completed upon creation of Artifact or Masterpiece
            "BRING_IDEAL_TO_THE_NOUN(ideal='peace',noun='world')",	#dreams of bringing lasting #ideal#(peace, war, religion, value) to the person/place (world)
            "BECOME_A_LEGENDARY_OCCUPATION(occupation='warrior')",	#dreams of becoming a legendary #occupation#(warrior, smith)
            "MASTER_A_SKILL(skill='smithing')",	#dreams of mastering a skill	Goal completed upon reaching Legendary skill status.
            "EXPERIENCE_IDEAL(ideal='love')",	#dreams of experiencing(falling in) an ideal state (love)
            "SEE_THE_GREAT_NATURAL_SITES(wonders=wonders)",	#dreams of seeing the great (natural) places of the world
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
            "DISCOVER(type='area')"	#learn new knowledge, discover new places, meet new people,
                #new to you, to society, to your people
        ],
        "place": [#location 
            "STAY_ALIVE",	
            "MAINTAIN_ENTITY_STATUS",
            "BECOME_CENTER_OF_#IDEA#" #(center of trade, politics, education, technology, culture)
        ],
        "quality": [
            "STAY_ALIVE",	
            "MAINTAIN_ENTITY_STATUS",	
            "BRING_#IDEAL#_TO_THE_#PERSON/PLACE#"	#dreams of bringing lasting #ideal#(peace, war, religion, value) to the person/place (world)
        ],
        "idea": [
            "STAY_ALIVE",	
            "MAINTAIN_ENTITY_STATUS",	
            "BRING_#IDEAL#_TO_THE_#PERSON/PLACE#"	#dreams of bringing lasting #ideal#(peace, war, religion, value) to the person/place (world)
        ],
        "action": [
            "STAY_ALIVE",	
            "MAINTAIN_ENTITY_STATUS",	
            "BRING_#IDEAL#_TO_THE_#PERSON/PLACE#"	#dreams of bringing lasting #ideal#(peace, war, religion, value) to the person/place (world)
        ],
        "state": [
            "STAY_ALIVE",	
            "MAINTAIN_ENTITY_STATUS",	
            "BECOME_A_LEGENDARY_#OCCUPATION#"	#dreams of becoming a legendary #occupation#(warrior, smith)
        ]
    }

    WORLD=simulation()

    # mainChar.name -> walksto(bank.name) -> toGet(money.amount)

    mainChar = generateCharacter()
    WORLD.creatures.append(mainChar)

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

def simulation_main_loop():
    
    # while (len(protagonist.goals()) > 0):
        # Protagonist selects one of it's available goals (ordered by urgency/optionality) 
        # if not protagonist.mainGoal:
        #     protagonist.mainGoal = protagonist.goals.pop()

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
    print("Exiting...")

if __name__ == "__main__":
    def traceryTest():
        rules = {
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

    def narrativeGenTest():
        simulation_init()
        simulation_main_loop()

    # maintest()
    narrativeGenTest()

