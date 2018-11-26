import queue
import Main
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r'C:\Users\thepe_000\Desktop\PP5\Void Scribe\Server Side\Active Work\void-scribe-firebase-adminsdk-xtf9j-a419db8670.json')
firebase_admin.initialize_app(cred)

DataBaseReference = firestore.client()
UploadQueue = queue.Queue()

doc_ref = db.collection(u'TEST_COLLECTION').document(u'TEST_DOCUMENT')
doc_ref.set({
    u'test1': u'Hello there,',
    u'test2': u'General',
    u'test3': u'Kenobi'
})


def UploadDocument(collection, document_content, document_name):
    #collection - A reference to the collection to insert into, utalize DataBaseReference to obtain this
    #document_content - A dictionary object that is the contents of the document to upload
    #docuement_name - An optional string used to name the uploaded document
    #If no document name is provided push() is used to generate a unique ID
    
    doc_ref = None
    if document_name == None:
        doc_ref = collection.push()
    else:
        doc_ref = collection.document(document_name)

    doc_ref.set(document_content)

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
            doc_info = UploadQueue.get(timeout=1/10)
        except:
            continue

        UploadDocument(doc_info[0], doc_info[1], doc_info[2])
