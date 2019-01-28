import pickle
import pkg_resources
import os

class NamesDictionary:
    def __init__(self):
        #__DATA_PATH__ is the folder in which pickled name files are stored
        self.__DATA_PATH__ = pkg_resources.resource_filename('void_scribe', 'data/Names/')
        #__index__ maps each Name_Type string to the filepath of its pickle data
        self.__index__ = self.__createIndex__(self.__DATA_PATH__)

    def __loadNameType__(self, Name_Type):

        return pickle.load(open(self.__index__[Name_Type], "rb" ))

    def __getitem__(self, key):
        if key not in self.keys():
            raise KeyError(f"Provided key: '{key}' is not a valid Name_Type.")

        return self.__loadNameType__(key)

    def __createIndex__(self, path):
        #helper function, yields all files in a directory
        def files(path):  
            for file in os.listdir(path):
                if os.path.isfile(os.path.join(path, file)):
                    yield file

        index = {}
        for file in files(path):
            key = file.split('.')[0]
            index[key] = path + file
        return index

    def keys(self):
        return list(self.__index__.keys())

    def items(self):
        for key in self.keys():
            yield (key, self.__getitem__(key))

    def values(self):
        for key in self.keys():
            yield self.__getitem__(key)
            

    

test = NamesDictionary()
print(test['americanForenames'])
