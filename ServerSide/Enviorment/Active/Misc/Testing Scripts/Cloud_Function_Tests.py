import requests
data = {"Req_Type":"Name", "Req_Arguments":{"Amount":5, "Name_Type":"americanCities"}, "User_ID":"Josh_Testing_Script"}
response = requests.post(r"https://us-central1-void-scribe.cloudfunctions.net/voidScribeRequest", json=data)
print(response.content)