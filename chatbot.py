# Simple Rule-Based Chatbot

print("Chatbot: Hello! I am your assistant. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Chatbot: Hi there! How can I help you today?")
    elif "how are you" in user_input:
        print("Chatbot: I'm just a program, but I'm doing great! How about you?")
    elif "your name" in user_input:
        print("Chatbot: I'm ChatBot 1.0, created to assist you!")
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        print("Chatbot: I'm not sure how to respond to that.")
