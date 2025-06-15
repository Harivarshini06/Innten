def chatbot():
    print("Hi! I'm ChatBot. Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("ChatBot: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hello! How can I help you today?")
        elif "how are you" in user_input:
            print("ChatBot: I'm just a program, but I'm doing great!")
        elif "your name" in user_input:
            print("ChatBot: I'm a simple chatbot built with Python.")
        elif "bye" in user_input:
            print("ChatBot: See you later!")
            break
        else:
            print("ChatBot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()
