import random



def createNGramListDEPRECATED(strings, order = 3):
    # ngramSet = pd.DataFrame(columns=['string', 'num', 'followers'])
    ngramList = []
    beginnings = []
    for string in strings:
        # print(f"String: {string}\t\tRange: {range(len(string) - order)}")
        for i in range(len(string) - order + 1):
            notFound = True
            gram = string[i:(i + order)]
            if i == 0:
                if gram not in beginnings:
                    beginnings.append(gram)
            # print(gram)
            j=0
            for val in ngramList:
                # print(type(val))
                # print(val[0])
                if val[0] == gram:
                    ngramList[j][1] += 1
                    # print(ngramList[j])
                    if i+order < len(string):
                        if string[i + order] not in ngramList[j][2]:
                            ngramList[j][2] += [string[i + order]]
                    notFound = False
                j += 1
            if notFound:
                ngramList.append([gram, 1, []])
                if i+order < len(string):
                    ngramList[j][2] = [string[i + order]]
            # print(gram)

    # for item in ngramList:
    #     print(item)
    # print('----')
    # for item in beginnings:
    #     print(item)
    
    total = 0
    for elem in ngramList:
        total += elem[1]
    prevElem = [0, 0, 0]
    for elem in ngramList:
        elem[1] = elem[1]/total 
        
        elem[1] += prevElem[1]
        prevElem = elem
        print(elem)

    return beginnings, ngramList

def createNGRAMList(strings, order = 3):
    ngrams = {}
    starters = []
    for string in strings:
        for i in range(len(string) - order + 1):
            gram = string[i:(i + order)]
            if i == 0:
                if gram not in starters:
                    starters.append(gram)
            if i+order < len(string):
                if gram not in ngrams.keys():
                    ngrams[gram] = []
                ngrams[gram].append(string[i+order])
    # for item in ngrams:
    #     print(f'{item} : {ngrams[item]}')
    # print()
    # for item in starters:
    #     print(item)
    return starters, ngrams

def markovIt(
        starters = ['default'], 
        ngrams = {'default':'this is default'}, 
        numGenerated = 10, 
        order = 3, 
        maxlength = 20, 
        seed = None):
    random.seed(seed)
    ret = []
    start = 0
    stop = len(starters)
    for i in range(numGenerated):
        randy = random.randrange(start, stop)
        ret.append(starters[randy])
        length = 0
        while ret[i][-order:] in ngrams.keys() and length < maxlength:
            potentials = ngrams[ret[i][-order:]]
            nextChar = random.choice(potentials)
            ret[i] += nextChar
            length += 1
            # print(f'Num: {randy} , text: {ret[i][-order:]} , potentionals: {potentials}')
    return ret

def generate(strings, numGenerated=10, order = 3, maxlength = 10, seed = None):
    maxlength = (len(max(strings, key=len)))
    starters, ngrams = createNGRAMList(strings, order)
    ret = markovIt(starters, ngrams, numGenerated, order, maxlength, seed)
    # print(ret)
    # print(ngrams[9])
    return ret
