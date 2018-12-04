import queue
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r'C:\Users\thepe_000\Desktop\PP5\Void Scribe\Server Side\Active Work\void-scribe-firebase-adminsdk-xtf9j-a419db8670.json')
firebase_admin.initialize_app(cred)

DataBaseReference = firestore.client()
_UploadQueue_ = queue.Queue()
#Objects in Queue must be indexable format -> [0] collection reference [1] document contents [2] (optional) document name

def _UploadDocument_(collection, document_content, document_name=None):
    #collection - A reference to the collection to insert into, utalize DataBaseReference to obtain this
    #document_content - A dictionary object that is the contents of the document to upload
    #document_name - An optional string used to name the uploaded document
    #If no document name is provided push() is used to generate a unique ID
    
    
    doc_ref = collection.document(document_name)
    doc_ref.set(document_data=document_content)

import NameGenerator
import re

name_types = NameGenerator.getNameTypes()
name_types = list(name_types)

list_obj = []
for name_type in name_types:
    dict_obj = {}
    dict_obj["Key"] = name_type

    temp = list(name_type)
    temp[0] = temp[0].upper()
    name_type = ''.join(temp)
    
    split = re.findall('[A-Z][^A-Z]*', name_type)

    display = ""
    for word in split:
        display += word
        display += " "

    dict_obj["Display"] = display

    list_obj.append(dict_obj)

data = {"Name_Types":list_obj}
DataBaseReference.collection("Algorithm_Information").document("Name_Types").set(data)

