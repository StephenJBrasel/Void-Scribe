from NameDataSource import NameDataSource
from requests import post, Response

voidWebURL = 'www.voidscribe.com/data/names'

class VoidWebDataSource(NameDataSource):
    def __baseWebRequestTemplate__(self, nameTypes):
        return {
            "nameTypes":nameTypes,
            "meta":False,
            "raw":False,
            "dictionary":False
        }

    def __sendRequest__(self, json):
        resp = post(voidWebURL, json=json)
        return resp.json()

    def Tags(self, nameTypes):
        return self.MetaData['Tags']

    def Category(self, nameTypes):
        return self.MetaData['Category']

    def Proper(self, nameTypes):
        return self.MetaData['Proper']

    def MarkovDictionary(self, nameTypes):
        req = self.__baseWebRequestTemplate__(nameTypes)
        req["dictionary"] = True
        return self.__sendRequest__(req)

    def RawData(self, nameTypes):
        req = self.__baseWebRequestTemplate__(nameTypes)
        req["raw"] = True
        return self.__sendRequest__(req)

    def MetaData(self, nameTypes):
        req = self.__baseWebRequestTemplate__(nameTypes)
        req["meta"] = True
        return self.__sendRequest__(req)

    def Data(self, nameTypes):
        req = self.__baseWebRequestTemplate__(nameTypes)
        req["meta"] = True
        req["raw"] = True
        req["dictionary"] = True
        return self.__sendRequest__(req)

from random import randint
for i in range(1, 20):
    x = randint(0, 2)
    print(x)