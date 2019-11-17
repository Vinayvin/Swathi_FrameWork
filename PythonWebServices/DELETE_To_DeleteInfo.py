import  requests
import json
import jsonpath


baseURL="https://reqres.in"
res="/api/users/2"

response=requests.delete(baseURL+res)
print(response.status_code)

