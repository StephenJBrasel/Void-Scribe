from flask import Flask, render_template, request, Response, jsonify
import json
import requests
from void_scribe import NameGenerator, Stories

app = Flask(__name__)

@app.route("/crossdomain.xml")
def crossdomain():
    return render_template('crossdomain.xml')

@app.route("/VoidScribeRequest", methods = ['POST'])
def VoidScribeRequest():
    data = request.get_json()
    print(data)

    #Validate Primary Fields
    if "Req_Type" not in data.keys():
        return Response(json.dumps({"Message":"Missing Required Argument: Req_Type"}), 400, mimetype='application/json')
    if "Req_Arguments" not in data.keys():
        return Response(json.dumps({"Message":"Missing Required Argument: Req_Argument"}), 400, mimetype='application/json')
    if "User_ID" not in data.keys():
        return Response(json.dumps({"Message":"Missing Required Argument: User_ID"}), 400, mimetype='application/json')

    #Validate Argument Fields
    if data["Req_Type"] == "Name":
        if "Name_Type" not in data["Req_Arguments"].keys():
            return Response(json.dumps({"Message":"Missing Required Argument For Name Request: Name_Type"}), 400, mimetype='application/json')
        if data["Req_Arguments"]["Name_Type"] not in list(NameGenerator.getNameTypes()):
            return Response(json.dumps({"Message":"Argument: Name_Type, Is An Unhandled Value"}), 400, mimetype='application/json')
        if "Amount" not in data["Req_Arguments"].keys():
            data["Req_Arguments"]["Amount"] = 1

    elif data["Req_Type"] == "Sentence":
        if "Sentence_Type" not in data["Req_Arguments"].keys():
            return Response(json.dumps({"Message":"Missing Required Argument For Name Request: Sentence_Type"}), 400, mimetype='application/json')
        if data["Req_Arguments"]["Sentence_Type"] not in Stories.data.keys():
            #return Response({"Message":"Argument: Sentence_Type, Is An Unhandled Value"}, 400, mimetype='application/json')
            return Response(json.dumps({"Message":"Argument: Sentence_Type, Is An Unhandled Value"}), 400, mimetype='application/json')
        if "Amount" not in data["Req_Arguments"].keys():
            data["Req_Arguments"]["Amount"] = 1

    else:
        #return Response({"Message":"Argument: Req_Type, Is An Unhandled Value"}, 400, mimetype='application/json')
        return Response(json.dumps({"Message":"Argument: Req_Type, Is An Unhandled Value"}), 400, mimetype='application/json')

    #Build Cloud Function Data Package
    cf_data = {"Req_Type":data["Req_Type"], "Req_Arguments":data["Req_Arguments"], "User_ID":data["User_ID"]}

    #Send To Cloud Function
    cf_req = requests.post(r"https://us-central1-void-scribe.cloudfunctions.net/voidScribeRequest", json=cf_data)

    print(cf_req.json())

    #Interpret Response From Firebase
    if cf_req.status_code != 200:
        #return Response({"Message":f"Error Code Received Comminucating With Cloud Function, Error Code: {cf_req.status_code}", "Data":cf_req.json()}, 424, mimetype='application/json')
        return Response(json.dumps({"Message":f"Error Code Received Comminucating With Cloud Function, Error Code: {cf_req.status_code}"}), 200, mimetype='application/json')
    else:
        #return Response(cf_req.json(), 200, mimetype='application/json')
        return Response(json.dumps({"Doc_ID":cf_req.json()}), 200, mimetype='application/json')

    print("Returned Final Response")

@app.route("/VoidScribeRetreive", methods = ['POST'])
def VoidScribeRetreive():
    data = request.get_json()

    #Validate Document ID Field
    if "Doc_ID" not in data.keys():
        return Response(json.dumps({"Message":"Missing Required Argument For Retreival: Doc_ID"}), 400, mimetype='application/json')
    
    #Build Cloud Function Data Package
    cf_data = {"Doc_ID":data["Doc_ID"]}

    #Send To Cloud Function
    cf_req = requests.put(r"https://us-central1-void-scribe.cloudfunctions.net/voidScribeRetreive", cf_data)

    #Interpret Response From Firebase
    if cf_req.status_code != 200:
        return Response(json.dumps({"Message":f"Error Code Received Comminucating With Cloud Function, Error Code: {cf_req.status_code}"}), 424, mimetype='application/json')
    else:
        return Response(json.dumps({"Data":cf_req.json()}), 200, mimetype='application/json')


    


