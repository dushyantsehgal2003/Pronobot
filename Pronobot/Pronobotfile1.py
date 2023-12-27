import os
import platform
import subprocess

def pronounce_text(text):
    system_platform = platform.system()

    if system_platform == "Darwin":  # macOS
        command = ["say", text]
    elif system_platform == "Linux":  # Linux (e.g., Ubuntu)
        command = ["espeak", text]
    elif system_platform == "Windows":  # Windows
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            return
        except ImportError:
            print("pyttsx3 is not installed. Please install it using: pip install pyttsx3")
            return
    else:
        print(f"Unsupported platform: {system_platform}")
        return

    subprocess.run(command)

if __name__ == '__main__':
    print("Welcome to Pronobot 1.1 created by Dushyant Sehgal,to exit please type 'exit.'")
    while True:
        user_input = input("Please enter the text you would like Pronobot to pronounce: ")
        if user_input == "exit.":
            pronounce_text("Thank you for using Pronobot developed by Dushyant Sehgal")
            break
        pronounce_text(user_input)
