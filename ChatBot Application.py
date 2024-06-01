import google.generativeai as genai

API_KEY = "AIzaSyBVN4FiHyg_6T1bFoZfV8nte1LmyDxBrGo"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "In this chat, respond as if you're explaining things to a five-year-old child."

def send_message(question):
    if question.strip() == '':
        return "Please ask something."

    response = chat.send_message(instruction + question)
    return response.text

def chat_with_bot():
    try:
        while True:
            question = input("You: ")
            if question.lower() == "exit":
                exit_conversation()
                return
            response = send_message(instruction + question)
            print("Bot:", response)
        
    except Exception as e:
        print("An error occurred:", e)

def exit_conversation():
    chat.history = []
    print("Conversation terminated. Type 'exit' to quit.")

print("Text-Based Chatbot")
print("Type 'exit' to quit the conversation.")

chat_with_bot()
print("Goodbye!")
