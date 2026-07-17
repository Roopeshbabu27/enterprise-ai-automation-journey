from google import genai

API_KEY = input("Enter your Gemini API Key: ")
client = genai.Client(api_key=API_KEY)

def get_multiline_input():
    print("Paste Python code (type END to finish):")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    return "\n".join(lines)

code = get_multiline_input()
prompt = f"""
You are a senior Python developer.

Review the following Python code.

Provide:

1. Bugs
2. Improvements
3. Corrected Code
4. Short explanation

Python code:

{code}
"""

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt
)
print(response.text)
choice = input("Would you like to save this review? (Y/N)").strip().upper()
if choice == "Y":
    with open("review.txt","w") as f:
        f.write(response.text)
elif choice == "N":
    print("Review not saved.")
else:
    print("Please enter Y or N.")
