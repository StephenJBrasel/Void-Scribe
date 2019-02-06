import pickle
import pkg_resources
import os

class MarkovIndex:
    def __init__(self):
        # __DATA_PATH__ is the folder in which pickled name files are stored
        self.__DATA_PATH__ = pkg_resources.resource_filename('void_scribe', 'data/MarkovDictionaries/')
        # __index__ maps each Name_Type string to the filepath of its pickle data
        self.__index__ = self.__createIndex__(self.__DATA_PATH__)

    def __loadMarkovDictionary__(self, Name_Type):

        return pickle.load(open(self.__index__[Name_Type], "rb" ))

    def __getitem__(self, key):
        if key not in self.keys():
            raise KeyError(f"Provided key: '{key}' is not a valid Name_Type, or a dictionary for the Name_Type does not exist.")

        return self.__loadMarkovDictionary__(key)

    def __len__(self):
        return len(self.__index__)

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

    def __updateIndex__(self):
        self.__index__ = self.__createIndex__(self.__DATA_PATH__)

    def __setitem__(self, key, value):
        self.update(value, key)

    def __delitem__(self, key):
        self.remove(key)

    def __iter__(self):
        return self.__index__.__iter__()

    def keys(self):
        return list(self.__index__.keys())

    def items(self):
        for key in self.keys():
            yield (key, self.__getitem__(key))

    def values(self):
        for key in self.keys():
            yield self.__getitem__(key)
            
    def remove(self, name_type):
        # Returns True if an entry was removed, False if not found
        # CAUTION WILL DELETE DATA FROM DISK
        if type(name_type) != type(""):
            raise ValueError("Argument 'name_type' was not required type: {}, 'name_type' is of type: {}.".format(type(""), type(name_type)))
        elif name_type not in self.keys():
            return False
        else:
            # Delete pickle file
            os.remove(self.__index__[name_type])
            # Update index
            self.__updateIndex__()
