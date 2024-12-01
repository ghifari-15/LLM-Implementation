# Import library
import re
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import pyttsx3  # Import pustaka untuk TTS
import speech_recognition as sr
from web_scraper import fetch_web_content  # Import fungsi dari file web_scraper.py
from db_helper import conn_db

# Load all environment variabels
load_dotenv() 

# Model used
model = "gemini-1.5-flash"
llm = ChatGoogleGenerativeAI(model=model)


engine = pyttsx3.init()  # Initialize tts engine
voices = engine.getProperty('voices') # Use female tts voice
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer() # Engine tts initialize

# Convert the text to voice
def speak(text):
    """Fungsi untuk mengubah teks menjadi suara"""
    engine.say(text)
    engine.runAndWait()


# Listen users when input
def listen():
    with sr.Microphone() as source:
        print("Listening... ")
        try:
            audio = recognizer.listen(source, phrase_time_limit=5)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}.")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return""
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout period")
            return("")

def clean_text_for_tts(text):
    return re.sub(r'\*+', '', text).strip()

messages = []


def main():
    print("Choose you want to speak or type?")
    print("1. Speak")
    print("2. Type")
    user_decision = input("Your input: ")
    while True:
        
        if user_decision == '1':
            user_input = listen()
        elif user_decision == '2':
            user_input = input("Please type your question: ")
        else:
            print("Invalid input. Please choose 1 or 2.")
            continue
        
        if user_input.lower() in ("", "exit", "q"):
                break
        
        conn_db.save_data("human", user_input) 


        urls = re.findall(r"https?://[^\s]+", user_input)
        if urls:
            for url in urls:
                content = fetch_web_content(url)
            
            if "Gagal" not in content and "Terjadi kesalahan" not in content:
                messages.append(("human", f"Analisis konten dari URL berikut: {user_input}\n\n{content}"))
                result = llm.invoke(messages)
                messages.append(("ai", result.content))
                print("\n")
                print(result.content)
                speak(clean_text_for_tts(result.content))  # Mengubah hasil analisis menjadi suara
                conn_db.save_data("ai", result.content) 
            else:
                print("\n")
                print(content)
                speak(clean_text_for_tts(content))  # Give the sound output when it's failed
                conn_db.save_data("ai", content)
        else:
            messages.append(("human", user_input))
            result = llm.invoke(messages)
            messages.append(("ai", result.content))

            conn_db.save_data("ai", result.content)
            print("\n")
            print(result.content)
            speak(clean_text_for_tts(result.content))  # Change result to voices

# Run the project 
main()
    
