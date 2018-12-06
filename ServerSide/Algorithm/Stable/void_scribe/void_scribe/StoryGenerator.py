from void_scribe import NameGenerator
from void_scribe.Stories import data
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

def getStoryElements():
    ret = []
    for i in data:
        ret.append(i)
    return ret

def generateSentence(
        Sentence_Type = 'quest', 
        amount = 3):
    ret = []
    for i in range(amount):
        grammar = tracery.Grammar(data[Sentence_Type])
        grammar.add_modifiers(base_english)
        ret.append(grammar.flatten('#origin#'))
    return ret


if __name__ == "__main__":
    items = generateSentence()
    for i in items:
        print(i)
