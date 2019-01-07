import random

# Generate dict of objects, classes -> uid
# Generate sequence of objects, story -> [class[uid], class[uid], class[uid]]
# Parse to text from sequence of objects -> The fox jumped

def createNGRAMList(strings = ["hello", "world"], order = 3):
    """
    Returns starters, ngrams: 

    starters = list of len(order) ngrams from the start of each string in strings.

    ngrams = dictionary with keys of ngrams and values of following individual characters.
    
    """
    ngrams = {}
    starts, ends = [], []
    for string in strings:
        for i in range(len(string) - order + 1):
            gram = string[i:(i + order)]
            if i == 0:
                if gram not in starts:
                    starts.append(gram)
            elif i == (len(string) - order):
                if gram not in ends:
                    ends.append(gram)
            if i+order < len(string):
                if gram not in ngrams.keys():
                    ngrams[gram] = []
                ngrams[gram].append(string[i+order])
    return starts, ends, ngrams

def fillProbabilities(data):
    
    totalProbability = 0
    numWithoutProb = 0
    for item in data:
        if len(item) > 1:
            # print(item)
            totalProbability += item[1]
        else:
            numWithoutProb += 1
    # print(totalProbability)
    if totalProbability < 1 and totalProbability >= 0  and numWithoutProb != 0:
        remainingProbability = 1 - totalProbability
        remainingProbability /= numWithoutProb
        for item in data:
            if len(item) == 1:
                item.append(remainingProbability)
    # print(data)
    return data

def PCFGtoTCFG(data):
    prob = 0
    for item in data:
        prob += item[1]
        item[1] = prob
    data[len(data) - 1][1] = 1
    return data

def markovIt(
        starters = ['def'],
        ends = ['ault'],
        ngrams = {'default':'this is default'},
        numGenerated = 10,
        order = 3,
        minlength = 3,
        maxlength = 20,
        seed = None):
    """
    Chomsky Normal-Form Grammar. 
    Returns list of [numGenerated] generated words.
    """
    random.seed(seed)
    ret = []
    start = 0
    stop = len(starters)
    for i in range(numGenerated):
        randy = random.randrange(start, stop)
        ret.append(starters[randy])
        length = len(ret[i])
        while ret[i][-order:] in ngrams.keys() and length < maxlength:
            if length >= minlength:
                # if the last bits of the word are in enders, break off, continue to next word.
                print(ret[i][-order:])
                if ret[i][-order:] in ends:
                    print(ret[i])
                    # break
            potentials = ngrams[ret[i][-order:]]
            nextChar = random.choice(potentials)
            ret[i] += nextChar
            length += 1
    return ret

def generate(strings = ["hello", "world"], numGenerated=10, order = 3, minlength = 3, maxlength = 10, seed = None):
    """
    Returns list of [numGenerated] generated words.
    """
    maxlength = (len(max(strings, key=len)))
    starts, ends, ngrams = createNGRAMList(strings, order)
    print(starts)
    print(ends)
    ret = markovIt(starts, ends, ngrams, numGenerated, order, minlength, maxlength, seed)
    return ret

if __name__ == "__main__":
    # words = []
    print(generate())