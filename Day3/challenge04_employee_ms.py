#challenge4 employee management system
employees = [
    {
        "id": 101,
        "name": "Roopesh",
        "department": "BPM",
        "salary": 90000
    },
    {
        "id": 102,
        "name": "Amit",
        "department": "HR",
        "salary": 70000
    },
    {
        "id": 103,
        "name": "Priya",
        "department": "Finance",
        "salary": 80000
    }
]

print("\n====================================\n")

for x in employees:
    for key,values in x.items():      
      print(f"{key}: {values}")
    print("\n====================================\n")

#Add new employee
employees.append({
   "id": 104,
        "name": "Sneha",
        "department": "IT",
        "salary": 85000
})

#Search an employee
found=False
search_item=input("Enter employee name: ")
for x in range(len(employees)):
    if search_item == employees[x]["name"]:
        print("Employee Found")
        found=True
        item = employees[x]
        for key,value in item.items():
           print(f"{key}: {value}")

if found == False:
    print("Not found")

#Update salary
employee_name = input("Enter employee name: ")
for x in range(len(employees)):
    if employee_name == employees[x]["name"]:
        new_salary=input("Enter new value: ")
        employees[x]["salary"] = new_salary
        item = employees[x]
        for key,value in item.items():
           print(f"{key}: {value}")  

#Highest paid Employee
highest_salary = employees[0]

for emp in employees[1:]:
    if int(emp["salary"]) > int(highest_salary["salary"]):
        highest_salary = emp

print("Highest Salary Employee" , highest_salary)

#Register new employee
employee_id = input("\nEnter Employee ID : ")
employee_name = input("\nEnter Employee Name : ")
employee_dept = input("\nEnter Employee Dept : ")
employee_salary = input("\nEnter Employee Salary : ")

employees.append(
    {
        "id": employee_id,
        "name": employee_name,
        "department": employee_dept,
        "salary": employee_salary
    }
)

for employee in employees:
    print("----------------")

    for key, value in employee.items():
        print(f"{key}: {value}")
