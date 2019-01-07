import queue
import firebase_admin.firestore
import FireStore_Uploader
import Utilities
from void_scribe import NameGenerator, StoryGenerator, MarkovGenerator, Stories

_RequestsQueue_ = queue.Queue()
def EnqueueRequest(request_document):
    _RequestsQueue_.put(request_document)

def __ProcessNameRequest__(request_document):
    values = request_document.to_dict()

    #Ensure Proper Request Format
    if "Req_Arguments" not in values.keys():
        print("Bad Name Request, No Req_Arguments Field")
        return ("Missing Required Field Req_Arguments", "Error")

    if "Amount" not in values["Req_Arguments"]:
        amount = 1
    else:
        amount = values["Req_Arguments"]["Amount"]

    if "Name_Type" not in values["Req_Arguments"]:
        print("Bad Request Arguemtns, No Name_Type Field")
        return ("Missing Required Argument Name_Type", "Error")
    else:
        name_type = values["Req_Arguments"]["Name_Type"]

    if name_type not in list(NameGenerator.getNameTypes()):
        print("Bad Request Arguments, Name_Type field is not a valid Name_Type")
        return ("Invalid Name_Type", "Error")

    #Generate Names
    gen_names = NameGenerator.MarkovName(Name_Type=name_type, amount=amount)

    return gen_names

def __ProcessSentenceRequest__(request_document):

    values = request_document.to_dict()

    #Ensure Proper Request Format
    if "Req_Arguments" not in values.keys():
        print("Bad Sentence Request, No Req_Arguments Field")
        return ("Missing Required Field Req_Arguments", "Error")

    if "Amount" not in values["Req_Arguments"]:
        amount = 1
    else:
        amount = values["Req_Arguments"]["Amount"]

    if "Sentence_Type" not in values["Req_Arguments"]:
        print("Bad Request Arguemtns, No Sentence_Type Field")
        return ("Missing Required Argument Sentence_Type", "Error")
    else:
        sentence_type = values["Req_Arguments"]["Sentence_Type"]

    if sentence_type not in Stories.data.keys():
        print("Bad Request Arguments, Sentence_Type field is not a valid Sentence_Type")
        return ("Invalid Sentence_Type", "Error")

    #Generate Sentences
    gen_names = StoryGenerator.generateSentence(Sentence_Type=sentence_type, amount=amount)

    return gen_names




_AlgorithmRequestMap_ = {"Name":__ProcessNameRequest__, "Sentence":__ProcessSentenceRequest__}
__StorageCollectionMap__ = {"Name":FireStore_Uploader.DataBaseReference.collection("Generated_Names"), "Sentence":FireStore_Uploader.DataBaseReference.collection("Generated_Sentences"), "None Specified":FireStore_Uploader.DataBaseReference.collection("Bad_Requests")}


def __ProcessRequest__(request_document):
    values = request_document.to_dict()

    #Ensure Proper Document Formatting
    error_found = False
    if "Req_Type" not in values.keys():
        print("Bad Document, No Req_Type Field")
        processed_req = ("There Was A Problem With The Document: No Required Req_Type Field", "Error")
        values["Req_Type"] = "None Specified"
    else:
        req_type = values["Req_Type"]
        processed_req = _AlgorithmRequestMap_[req_type](request_document)

        if "Error" in processed_req:
            processed_req = [processed_req[1]]
            error_found = True

    #Format Completed_Request and Storage documents then send them for uploading
    proc_req_doc = {}
    storage_doc = {}

    proc_req_doc["Request"] = values
    storage_doc["Data"] = processed_req
    storage_doc["Timestamp"] = Utilities.GetTimeStamp()
    proc_req_doc["Timestamp"] = Utilities.GetTimeStamp()
    proc_req_doc["Processed_Request"] = processed_req
    proc_req_doc["Req_Doc_ID"] = request_document.id

    if "Hash_Key" in values.keys():
        proc_req_doc["Hash_Key"] = values["Hash_Key"]
        storage_doc["Hash_Key"] = values["Hash_Key"]

    if "User_ID" in values.keys():
        proc_req_doc["User_ID"] = values["User_ID"]
        storage_doc["User_ID"] = values["User_ID"]
    
    proc_doc_colec_ref = FireStore_Uploader.DataBaseReference.collection("Completed_Requests")


     #Check For Format Error Within processed_req
    if error_found:
        storage_doc["Original_Request_Document"] = values
        storage_doc["Original_Request_Document_ID"] = request_document.id
        storage_doc_colec_ref = FireStore_Uploader.DataBaseReference.collection("Bad_Requests")
    else:
        storage_doc_colec_ref = __StorageCollectionMap__[values["Req_Type"]]

    FireStore_Uploader.EnqueueDocument(proc_doc_colec_ref, proc_req_doc)
    FireStore_Uploader.EnqueueDocument(storage_doc_colec_ref, storage_doc)

def AlgorithmProcessorEntryPoint():
    
    shut_down = False
    def Shutdown_Processor():
        nonlocal shut_down
        shut_down = True
    from Main import AddShutDownProcess
    AddShutDownProcess(Shutdown_Processor)

    while True:
        if shut_down:
            break
        
        alg_req = None
        try:
            alg_req = _RequestsQueue_.get(timeout=1/10)
        except:
            continue

        if alg_req == None:
            continue
        
        __ProcessRequest__(alg_req)
 

        





# import NameGenerator
# print(NameGenerator.MarkovName(Name_Type="pokemon", amount=50))


    


