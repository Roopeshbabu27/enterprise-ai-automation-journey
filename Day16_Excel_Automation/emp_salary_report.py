import json

employees = [
    {"id":101, "name":"John", "department":"IT", "salary":65000},
    {"id":102, "name":"Alice", "department":"HR", "salary":45000},
    {"id":103, "name":"Bob", "department":"Finance", "salary":70000},
    {"id":104, "name":"David", "department":"IT", "salary":80000},
    {"id":105, "name":"Emma", "department":"HR", "salary":52000}
]

for emp in employees:
    print(f"{emp['id']} {emp['name']} {emp['department']} {emp['salary']}")

print(f"Total employees: {len(employees)}")
total_sal = sum(emp["salary"] for emp in employees)
print(f"Total salary: {total_sal}")
avg_sal = total_sal/len(employees)
print(f"Average salary: {avg_sal:.2f}")

highest_paid_emp = max(employees, key=lambda x:x['salary'])
print(f"Highest Paid Employee: {highest_paid_emp['name']} {highest_paid_emp['salary']}")

emp_over_60k = [emp for emp in employees if emp['salary']>60000]
print(emp_over_60k)

for emp in employees:
    new_sal = emp["salary"] + (emp["salary"] * 10 / 100)
    emp["salary"] = new_sal

with open("employee_report.json","w") as file:
    json.dump(employees,file,indent=4)

def search_employee(emp_id):
    for emp in employees:
        if emp['id'] == emp_id:
            return emp

    return None
user_input = int(input("Enter emp id: "))
search_emp = search_employee(user_input)
if search_emp:
    print("Employee found")
    print(f"Name: {search_emp['name']} \n Department: {search_emp['department']} \n Salary: {search_emp['salary']}")
else:
    print("Employee not found")