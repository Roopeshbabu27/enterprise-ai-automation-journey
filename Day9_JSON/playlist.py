import json

def load_songs():
    try:
        with open("songs.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
#Add songs
def add_song(songs,new_song):
    if new_song:
        songs.append(new_song)

    with open("songs.json","w") as f:
        json.dump(songs,f,indent=4)

#View songs
def view_songs():
    try:
        songs = load_songs()
        if isinstance(songs, dict):
            songs = [songs]
        for s in songs:
            print(f"title: {s["title"]}, artist: {s["artist"]}")
        
    except FileNotFoundError:
        print("File not found")

def search_song(song_search):
    songs = load_songs()
    for s in songs:
        found = song_search == s["title"]
        if found:
            return found     

    return None       

def main():     
    while True:
        print(   
            '''
            ======== Playlist Manager ========
            1. View Playlist
            2. Add Playlist
            3. Search Playlist
            4. Exit
            '''
            )
        try:
            #songs = list()
            choice = int(input("Enter a choice 1/2/3/4: "))
            if 1 <= choice <= 4:
                if choice == 1:
                    view_songs()
                elif choice == 2:
                    songs = load_songs()
                    title = input("Enter the song title: ")
                    artist = input("Enter the song artist: ")
                    new_song = {
                        "title": title,
                        "artist" : artist
                    }
                    add_song(songs,new_song)
                elif choice == 3:
                    song_search = input("Enter the song: ")
                    res = search_song(song_search)
                    if res:
                        print(f"{song_search} FOUND")
                    else:
                        print(f"{song_search} NOT FOUND")
                elif choice == 4:
                    break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Enter a valid number")    

main()
