import requests
import json
access_token = 'M2NkMGI4MmEtN2Y4OC00ODI4LTk0MTQtYmM2NGY3YzI5MThjZjIzMzJhZjMtYjBi_PE93_9423ebf1-df21-4e89-8049-a08f8e9c5998'

url = 'https://webexapis.com/v1/people'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {
 'email': '12002284@student.pxl.be'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

person_id = 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yMDUxOTVlMy02MmU0LTQ4ZmMtODQwYi1jZGI2MTE3MzE1YjQ'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
 }
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
