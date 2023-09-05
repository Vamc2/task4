import nltk
from nltk.chat.util import Chat, reflections

# Define some simple patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you!', 'I am just a chatbot, but I am doing well!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
]

# Create a Chat object with the defined patterns and responses
chatbot = Chat(patterns, reflections)

# Start the chatbot
print("Chatbot: Hi! I'm your chatbot. You can say 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
