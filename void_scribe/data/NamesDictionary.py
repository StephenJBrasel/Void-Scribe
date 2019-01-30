import pickle
import pkg_resources
import os

class NamesDictionary:
    def __init__(self):
        # __DATA_PATH__ is the folder in which pickled name files are stored
        self.__DATA_PATH__ = pkg_resources.resource_filename('void_scribe', 'data/Names/')
        # __index__ maps each Name_Type string to the filepath of its pickle data
        self.__index__ = self.__createIndex__(self.__DATA_PATH__)
        # __requiredKeys__ is a list of keys that are required of incoming Name_Types
        self.__requiredKeys__ = ['Category', 'Tags', 'Data']

    def __loadNameType__(self, Name_Type):

        return pickle.load(open(self.__index__[Name_Type], "rb" ))

    def __saveNameType__(self, name_type, data):
        if type(data) != type({}):
            raise ValueError("Argument 'data' must be of type {}, passed argument is of type {}.".format(type({}), type(data)))
        if type(name_type) != type(""):
            raise ValueError("Argument 'name_type' must be of type {}, passed argument is of type {}.".format(type(""), type(name_type)))
        pickle.dump(data, open(self.__DATA_PATH__ + name_type + '.p', "wb"))
        # Update Index
        self.__updateIndex__()

    def __verifyNameType__(self, data):
        if type(data) != type({}):
            raise ValueError("Argument data must be of type {}, passed argument is of type {}.".format(type({}), type(data)))
        for req in self.__requiredKeys__:
            if req not in data.keys():
                return req
        return True

    def __getitem__(self, key):
        if key not in self.keys():
            raise KeyError(f"Provided key: '{key}' is not a valid Name_Type.")

        return self.__loadNameType__(key)

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

    def update(self, data, name_type, overwrite=False):
        # Updates the NamesDictionary with the given "other"
        # data must be either a dictionary or an iterable with key/values pairs
        # either as tuples or iterables of length 2
        # Returns the key of the dictionary if one was added, returns None if no update was made.
        # If a entry already exists under the provided name_type an execption is raised,
        # unless overwrite is set to True. In this case the existing entry is overwritten NOT merged.
        # data must contain the following keys with the associatly typed value,
        # otherwise an execption is raised.
        # Additional keys are ignored.
        #
        #   {
        #       'Category':'CATEGORY_NAME',  
        #       'Tags':[ITERABLE OF TYPE STRING],
        #       'Data':[ITERABLE OF TYPE STRING]
        #   }

        if data == None:
            raise ValueError("Missing required argument: 'data'.")
        elif name_type == None:
            raise ValueError("Missing required argument: 'name_type'.")
        elif type(name_type) != type(""):
            raise ValueError("Argument 'name_type' must be of type {} not of type {} .".format(type(""), type(name_type)))

        if len(data) == 0:
            return None

        if overwrite == False and name_type in self.keys():
            raise KeyError("Key {} already exists and 'overwrite' is not enabled. To enbale overwrite use the update() function.".format(name_type))

        save = {}

        # Build the save object
        if type(data) == type({}):
            # data is a dictionairy
            # Check for required keys
            res = self.__verifyNameType__(data)
            if res != True:
                raise ValueError("Argument 'data' was missing required key {}.".format(res))
            # build save object
            for req in self.__requiredKeys__:
                save[req] = data[req]
        elif '__iter__' not in dir(data):
            raise ValueError("Argument 'data' must be of type {} or be iterable.".format(type({})))
        else:
            # data is an iterable
            # Check for contents to be iterble
            if '__iter__' not in dir(data[0]):
                raise ValueError("Argument 'data' was an iterable but contains non-iterable key/value pairs")
            # Check for length two componets.
            elif len(data[0]) != 2:
                raise ValueError("Argument 'data' was an iterable but contains iterable objects that are not length 2.")
            temp = {}
            # Build a dictionary from k/v pairs.
            for pair in data:
                temp[pair[0]] = pair[1]
            # Check for required keys.
            res = self.__verifyNameType__(temp)
            if res != True:
                raise ValueError("Argument 'data' was missing required key {}.".format(res))
            # Build save object.
            for req in self.__requiredKeys__:
                save[req] = temp[req]  
        # Save Object
        self.__saveNameType__(name_type, save)
            
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


            
        
        


            

    
