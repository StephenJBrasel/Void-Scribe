import os
import json
import uuid

data_path = 'C:/Users/thepe_000/Desktop/PP5/Void-Scribe/void_scribe/data/PromptTemplates/'
dest_path = 'C:/Users/thepe_000/Desktop/PP5/Void-Scribe/void_scribe/data/TempPromptTemplates/'

for jsonFile in os.listdir(data_path):

    with open(data_path + jsonFile) as f:
            jsonData = json.load(f)
    subject = jsonData[0]['phrase']['subject']
    predicate = jsonData[0]['phrase']['predicate']
    if 'objekt' in jsonData[0]['phrase']:
        objekt = jsonData[0]['phrase']['objekt']
    features = jsonData[0]['features']

    if 'complements' in jsonData[0]:
        complements = jsonData[0]['complements']

    newJSON = {}
    newJSON['componets'] = {}
    newJSON['clauses'] = []
    newJSON['clauses'].append({})

    #subject
    uid = uuid.uuid4().hex
    newJSON['componets'][uid] = subject
    newJSON['clauses'][0]['subject'] = [uid]
    #predicate
    uid = uuid.uuid4().hex
    newJSON['componets'][uid] = predicate
    newJSON['clauses'][0]['predicate'] = [uid]
    #objekt
    if 'objekt' in jsonData[0]['phrase']:
        uid = uuid.uuid4().hex
        newJSON['componets'][uid] = objekt
        newJSON['clauses'][0]['objekt'] = [uid]
    #features
    newJSON['clauses'][0]['features'] = features
    #complements
    if 'complements' in jsonData[0]:
        newJSON['clauses'][0]['complements'] = []
        for complement in complements:
            newComplements = []
            for componet in complement:
                uid = uuid.uuid4().hex
                newJSON['componets'][uid] = componet
                newComplements.append(uid)
            newJSON['clauses'][0]['complements'].append(newComplements)

    with open(dest_path + jsonFile, 'w') as outfile:
        json.dump(newJSON, outfile)