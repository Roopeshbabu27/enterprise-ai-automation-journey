#initial employees list
Employees = ["Roopesh","Amit","Rahul"]
print("Intial Employees List: \n")
for emp in Employees:
    print(emp)

#Adding new employees
newEmployees=["Priya","Sneha"]
#Combining lists
Employees.extend(newEmployees)
print("\nAdding New Employees...")
print("\nUpdated Employees List: ")
for emp in Employees:
    print(emp)

#Removing employee
Employees.remove("Rahul")
print("\nRemoving Employees...")
#Final Employee Lists
print("\nFinal Employees List: ")
for emp in Employees:
    print(emp)

print("\nTotal Number of employees : ", len(Employees))

