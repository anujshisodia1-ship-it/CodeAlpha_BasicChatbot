def chatbot():

    print("🤖 Chatbot: Hello! I am a simple chatbot.")
    print("🤖 Chatbot: Type 'bye' to end the chat.")

    while True:

        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! 👋")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! 😊")

        elif user == "bye":
            print("Bot: Goodbye! 👋")
            break

        else:
            print("Bot: Sorry, I don't understand that. 😅")


chatbot()