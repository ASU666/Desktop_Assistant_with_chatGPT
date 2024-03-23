import win32com.client
import os
import webbrowser
import random
import datetime
import openai

openai.api_key = "your_api_key"


def chatGPT(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        msg=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].msg.content.strip()


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    print(text)
    return speaker.speak(text)


def play_songs():
    sngs = [file for file in os.listdir('songs') if file.endswith('.mp3')]
    print(sngs)
    song_to_play = input("Please Choose the Song Name(Case Sensitive) : ")
    print(f"Jarvis : Now Playing {song_to_play}")
    song_path = os.path.join('songs', song_to_play)
    os.startfile(song_path)


def respond_to_greeting():
    responses = ["Hello!", "Hi there!", "Hey! How can I help you?"]
    return random.choice(responses)


def respond_to_question():
    responses = ["I'm not sure.", "I'll need more information to answer that.", "Let me check for you."]
    return random.choice(responses)


def respond_to_farewell():
    responses = ["Goodbye!", "See you later!", "Take care!"]
    return random.choice(responses)


def fun_mode(input_text):
    input_text = input_text.lower()
    if "hello" in input_text or "hi" in input_text or "hey" in input_text:
        return respond_to_greeting()
    elif "?" in input_text:
        return respond_to_question()
    elif "bye" in input_text or "goodbye" in input_text:
        return respond_to_farewell()
    else:
        return "I'm sorry, I don't understand. Can you please retry?"


def open_camera():
    os.system("start microsoft.windows.camera:")


def open_vscode():
    os.system("code")


def main():
    print("Jarvis : Connecting....\nConnected Succesfully.")
    say("Hello I am Jarvis A.I.")

    while True:
        cmd = input("Asu : ")

        if "say" in cmd.split()[0].lower():
            print("Jarvis : ", end="")
            text = " ".join(cmd.split()[1:])
            say(text)

        elif "time" in cmd.lower():
            print("Jarvis : ", end="")
            say(f"The time is {datetime.datetime.now().strftime("%H:%M:%S")}")

        elif "open app" in cmd.lower():
            appList = ["Camera", "Vscode"]
            print(appList)
            app = input("Enter The App name(Case Sensitive) : ")
            print("Jarvis : ", end="")
            say(f"Opening {app} sir!!!")
            if app == "Camera":
                open_camera()
            elif app == "Vscode":
                open_vscode()

        elif "open" in cmd.lower():
            site = cmd.split()[1].lower()
            print("Jarvis : ", end="")
            say(f"Opening {site} sir!!!")
            webbrowser.open(f"https://{site}.com")

        elif "play music" in cmd.lower():
            play_songs()
            while True:
                play_next = input("Do You Want to play Next Song?(Y/N) : ")
                if play_next == "Y":
                    play_songs()
                else:
                    break
        elif "use chatgpt" in cmd.lower():
            while True:
                pmt = input("Enter Your Prompt : ")
                if pmt == "exit":
                    break
                else:
                    print("Jarvis : ", end="")
                    say(chatGPT(pmt))

        elif "exit" in cmd.lower():
            print("Disconnecting....")
            say("Signing off!!!")
            break
        elif "enter fun mode" in cmd.lower():
            print("Entering Fun Mode....")
            print("Successful")
            while True:
                text_inn = input("Asu : ")
                print("Jarvis(Fun_Mode) : ", end="")
                say(fun_mode(text_inn))
        else:
            print("Jarvis : ", end="")
            say("Oops!!! Invalid Command. Try Again.")


if __name__ == "__main__":
    main()
