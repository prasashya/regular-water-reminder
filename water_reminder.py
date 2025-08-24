import time
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def water_reminder(interval_minutes=4):
    while True:
        time.sleep(interval_minutes * 4)
        speak("Drink some  water")

if __name__ == "__main__":
    print("💧 Water Reminder App Started (every 60 minutes)")
    water_reminder(1)  # reminder every 60 minutes
