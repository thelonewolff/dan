import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pywhatkit
import smtplib
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
GOOGLE_PASSWORD = os.environ.get('GOOGLE_PASSWORD')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning! ")

    elif 12 <= hour < 17:
        speak("Good Afternoon! ")

    elif 17 <= hour < 19:
        speak("Good Evening! ")

    else:
        speak("Good Night! ")

    speak("I am your Virtual Assistant Dan. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    rr = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rr.pause_threshold = 1
        audio = rr.listen(source)

    try:
        print("Recognizing...")
        query = rr.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Connection error")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('youremailhere', GOOGLE_PASSWORD)
    server.sendmail('youremailhere', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif "hello" in query or "hello Danny" in query:
            hello1 = "Hello ! How May i Help you.."
            print(hello1)
            speak(hello1)

        elif "who are you" in query or "about you" in query or "your details" in query:
            who_are_you = "I am Dan an AI based computer program but i can help you lot like a your assistant ! try to give me a  simple command !"
            print(who_are_you)
            speak(who_are_you)

        elif 'who make you' in query or 'who made you' in query or 'who created you' in query or 'who develop you' in query:
            print(
                " For your information Danish and Arko Created me !    I can show you his Github In profile if you want to see.    Yes or no .....")
            speak(
                " For your information Danish and Arko Created me !    I can show you his Github In profile if you want to see.    Yes or no .....")
            ans_from_user_who_made_you = takeCommand()
            if 'yes' in ans_from_user_who_made_you or 'ok' in ans_from_user_who_made_you or 'yeah' in ans_from_user_who_made_you:
                webbrowser.open("https://www.github.com/thelonewolff")
                speak('opening his profile...... please wait')

            elif 'no' in ans_from_user_who_made_you or 'no thanks' in ans_from_user_who_made_you or 'not' in ans_from_user_who_made_you:
                speak("All right ! OK...")
            else:
                speak("I can't understand. Please say that again !")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")

        elif 'play music' in query:
            speak("ok i am playing music")
            music_dir = 'E:\\My MUSIC'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = 'E:\\\My Videos'
            Videos = os.listdir(video_dir)
            print(Videos)
            os.startfile(os.path.join(video_dir, Videos[0]))

        elif 'good bye' in query:
            speak("good bye")
            exit()

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')

        elif "your name" in query or "sweat name" in query:
            naa_mme = "Thanks for Asking my self ! Suzi"
            print(naa_mme)
            speak(naa_mme)

        elif "you feeling" in query:
            print("feeling Very happy to help you")
            speak("feeling Very happy to help you")

        elif query == 'none':
            continue

        elif 'exit' in query or 'stop' in query or 'quit' in query:
            exx_exit = 'See you soon. Bye'
            speak(exx_exit)
            exit()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\\vs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opening visual studio code")

        elif 'open word' in query:
            os.system('start winword')

        elif 'open excel' in query:
            os.system('start excel')

        elif 'close chrome' in query:
            os.system('taskkill /IM chrome.exe /F')

        elif 'open vlc' in query:
            os.system('start VLC')

        elif 'open chrome' in query:
            webbrowser.open("https://www.google.com")

        elif 'open discord' in query:
            os.system('start discord')

        elif 'send email' in query:
            try:
                speak("Who should I send the email to")
                to = input("Please enter the email id:").lower()
                speak("What should I say?")
                content = input("Please type your message:")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry.... I am not able to send this email")

        elif 'how are you' in query:
            setMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            ans_qus = random.choice(setMsgs)
            speak(ans_qus)
            speak(" How are you'")
            ans_from_user_how_are_you = takeCommand()
            if 'fine' in ans_from_user_how_are_you or 'happy' in ans_from_user_how_are_you or 'okey' in ans_from_user_how_are_you:
                speak('Great')
            elif 'not' in ans_from_user_how_are_you or 'sad' in ans_from_user_how_are_you or 'upset' in ans_from_user_how_are_you:
                speak('Tell me how can i make you happy')
            else:
                speak("I can't understand. Please say that again !")

        else:
            tempp = query.replace(' ', '+')
            prasun_url = "https://www.google.com/search?q="
            res_prasun = 'sorry! i cant understand but i search from internet to give your answer !'
            print(res_prasun)
            speak(res_prasun)
            webbrowser.open(prasun_url + tempp)