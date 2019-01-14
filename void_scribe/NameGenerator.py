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
        potentials = __df__[Name_Type]
        ret.append(random.choice(potentials))
    return ret

def MarkovName(
        Name_Type = 'americanForenames', 
        amount = 3, 
        order = 3, 
        maxlength = 0, 
        seed = None):
    txt = __df__[Name_Type]
    ret = (markov.generate(txt, amount, order, maxlength=maxlength, seed=seed)) 
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
