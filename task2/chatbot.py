def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you?"
    elif "company" in user_input:
        return "Tell me the company name, I will analyze it."
    elif "tesla" in user_input:
        return "Tesla is growing fast. Good investment option."
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand. Please ask something else."
