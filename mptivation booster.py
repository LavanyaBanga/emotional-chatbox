'''/import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Simple rule-based responses
def get_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm doing well, thanks!", "I'm great, how about you?", "Pretty good, thanks!"],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "sad": ["I'm sorry to hear that. Here's a motivational message: You're stronger than you think!",
                "Cheer up! Tough times don't last, but tough people do!",
                "Remember, every cloud has a silver lining."],
        "happy": ["That's wonderful! Let's celebrate! 🎉", "Great to hear! Keep spreading the joy!", "Awesome! Keep smiling! 😊"]
    }
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I didn't understand that."

def on_submit():
    user_input = entry.get()
    if user_input.strip():  # Ensure the user input is not empty
        try:
            response = get_response(user_input)
            chat_log.insert(tk.END, "You: " + user_input + "\n")
            chat_log.insert(tk.END, "Bot: " + response + "\n")
            chat_log.see(tk.END)
            speak(response)
            entry.delete(0, tk.END)
        except Exception as e:
            chat_log.insert(tk.END, "Error: " + str(e) + "\n")
            chat_log.see(tk.END)

# Create the main application window
app = tk.Tk()
app.title("Simple Chatbot")

# Create and place the chat log
chat_log = scrolledtext.ScrolledText(app, wrap=tk.WORD, state='normal', width=50, height=20)
chat_log.pack(pady=10)

# Create and place the user input entry box
entry = tk.Entry(app, width=50)
entry.pack(pady=10)

# Bind the Enter key to the on_submit function
entry.bind("<Return>", lambda event: on_submit())

# Create and place the submit button
submit_button = tk.Button(app, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Run the main application loop
app.mainloop()
import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import random
import os

# Initialize the text-to-speech engine with a female voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change to a female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Simple rule-based responses
def get_response(user_input):
    # Define some simple rules to generate responses
    if "hello" in user_input.lower():
        return "Hi there!"
    elif "how are you" in user_input.lower():
        return "I'm doing well, thank you for asking!"
    elif "bye" in user_input.lower():
        return "Goodbye! Take care!"
    elif "sad" in user_input.lower():
        # Play a motivational sound
        speak("Cheer up! You're stronger than you think.")
        return "Cheer up! You're stronger than you think."
    elif "happy" in user_input.lower():
        # Play a celebration sound
        os.system("aplay yeah_sound.wav")  # Play "yeah" sound
        speak("Yay! It's great to hear you're happy!")  # Speak the message
        return "Yay! It's great to hear you're happy!"
    else:
        # If no rule matches, generate a generic response
        responses = [
            "I'm not sure I understand.",
            "Could you please elaborate?",
            "That's interesting!",
            "Tell me more."
        ]
        return random.choice(responses)

def on_submit():
    user_input = entry.get()
    if user_input.strip():  # Ensure the user input is not empty
        try:
            response = get_response(user_input)
            chat_log.insert(tk.END, "You: " + user_input + "\n")
            chat_log.insert(tk.END, "Bot: " + response + "\n")
            chat_log.see(tk.END)
            entry.delete(0, tk.END)
        except Exception as e:
            chat_log.insert(tk.END, "Error: " + str(e) + "\n")
            chat_log.see(tk.END)

# Create the main application window
app = tk.Tk()
app.title("Emotional Chatbot")

# Create and place the chat log
chat_log = scrolledtext.ScrolledText(app, wrap=tk.WORD, state='normal', width=50, height=20)
chat_log.pack(pady=10)

# Create and place the user input entry box
entry = tk.Entry(app, width=50)
entry.pack(pady=10)

# Bind the Enter key to the on_submit function
entry.bind("<Return>", lambda event: on_submit())

# Create and place the submit button
submit_button = tk.Button(app, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Run the main application loop
app.mainloop()'''
import tkinter as tk
from tkinter import scrolledtext, messagebox
import pyttsx3
import random
import os

# Initialize the text-to-speech engine with a female voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change to a female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Simple rule-based responses
def get_response(user_input):
    # Define some simple rules to generate responses
    if "hello" in user_input.lower():
        return "Hi there!"
    elif "how are you" in user_input.lower():
        return "I'm doing well, thank you for asking!"
    elif "bye" in user_input.lower():
        return "Goodbye! Take care!"
    elif "sad" in user_input.lower():
        # Play a motivational sound
        speak("Cheer up! You're stronger than you think.")
        return "Cheer up! You're stronger than you think."
    elif "happy" in user_input.lower():
        # Play a celebration sound
        os.system("aplay yeah_sound.wav")  # Play "yeah" sound
        speak("Yay! It's great to hear you're happy!")  # Speak the message
        return "Yay! It's great to hear you're happy!"
    else:
        # If no rule matches, generate a generic response
        responses = [
            "I'm not sure I understand.",
            "Could you please elaborate?",
            "That's interesting!",
            "Tell me more."
        ]
        return random.choice(responses)

def on_submit():
    user_input = entry.get()
    if user_input.strip():  # Ensure the user input is not empty
        try:
            response = get_response(user_input)
            chat_log.insert(tk.END, "You: " + user_input + "\n")
            chat_log.insert(tk.END, "Bot: " + response + "\n")
            chat_log.see(tk.END)
            entry.delete(0, tk.END)
        except Exception as e:
            chat_log.insert(tk.END, "Error: " + str(e) + "\n")
            chat_log.see(tk.END)

# Create the main application window
app = tk.Tk()
app.title("Emotional Chatbot")

# Speak a greeting message when the application starts
speak("Please enter your password:")

# Create and place the password entry box
password_entry = tk.Entry(app, width=50, show="*")
password_entry.pack(pady=10)

def validate_password():
    password = password_entry.get()
    if password == "lavanya":  # Set the password to "lavanya"
        speak("How can I help you?")
        messagebox.showinfo("Welcome", "Welcome! How can I help you?")
    else:
        speak("Invalid password. Please try again.")

# Create and place the submit password button
submit_password_button = tk.Button(app, text="Submit Password", command=validate_password)
submit_password_button.pack(pady=10)

# Create and place the user input entry box
entry = tk.Entry(app, width=50)
entry.pack(pady=10)

# Create and place the chat log
chat_log = scrolledtext.ScrolledText(app, wrap=tk.WORD, state='normal', width=50, height=20)
chat_log.pack(pady=10)

# Bind the Enter key to the on_submit function
entry.bind("<Return>", lambda event: on_submit())

# Create and place the submit button
submit_button = tk.Button(app, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Run the main application loop
app.mainloop()
