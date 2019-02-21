import random
import json

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

        NGrams.append("".join(NGram)) 

    return NGrams

def createMarkovChain(ngrams):
    #Parameters
    ##ngrams - Indexable collections of strings (Of the same len())
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
    ##filepath - Optional argument, if provided path is valid and ends with .json, 
    # the dictionary will be saved
    #Return
    ##The Markov Dictionary

    #NGram Data, Generate Chains
    chains = {}
    for i, entry in enumerate(data):
        ngrams = createNGrams(entry, order)
        if len(ngrams) != 0:
            new_chains = createMarkovChain(ngrams)
            chains = updateMarkovDictionary(chains, new_chains)

    if filepath != None and filepath.endswith('.json'):
        with open(filepath, 'w') as f:
            json.dump(chains, f, indent=4, sort_keys=True)

    return chains

def markovGenerate(markovDictionary, order, amount, max_length=15):
    #Parameters
    ##markovDictionary
    ##order
    ##amount
    ##max_length
    #Return
    ##generated_outputs - List of amount number Lists of ordered objects occording to markov algorithm

    #Helper Function
    def stringifyEndofList(_list):
        return "".join(_list[(-1 * order):])
    
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
        while len(output) < max_length and stringifyEndofList(output) in markovDictionary.keys():
            #Build population and Weights
            links = markovDictionary[stringifyEndofList(output)]
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