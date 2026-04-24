from chatbot import chatbot_response

print("Chatbot started (type 'bye' to exit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Bot:", response)
