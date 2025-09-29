import os
from dotenv import load_dotenv
from groq import Groq
import pyttsx3

# --- Load API key ---
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API key not found. Did you set GROQ_API_KEY?")

# --- Initialize Groq client ---
client = Groq(api_key=api_key)

# --- Speak Function (reinitialize each time) ---
def speak(text):
    engine = pyttsx3.init(driverName='sapi5')   # fresh engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()   # release resources properly

# --- Story Generator ---
def generate_story(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a creative storyteller for kids. Keep the story short and engaging."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# --- Main Chat Loop ---
print("🤖 Storytelling Chatbot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye 👋")
        break

    story = generate_story(user_input)
    print("Bot:", story)

    # Speak along with text
    speak(story)
