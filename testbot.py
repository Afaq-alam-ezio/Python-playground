import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking.']),
    (r'what is your name?', ['You can call me Chatbot.', 'I am Chatbot.']),
    # Add more patterns and responses as needed
]

# Create a Chat object
chatbot = Chat(patterns, reflections)

# Start chatting
print("Welcome to the Chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Bot:", response)

    if user_input.lower() == 'quit':
        break
