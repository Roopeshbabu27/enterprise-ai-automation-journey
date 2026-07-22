import csv
from google import genai
from prompt_template import *
import json

with open("employees.csv") as f:
    employees = list(csv.DictReader(f))

API_KEY = input("Enter your Gemini API Key: ")
client = genai.Client(api_key=API_KEY)

def review_ai(prompt):
    prompt = json.dumps(prompt)
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )
    return response.text

def export_ai():
    with open("employee_ai_report.txt","a") as txt_file:
        for emp in employees:
            txt_file.write(review_ai(emp))

print(
'''
=================================
AI Employee Management Assistant
=================================
1. Employee Dashboard
2. Filter Employees
3. AI Performance Summary
4. Export Report
5. Exit
'''
)

def emp_dash():
    total_emps = len(employees)
    total_sal = sum(int(row['Salary']) for row in employees)
    avg_sal = total_sal / len(employees)
    highest_paid = max(int(row['Salary']) for row in employees)
    lowest_paid = min(int(row['Salary']) for row in employees)

    with open("employee_dashboard.txt","w") as txt_file:
        txt_file.write(
    f'''
    =========================
    Employee Dashboard
    =========================
    Total Employees : {total_emps}
    Total Salary    : {total_sal}
    Average Salary  : {avg_sal:.2f}   
    Highest Paid    : {highest_paid}
    Lowest Paid     : {lowest_paid}

    '''
        )

        departments = ["IT","Finance","HR"]
        txt_file.write("\nDepartment Summary\n")
        for dept in departments:
            dept_emp = [row for row in employees if row["Department"] == dept]
            txt_file.write(f"{dept} : {len(dept_emp)} Employees\n")

def filter_emp(dept):
    dept_filter = [row for row in employees if row["Department"] == dept]
    if dept_filter:
        return dept_filter
    else:
        return []

def min_sal(sal):
    new_list = []
    for emp in employees:
        if int(emp["Salary"]) >= sal:
            new_list.append(emp)

    if new_list:
        return new_list
    else:
        return []

def dept_sal(dept,sal):
    new_list = []
    for emp in employees:
        if int(emp["Salary"]) >= sal and emp["Department"] == dept:
            new_list.append(emp)

    if new_list:
        return new_list
    else:
        return []

def write_res(emp, write_header=False):
    with open("filtered_employees.csv","w",newline="") as f:
        fieldnames = ["ID","Name","Department","Salary","Performance"]
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerows(emp)



while True:
    try:
        choice = int(input("\nEnter a choice: "))
    except ValueError:
            print("Enter only number")
            continue
    
    if 1<=choice<=5:
        if choice == 1:
            emp_dash()                
        elif choice ==2:
            print("\n1.Department \n2.Minimum Salary\n 3. Dept + Salary")
            user_input = int(input("Select the option to filter"))
            if user_input == 1:
                dept_name = input("Enter dept to search: ")
                print(filter_emp(dept_name))
                write_res(filter_emp(dept_name))
            elif user_input == 2:
                mini_sal = int(input("Enter minimum salary: "))
                print(min_sal(mini_sal))
                write_res(min_sal(mini_sal))
            elif user_input == 3:
                dept_name = input("Enter dept to search: ")
                mini_sal = int(input("Enter minimum salary: "))
                print(dept_sal(dept_name,mini_sal))
                write_res(dept_sal(dept_name,mini_sal))              

        elif choice == 3:
            emp_id = int(input("Enter emp id: ")) 
            prompt = SUMMARY_TEMPLATE.format(text=emp_id)
            print(review_ai(prompt))
            
        elif choice == 4:
            user_choice = input("Generate AI report for all employees? (Y/N): ")
            if user_choice == "Y":
                export_ai()

        elif choice == 5:
            break

    