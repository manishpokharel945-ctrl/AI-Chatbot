# Simple AI Chatbot Project
# Created by Manish Pokharel

print("===================================")
print("        Simple AI Chatbot")
print("===================================")
print("Hello! I am your chatbot.")
print("You can ask me simple questions.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "what is your name":
        print("Bot: My name is Simple AI Chatbot.")

    elif user_input == "what is python":
        print("Bot: Python is a popular programming language used for web development, AI, data science, and automation.")

    elif "ai" in user_input:
        print("Bot: AI means Artificial Intelligence. It allows machines to think and learn like humans.")

    elif "llm" in user_input:
        print("Bot: LLM stands for Large Language Model. It is an AI model trained on large amounts of text data.")

    elif "github" in user_input:
        print("Bot: GitHub is a platform where developers store and share their code.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please ask another question.")