import re
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import pyttsx3  # Import pyttsx3
from web_scraper import fetch_web_content  # Function import web_scrapper
from db import conn_db # Import from conn_db.py file



load_dotenv() 

model = "gemini-1.5-flash" # Model from gemini
llm = ChatGoogleGenerativeAI(model=model)

engine = pyttsx3.init()  # Engine TTS initialize 


def speak(text):
    """Change text to voice"""
    engine.say(text)
    engine.runAndWait()

def clean_text_for_tts(text):
    return re.sub(r'\*+', '', text).strip()

messages = []

while True:
    user_input = input("Please kindly input your questions: ")
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
            speak(clean_text_for_tts(result.content))  # Change analyze result to voice
            conn_db.save_data("ai", result.content)
        else:
            print("\n")
            print(content)
            speak(clean_text_for_tts(content))  # Give an output voice while failed
            conn_db.save_data("ai", content)
    else:
        messages.append(("human", user_input))
        result = llm.invoke(messages)
        messages.append(("ai", result.content))

        conn_db.save_data("ai", result.content)
        print("\n")
        print(result.content)
        speak(clean_text_for_tts(result.content))  # Change analyze to voice
