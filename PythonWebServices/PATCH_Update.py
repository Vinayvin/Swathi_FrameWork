import  requests
import json
import jsonpath


baseURL="https://reqres.in"
res="/api/users/2"
file=open("./PatchUpdate.json","r")
json_input=file.read()
req=json.loads(json_input)

response=requests.patch(baseURL+res,req)
print(response.status_code)
print(response.text)
json_response=json.loads(response.text)
name=jsonpath.jsonpath(json_response,"name")
print(name[0])