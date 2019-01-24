from void_scribe import MarkovGen as markov
import random
from void_scribe.data.names import names as __df__

def getNames(
        Name_Type = 'americanForenames', 
        amount = 3, 
        seed = None):
    random.seed(seed)
    ret = []
    for i in range(amount):
        potentials = __df__[Name_Type]["Data"]
        ret.append(random.choice(potentials))
    return ret

def MarkovName(
        Name_Type = 'americanForenames', 
        amount = 3, 
        order = 3, 
        minlength = 3,
        maxlength = 0, 
        seed = None, 
        prior = 0):
    txt = __df__[Name_Type]["Data"]
    ret = (markov.generate(txt, amount, order, minlength, maxlength, seed, prior)) 
    return ret 

def getNameTypes():
    return list(__df__.keys())


if __name__ == "__main__":
    # print(getNameTypes())
    # print(getNames(Name_Type = 'werewolfForenames'))
    # print(MarkovName(Name_Type = 'werewolfForenames'))
    def getGenNames():
        for nameType in getNameTypes():
            print(f"{nameType} : {MarkovName(Name_Type=nameType)} ||| {getNames(Name_Type=nameType)}")
    getGenNames()
