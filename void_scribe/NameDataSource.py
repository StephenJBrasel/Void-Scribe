#This class is meant to be implemented as an abstract base class
#Allowing to create a dynamic source of data for use in markov generation.
#This is helpful as the Server Enviorment could utalize local files rather
#than the API

from abc import ABC, abstractmethod

class NameDataSource(ABC):
    @abstractmethod
    def Tags(self, nameTypes):
        pass

    @abstractmethod
    def Category(self, nameTypes):
        pass

    @abstractmethod
    def Proper(self, nameTypes):
        pass

    @abstractmethod
    def MarkovDictionary(self, nameTypes):
        pass

    @abstractmethod
    def RawData(self, nameTypes):
        pass

    @abstractmethod
    def MetaData(self, nameTypes):
        pass

    @abstractmethod
    def Data(self, nameTypes):
        pass

    @abstractmethod
    def GenerationData(self, nameTypes):
        pass

    @abstractmethod
    @property
    def NameTypes(self):
        pass