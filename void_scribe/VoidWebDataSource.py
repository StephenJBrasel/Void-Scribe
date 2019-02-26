from requests import post, Response

voidWebURL = 'http://www.voidscribe.com/data/names'

class VoidWebDataSource():
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

    def Tags(self, nameTypes):
        return self.MetaData(nameTypes)['Tags']

    def Category(self, nameTypes):
        return self.MetaData(nameTypes)['Category']

    def Proper(self, nameTypes):
        return self.MetaData(nameTypes)['Proper']

    def GenerationData(self, nameTypes):
        req = self.__baseWebRequestTemplate__(nameTypes)
        req["meta"] = True
        req["dictionary"] = True
        return self.__sendRequest__(req)

    def NameTypes(self):
        from requests import get

        resp = get(url='http://www.voidscribe.com/data/names/nameTypes')
        return resp.json()

 