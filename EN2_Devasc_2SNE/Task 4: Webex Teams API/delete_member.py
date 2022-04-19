import requests
access_token = 'M2NkMGI4MmEtN2Y4OC00ODI4LTk0MTQtYmM2NGY3YzI5MThjZjIzMzJhZjMtYjBi_PE93_9423ebf1-df21-4e89-8049-a08f8e9c5998'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNDMxZWFiNTAtYTQzOC0xMWVjLWJmMDktMTdiYWVkYmVmMGY2'
membership_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL01FTUJFUlNISVAvZDhhOTI5MzUtNDA2Zi00YmRmLWEzMmItNzZjMzdiMDczN2RmOjQzMWVhYjUwLWE0MzgtMTFlYy1iZjA5LTE3YmFlZGJlZjBmNg'
url = 'https://webexapis.com/v1/memberships/'+membership_id
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
res = requests.delete(url, headers=headers)
print(res.json())
