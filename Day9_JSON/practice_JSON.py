import json

student = list()
student_id = int(input("Enter Student ID :"))
student_name = input("Enter student name: ")
course = input("Enter course name: ")
completed = input("Course completed? (yes/no): ").strip().lower()
completed = completed == "yes"

try:
    with open("student.json","r") as f:
        student = json.load(f)
        if isinstance(student, dict):
            student = [student]
except FileNotFoundError:
    student = []

new_student = {
        "id":student_id,
        "name":student_name,
        "course":course,
        "completed":completed
    }

student.append(new_student)

with open("student.json",'w') as f:
    json.dump(student,f,indent=4)

print("\nAll Students:")
for s in student:
    print(f"ID: {s["id"]}, name: {s["name"]} , course: {s["course"]}, completed: {s["completed"]}")

'''
#JSON Load 
with open("student.json") as f:
    student = json.load(f)
    for key,value in student.items():
        print(f"{key}: {value}")
'''
with open("student.json","r") as f:
    student = json.load(f)

'''
#JSON Dump 


#x = '{ "name":"Roopesh", "age" : 30,"city": "Bangalore"}'
x = { 
    "name":"Roopesh", 
    "age" : 30,
    "city": "Bangalore"
    }

#y = json.loads(x)
y=json.dumps(x)
print(y)
print(type(y))

movie = {
    "title": "Interstellar",
    "year": 2014,
    "rating": 8.7
}

#with open("movie.json", "w") as f:
#    json.dump(movie,f,indent=4)

with open("movie.json") as f:
    movie = json.load(f)

print(movie)
'''