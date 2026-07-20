from  google import genai

with open("prompts.txt","r") as f:
    prompts = f.readlines()

API_KEY = input("Enter your Gemini API Key: ")
client = genai.Client(api_key=API_KEY)

def ask_ai(prompt):
    if "FAIL" in prompt:
        raise Exception("Simulated AI API Failure")
    else:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )
        return response.text

errorfound = False
q_no = 1
if q_no <= 1:
    with open("results.txt","w") as results , \
         open("errors.txt","w") as errors:
        for q_no, prompt in enumerate(prompts, start=1):
            prompt = prompt.strip()
            print(f"Processing Question {q_no}")  

            try:
                answer = ask_ai(prompt)
                results.write(f"{q_no}: {prompt}\n{answer}\n")
                print("✓ Completed")      
            except Exception as e:
                # Log the error separately
                errors.write(f"{q_no}: {prompt}\nError: {e}\n")
                print(f"✗ Error on Question {q_no}: {e}")
                errorfound = True

        print("Done!")
        print("Results saved to results.txt")
        if errorfound:
            print("Errors saved to errors.txt")