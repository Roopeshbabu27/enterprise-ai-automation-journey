#Challenge – Employee Promotion System

employees = [
    {
        "id": 101,
        "name": "Roopesh Babu",
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

def delete_employee(employees, name):
    for i in range(len(employees)):
        if employees[i]["name"] == name:
            del employees[i]
            return   # stop after deleting
    
def generate_email(employee):
    if employee:
        employee["name"] = employee["name"].lower()
        employee["name"] = employee["name"].replace(" ", ".")
        employee["email"] = employee["name"] + "@gmail.com"
        return employee


def promote_employee(employee):
    if employee:
        employee["salary"] =  employee["salary"] * 1.10
        return employee

def display_employee(employee):
    if employee:
        for key,value in employee.items():
            print(f"{key}: {value}")
    else:
        print("Employee Not found")

def search_employee(employees,name):
    for employee in employees:
        if name == employee["name"]:
            return employee
    return None

def main():
    name = input("Enter employee name: ")
    employee = search_employee(employees,name)
    print("-----Before Increase--------")
    display_employee(employee)
    Updated_employee = promote_employee(employee)
    print("-----After Increase--------")
    display_employee(Updated_employee)
    print("-----Added Email Field--------")
   # email = generate_email(employee)
    #display_employee(email)
    delete_employee(employees,name)
    print("-----Remaining Employees--------")
    print(employees)

main()
'''

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

def display_employee(employee):
    for key,value in employee.items():
        print(f"\n{key}: {value}")

def search_employee(employees, name):
    for employee in employees:
        if name == employee["name"]:
            return employee
        
    return None

employee = search_employee(employees,"Amit")
if employee:
    display_employee(employee)
else:
    print("Not found")

'''