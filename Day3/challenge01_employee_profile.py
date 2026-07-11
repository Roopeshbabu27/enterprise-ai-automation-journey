#Challenge1 Employee Profile
#Define Dictionary
employee = {
    "Name":"Roopesh",
    "Department":"BPM",
    "Salary":80000,
    "Location":"Bangalore"
}
#Update salary
employee["Salary"] = 90000

#Add email item
employee["Email"] = "roopesh@gmail.com"

#Remove location key
employee.pop("Location")

print(employee)