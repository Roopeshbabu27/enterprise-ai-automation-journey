from prompt_templates import *
from google import genai

API_KEY = input("Enter your Gemini API Key: ")
client = genai.Client(api_key=API_KEY)

print(
'''
=========================
AI Prompt Library
=========================
1. Explain Concept
2. Generate Email
3. Summarize Text
4. Exit
'''
)

def ask_ai(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )
    return response.text

def get_multiline_input():
    print("Paste Python code (type END to finish):")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    return "\n".join(lines)

while True:
    choice = int(input("Enter ur choice: "))
    if 1<= choice <=4:
        if choice == 1:
            user_topic = input("Enter topic: ")
            prompt = EXPLAIN_TEMPLATE.format(topic=user_topic)
            print(ask_ai(prompt))
        elif choice == 2:
            email_topic = input("Enter topic: ")
            prompt = EMAIL_TEMPLATE.format(topic=email_topic)
            print(ask_ai(prompt))
        elif choice ==3 :
            code = get_multiline_input()
            prompt = SUMMARY_TEMPLATE.format(text=code)
            print(ask_ai(prompt))
        elif choice == 4:
            break
    else:
        print("Enter a valid number")