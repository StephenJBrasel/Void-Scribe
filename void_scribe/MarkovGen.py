import random
import pickle

# Generate dict of objects, classes -> uid
# Generate sequence of objects, story -> [class[uid], class[uid], class[uid]]
# Parse to text from sequence of objects -> The fox jumped


def createNGrams(elements=None, order=3):
    #Parameters
    ##elements - iterable object that contains individual elements
    ##order - The order of the generated ngrams
    #Returns
    ##NGrams - A List of shingles of order(order)
    if elements == None: 
        return None
    if order == None:
        return None
    if order == 0:
        return []
    if order > len(elements):
        return []

    NGrams = []
    count = len(elements)
    for index, element in enumerate(elements):
        if count - index < order: 
            break

        NGram = []

        for i in range(order):
            NGram.append(elements[index + i])

        NGrams.append(tuple(NGram))

    return NGrams

def createMarkovChain(ngrams):
    #Parameters
    ##ngrams - Indexable collections of Indexable Collections (Of the same len())
    #Returns
    ##chain - The markov chain, follows the following format...
    #{ ngram:{ link:count, link:count } ngram:{ link:count } }
    #where... 
    ##ngram is a unique ngram from the provided ngrams parameter
    ##link is the expected following entry
    ##count is the occurance rate of that link for that ngram

    #Validate elements to ensure the order is uniform
    order = len(ngrams[0])
    for ngram in ngrams:
        if (len(ngram) != order):
            raise ValueError("NGrams are not of the same order")
    
    #Output Variable
    chain = {}
    #Record the size to prevent out of range
    count = len(ngrams)
    #Generate NGram-Link relationships for every NGram
    for index, ngram in enumerate(ngrams):
        #The last NGram cannot have a link (it is an end)
        if index == count - 1: 
            break

        #Capture the link for this NGram
        link = ngrams[index + 1][order - 1]

        #If the Ngram does not exist create the entry and set the link count to 1
        if ngram not in chain.keys():
            entry = {}
            entry[link] = 1
            chain[ngram] = entry
        #If the Ngram already exists, update the Links
        else:
            #If the link already exists, increment the count
            if link in chain[ngram].keys():
                chain[ngram][link] += 1
            #Otherwise set the link count to 1
            else:
                chain[ngram][link] = 1
            
    return chain

def updateMarkovDictionary(markovDict, new_Chains):
    #Determine NGrams that are being added that already existed
    shared = set(markovDict.keys()) & set(new_Chains.keys())
    shared = list(shared)
    #Determine NGrams that are new to the original MarkovDictionary
    new = set(new_Chains.keys()) - set(markovDict.keys())
    new = list(new)

    #Update MarkovDictionary with new NGrams
    for NGram in new:
        markovDict[NGram] = new_Chains[NGram]

    #Update existing NGram entries with new counts
    for NGram in shared:
        #Get a list of links for this NGram
        links = new_Chains[NGram].keys()

        #Update the count for every link
        for link in links:
            #If a link already exists update the count
            if link in markovDict[NGram].keys():
                markovDict[NGram][link] += new_Chains[NGram][link]
            #Otherwise create the entry
            else:
                markovDict[NGram][link] = new_Chains[NGram][link]

    return markovDict
    
def createMarkovDictionary(data, order, filepath=None):
    #Parameters
    ##data - Data formated for use with NGrams, 
    # this is a list of list of single objects by which to create NGrams from
    ##order - The order of NGrams to generate
    ##filepath - Optional argument, if provided path is valid and ends with .p, 
    # the dictionary will be pickled
    #Return
    ##The Markov Dictionary

    #NGram Data, Generate Chains
    chains = {}
    for i, entry in enumerate(data):
        ngrams = createNGrams(entry, order)
        if len(ngrams) != 0:
            new_chains = createMarkovChain(ngrams)
            chains = updateMarkovDictionary(chains, new_chains)

    if filepath != None and filepath.endswith('.p'):
        pickle.dump(chains, open(filepath, "wb"))

    return chains

def markovGenerate(markovDictionary, order, amount, max_length=15):
    #Parameters
    ##data - List of List of Objects
    #Return
    ##generated_outputs - List of amount number Lists of ordered objects occording to markov algorithm

    #Helper Function
    def tupleEndofList(_list):
        return tuple(_list[(-1 * order):])
    
    generated_outputs = []
    for i in range(amount):
        #Select random start ngram
        start = random.randint(0, len(markovDictionary.keys()) - 1)
        start = list(markovDictionary.keys())[start]

        #Generate Output Using Chains    
        output = []
        #Start by appening the start grams
        for item in start:
            output.append(item)

        #Now utalize the MarkovDictionary
        while len(output) < max_length and tupleEndofList(output) in markovDictionary.keys():
            #Build population and Weights
            links = markovDictionary[tupleEndofList(output)]
            population = list(links.keys())

            #Get Key-Value pairs (key = link, value = frequency)
            items = links.items()

            #Determine population total by adding all frequencies
            total = 0
            for item in items:
                total += item[1]

            #Determine Weights using population total
            weights = []
            for item in items:
                weights.append(item[1] / total)

            #Choose from links using distribution
            next_gram = random.choices(population=population, weights=weights)[0]

            #Append choice to output
            output.append(next_gram)

        generated_outputs.append(output)

    return generated_outputs


    
     




