import pyttsx3
import speech_recognition as sr
from datetime import datetime
from functions import online_ops, os_ops
import requests


# Python text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    # speak funciton
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    # Listening
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("user said:", query)
    except Exception as e:
        print(e)
        print("can't recognize you. try again")
        return "None"
    return query

def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning')
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    # speak("welcome sir")
    print('What can I do for you...')
    speak('what can i do for you...')

if __name__ == "__main__":
    wishMe()
    my_name = {"awani", "hey awani", "okay awani", "avani", "hey avani", "okay awani" ,"avni", "hey avni", "okay awani"}
    while True:
        query = takecommand().lower()
        if "open notepad" in query:
            os_ops.open_notepad()

        elif 'open command prompt' in query or 'open cmd' in query:
            os_ops.open_cmd()

        elif 'open camera' in query:
            os_ops.open_camera()

        elif 'open calculator' in query:
            os_ops.open_calculator()

        elif 'ip address' in query:
            ip_address = os_ops.get_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = takecommand().lower()
            results = online_ops.search_Wiki(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = takecommand().lower()
            online_ops.play_Youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = takecommand().lower()
            online_ops.search_Google(query)

        elif "send whatsapp message" in query:
            speak(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takecommand().lower()
            online_ops.send_wp_msg(number, message)
            speak("I've sent the message sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = online_ops.get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = online_ops.get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)

        elif "trending movies" in query:
            moves = online_ops.get_trending_movies()
            speak(f"Some of the trending movies are: {moves}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*moves, sep='\n')

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(online_ops.get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*online_ops.get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = online_ops.find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = online_ops.get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif 'the date' in query:
            strDate = datetime.now().date
            speak(f"Sir, the Date is {strDate}")

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")