def chatbot():
    print("Welcome to SimpleChatBot!")
    print("Type something (type 'bye' to exit):")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "what's your name":
            print("Bot: I'm ChatBot 1.0.")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
