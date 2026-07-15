import requests

def display_profile(data):
    print("Username: ",data["login"])
    print("Name: ",data["name"])
    print("Followers: ",data["followers"])
    print("Following: ",data["following"])
    print("Public Repositories: ",data["public_repos"])
    print("Profile URL: ", data["html_url"])    

def search_profile(name):
    url = f"https://api.github.com/users/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        display_profile(data)
    else:
        print("Invalid GitHub username")
        print(f"Status Code: {response.status_code}")

def main():
    while True:
        print(
        '''
        =============================
        GitHub Explorer
        =============================

        1. Search Profile
        2. Exit
        '''
        )
        try:
            choice= int(input("Enter ur choice: "))
            if 1 <= choice <=2:                            
                if choice == 1:
                    user_name = input("Enter GitHub Username:")
                    if user_name.strip():                  
                        search_profile(user_name)
                        while True:
                            search_more = input("Search another profile? (Y/N): ").strip().upper()
                            if search_more == "Y":
                                user_name = input("Enter GitHub Username:")
                                search_profile(user_name)
                            else:
                                break
                    else:
                        print("Username cannot be empty.")
                elif choice == 2:
                    break
            else:
                print("Enter a valid choice")
        except ValueError:
            print("Enter a valid number")

main()