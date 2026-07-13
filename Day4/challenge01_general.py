#check if number is even
'''
def is_even(num):
    return num % 2 == 0
    
number = int(input("Enter a number: "))
result = is_even(number)
if result == True:
    print(f"{number} is a Even Number")
else:
    print(f"{number} is a Odd Number")

#reverse_string(text)
def reverse_string(text):
    reversed_string = ""
    for i in text[::-1]:
        reversed_string += i
    return reversed_string

def is_palindrome(text):
    text = text.lower()
    return text == reverse_string(text)
       
text = input("Enter a String: " )
print(reverse_string(text))
print(is_palindrome(text))
'''
#Challenge 3 find max number
'''
def find_max(numbers):  
    max_num = numbers[0]  
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [12, 45, 78, 123, 99, 56]
print(find_max(numbers))
'''

'''
def view_movies():
    for i in movies:
        print("\n")
        for key,value in i.items():
            print(f"{key}: {value}")

#view_movies()

movie_title = input("Enter a movie: ")
genre = input("Enter a genre: ")
rating = int(input("Enter a rating: "))

movies.append({
     "title": movie_title,
     "genre": genre,
     "rating": rating
})

view_movies()

movie_name = input("Enter a movie: ")
def search_movie(movie_name):
    for i in range(len(movies)):
        item = movies[i]
        if movie_name == item["title"]:
            for key,value in item.items():
                print(f"{key} : {value}")
        #print(item)

    return "Not Found"

search_movie(movie_name)

def update_rating(movie,rating):
    for i in range(len(movies)):
        if movies[i]["title"] == movie:
            new_rating=input("Enter new rating: ")
            movies[i]["rating"] = new_rating
            item = movies[i]
            for key,value in item.items():
                print(f"{key}: {value}")
    
update_movie = update_rating("Avatar",11)
print(update_movie)

movie_n = input("Enter a movie to delete: ")

def del_movie(movie_n):
    for i in range(len(movies)):
        if movie_n == movies[i]["title"]:
            del movies[i]
            return

del_movie(movie_n)
print("-----Remaining Employees--------")
print(movies)

movies = [
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "rating": 9
    },
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "rating": 11
    },
    {
        "title": "Avatar",
        "genre": "Fantasy",
        "rating": 10
    }
]

def highest_num():
    max_num = int(movies[0]["rating"])
    print("First time : ", max_num)
    for i in range(len(movies)):
        if int(movies[i]["rating"]) > max_num:
            max_num = movies[i]["rating"]
    return max_num

print(highest_num())
'''    

students = [
    {"name": "Alice", "scores": [80, 90, 85]},
    {"name": "Bob", "scores": [60, 70, 65]},
    {"name": "Charlie", "scores": [95, 92, 98]}
]

for i in range(len(students)):
    avg_score = float(sum(students[i]["scores"])) / len(students[i]["scores"])
    students[i]["Average"] = avg_score
    if avg_score >=70:
        students[i]["Result"] = "PASS" 
    else:
        students[i]["Result"] = "FAIL"
    for key,value in students[i].items():        
        print(f"{key} : {value}")

top_performer = float(students[0]["Average"])
print("Before for loop: ",top_performer)
for i in students[1:]:    
    print("I" , i)
    if float(i["Average"]) > top_performer:
        top_performer = i["Average"]
        print("Inside loop: ",top_performer)


print("At last: ",top_performer)