from  google import genai

with open("prompts.txt","r") as f:
    prompts = f.readlines()

API_KEY = input("Enter your Gemini API Key: ")
client = genai.Client(api_key=API_KEY)

def ask_ai(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )
    return response.text

q_no = 1
if q_no <= 1:
    with open("results.txt","w") as f:        
        for q_no, question in enumerate(prompts, start=1):
            question = question.strip()
            print(f"Processing Question {q_no}")        
            f.write(f"{q_no}:{question}\n{ask_ai(question)}")

            print("✓ Completed")
            q_no += 1
        print("Done!")
        print("Results saved to results.txt")
    

        

