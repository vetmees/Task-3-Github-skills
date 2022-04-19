#!/usr/bin/env python3

## inporteer librarys die nodig zijn voor het gebruik van het script
import requests
import json

## definieer variabelen
APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

# het genereren van een authentication token
def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")
# het verwijderen van een boek uit de school bibliotheek
def removeBook(book,apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{ID}", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book {book} deleted.")
        #print(apiKey)
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to remove book {book}.") 

apiKey = getAuthToken()     

for i in range(4, 5):
    ID=i
    book = {"id":i}
    removeBook(book, apiKey)