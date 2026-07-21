import csv

with open("employees.csv","r") as f:
    employees = list(csv.DictReader(f))
print(
'''
Department Report
-----------------
'''
)

def avg_sal(total_sal,no_of_emp):
    if no_of_emp == 0:
        return 0
    return total_sal / no_of_emp

departments = ["IT","HR","Finance","Sales"]
for dept in departments:
    print(dept)
    dept_emp =  [row for row in employees if row["Department"] == dept]
    emp_count = len(dept_emp)
    print("Employees:", emp_count)
    total_salary = sum(int(row["Salary"]) for row in dept_emp)
    print(f"Total Salary: {total_salary}")
    average_sal = avg_sal(total_salary,emp_count)
    print(f"Average Salary:  {average_sal:.2f}\n")
