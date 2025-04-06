import requests
import json


result = requests.get("https://dog.ceo/api/breed/hound/images")
result = result.json()['message']
total = 0
for elem in result:
    if 'hound-english' in elem:
        total +=1

print(total)
