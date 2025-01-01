from datetime import datetime

def chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif 'hey' in user_input:
            print("Hi ! How Are You ? How Can I Help You ?")

        elif user_input == 'help':
            print("Chatbot: You can ask me about the weather, time, or exit the conversation. Type 'exit' to leave.")

        elif 'weather' in user_input:
            print("Chatbot: The weather is sunny today!")
        
        elif 'time' in user_input:
            current_time = datetime.now().strftime("%H:%M")
            print(f"Chatbot: The current time is {current_time}.")
        
        elif not user_input or len(user_input) < 2:
            print("Chatbot: Please type something more specific.")

        elif 'joke' in user_input:
            print("Chatbot:Why did the scarecrow win an award? Because he was outstanding in his field! 😄")
          
        else:
            print("Chatbot: Sorry, I don't understand that. Type 'help' to see what I can do.")
        
chatbot()
