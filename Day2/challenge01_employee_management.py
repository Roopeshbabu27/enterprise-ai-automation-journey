# ---------------------------------------
# Step 1: Create Initial Employee List
# ---------------------------------------
employees = ["Roopesh","Amit","Rahul","Priya"]
# Step 2: Add New Employee
employees.append("Sneha")
employees.insert(0,"CEO")
#Two interns joined
interns = ["Kiran","Divya"]
employees.extend(interns)
#Rahul resigned
employees.remove("Rahul")

print("Removed Employee : ",employees.pop())
print("Total Employees : ",len(employees))
employees.sort()
employees.reverse()
print(employees)
employee_name=input("Enter Employee Name: ")
if employee_name in employees:
    print("Employee found")
else:
    print("Employee Not Found")

counter = 1

for employee in employees:
    print(f"Employee Number {counter}: {employee}")
    counter += 1