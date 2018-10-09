import requests

url = "https://api.imgur.com/3/account/{{username}}"

headers = {'Authorization': 'Client-ID {{soulwawa}}'}

response = requests.request("GET", url, headers=headers)

print(response.text)