#initial employees list
Employees = ["Roopesh","Amit","Rahul","Priya","Sneha","Rahul"]

#User input
choice = input("Enter employee name: ")

try:
    if choice in Employees:
        print("Employee found")
        print("Position: ",Employees.index(choice)+1)

    else:
        print("Employee Not found")
except:
    print("Please Enter a valid input")