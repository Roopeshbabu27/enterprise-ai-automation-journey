#Challenge 3 – Employee ID Card

employee = {
    "employee_id": 101,
    "name": "Roopesh",
    "department": "BPM",
    "designation": "Developer",
    "salary": 90000,
    "location": "Bangalore"
}

print(
'''
=================================
      EMPLOYEE ID CARD
=================================
'''
)
for x,y in employee.items():
    print(f"{x} : {y}")

print(
"================================="
)

choice = input("Which field do you want to update.? ")
if choice in employee.keys():
    value = input("Enter a new value: ")
    employee[choice]= value
    print(f"Updated value for {choice} is {value}")
else:
    print("Field not available")


print("\nUpdated Details: ",employee)