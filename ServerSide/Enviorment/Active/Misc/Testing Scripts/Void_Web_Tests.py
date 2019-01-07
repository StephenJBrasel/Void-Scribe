import requests
import time

good_data_1 = {"Req_Type":"Name", "Req_Arguments":{"Amount":5, "Name_Type":"americanCities"}, "User_ID":"Josh_Testing_Script"}
good_data_2 = {"Req_Type":"Sentence", "Req_Arguments":{"Amount":5, "Sentence_Type":"myth"}, "User_ID":"Josh_Testing_Script"}
bad_data_1 = {"Reqqq_Type":"Name", "Req_Arguments":{"Amount":5, "Name_Type":"pokemon"}, "User_ID":"Josh_Testing_Script"}
bad_data_2 = {"Req_Type":"Name", "Req_Arguments":{"Amount":5, "Name_Type":"pokeman"}, "User_ID":"Josh_Testing_Script"}
bad_data_3 = {"Req_Type":"Sentence", "Req_Arguments":{"Amount":5, "Sentencee_Type":"myth"}, "User_ID":"Josh_Testing_Script"}

def TestRequest(data, name):
    req = requests.post(r"http://127.0.0.1:5000/VoidScribeRequest", json=data)

    print("Test " + name + " Status: " + str(req.status_code))
    print(req.json())
    if req.status_code == 200:
        return (200, req.json()["Doc_ID"])
    else:
        return (400, )

def TestRetreive(Doc_ID):
    start = time.time()
    resp = requests.post(r"http://127.0.0.1:5000/VoidScribeRetreive", json={"Doc_ID":Doc_ID})

    while (resp.json()["Data"]["completed"] == False):
        time.sleep(.5)
        resp = requests.post(r"http://127.0.0.1:5000/VoidScribeRetreive", json={"Doc_ID":Doc_ID})

    print(f"Successfully Retreived After: {time.time() - start}")
    print(resp.json())

Tests = []

Tests.append((good_data_1, "White 1"))
Tests.append((good_data_2, "White 2"))
Tests.append((bad_data_1, "Black 1"))
Tests.append((bad_data_2, "Black 2"))
Tests.append((bad_data_3, "Black 3"))

for test in Tests:
    resp = TestRequest(test[0], test[1])
    if resp[0] == 200:
        TestRetreive(resp[1])


    
