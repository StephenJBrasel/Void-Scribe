import void_scribe
print(dir(void_scribe))

from void_scribe import MarkovGenerator
print(dir(MarkovGenerator))

from void_scribe import NameGenerator
print(dir(NameGenerator))

print(NameGenerator.MarkovName(amount=15))

from void_scribe import StoryGenerator
print(dir(StoryGenerator))

print(StoryGenerator.generateSentence(amount=1))