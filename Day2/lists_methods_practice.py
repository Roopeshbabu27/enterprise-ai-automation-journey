
employees = ["Roopesh","Amit","Rahul","Priya"]

employees.append("Sneha")
employees.insert(0,"CEO")

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
    print("Employee Not found")