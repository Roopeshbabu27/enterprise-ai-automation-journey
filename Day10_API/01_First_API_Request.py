import requests

url = "https://api.github.com/users/torvalds"

response = requests.get(url)
print(response)
data = response.json()
'''
print(data["login"])
print(data["name"])
print(data["followers"])
print(data["following"])
print(data["public_repos"])
'''