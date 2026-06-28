"""
Project : Rule-Based Chatbot
Author  : Your Name
Language: Python 3

Description:
A simple rule-based chatbot that responds to user queries using
predefined rules and pattern matching.
"""

import datetime
import random


JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It left its Windows open!",
    "Why did the Python developer wear glasses? Because they couldn't C!"
]

QUOTES = [
    "Success is the sum of small efforts repeated every day.",
    "Believe in yourself and never stop learning.",
    "Hard work beats talent when talent doesn't work hard.",
    "Every expert was once a beginner."
]

GENERAL_KNOWLEDGE = {
    "capital of india": "The capital of India is New Delhi.",
    "largest planet": "Jupiter is the largest planet in our Solar System.",
    "father of computer": "Charles Babbage is known as the Father of the Computer.",
    "python": "Python is a high-level, interpreted programming language."
}


def greet():
    """Display chatbot introduction."""
    print("=" * 60)
    print("         WELCOME TO RULE-BASED CHATBOT")
    print("=" * 60)
    print("Hello! I am RuleBot.")
    print("Type 'help' to view available commands.")
    print("Type 'exit', 'quit', or 'bye' to end the chat.\n")


def show_help():
    """Display chatbot capabilities."""
    print("\nI can help you with:")
    print("- Greetings")
    print("- Date and Time")
    print("- Basic Calculations")
    print("- Motivational Quotes")
    print("- Programming Jokes")
    print("- General Knowledge")
    print("- Basic Conversation\n")


def calculate(expression):
    """Evaluate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Invalid mathematical expression."


def get_response(user):
    """Generate chatbot response."""

    if user in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"

    elif "how are you" in user:
        return "I'm doing great. Thanks for asking!"

    elif "your name" in user:
        return "My name is RuleBot."

    elif "who created you" in user:
        return "I was created using Python as a Rule-Based Chatbot project."

    elif "date" in user:
        today = datetime.date.today()
        return f"Today's date is {today}."

    elif "time" in user:
        now = datetime.datetime.now().strftime("%I:%M:%S %p")
        return f"Current time is {now}."

    elif user.startswith("calculate"):
        expression = user.replace("calculate", "").strip()
        return calculate(expression)

    elif "quote" in user or "motivate" in user:
        return random.choice(QUOTES)

    elif "joke" in user:
        return random.choice(JOKES)

    elif "thank" in user:
        return "You're welcome! Happy to help."

    elif "help" in user:
        show_help()
        return ""

    else:
        for key in GENERAL_KNOWLEDGE:
            if key in user:
                return GENERAL_KNOWLEDGE[key]

    return "Sorry, I didn't understand that. Please try another question."


def chatbot():
    """Main chatbot loop."""
    greet()

    while True:
        user = input("You: ").lower().strip()

        if user in ["bye", "exit", "quit"]:
            print("Bot: Thank you for chatting with me. Have a wonderful day!")
            break

        response = get_response(user)

        if response:
            print("Bot:", response)


if __name__ == "__main__":
    chatbot()