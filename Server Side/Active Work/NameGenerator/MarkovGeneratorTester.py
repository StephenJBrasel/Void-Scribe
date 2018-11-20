import MarkovGenerator as markov
import pandas as pd


def load(filepath="names.csv"):
    df = pd.read_csv(
        filepath,
        # sep=",",
        engine="python",
        encoding="latin1",
        # index_col=0
        )
    # df.info()
    # print(df)
    return df

def parse(parsee="names example"):
    ret = parsee.split(' ')
    # print(ret)
    return ret

def main(repeatCount = 10):
    df = load("Server Side/Active Work/NameGenerator/names.csv")
    # for item in df.examples:
    #     print(parse(item))
    generatedContent = []
    # print(df.values[0][0])
    for i in range(len(df)):
        # print(df.values[i][0])
        for j in range(repeatCount):
            txt = parse(df.values[i][1])
            # print(txt)
            generatedContent.append([df.values[i][0], markov.generate(txt, order = 3)])
        # print()
    
    # txt = parse(names['test'])
    # markov(txt, order=2)
    for item in generatedContent:
        print(item)

main(1)
