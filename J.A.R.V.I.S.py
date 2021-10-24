import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import smtplib
import time
import pyjokes
import requests
import ctypes
import pyautogui
import psutil
import winshell
import random
import calendar
from datetime import date
from random import randint

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("JARVIS: Good Morning!")
        speak("Good Morning! ")

    elif hour>=12 and hour<17:
        print("JARVIS: Good Afternoon!")
        speak("Good Afternoon! ")

    elif hour>=17 and hour<19 :
        print("JARVIS: Good Evening!")
        speak("Good Evening! ")

    else:
        print("JARVIS: Good Night!")
        speak("Good Night! ")

    print("JARVIS: I am your  Virtual  Assistant JARVIS. Please tell me how may I help you")
    speak("I am your  Virtual  Assistant JARVIS. Please tell me how may I help you")

def takeCommand():

    rr = sr.Recognizer()
    with sr.Microphone() as source:
        print("JARVIS: Listening...")
        rr.pause_threshold = 1
        audio = rr.listen(source)

    try:
        print("JARVIS: Recognizing...")
        query = rr.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")

    except Exception as e:
        print("JARVIS: Say that again please...")
        speak("Say that again please")
        return "None"
    return query

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'search' in query:
            print("JARVIS: Searching...")
            speak('Searching...')
            query = query.replace("search", " ")
            results = wikipedia.summary(query, 2)
            print("JARVIS: According to Google")
            speak("According to google")
            print("JARVIS:" + results)
            speak(results)

        elif 'stopwatch' in query:
            def time_convert(sec):
                mins = sec // 60
                sec = sec % 60
                hours = mins // 60
                mins = mins % 60
                print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
            input("Press Enter to start")
            start_time = time.time()
            input("Press Enter to stop")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)

        elif "hello" in query or "hello Jarvis" in query:
            hello1 = "Hello ! How May i Help you.."
            print("JARVIS:" + hello1)
            speak(hello1)

        elif "who are you" in query or "about you" in query or "your details" in query:
            who_are_you = "I am JARVIS an A I based computer program but i can help you lot like a your assistant ! try me to give simple command !"
            print("JARVIS" + who_are_you)
            speak(who_are_you)

        elif 'who made you' in query or 'who created you' in query or 'who develop you' in query:
            print("JARVIS: For your information Malyadri Chowdary Marneni Created me !")
            speak(" For your information Malyadri Chowdary Marneni Created me !")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            print("JARVIS: Opening Youtube")
            speak("opening youtube")

        elif 'open google earth' in query:
            webbrowser.open("https://www.google.com/earth/")
            print("JARVIS: Opening Google Earth")
            speak("opening google earth")

        elif 'open google maps' in query:
            webbrowser.open("https://www.google.com/maps/")
            print("JARVIS: Opening Google Maps")
            speak("opening google maps")

        elif 'open techwiz' in query:
            webbrowser.open("http://thetechwiz.ml/?i")
            print("JARVIS: Opening Techwiz")
            speak("opening techwiz")   

        elif 'open google' in query:
            webbrowser.open("google.com")
            print("JARVIS: Opening Google")
            speak("opening google")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            print("JARVIS: Opening Whatsapp")
            speak("opening whatsapp")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            print("JARVIS: Opening Yahoo")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            print("JARVIS: Opening Gmail")
            speak("opening google mail") 
            
        elif 'open github' in query:
            webbrowser.open("https://github.com/PythonProgrammers8")
            print("JARVIS: Opening Github") 
            speak("opening github")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            print("JARVIS: Opening Amazon")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            print("JARVIS: Opening Flipkart")
            speak("opening flipkart")
        
        elif 'open discord' in query:
            webbrowser.open("https://discord.com/channels/@me")
            print("JARVIS: Opening Discord")
            speak("opening discord")

        elif 'play' in query:
            query = query.replace('play', '')
            print("JARVIS: Playing" + query)
            speak('playing' + query)
            pywhatkit.playonyt(query)

        elif 'good bye' in query:
            print("JARVIS: Good Bye, have a nice")
            speak("good bye, have a nice day")
            exit()

        elif "shutdown" in query:
            print("JARVIS: Shutting Down")
            speak("shutting down")
            os.system('shutdown -s')

        elif "your name" in query:
            naa_mme = "Thanks for Asking my self ! My name is JARVIS"
            print("JARVIS:" + naa_mme)
            speak(naa_mme)

        elif "your feeling" in query:
            print("JARVIS: I'm feeling Very happy to help you")
            speak("i'm feeling Very happy to help you")

        elif query == 'none':
            continue

        elif 'exit' in query or 'stop' in query or 'quit' in query :
            exx_exit = 'See you soon. Bye'
            print("JARVIS:" + exx_exit)
            speak(exx_exit)
            exit() 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            print("JARVIS:" + f"the time is {strTime}")
            speak(f"the time is {strTime}")
        elif 'how are you' in query:
            setMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            ans_qus = random.choice(setMsgs)
            print(ans_qus)
            speak(ans_qus)
            print("JARVIS: How are you")
            speak(" How are you ")
            ans_from_user_how_are_you = takeCommand()
            if 'fine' in ans_from_user_how_are_you or 'happy' in ans_from_user_how_are_you or 'okay' in ans_from_user_how_are_you:
                print('JARVIS: Great')
                speak('Great')  
            elif 'not' in ans_from_user_how_are_you or 'sad' in ans_from_user_how_are_you or 'upset' in ans_from_user_how_are_you:
                print("JARVIS: Tell me how can i make you happy")
                speak('Tell me how can i make you happy')
            else :
                print("JARVIS: I can't understand. Please say that again !")
                speak("I can't understand. Please say that again !")
        elif 'bored' in query:
            print("JARVIS: Then let's play rock, paper, scissors")
            speak("Then let's play rock, paper, scissors")
            t = ["Rock", "Paper", "Scissors"]

            computer = t[randint(0,2)]

            player = False

            while True:
                player = input("Rock, Paper, Scissors?")
                if player == computer:
                    print("Tie!")
                elif player == "Rock":
                    if computer == "Paper":
                        print("You lose!", computer, "covers", player)
                    else:
                        print("You win!", player, "smashes", computer)
                elif player == "Paper":
                    if computer == "Scissors":
                        print("You lose!", computer, "cut", player)
                    else:
                        print("You win!", player, "covers", computer)
                elif player == "Scissors":
                    if computer == "Rock":
                        print("You lose...", computer, "smashes", player)
                    else:
                        print("You win!", player, "cut", computer)
                else:
                    print("JARVIS: Had a Great time with you")
                    speak("Had a Great time with you")
                    break
                player = False
                computer = t[randint(0,2)]
        elif 'timer' in query:
            def countdown(t): 
    
                while t: 
                    mins, secs = divmod(t, 60) 
                    timer = '{:02d}:{:02d}'.format(mins, secs) 
                    print(timer, end="\r") 
                    time.sleep(1) 
                    t -= 1
      
                print('JARVIS: Time up!!') 
                speak('time up, time up, time up')
  
   
            t = input("Enter the time in seconds: ") 

            countdown(int(t))
        elif 'joke' in query:
            jarvis_joke = pyjokes.get_joke()
            print(jarvis_joke)
            speak(jarvis_joke)
        elif 'flip a coin' in query:
            flipacoin = ["Heads","Tail"]
            coinans = random.choice(flipacoin)
            print("JARVIS:It's " + coinans)
            speak("it is" + coinans)
        elif 'lock' in query:
            print("JARVIS: As you wish")
            speak('As You Wish')
            ctypes.windll.user32.LockWorkStation()
        elif 'screenshot' in query:
            print("JARVIS: Ok, Let me take a snap")
            speak('ok sir, let me take a snap')
            pic = pyautogui.screenshot()
            print("JARVIS: Ok done, I have saved it in Nani Folder")
            speak('ok done, i have saved it in nani folder')
            pic.save('C:\\Users\\Saikumar\\OneDrive\\Desktop\\Nani\\Screenshot.jpg')
        elif 'charge' in query or 'power' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent) 
            time_left = secs2hours(battery.secsleft)
            print ("JARVIS: The battery percentage is " + percent)
            speak("the battery perecentage is " + percent)
            if percent < 40:
                print("JARVIS: Please connect charger because i can survive only "+ time_left)
                speak('please connect charger because i can survive only '+ time_left)
            if percent > 40:
                print("JARVIS: No need to connect the charger because i can survive "+ time_left)
                speak("no need to connect the charger because i can survive "+ time_left)
            else:
                print("JARVIS: Don't worry , charger is connected")
                speak("don't worry sir, charger is connected")
        elif "don't listen" in query or "stop listening" in query:
            print("JARVIS: For how much time you want to stop me from listening commands")
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            print("JARVIS: The Recycle Bin has been emptied") 
            speak("recycle bin has been emptied")
        elif "weather" in query:
            api_key="2dd26f86c27ef425150b565d77c8893c"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            complete_url=base_url+"appid="+api_key+"&q=Bangalore"
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print("JARVIS: Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            print("JARVIS: Here are some headlines from the Times of India,Happy reading")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        elif 'thank you' in query:
            print("JARVIS: Your Welcome, I'm always there for you!!")
            speak("your welcome, I'm always there for you")
        elif 'day' in query:
            def findDay(date): 
                day, month, year = (int(i) for i in date.split(' '))     
                born = datetime.date(year, month, day) 
                return born.strftime("%A") 
  
            date = '28 01 2021'
            print("JARVIS: It is " + findDay(date))
            speak("it is " + findDay(date))
        elif 'are you there' in query:
            print("JARVIS: At your service!!")
            speak("at your service")
        elif 'my youtube channel' in query:
            print("JARVIS: Your youtube channel name is Malyadri Talentz")
            speak("your youtube channel name is Malyadri talentz")
        elif 'calculate' in query:
            print("JARVIS: Select an operation:")
            speak("select an operation")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")
            choice = input("Enter choice(1/2/3/4): ")
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                speak("entered first number")
                num2 = float(input("Enter second number: "))
                speak("entered second number")
            if choice == '1':
                print("JARVIS: The answer is ", add(num1, num2))
                speak(add(num1, num2))
            elif choice == '2':
                print("JARVIS: The answer is ", subtract(num1, num2))
                speak(subtract(num1, num2))
            elif choice == '3':
                print("JARVIS: The answer is ", multiply(num1, num2))
                speak(multiply(num1, num2))
            elif choice == '4':
                print("JARVIS: The answer is ", divide(num1, num2))
                speak(divide(num1, num2))
            else:
                print("JARVIS: Invalid Input")
                speak("invaild input")
        elif 'spell' in query:
            speak("of course what should i spell for you")
            spelling = input("JARVIS: Off course, what should I spell for you?")
            print("JARVIS: ", spelling)
            speak(spelling)
        elif 'map' in query:
            speak("which place location would you like to see")
            location = input("Which place location would you like to see??")
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            print('Here is the map of ' + location)
            speak('Here is the map of ' + location)
        elif 'google' in query:
            tempp = query.replace('google','+')
            search_url="https://www.google.com/search?q="    
            internet_search = 'I have searched from internet to give your answer !'
            print("JARVIS: " + internet_search)
            speak(internet_search)
            webbrowser.open(search_url+tempp)