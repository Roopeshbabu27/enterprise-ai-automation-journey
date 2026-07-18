from google import genai
from prompt_templates import *

API_KEY = input("Enter your Gemini API Key: ")
client = genai.Client(api_key=API_KEY)

def ask_ai(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )
    return response.text

with open("employee.txt","r") as f:
    employees = f.readlines()



with open("performance_report.txt","w", encoding="utf-8") as f:
    emp = 1
    for employee in employees:
        employee = employee.strip()
        print(f"Processing employee {emp}.....")
        prompt = GEN_REPORT_TEMPLATE.format(text=employee)
        result = f'''
        ==========================================
        Employee: {employee}
        ==========================================

        AI Performance Summary:
        {ask_ai(prompt)}
        ------------------------------------------
        '''
        f.write(result)
        emp += 1
    print("Done!")
    print("Results saved to performance_report.txt")
    
