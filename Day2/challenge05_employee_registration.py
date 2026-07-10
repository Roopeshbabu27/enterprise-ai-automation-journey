#Employee list
employees=list()
num_of_employees=int(input("How many employees do you want to register? "))
i=0
while i<num_of_employees:
    employee_name = input("Enter Employee Name: ")
    employees.append(employee_name)
    i += 1

print("Employee Registration Completed\n")

counter=1
for emp in employees:
    print(f"Employee {counter}: {emp}\n")
    counter +=1

print("Total Employees: " , len(employees))