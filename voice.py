import pyttsx3
import datetime
import speech_recognition as speech
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
#Driver
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 11:
        speak("Good Morning!")
    if hour >= 12 and hour <= 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hi I am Melez  ! How can I help you?")


def takeCommand():
    r = speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("I can't hear you..")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ferdibulus08@gmail.com', 'Melez.Prens152')
    server.sendmail('ferdibulus08@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()

        # Execution Logic
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            music_dir = 'C:/Users/Default/Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H: %M: %S")
            speak(f"The time is, {Time}")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ferdibulus08@gmail.com"
                sendEmail(to, content)
                speak("Email has been succesfully sent!")

            except Exception as e:
                print(e)
                speak("Sorry, email can't be sent.")

        elif 'close the program' in query:
            speak("Nice talking with you. Take care")
            break
print("Program is closed")