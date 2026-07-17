from google import genai

API_KEY = input("Enter your Gemini API Key: ")
client = genai.Client(api_key=API_KEY)
print(
'''
====================
AI Assistant
====================
'''
)
while True:

    prompt = input("Ask AI: ")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print(response.text)
    more_prompt = input("Ask another question? (Y/N)").upper()
    if more_prompt == "Y":
        continue
    elif more_prompt == "N":
        break
    else:
        print("Please enter Y or N.")


'''
for model in client.models.list():
    print(model.name)
'''