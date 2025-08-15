# chatbot.py
Task 8: Build a Chatbot using if-else

Objective:
Create a simple rule-based chatbot in Python that uses if-else statements to respond to user inputs.

Tools:
Python (no external libraries required)

Steps:
1. Create a new Python file (e.g., chatbot.py).
2. Use a while True loop to repeatedly get input from the user.
3. Convert user input to lowercase for easy comparison.
4. Use if-elif-else statements to match keywords or phrases.
5. Print responses based on matched conditions.
6. Exit the loop if the user types "bye".# Task 8: Build a Chatbot using if-else

## Objective
Create a simple rule-based chatbot in Python that uses if-else statements to respond to user inputs.

## Tools
- Python (no external libraries required)

## Steps
1. Create a new Python file (e.g., `chatbot.py`).
2. Use a `while True` loop to repeatedly get input from the user.
3. Convert user input to lowercase for easy comparison.
4. Use `if-elif-else` statements to match keywords or phrases.
5. Print responses based on matched conditions.
6. Exit the loop if the user types `"bye"`.

## Example Code
```python
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


Example Code:
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

Expected Outcome:
A working console chatbot that replies according to predefined rules, helping you learn basic conditional logic and text handling in Python.
