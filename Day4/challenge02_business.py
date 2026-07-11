
#Challenge 1 – Register Employee
def register_employee():
    employee_id = input("\nEnter Employee ID : ")
    employee_name = input("\nEnter Employee Name : ")
    employee_dept = input("\nEnter Employee Dept : ")
    employee_salary = int(input("\nEnter Employee Salary : "))
    employee = {
            "id": employee_id,
            "name": employee_name,
            "department": employee_dept,
            "salary": employee_salary
        }    
    return employee
employee = register_employee()
print(employee)


#Challenge 2 – Display Employee
def display_employee(employee):
    for key,value in employee.items():
        print(f"\n{key}: {value}")

print(
'''\n
==============================
Employee Details
==============================
'''
)
display_employee(employee)
print(
'''\n
==============================
'''
)

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

def search_employee(employees, name):
    for x in range(len(employees)):
        if name == employees[x]["name"]:
            print(name , employees[x]["name"])
            return display_employee(employees[x])


res = search_employee(employees, "Priya")
print(res)