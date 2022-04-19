import requests
roomID = "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vZDA1ZGY2MDAtYmZiNC0xMWVjLWEwNzUtZGQ2NTZlYjEwOGYx"
message = "Hier zijn mijn schermafbeeldingen van EN2_Devasc_2SNE-taken"
token = 'MTUyNDJjMmYtNzA5Yy00ZThhLTk0NWMtMzQ0ZjY1MDE0ZGY0MWYxZDg0MjUtODEy_PE93_9423ebf1-df21-4e89-8049-a08f8e9c5998'

url = 'https://webexapis.com/v1/messages'

headers = {
 'Authorization': 'Bearer {}'.format(token),
 'Content-Type': 'application/json'
}

params={'roomId': roomID, 'text' : message}

res = requests.post(url, headers=headers, json=params)
print(res.json())

session = requests.Session()
