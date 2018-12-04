import NameGenerator
from Stories import data
import tracery
from tracery.modifiers import base_english

# class Entity():
#     components = []

# def makeCharacter():
#     character = Entity()
#     return character

def main():
    # mainChar = Entity()
    # for i in range(10):
    #     print(hash(mainChar))
    fun = data['adjective']
    fun2 = {
        # ensure adjectives don't contradict one another. 
        'origin':['#[quantity:#adjQuantity#][opinion:#adjOpinion#][size:#adjSize#][age:#adjAge#][shape:#adjShape#][colour:#adjColour#][origin:#adjOrigin#][material:#adjMaterial#][purpose:#adjPurpose#]adjectiveOrderList#'],
        'adjectiveOrderList': [ #(2^numAdjCategories) - 1, 2^8-1 = 255
            '#adjectiveQuantity# #noun#'],
        'noun':['knife'],
        'adjectiveQuantity':['[noun:#noun.s#]#quantity# #adjectiveOpinion#','#adjectiveOpinion#'],
        'adjectiveOpinion':['#opinion# #adjectiveSize#','#adjectiveSize#'],
        'adjectiveSize':['#size# #adjectiveAge#','#adjectiveAge#'],
        'adjectiveAge':['#age# #adjectiveShape#','#adjectiveShape#'],
        'adjectiveShape':['#shape# #adjectiveColour#','#adjectiveColour#'],
        'adjectiveColour':['#colour# #adjectiveOrigin#','#adjectiveOrigin#'],
        'adjectiveOrigin':['#origin# #adjectiveMaterial#','#adjectiveMaterial#'],
        'adjectiveMaterial':['#material# #adjectivePurpose#','#adjectivePurpose#'],
        'adjectivePurpose':['#purpose#',''],
        'adjQuantity':['many'],
        'adjOpinion': ['lovely'],
        'adjSize': ['little'],
        'adjAge': ['old'],
        'adjShape': [ #including height and weight
            'rectangular'], 
        'adjColour': ['green'],
        'adjOrigin': [ #nationality/planetality/systemality
            'French'], 
        'adjMaterial': ['silver'],
        'adjPurpose':[ # or qualifier
            'whittling'] 
    }
    # for i in fun:
    #     print(i)
    #     print(fun[i])
    # print(fun)
    rules = {
        'origin': ['#hello.capitalize#, #location#!'],
        'hello': ['hello', 'greetings', 'howdy', 'hey'],
        'location': ['world', 'solar system', 'galaxy', 'universe']
        }
    # for j in rules:
    #     print(j)
    #     print(rules[j])
    # print(rules)
    for i in data:
        print(i)
        print()
        for j in range(10):
            grammar = tracery.Grammar(data[i])
            grammar.add_modifiers(base_english)
            print(grammar.flatten('#origin#'))  # prints, e.g., 'Hello, world!'

        


main()
