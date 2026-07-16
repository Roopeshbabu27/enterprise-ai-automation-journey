import requests

url = "https://randomuser.me/api/"

response = requests.get(url)

data = response.json()

print(
'''
Random User Report
------------------
'''
)
print("Title: ", data["results"][0]["name"]["title"])
print("First Name: ", data["results"][0]["name"]["first"] )
print("Last Name: ", data["results"][0]["name"]["last"])
print("Email: ", data["results"][0]["email"] )
print("Phone: ", data["results"][0]["phone"] )
print("Country: ", data["results"][0]["location"]["country"])
'''



print(data)
'''