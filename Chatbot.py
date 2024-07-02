def chatbot_response(user_input):
    # Convert the user input to lowercase to make the matching case-insensitive
    user_input = user_input.lower()

    # Predefined responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm a chatbot created to assist you. You can call me Chatter."
    elif "help" in user_input:
        return "Sure, I'm here to help. What do you need assistance with?"
    elif "What is your job?" in user_input:
        return "My job is to help in your quires and give you solution on your problem."
    elif "What to do after diploma?" in user_input:
        return "You can do any Bachelor degree according to your preference."
    elif "Which Language can you speak?" in user_input:
        return "I can speak in many languages but i preferes English mostly."
    elif "Name 3 things you really want to recommend to me.." in user_input:
        return "Do Exercise Daily, Read Books and Priorities.."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Chatbot: Hello! Type 'bye' or 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    main()
