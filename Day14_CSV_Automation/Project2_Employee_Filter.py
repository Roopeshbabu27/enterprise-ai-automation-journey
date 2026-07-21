import csv

with open("employees.csv") as f:
    employees = list(csv.DictReader(f))

print(
'''
=========================
Employee Filter Tool
=========================
1. Filter by Department
2. Filter by Minimum Salary
3. Filter by Both
4. Exit
'''
)

departments = ["IT","HR","Finance","Sales"]
def filter_dept(dept_name):
    new_list =[]  
    for emp in employees:
        if emp['Department'] == dept_name:
            new_list.append(emp)
        
    return new_list

def minimum_salary(min_salary):  
    new_list =[]  
    for emp in employees:
        if int(emp['Salary']) >= min_salary:
            new_list.append(emp)

    if new_list:
        return new_list
    else:
        return []

def dept_salary(dept,salary):
    new_list =[]
    for emp in employees:
        if int(emp['Salary']) >= salary and emp['Department'] == dept:
            new_list.append(emp)

    if new_list:
        return new_list
    else:
        return []

def write_res(emp, write_header=False):
    with open("filtered_employees.csv", "a", newline="") as f:
        fieldnames = ["ID", "Name", "Department", "Salary"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:          
            writer.writeheader()  # write column headers
        writer.writerows(emp)  # write all rows

while True:
    try:
        choice = int(input("\nEnter a choice: "))
        if 1<=choice<=4:
            if choice == 1:
                dept_name = input("Enter the department: ")
                print(filter_dept(dept_name))
                write_res(filter_dept(dept_name))                
            elif choice ==2:
                min_salary = int(input("Enter the min salary: "))
                print(f"Employees earning at least {min_salary}\n")
                print(minimum_salary(min_salary))
                write_res(minimum_salary(min_salary))     
            elif choice == 3:
                dept_name = input("Enter the department: ")
                min_salary = int(input("Enter the min salary: "))
                print(dept_salary(dept_name,min_salary))
                write_res(dept_salary(dept_name,min_salary))     
            elif choice == 4:
                break
        else:
            print("Enter a valid number")
    except ValueError:
        print("Enter only number")