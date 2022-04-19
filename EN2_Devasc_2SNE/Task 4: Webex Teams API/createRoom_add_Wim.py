import requests

WEBEX_ROOM = 'DEVASC_JONAS_VERMESEN_2SNE'
url = 'https://webexapis.com/v1/rooms'
token = 'M2VmYjFlNzItMTY3NC00ZjA1LThkZDMtYzEwYWY1MjZiNTJlMjI1MThkZGItZTE2_PE93_9423ebf1-df21-4e89-8049-a08f8e9c5998'

headers = {
 'Authorization': 'Bearer {}'.format(token),
 'Content-Type': 'application/json'
}
params={'title': WEBEX_ROOM}
res = requests.post(url, headers=headers, json=params)
print(res.json())

session = requests.Session()

header = {
    'Authorization': 'Bearer {}'.format(token)
}

session.headers.update(header)

rooms = session.get(url)

rooms_json = rooms.json()
room_id = None
for i in rooms_json["items"]:
    if i["title"] == WEBEX_ROOM:
        room_id = i["id"]


person_email = 'wim.leppens@pxl.be'
new_url = 'https://webexapis.com/v1/memberships'
headers01 = {
 'Authorization': 'Bearer {}'.format(token),
 'Content-Type': 'application/json'
}
params01 = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(new_url, headers=headers01, json=params01)
print(res.json())