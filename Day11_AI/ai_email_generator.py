from google import genai

API_KEY = input("Enter your Gemini API Key: ")
client = genai.Client(api_key=API_KEY)
print(
'''
====================
AI Email Generator
====================
'''
)
reason = input("Enter a reason for leave: ")
no_of_days = int(input("Enter no of days leave needed: "))
# Multi-line prompt with better engineering + format control

prompt = f"""
You are a professional email writer.

Write a formal leave request email.

Reason: {reason}
Duration: {no_of_days} days

Output:
- Subject
- Greeting
- Body
- Closing
"""
response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt
)
print("Generated Email:\n")
print(response.text)