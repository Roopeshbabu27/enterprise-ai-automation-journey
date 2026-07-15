import requests

def display_profile(data):
    print(
    '''
    GitHub Profile Report
    ---------------------
    '''
    )    
    print("Username: ",data["login"])
    print("Name: ",data["name"])
    print("Followers: ",data["followers"])
    print("Following: ",data["following"])
    print("Public Repositories: ",data["public_repos"])
    print("Profile URL: ", data["html_url"])


username = input("Enter GitHub Username: ")
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    display_profile(data)
else:
    print("GitHub user not found.")
    print(f"Status Code: {response.status_code}")