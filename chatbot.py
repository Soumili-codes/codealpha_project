# Basic Rule-based Chatbot
def chatbot():
    while True:
        user = input("You: ").lower().strip()
        if user == "bye":
            print("Chatbot: Goodbye!")
            break
        # Check user input and respond accordingly
        if user == "hello":
            print("Chatbot: Hi there!")
        elif user == "how are you?":
            print("Chatbot: I' m just a bot, but I'm doing great! How about you?")
        elif user == "what is your name?":
            print("Chatbot: I'm a simple chatbot created to assist you")
        elif user == "what can you do?":
            print("Chatbot: I can chat with you and answer simple questions")
        elif user == "thank you":
            print("Chatbot: You're welcome!")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")


# start the chatbot
chatbot()



