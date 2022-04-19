import requests
import json
access_token = 'M2NkMGI4MmEtN2Y4OC00ODI4LTk0MTQtYmM2NGY3YzI5MThjZjIzMzJhZjMtYjBi_PE93_9423ebf1-df21-4e89-8049-a08f8e9c5998'
url = 'https://webexapis.com/v1/people/me'

headers = {
 'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
