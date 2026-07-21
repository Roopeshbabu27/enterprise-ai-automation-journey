import csv

with open("employees.csv") as f:
    employees = list(csv.DictReader(f))

total_emps = len(employees)
total_sal = sum(int(row['Salary']) for row in employees)
average_sal = total_sal / total_emps

with open("employee_dashboard.txt", "w") as txt_file:
    txt_file.write(
f'''
=========================
Employee Dashboard
=========================
Total Employees : {total_emps}
Total Salary    : {total_sal}
Average Salary  : {average_sal:.2f}
'''
)

    highest_paid_emp = max(employees, key=lambda emp: int(emp['Salary']))
    print(highest_paid_emp['Name'], "-", highest_paid_emp['Department'], "-", highest_paid_emp['Salary'])
    min_paid_emp = min(employees, key=lambda emp: int(emp['Salary']))
    print(min_paid_emp['Name'], "-", min_paid_emp['Department'], "-", min_paid_emp['Salary'])
    txt_file.write(f"\nHighest Paid : {highest_paid_emp['Name']} - {highest_paid_emp['Department']} - {highest_paid_emp['Salary']}")
    txt_file.write(f"\nLowest Paid  : {min_paid_emp['Name']} - {min_paid_emp['Department']} - {min_paid_emp['Salary']}\n")

    txt_file.write("\nDepartment Summary\n")
    departments = ["IT","HR","Finance","Sales"]
    for dept in departments:
        dept_emp =  [row for row in employees if row["Department"] == dept]
        txt_file.write(f"{dept} : {len(dept_emp)} Employees\n")