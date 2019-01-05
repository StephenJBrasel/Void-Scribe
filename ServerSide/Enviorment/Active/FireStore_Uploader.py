import queue
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r'C:\Users\Joshua\Desktop\PP5\Void-Scribe\ServerSide\Enviorment\Active\Non-Public\void-scribe-firebase-adminsdk-xtf9j-a419db8670.json')
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

def EnqueueDocument(collection, document_content, document_name=None):
    _UploadQueue_.put((collection, document_content, document_name))

def FireStoreUploaderEntryPoint():

    shut_down = False
    def Shutdown_Uploader():
        nonlocal shut_down
        shut_down = True
    from Main import AddShutDownProcess
    AddShutDownProcess(Shutdown_Uploader)

    while True:

        if shut_down:
            break

        try:
            doc_info = _UploadQueue_.get(timeout=1/10)
        except:
            continue

        doc_name = None
        try:
            doc_name = doc_info[2]
        except:
            doc_name = None

        _UploadDocument_(doc_info[0], doc_info[1], doc_name)
