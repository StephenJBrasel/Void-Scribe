import queue
import firebase_admin.firestore

_RequestsQueue_ = queue.Queue()
def EnqueueRequest(request_document):
    _RequestsQueue_.put(request_document)

def __ProcessNameRequest__(request_document):
    import NameGenerator.NameGenerator
    
    values = request_document.to_dict()




_AlgorithmRequestMap_ = {}


def ProcessRequest():
    return None
import NameGenerator.NameGenerator
print(NameGenerator.NameGenerator.getNameTypes())

