import queue
import Main
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r'C:\Users\thepe_000\Desktop\PP5\Void Scribe\Server Side\Active Work\void-scribe-firebase-adminsdk-xtf9j-a419db8670.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'TEST_COLLECTION').document(u'TEST_DOCUMENT')
doc_ref.set({
    u'test1': u'Hello there,',
    u'test2': u'General',
    u'test3': u'Kenobi'
})


