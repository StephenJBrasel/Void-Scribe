
def FireStoreMonitorEntryPoint():
    # #Create a secure connection to the Firestore REST API using google Oauth2
    # from google.oauth2 import service_account
    # from google.auth.transport.requests import AuthorizedSession
    # scopes = ["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/firebase.database"]

    # credentials = service_account.Credentials.from_service_account_file( r'C:\Users\thepe_000\Desktop\PP5\Void Scribe\Server Side\Active Work\void-scribe-firebase-adminsdk-xtf9j-a419db8670.json', scopes=scopes)

    # authed_session = AuthorizedSession(credentials)

    # #Use authenticated session to retreive the current timestamp
    # import json
    # my_data = dict()
    # my_data["timestamp"] = {".sv": "timestamp"}
    # json_data = json.dumps(my_data).encode()

    # response = authed_session.put("https://void-scribe.firebaseio.com/TEST_COLLECTION/TEST_DOCUMENT_2.json", data=json_data)

    # if response.status_code != 200:
    #     raise Exception("Communication With The Firebase REST Server Unsuccesful")

    # last_timestamp = response.json()['timestamp']


    #Establish database connection
    import firebase_admin
    from firebase_admin import credentials, firestore
    cred = credentials.Certificate(r'C:\Users\Joshua\Desktop\PP5\Void-Scribe\ServerSide\Enviorment\Active\Non-Public\void-scribe-firebase-adminsdk-xtf9j-a419db8670.json')
    firebase_admin.initialize_app(cred, name="Monitor")
    db = firestore.client()
    requests_ref = db.collection(u'Algorithm_Requests')

    #Register Callback to allow safe termination
    shut_down = False
    def Shutdown_Monitor():
        nonlocal shut_down
        shut_down = True
    from Main import AddShutDownProcess
    AddShutDownProcess(Shutdown_Monitor)

    #Register Terminal Command To Adjust Interval of Query
    query_rate = 1
    def command_QueryRate(arguments=None):
        if arguments == None or len(arguments) != 1:
            return "QueryRate has one required argument,\n\tex: QueryRate 5\n\tThis will set the QueryRate to 1/5 query per second." 
        try:
            float(arguments[0])
        except:
            return "Argument was passed with invalid syntax."
        
        nonlocal query_rate
        query_rate = float(arguments[0])

    queryrate_tip_help = "Adjusts the rate that Firestore is Queried for new requests.\n\tArguments\n\t\t1. Query Rate Value - Value to be set as the new Query Rate"
    def post_report_queryrate(result=None):
        if result==None:
            return
        print(result)
    from Terminal_Controller import AddTerminalCommand
    AddTerminalCommand("QueryRate", command_QueryRate, queryrate_tip_help, post_report_queryrate)


    import time
    import Algorithm_Processor
    while True:
        if shut_down:
            break

        query_ref = requests_ref.where(u'Processed', u'==', False)

        doc_generator = query_ref.get()

        for doc in doc_generator:
            
            values = doc.to_dict()

            Algorithm_Processor.EnqueueRequest(doc)
            
            doc.reference.update({'Processed':True})
            

        time.sleep(query_rate)

