


def FireStoreMonitorEntryPoint():
    #Create a secure connection to the Firestore REST API using google Oauth2
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession
    scopes = ["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/firebase.database"]

    credentials = service_account.Credentials.from_service_account_file( r'C:\Users\thepe_000\Desktop\PP5\Void Scribe\Server Side\Active Work\void-scribe-firebase-adminsdk-xtf9j-a419db8670.json', scopes=scopes)

    authed_session = AuthorizedSession(credentials)

    #Use authenticated session to retreive the current timestamp
    import json
    my_data = dict()
    my_data["timestamp"] = {".sv": "timestamp"}
    json_data = json.dumps(my_data).encode()

    response = authed_session.put("https://void-scribe.firebaseio.com/TEST_COLLECTION/TEST_DOCUMENT_2.json", data=json_data)

    if response.status_code != 200:
        raise Exception("Communication With The Firebase REST Server Unsuccesful")

    last_timestamp = response.json()['timestamp']

    #Establish database connection
    import firebase_admin
    from firebase_admin import credentials, firestore
    cred = credentials.Certificate(r'C:\Users\thepe_000\Desktop\PP5\Void Scribe\Server Side\Active Work\void-scribe-firebase-adminsdk-xtf9j-a419db8670.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    requests_ref = db.collection(u'Algorithm_Requests')

    #Register Callback to allow safe termination
    shut_down = False
        def Shutdown_Monitor():
            nonlocal shut_down
            shut_down = True
        from Main import AddShutDownProcess
        AddShutDownProcess(Shutdown_Monitor)

    import time
    while True:
        if shut_down:
            break

        query_ref = requests_ref.where(u'Timestamp', u'>', last_timestamp)

        doc_generator = query_ref.get()

        for doc in doc_generator:
            
            values = doc.to_dict()

            if values['Timestamp'] > last_timestamp:
                last_timestamp = values['Timestamp']

        time.sleep(1/5)