# TODO Stop returning a markov Chain, this is just supposed to generate the NGRAMS. 
def createNGRAMList(strings = ["hello", "world"], order = 3):
    """
    Returns starts, ends, ngrams:  

    starts = list of len(order) ngrams from the start of each string in strings.  
    ends = list of len(order) ngrams from the end of each string in strings.  
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

# TODO Integrate this into createNGRAMList to speed up algorithm.
def createNGramFullList(strings = ["hello", "world"], order = 3):
    """
    Returns starts, ends, ngrams:  

    starts = list of len(order) ngrams from the start of each string in strings.  
    ends = list of len(order) ngrams from the end of each string in strings.  
    ngrams = list of dictionaries with keys of ngrams from length [order] to length[1] and values of following individual characters.
    
    """
    fullList, starts, starters, ends, enders = [], [], [], [], []
    count = int(order)
    # maximum = len(max(strings, key=len))
    # if order > maximum:
    #     count = maximum
    while count > 0:
        starters, enders, ngrams = createNGRAMList(strings, count)
        if count == order:
            starts = starters
            ends = enders
        fullList.append(ngrams)
        count -= 1
    # print(starts)
    # print(starters)
    # print(ends)
    # print(enders)
    # print(fullList)
    return starts, ends, fullList

def listToListOfLists(data = ['a', 'b']):
    ''' 
    data = list of elements

    returns a list of the elements in data in their own list.
    ['a', 'b'] BECOMES [['a'], ['b']]
    '''
    ret = []
    for item in data:
        ret.append([item])
    return ret

def fillProbabilities(data = [['i', 0.5], ['j']]):
    '''
    data = list of elements

    Converts a null or partially filled list of [events, probabilities] into full probability list.
    [['i', 0.5], ['j']] -> BECOMES -> [['i', 0.5], ['j', 0.5]]
    '''
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

def duplicateElemToPCFG(data = [['a'], ['a'], ['a'], ['b']]):
    uniqueCounts = {}
    PCFG = []
    total = len(data)
    for item in data:
        if item[0] not in uniqueCounts.keys():
            uniqueCounts[item[0]] = 1
        else:
            uniqueCounts[item[0]] += 1
    for item in uniqueCounts:
        PCFG.append([item, (uniqueCounts[item]/total)])
    return PCFG

def completeListWithPriors(
    data = [['y'], ['e'], ['i']], 
    prior = 0.02,
    completeSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ):
    '''
    data = a list of lists where each individual list is [element, probability]
    prior = Dirichlet prior (?), small probability (range(infinitesimal, 0.05)) that all [elements] not in data[elementlist] be chosen.
    completeSet = (superset) list of unique elements to assign Prior probability to. MUST INCLUDE ALL ELEMENTS IN DATA.

    This function assigns the elements of the completeSet not already in the list of possible elements [data] a small possibility (range(infinitesimal, 0.05)).

    returns list of lists of elements with assigned probabilities. data with high probability, elements in complete set that weren't in data have a low probability.
    '''
    if prior == 0 or len(data) >= len(completeSet):
        return fillProbabilities(data)
    currentProb = (1-prior)
    otherProb = prior/(len(completeSet)-len(data))
    data = fillProbabilities(data)
    totalProb = 0
    # if all letters already exist in an ngram list, DO NOT ALTER PROBABILITY.
    # for i in data:
    #     i[1] *= currentProb
    for i in completeSet:
        # if i not in data elements
        inData = False
        for j in data:
            if i == j[0]:
                inData = True
                j[1] *= currentProb
                break
        if not inData:
        # put it in the elements
            data.append([i, otherProb])   
    for i in data:
        totalProb += i[1]
    # print(totalProb)
    # print(data)
    return data

def PCFGtoTCFG(data = [['i', 0.5], ['j', 0.5]]):
    '''
    Converts data from individually probabilistic Chomsky Normal Form Grammars to consecutively, cumulatively probabilistic CFG's:  
    [['i', 0.5], ['j', 0.5]] -> BECOMES -> [['i', 0.5], ['j', 1]]
    '''
    prob = 0
    for item in data:
        prob += item[1]
        item[1] = prob
    data[len(data) - 1][1] = 1
    return data

def markovIt(
        starters = ['def'],
        ends = ['ault'],
        ngrams = {'default':'a'},
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
            # if length >= minlength:
                # TODO if the last bits of the word are proper ends, break off, continue to next word.
                # print(ret[i][-order:])
                # if ret[i][-order:] in ends:
                #     print(ret[i])
                #     break
            potentials = ngrams[ret[i][-order:]]
            nextChar = random.choice(potentials)
            ret[i] += nextChar
            length += 1
    return ret

def generate(
        strings = ["hello", "world"], 
        numGenerated=10, 
        order = 3, 
        minlength = 3, 
        maxlength = 0, 
        seed = None, 
        prior = 0):
    """
    Returns list of [numGenerated] generated words.
    """
    if maxlength == 0:
        maxlength = (len(max(strings, key=len)))
    starts, ends, ngrams = createNGRAMList(strings, order)
    ret = markovIt(starts, ends, ngrams, numGenerated, order, minlength, maxlength, seed)
    return ret

def checkPotentialNodes(listDicts, currentList, key, n):
    """
    function returns list of potential next nodes in markov chain.
    if no nodes exist, returns None.
    """
    potentials = None
    if key[-n:] in listDicts[currentList].keys():
        potentials = listDicts[currentList][key[-n:]]
    else:
        if  (currentList + 1) < len(listDicts):
            currentList += 1
            n -= 1
            potentials = checkPotentialNodes(listDicts, currentList, key, n)
    if potentials:
        if len(potentials) == 0:
            if  (currentList + 1) < len(listDicts):
                currentList += 1
                n -= 1
                potentials = checkPotentialNodes(listDicts, currentList, key, n)
    return potentials

# TODO incorporate new [list of dictionaries] structure with [elem, probability] generation into markov model.
def markovItv2(
        starters = ['def'],
        ends = ['ault'],
        listDicts = {'default':'a'},
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
    midLength = (minlength + maxlength) / 2
    listMin = 0
    listMax = len(listDicts) - 1
    start = 0
    stop = len(starters)
    for i in range(numGenerated):
        randy = random.randrange(start, stop)
        ret.append(starters[randy])
        length = len(ret[i])
        currentList = 0
        hasEnded = False
        while length < (maxlength - order):
            # potentials = listDicts[currentList][ret[i][-order:]]
            n = int(order)
            # option to set potentials the old way: via the order set at the beginning
            potentials = checkPotentialNodes(listDicts, currentList, ret[i], n)
            if potentials is not None:
                prob = random.random()
                # nextChar = random.choice(potentials)
                for elem in potentials:
                    if elem[1] > prob:
                        nextChar = elem[0]
                        break
                ret[i] += nextChar
                length += 1
            else:
                break
            if length > minlength:
                chance = random.randint(minlength, maxlength)
                if chance < len(ret[i]):
                    hasEnded = False
                    for end in ends:
                        if ret[i][-1:] == end[0]:
                            ret[i] = ret[i][:-1]
                            ret[i] += end
                            hasEnded = True
                            break
                    if hasEnded:
                        break
        # if not hasEnded:
        #     ret[i] += random.choice(ends)
    return ret

def generateFull(strings = ["hello", "world"], numGenerated=10, order = 3, minlength = 3, maxlength = 0, seed = None, prior = 0):
    """
    Returns list of [numGenerated] generated words.
    """
    if maxlength == 0:
        maxlength = (len(max(strings, key=len)))
    # starts, ends, ngrams = createNGRAMList(strings, order)
    starts, ends, dictList = createNGramFullList(strings, order)
    for i in range(len(dictList)):
        for key in dictList[i]:
            if i != (len(dictList) - 1):
                # TODO Fix this ridiculousness.
                dictList[i][key] = PCFGtoTCFG(duplicateElemToPCFG(listToListOfLists(dictList[i][key])))
            else:
                # TODO Fix this ridiculousness.
                dictList[i][key] = PCFGtoTCFG(completeListWithPriors(duplicateElemToPCFG(listToListOfLists(dictList[i][key])), prior))

    ret = markovItv2(starts, ends, dictList, numGenerated, order, minlength, maxlength, seed)
    return ret

if __name__ == "__main__":
    '''
    mainDescriptor
        This program generates words based on a Markov Model.
        It takes in a list of words, 
        creates 
        - a list of starters of length [order]
        - a list of enders of length [order] and
        - a list of dictionaries with descending lengths from [order] to [1] with the corresponding list of ['char', probability].
        from there it generates a full list of dictionaries of lists of [element, prob] based on completing it with all 
            alphabet characters with probabilities equal to Prior/number of letters that weren't seen on the first pass.
        with the list of starts, ends, and dictionaries, 
            we choose a start from the list of starts,
            generate the next characters from the dictionaries of possible characters starting with the dictionary of key length [order]
                if no further options are found, search dict of key length [order - 1] up to key length [1]
                key length one should have every possible character assigned a value via Priors, if Prior is greater than 0.
            until we either 
                reach a character that has no further character OR 
                a max length is achieved OR 
                the last [order] characters match any of the possible [ends] and the word is longer than min length.
        we do this [numGenerated] number of times and send back the list of generated words.
    '''

    def probTest():
        alphabet = { # 1/26 = 0.038461538461538464
            "letters" : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            "partialProb" : [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h'], ['i'], ['j'], ['k'], ['l'], ['m'], ['n'], ['o'], ['p'], ['q'], ['r'], ['s'], ['t'], ['u'], ['v'], ['w'], ['x'], ['y'], ['z']],
            "filledPartial" : [['a', 0.5], ['b', 0.02], ['c', 0.02], ['d', 0.02], ['e', 0.02], ['f', 0.02], ['g', 0.02], ['h', 0.02], ['i', 0.02], ['j', 0.02], ['k', 0.02], ['l', 0.02], ['m', 0.02], ['n', 0.02], ['o', 0.02], ['p', 0.02], ['q', 0.02], ['r', 0.02], ['s', 0.02], ['t', 0.02], ['u', 0.02], ['v', 0.02], ['w', 0.02], ['x', 0.02], ['y', 0.02], ['z', 0.02]],
            "TPCFG" : [['a', 0.5], ['b', 0.52], ['c', 0.54], ['d', 0.56], ['e', 0.5800000000000001], ['f', 0.6000000000000001], ['g', 0.6200000000000001], ['h', 0.6400000000000001], ['i', 0.6600000000000001], ['j', 0.6800000000000002], ['k', 0.7000000000000002], ['l', 0.7200000000000002], ['m', 0.7400000000000002], ['n', 0.7600000000000002], ['o', 0.7800000000000002], ['p', 0.8000000000000003], ['q', 0.8200000000000003], ['r', 0.8400000000000003], ['s', 0.8600000000000003], ['t', 0.8800000000000003], ['u', 0.9000000000000004], ['v', 0.9200000000000004], ['w', 0.9400000000000004], ['x', 0.9600000000000004], ['y', 0.9800000000000004], ['z', 1]]
        }
        # for i in letters:
        #     alphabet.append([i])
        # print(alphabet)
        print(fillProbabilities(alphabet['partialProb']))
        # print(PCFGtoTCFG(alphabet["filledPartial"]))

    def ngramTest():
        from void_scribe.data.names import names as __df__
        # print(list(__df__.keys()))
        starts, ends, ngrams = createNGRAMList(__df__['test2'])
        # print(starts)
        # print(ends)
        # # print(ngrams)
        for item in ngrams:
            print(f"{item} : {ngrams[item]}")
        for i in ngrams:
            ngrams[i] = completeListWithPriors(listToListOfLists(ngrams[i]), prior=0.01)
            print(f"{i} : {ngrams[i]}")
            print()
        # print(ngrams)
    
    def duplicateTest():
        data = [['a'], ['a'], ['a'], ['b']]
        catch = duplicateElemToPCFG(data)
        print(f'outside: {data}')
        print(catch)

    def fullListTest():
        print('Regular')
        createNGramFullList()
        print('Order = 3')
        createNGramFullList(order=3)
        print('Order = -1')
        createNGramFullList(order=-1)

    def generateTest():
        from void_scribe.data.names import names as __df__
        for nameType in __df__:
            print(f"{nameType}: {generate(__df__[nameType], numGenerated=10, order = 3, minlength = 3, maxlength = 0, seed = None, prior = 0)}")
    
    def generateWerewolfTest():
        from void_scribe.data.names import names as __df__
        nameType = 'werewolfForenames'
        print(f"{nameType}: {generate(__df__[nameType], numGenerated=10, order = 3, minlength = 3, maxlength = 0, seed = None, prior = 0)}")
    
    def generateFullTest():
        from void_scribe.data.names import names as __df__
        for nameType in __df__:
            print(f"{nameType}: {generateFull(__df__[nameType], numGenerated=10, order = 3, minlength = 3, maxlength = 0, seed = None, prior = 0)}")
    
    # ngramTest()
    # print(completeListWithPriors())
    # duplicateTest()
    # fullListTest()
    generateTest()
    # generateWerewolfTest()
    # generateFullTest()