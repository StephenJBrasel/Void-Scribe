from void_scribe.VoidWebDataSource import VoidWebDataSource

class NameGenerator():
    def __init__(self, dataSource = VoidWebDataSource()):
        self.__dataSource__ = dataSource

    def generateNames(self, nameType = None, amount = 0):
        if nameType == None or amount == 0:
            return []

        from MarkovGen import markovGenerate        

        generationData = self.__dataSource__.GenerationData([nameType])
        markovDictionary = generationData[nameType]['dictionary']
        proper = generationData[nameType]['meta']['Proper']

        names = markovGenerate(markovDictionary, 3, amount)

        names = ["".join(name) for name in names]

        if proper:
            names = [name.title() for name in names]

        return names
        
    @property
    def ValidNameTypes(self):
        return self.__dataSource__.NameTypes()
        
    def retreiveNames(self, nameType, amount):
        from random import choice

        rawData = self.__dataSource__.RawData([nameType])
        rawData = rawData[nameType]['raw']['Data']
        metaData = self.__dataSource__.MetaData([nameType])
        proper = metaData[nameType]['meta']['Proper']

        chosenNames = []
        for i in range(amount):
            chosenNames.append(choice(rawData))

        if proper:
            chosenNames = [name.title() for name in chosenNames]


        return chosenNames

