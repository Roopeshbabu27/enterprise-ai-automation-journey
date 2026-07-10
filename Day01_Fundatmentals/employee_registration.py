continue_registration = True
counter = 0
while counter < 4:
    employee_name = input("Enter Employee Name: ")
    employee_age = input("Enter Employee Age: ")
    employee_department = input("Enter Department: ")
    employee_salary = input("Enter your salary: ")

    print('''
    ================================

    Employee Registered Successfully

    ================================

    '''
    )
    counter += 1;

    print("Name : ", employee_name)
    print("Age : ", employee_age)
    print("Department : ", employee_department)
    print("Salary : ", employee_salary)

    '''choice = input('Do you want to register another employee? Y/N').upper()
    if choice == "N":
        continue_registration = False
        break
    '''

print('''
====================================
Registration Completed Successfully
====================================

    '''
)
print("Total Employees Registered: ", counter)
print("Thank you!")