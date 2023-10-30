import speech_recognition as sr
import subprocess
import os


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return "Sorry, there was an error with the request. {0}".format(e)


def execute_command(command):
    if "open notepad" in command:
        subprocess.Popen(["notepad.exe"])
    elif "open calculator" in command:
        subprocess.Popen(["calc.exe"])
    elif "open browser" in command:
        subprocess.Popen(["chrome.exe"])
    elif "exit" in command:
        exit()


if __name__ == "__main__":
    while True:
        command = listen().lower()
        print("You said: " + command)
        execute_command(command)
