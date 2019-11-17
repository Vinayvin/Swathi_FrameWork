#POST is used to create new information
import  requests
import json
import jsonpath


baseURL="https://reqres.in"
resource = "/api/register"
file=open("./User.json","r")
#reading the data from json file
json_input=file.read()
req=json.loads(json_input)

print(req)
response=requests.post(baseURL+resource,req)
print(response)
print(response.status_code)

print(response.text)
response_json=json.loads(response.text)
id=jsonpath.jsonpath(response_json,"id")
print(id)